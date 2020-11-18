from PySide2.QtCore import QSettings, QUrl, QUrlQuery, QByteArray, Signal, Slot, QObject
from PySide2.QtNetwork import QNetworkAccessManager, QNetworkRequest
from munch import munchify
import json

from ast import literal_eval


class ReplyParser(QObject):
    parsed = Signal(dict)

    def __init__(self, reply):
        super().__init__()
        self.reply = reply

    @Slot()
    def parse_reply(self):
        def parse():
            data = literal_eval(str(self.reply.readAll()))
            self.parsed.emit(json.loads(data))
        return parse


class API:
    manager = QNetworkAccessManager()

    def __init__(self, settings: QSettings):
        self.api_endpoint = settings.value('api_host') + '/api/v1'
        self.token = settings.value('login_token')

        api = {
            'users': {
                'me': lambda: self.__get('/users/me'),
            },
            'artists': {
                'all': lambda: self.__get('/artists'),
                'get': lambda idx: self.__get(f'/artists/{idx}'),
                'libraries': lambda idx: self.__get(f'/artists/{idx}/libraries')
            },
            'albums': {
                'all': lambda: self.__get('/albums'),
                'get': lambda idx: self.__get(f'/albums/{idx}'),
                'libraries': lambda idx: self.__get(f'/albums/{idx}/libraries')
            },
            'tracks': {
                'all': lambda: self.__get('/tracks'),
                'get': lambda idx: self.__get(f'/tracks/{idx}'),
                'libraries': lambda idx: self.__get(f'/tracks/{idx}/libraries')
            },
            'listen': lambda uuid: self.__get(f'/listen/{uuid}'),
            'licenses': {
                'all': lambda: self.__get('/licenses'),
                'get': lambda code: self.__get(f'/licenses/{code}')
            },
            'libraries': {},
            'uploads': {},
            'channels': {},
            'subscriptions': {},
            'favourites': {},
            'playlists': {},
            'history': {
                'all': lambda: self.__get('/history/listenings'),
                'add': lambda track_id: self.__post('/history/listenings', {'track': track_id})
            },
        }

        for key, value in api.items():
            setattr(self, key, munchify(value))

    def __request(self, url):
        print(self.api_endpoint + url)
        req = QNetworkRequest(QUrl(self.api_endpoint + url))
        req.setRawHeader(QByteArray(b'Authorization'), QByteArray(f'Bearer {self.token}'.encode()))
        return req

    def __parse(self, reply):
        parser = ReplyParser(reply)
        reply.finished.connect(parser.parse_reply())
        return parser.parsed

    def __get(self, url):
        req = self.__request(url)
        return self.__parse(self.manager.get(req))

    def __post(self, url, data):
        req = self.__request(url)

        query = QUrlQuery()
        for key, value in data:
            query.addQueryItem(key, value)

        req.setHeader(QNetworkRequest.ContentTypeHeader, 'application/x-www-form-urlencoded')
        return self.__parse(self.manager.post(req, query.toString(QUrl.FullyEncoded)))
