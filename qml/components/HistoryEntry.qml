import QtQuick
import Qt5Compat.GraphicalEffects

Rectangle {
    id: root
    radius: Style.radius
    color: Style.gray

    width: 200
    height: col.height

    Row {
        id: row
        spacing: 10
        width: parent.width

        RoundImage {
            id: image
            height: col.height
            width: height

            radius: Style.radius

            source: "../../assets/cover.jpg"

            layer.enabled: true
            layer.effect: DropShadow {
                radius: 8.0
                color: Style.darkGray
                transparentBorder: true
            }
        }

        Column {
            id: col
            spacing: 4
            topPadding: parent.spacing
            bottomPadding: parent.spacing
            width: parent.width - image.width - info.width - parent.spacing * 3

            Text {
                id: album
                text: qsTr("DeA.D. Alive! (Live)")
                font.pixelSize: 16
                color: Style.text
            }

            Text {
                id: artist
                text: qsTr("Misfits")
                font.pixelSize: 12
                color: Style.text
            }
        }

        Column {
            id: info
            spacing: 8
            topPadding: parent.spacing
            bottomPadding: parent.spacing

            Text {
                id: date
                text: qsTr("13:43")
                font.pixelSize: 12
                horizontalAlignment: Text.AlignRight
                color: Style.textGray
                anchors.right: parent.right
                anchors.rightMargin: 0
            }

            Text {
                id: user
                text: qsTr("@wvffle")
                font.pixelSize: 12
                horizontalAlignment: Text.AlignRight
                color: Style.text
                anchors.right: parent.right
                anchors.rightMargin: 0
            }
        }
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:8}
}
##^##*/
