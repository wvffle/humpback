from PySide2.QtCore import QSettings, QUrl, QUrlQuery, QByteArray, Signal, Slot, QObject, Qt
from PySide2.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PySide2.QtGui import QPixmap
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


class CoverFetcher(QObject):
    fetched = Signal(QPixmap)

    def __init__(self, reply, size):
        super().__init__()
        self.reply = reply
        self.size = size
        reply.finished.connect(self.fetch())

    @Slot()
    def fetch(self):
        # TODO: Add caching
        def do():
            pixmap = QPixmap()
            pixmap.loadFromData(self.reply.readAll())
            pixmap.scaled(self.size, self.size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.fetched.emit(pixmap)
        return do


class API:
    manager = QNetworkAccessManager()

    def __init__(self, settings: QSettings):
        self.api_endpoint = settings.value('api_host') + '/api/v1'
        self.token = settings.value('login_token')

        api = {
            'users': {
                'me': APIEntry(lambda params: self.__get('/users/me', params=params)),
            },
            'artists': {
                'all': APIEntry(lambda params: self.__get('/artists', params=params)),
                'cover': APIEntry(lambda idx, params: self.__get(f'/artists/{idx}', params=params)),
                'libraries': APIEntry(lambda idx, params: self.__get(f'/artists/{idx}/libraries', params=params))
            },
            'albums': {
                'all': APIEntry(lambda params: self.__get('/albums', params=params)),
                'cover': APIEntry(lambda idx, params: self.__get(f'/albums/{idx}', params=params)),
                'libraries': APIEntry(lambda idx, params: self.__get(f'/albums/{idx}/libraries', params=params))
            },
            'tracks': {
                'all': APIEntry(lambda params: self.__get('/tracks', params=params)),
                'cover': APIEntry(lambda idx, params: self.__get(f'/tracks/{idx}', params=params)),
                'libraries': APIEntry(lambda idx, params: self.__get(f'/tracks/{idx}/libraries', params=params))
            },
            'listen': APIEntry(lambda track_id, params: self.__request(f'/listen/{track_id}', params=params)),
            'licenses': {
                'all': APIEntry(lambda params: self.__get('/licenses', params=params)),
                'cover': APIEntry(lambda code, params: self.__get(f'/licenses/{code}', params=params))
            },
            'libraries': {},
            'uploads': {},
            'channels': {},
            'subscriptions': {},
            'favourites': {
                'all': APIEntry(lambda params: self.__get('/favorites/tracks?scope=all', params=params)),
                'me': APIEntry(lambda params: self.__get('/favorites/tracks?scope=me', params=params)),
                'add': APIEntry(lambda track_id, params: self.__post('/favorites/tracks', {'track': track_id}, params=params)),
                'remove': APIEntry(lambda track_id, params: self.__post('/favorites/tracks/remove', {'track': track_id}, params=params)),
            },
            'playlists': {},
            'history': {
                'all': APIEntry(lambda params: self.__get('/history/listenings', params=params)),
                'add': APIEntry(lambda track_id, params: self.__post('/history/listenings', {'track': track_id}, params=params)),
            },
        }

        for key, value in api.items():
            setattr(self, f'{key}', munchify(value))

    def __request(self, url, params = None):
        qurl = QUrl(self.api_endpoint + url)
        if type(params) == dict:
            query = QUrlQuery()
            for key, value in params.items():
                query.addQueryItem(key, str(value))

            qurl.setQuery(query)

        req = QNetworkRequest(qurl)
        req.setRawHeader(QByteArray(b'Authorization'), QByteArray(f'Bearer {self.token}'.encode()))
        return req

    def __parse(self, reply):
        parser = ReplyParser(reply)
        reply.finished.connect(parser.parse_reply())
        return parser.parsed

    def __get(self, url, params):
        req = self.__request(url, params)
        return self.__parse(self.manager.get(req))

    def __post(self, url, data, params):
        req = self.__request(url, params)

        query = QUrlQuery()
        for key, value in data:
            query.addQueryItem(key, value)

        req.setHeader(QNetworkRequest.ContentTypeHeader, 'application/x-www-form-urlencoded')
        return self.__parse(self.manager.post(req, query.toString(QUrl.FullyEncoded)))

    def cover(self, url, size):
        request = QNetworkRequest(QUrl(url))
        return CoverFetcher(self.manager.get(request), size).fetched


class APIEntry:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        return self.fn(*args, {})

    def with_params(self, *args):
        return self.fn(*args)
