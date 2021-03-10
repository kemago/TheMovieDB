import QtQuick 2.0
import QtQuick.Layouts 1.15

Item {
    ColumnLayout{
        anchors.fill: parent

        // navbar
        NavBar{
            Layout.fillWidth: true
            //Layout.alignment: Qt.AlignTop
        }

        RowLayout{
            Layout.fillHeight: true
            Layout.fillWidth: true

            // filter panel
            FilterPanel{
                Layout.fillHeight: true
            }

            // grid wiew
            MovieGridView{
                Layout.fillHeight: true
                Layout.fillWidth: true
            }

        }
   }


}
