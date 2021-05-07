import QtQuick 2.15
import QtQuick.Window 2.15
import "component"

Window {
    id: root
    width: 640
    height: 480
    visible: true
    title: qsTr("waffwhale")

    visibility: "Maximized"

    Controls {
        y: root.height - height
        width: root.width
        id: controls
    }

    Rectangle {
        height: root.height - controls.height
        width: root.width

    }
}
