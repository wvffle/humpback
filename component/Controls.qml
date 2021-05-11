import QtQuick
import QtQuick.Controls
import "."

Item {
    id: controls
    property string track: "Track Title"
    property string artist: "Artist"
    property string album: "Album"

    signal play()
    signal pause()

    height: 128
//    property alias coverartRadius: coverart.radius

    Rectangle {
        id: bg
        color: '#00000000'
        width: controls.width
        height: controls.height
        anchors.margins: 0

        Row {
            id: row
            y: spacing
            height: parent.height - spacing * 2
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.margins: spacing
            spacing: 9

            Item {
                width: parent.width
                height: parent.height

                Item {
                    width: parent.width
                    height: parent.height - sliderRow.height

                    Row {
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.left: parent.left
                        spacing: 9

                        ImageButton {
                            id: markFavourite
                            width: 36
                            color: Style.gray
                            height: width
                            padding: 8
                            radius: Style.radius
                            anchors.verticalCenter: parent.verticalCenter
                            active: false
                            file: "../assets/icons/heart.svg"

                            Connections {
                                target: markFavourite

                                function onClicked () {
                                    console.log("clicked")
                                }
                            }
                        }

                        ImageButton {
                            id: addToPlaylist
                            width: markFavourite.width
                            color: Style.gray
                            height: width
                            padding: markFavourite.padding
                            radius: Style.radius
                            anchors.verticalCenter: parent.verticalCenter
                            active: false
                            file: "../assets/icons/list.svg"

                            Connections {
                                target: addToPlaylist

                                function onClicked () {
                                    console.log("clicked")
                                }
                            }
                        }

                        ImageButton {
                            id: hideArtist
                            width: markFavourite.width
                            color: Style.gray
                            height: width
                            padding: markFavourite.padding
                            radius: Style.radius
                            anchors.verticalCenter: parent.verticalCenter
                            active: false
                            file: "../assets/icons/eye-off.svg"

                            Connections {
                                target: hideArtist

                                function onClicked () {
                                    console.log("clicked")
                                }
                            }
                        }
                    }

                    Row {
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.horizontalCenter: parent.horizontalCenter
                        spacing: 19

                        ImageButton {
                            id: repeat
                            width: 16
                            height: width
                            anchors.verticalCenter: parent.verticalCenter
                            file: "../assets/icons/repeat.svg"
                            inactiveColor: Style.textGray
                            activeColor: Style.text

                            Connections {
                                target: repeat

                                function onClicked () {
                                    console.log("clicked")
                                }
                            }
                        }

                        ImageButton {
                            id: prev
                            width: 24
                            height: width
                            anchors.verticalCenter: parent.verticalCenter
                            file: "../assets/icons/skip-back.svg"
                            inactiveColor: Style.accent

                            Connections {
                                target: prev

                                function onClicked () {
                                    console.log("clicked")
                                }
                            }
                        }

                        ImageButton {
                            id: playPause
                            width: 42
                            height: width
                            anchors.verticalCenter: parent.verticalCenter
                            file: "../assets/icons/play.svg"
                            inactiveColor: Style.text
                            color: Style.accent
                            radius: width
                            padding: (width - prev.width) / 2

                            Connections {
                                target: playPause

                                function onClicked () {
                                    console.log("clicked")
                                }
                            }
                        }

                        ImageButton {
                            id: next
                            width: 24
                            height: width
                            anchors.verticalCenter: parent.verticalCenter
                            file: "../assets/icons/skip-forward.svg"
                            inactiveColor: Style.accent

                            Connections {
                                target: next

                                function onClicked () {
                                    console.log("clicked")
                                }
                            }
                        }

                        ImageButton {
                            id: shuffle
                            width: 16
                            height: width
                            anchors.verticalCenter: parent.verticalCenter
                            file: "../assets/icons/shuffle.svg"
                            inactiveColor: Style.textGray
                            activeColor: Style.text

                            Connections {
                                target: shuffle

                                function onClicked () {
                                    console.log("clicked")
                                }
                            }
                        }
                    }

                    Row {
                        anchors.verticalCenter: parent.verticalCenter
                        anchors.right: parent.right
                        anchors.rightMargin: 0
                        spacing: 9

                        ImageButton {
                            file: "../assets/icons/volume-1.svg"
                            width: 24
                            height: width
                        }

                        StyledSlider {
                            id: volumeSlider
                            value: 0.5
                            width: 150
                            anchors.verticalCenter: parent.verticalCenter
                            wheelEnabled: true
                        }

                        ImageButton {
                            file: "../assets/icons/volume-2.svg"
                            width: 24
                            height: width
                        }
                    }
                }



                Row {
                    id: sliderRow
                    width: parent.width
                    anchors.bottom: parent.bottom
                    anchors.bottomMargin: 0
                    spacing: 9

                    Text {
                        id: timePre
                        text: qsTr("5:44")
                        font.pixelSize: 12
                        color: Style.textGray
                    }

                    StyledSlider {
                        id: playbackSlider
                        width: parent.width - timePost.width - timePre.width - parent.spacing * 2
                        value: 0.5
                        color: Style.accent
                        handleSize: 16
                    }

                    Text {
                        id: timePost
                        text: qsTr("7:24")
                        font.pixelSize: 12
                        color: Style.textGray
                    }
                }
            }
        }
    }
}




/*##^##
Designer {
    D{i:0;formeditorZoom:0.9}
}
##^##*/
