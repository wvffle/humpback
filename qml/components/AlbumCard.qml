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

        RoundImage {
            id: image
            x: parent.topPadding
            width: root.width - parent.topPadding * 2
            height: width
            radius: Style.radius

            source: "../../assets/cover.jpg"
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


    //    Rectangle {
    //        id: mask
    //        anchors.fill: parent
    //        radius: root.radius
    //        visible: false
    //    }

    //    OpacityMask {
    //        anchors.fill: parent
    //        source: root
    //        maskSource: mask
    //        antialiasing: root.antialiasing
    //    }
}
