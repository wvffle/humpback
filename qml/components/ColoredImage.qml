import QtQuick
import Qt5Compat.GraphicalEffects

Item {
    id: root

    property url file: ""
    property color color: Style.accent

        Image {
            id: image
            anchors.fill: parent
            source: root.file
            sourceSize.height: root.height
            sourceSize.width: root.width
            antialiasing: true
            visible: false
        }

        ColorOverlay {
            source: image
            anchors.fill: image
            color: root.color
            antialiasing: true
            visible: true
        }
}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
