import QtQuick
import Qt5Compat.GraphicalEffects
Item {
    id: root
    property int radius: 0
    property url source: ""
    property bool asynchronous: img.asynchronous
    property int fillMode: img.fillMode

    Image {
        id: img
        anchors.fill: parent
        source: root.source
        asynchronous: false
        fillMode: Image.PreserveAspectFit
        antialiasing: root.antialiasing
        visible: false
    }

    Rectangle {
        id: mask
        anchors.fill: parent
        radius: root.radius
        visible: false
    }

    OpacityMask {
        anchors.fill: parent
        source: img
        maskSource: mask
        antialiasing: root.antialiasing
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:6;height:56;width:56}
}
##^##*/
