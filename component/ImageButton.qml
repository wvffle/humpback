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

    property string text: ""
    property int textSize: 12
    property color textColor: inactiveColor
    property int textPadding: padding
    property bool textBold: false

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

        Column {
            anchors.fill: parent
            anchors.margins: button.padding

            ColoredImage {
                file: button.file
                color: active ? activeColor : inactiveColor
                width: parent.width
                height: width
            }

            Text {
                width: parent.width
                text: qsTr(button.text)
                font.pixelSize: button.textSize
                color: active ? activeColor : inactiveColor
                visible: button.text != ""
                horizontalAlignment: Text.AlignHCenter
                topPadding: button.textPadding
                font.bold: button.textBold
            }
        }
    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/
