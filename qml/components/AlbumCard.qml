import QtQuick
import Qt5Compat.GraphicalEffects

Item {
    id: root
    width: 300
    height: col.height

    property int radius: Style.radius
    property bool antialiasing: true

    Rectangle {
        id: bg
        anchors.fill: parent
        color: Style.gray
        radius: root.radius
    }

    Column {
        id: col
        width: parent.width
        topPadding: 10

        Rectangle {
            x: parent.topPadding
            width: root.width - parent.topPadding * 2
            height: width
            radius: image.radius
            color: "#00000000"

            layer.enabled: true
            layer.effect: DropShadow {
                radius: 8.0
                color: Style.darkGray
                transparentBorder: true
            }

            RoundImage {
                id: image
                x: parent.topPadding
                anchors.fill: parent
                radius: Style.radius

                source: "../../assets/cover.jpg"
            }
        }


        Text {
            id: album
            text: qsTr("DeA.D. Alive! (Live)")
            font.pixelSize: 16
            color: Style.text
            topPadding: 8
            bottomPadding: 0
            padding: parent.topPadding
        }

        Text {
            id: artist
            text: qsTr("Misfits")
            font.pixelSize: 16
            color: Style.text
            topPadding: 4
            padding: parent.topPadding
        }
    }




}
