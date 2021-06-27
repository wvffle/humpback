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

    property int imageSize: 32

    property string text: ""
    property int textSize: 12
    property color textColor: inactiveColor
    property int textPadding: padding
    property bool textBold: false

    height: image.height + padding * 2 + (text != "" ? textPadding + textSize : 0)
    width: height

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
            id: column
            anchors.fill: parent
            anchors.margins: button.padding

            ColoredImage {
                id: image
                color: active ? activeColor : inactiveColor

                width: button.imageSize
                height: width

                anchors.left: parent.left
                file: button.file
                anchors.leftMargin: button.width / 2 - width / 2 - button.padding
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
    D{i:0;formeditorZoom:2;height:64;width:64}
}
##^##*/
