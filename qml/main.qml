import QtQuick
import QtQuick.Window
import Qt5Compat.GraphicalEffects
import "components"

Window {
    id: root
    width: 640
    height: 480
    visible: true
    title: qsTr("waffwhale")
    color: Style.darkGray

    visibility: "Maximized"

    Row {
        Item {
            property int radius: Style.radius * 2
            id: menu
            width: 100 + radius
            height: parent.height

            Rectangle {
                color: Style.accent
                anchors.fill: parent

                Rectangle {
                    color: Style.darkGray
                    height: parent.height
                    width: radius * 2
                    radius: menu.radius
                    x: parent.width - radius
                }
            }

            Column {
                spacing: 64
                width: parent.width - parent.radius
                anchors.verticalCenter: parent.verticalCenter

                ImageButton {
                    file: '../../assets/icons/grid.svg'
                    width: 32
                    height: 32

                    inactiveColor: Style.text
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: 'Browse'
                    textSize: 14
                    textPadding: 8
                }

                ImageButton {
                    file: '../../assets/icons/disc.svg'
                    width: 32
                    height: 32

                    inactiveColor: Style.text
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: 'Albums'
                    textSize: 14
                    textPadding: 8
                }

                ImageButton {
                    file: '../../assets/icons/user.svg'
                    width: 32
                    height: 32

                    inactiveColor: Style.text
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: 'Artists'
                    textSize: 14
                    textPadding: 8
                }

                ImageButton {
                    file: '../../assets/icons/list.svg'
                    width: 32
                    height: 32
                    text: 'Playlists'
                    textSize: 14
                    textPadding: 8

                    inactiveColor: Style.text
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                ImageButton {
                    file: '../../assets/icons/rss.svg'
                    width: 32
                    height: 32
                    text: 'Radios'
                    textSize: 14
                    textPadding: 8

                    inactiveColor: Style.text
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                ImageButton {
                    file: '../../assets/icons/heart.svg'
                    width: 32
                    height: 32

                    inactiveColor: Style.text
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: 'Favourites'
                    textSize: 14
                    textPadding: 8
                }
            }
        }

        Column {
            property int margins: 77
            width: root.width - menu.width - panel.width
            height: root.height

            Row {
                height: parent.height - controls.height
                width: controls.width
                x: parent.margins

                Column {
                    id: main
                    width: parent.width - panel.width
                    height: parent.height
                }

            }

            Controls {
                id: controls
                width: parent.width - 2 * parent.margins
                x: parent.margins
            }
        }

        Rectangle {
            id: panel
            width: 400
            height: parent.height
            color: Style.gray

            Rectangle {
                color: Style.darkGray
                radius: menu.radius
                width: radius * 2
                height: parent.height
                x: -radius
            }

            Column {
                anchors.fill: parent
                anchors.margins: 47
                spacing: 7

                RoundImage {
                    source: '../../assets/cover.jpg'
                    width: parent.width
                    height: width
                    radius: 17
                }

                Text {
                    text: qsTr('Saturday Night')
                    font.pixelSize: 24
                    color: Style.accent
                }

                Text {
                    text: qsTr('DeA.D. Alive! (Live) ')
                    font.pixelSize: 16
                    color: Style.text
                }

                Text {
                    text: qsTr('Misfits')
                    font.pixelSize: 12
                    color: Style.text
                }

                Text {
                    topPadding: 32
                    bottomPadding: 16
                    text: qsTr('Listening Queue')
                    font.pixelSize: 24
                    font.weight: Font.Black
                    color: Style.text
                }

                Column {
                    width: parent.width
                    spacing: 10

                    Rectangle {
                        width: parent.width
                        height: 48
                        color: '#00000000'
                        radius: 8

                        Row {
                            anchors.fill: parent
                            spacing: 4

                            RoundImage {
                                source: '../../assets/cover.jpg'
                                width: 48
                                height: width
                                radius: 8
                            }

                            Column {
                                anchors.verticalCenter: parent.verticalCenter
                                spacing: 4

                                Text {
                                    text: qsTr('Dig Up Her Bones')
                                    font.pixelSize: 15
                                    color: Style.text
                                }

                                Text {
                                    text: qsTr('Misfits')
                                    font.pixelSize: 13
                                    color: Style.textLight
                                }
                            }
                        }
                    }

                    Rectangle {
                        width: parent.width
                        height: 48
                        color: '#00000000'
                        radius: 8

                        Row {
                            anchors.fill: parent
                            spacing: 4

                            RoundImage {
                                source: '../../assets/cover.jpg'
                                width: 48
                                height: width
                                radius: 8
                            }

                            Column {
                                anchors.verticalCenter: parent.verticalCenter
                                spacing: 4

                                Text {
                                    text: qsTr('Helena')
                                    font.pixelSize: 15
                                    color: Style.text
                                }

                                Text {
                                    text: qsTr('Misfits')
                                    font.pixelSize: 13
                                    color: Style.textLight
                                }
                            }
                        }
                    }

                    Rectangle {
                        width: parent.width
                        height: 48
                        color: Style.lightGray
                        radius: 8

                        Row {
                            anchors.fill: parent
                            spacing: 4

                            RoundImage {
                                source: '../../assets/cover.jpg'
                                width: 48
                                height: width
                                radius: 8
                            }

                            Column {
                                anchors.verticalCenter: parent.verticalCenter
                                spacing: 4

                                Text {
                                    text: qsTr('Saturday Night')
                                    font.pixelSize: 15
                                    color: Style.accent
                                }

                                Text {
                                    text: qsTr('Misfits')
                                    font.pixelSize: 13
                                    color: Style.text
                                }
                            }
                        }
                    }
                }
            }

        }
    }

}
