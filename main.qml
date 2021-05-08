import QtQuick
import QtQuick.Window
import Qt5Compat.GraphicalEffects
import "component"

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
                    file: '../assets/icons/grid.svg'
                    width: 32
                    height: 32

                    inactiveColor: Style.text
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                ImageButton {
                    file: '../assets/icons/disc.svg'
                    width: 32
                    height: 32

                    inactiveColor: Style.text
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                ImageButton {
                    file: '../assets/icons/user.svg'
                    width: 32
                    height: 32

                    inactiveColor: Style.text
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                ImageButton {
                    file: '../assets/icons/list.svg'
                    width: 32
                    height: 32

                    inactiveColor: Style.text
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                ImageButton {
                    file: '../assets/icons/rss.svg'
                    width: 32
                    height: 32

                    inactiveColor: Style.text
                    anchors.horizontalCenter: parent.horizontalCenter
                }

                ImageButton {
                    file: '../assets/icons/heart.svg'
                    width: 32
                    height: 32

                    inactiveColor: Style.text
                    anchors.horizontalCenter: parent.horizontalCenter
                }
            }
        }

        Column {
            Row {
                x: -menu.radius
                height: root.height - controls.height
                width: controls.width

                Column {
                    id: main
                    width: parent.width - panel.width
                    height: parent.height
                }

                Rectangle {
                    id: panel
                    width: 400
                    height: parent.height
                    color: Style.gray
                    Column {
                        anchors.fill: parent
                        anchors.margins: 47
                        spacing: 7

                        RoundImage {
                            source: '../assets/cover.jpg'
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
                    }

                }
            }

            Controls {
                x: -menu.radius
                id: controls
                width: root.width - menu.width + menu.radius
            }
        }
    }

}
