import QtQuick
import Qt5Compat.GraphicalEffects

Item {
    id: button
    property url file: ""
    property bool active: false
    property color activeColor: Style.accent
    property color inactiveColor: Style.textGray
    property color color: "#00ffffff"
    property int radius: 0
    property int padding: 0

    signal clicked()

    Rectangle {
        color: button.color
        radius: button.radius
        anchors.fill: parent

        MouseArea {
            anchors.fill: parent
            onPressed: {
                button.clicked()
            }
        }

        Image {
            id: image
            anchors.fill: parent
            anchors.margins: button.padding
            source: button.file
            sourceSize.height: button.height
            sourceSize.width: button.width
            antialiasing: true
            visible: false
        }

        ColorOverlay {
            source: image
            anchors.fill: image
            color: active ? activeColor : inactiveColor
            antialiasing: true
            visible: true
        }
    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
