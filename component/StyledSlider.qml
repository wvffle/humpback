import QtQuick
import QtQuick.Controls
import '.'

Item {
    id: root

    property double value: 0.5
    property bool wheelEnabled: false

    property int trackHeight: 4
    property int handleSize: 3 * trackHeight

    property color color: Style.lightGray
    property color trackColor: Style.gray
    property color handleColor: Style.text

    height: Math.min(8, handleSize)
    width: 200

    Row {
        Rectangle {
            width: root.width * root.value - handle.width / 2
            height: root.trackHeight
            color: root.color
            y: root.height / 2 - height / 2
        }

        Rectangle {
            id: handle
            width: root.handleSize
            height: root.handleSize
            radius: root.handleSize
            color: root.handleColor
            y: root.height / 2 - height / 2
        }

        Rectangle {
            width: root.width * (1 - root.value) - handle.width / 2
            height: root.trackHeight
            color: root.trackColor
            y: root.height / 2 - height / 2
        }
    }
}



