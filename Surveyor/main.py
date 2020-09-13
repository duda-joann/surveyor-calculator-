import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt
from function import (
        count_length, convert_degree_to_radians,
        convert_degree_to_grad,
        convert_grad_to_radians,
        count_azimuth,
        convert_grad_to_degree,
        count_horizontal_angle,
        count_area_with_gauss
)


class Calculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.interface()

    def interface(self):
        """
         set defqault parametres to  gui and layout
        :return:  None

        """
        self.setStyleSheet("background-color: beige;")
        self.resize(400, 400)
        self.setWindowTitle("Surveyor's Calculator")
        self.show()

        # Labels
        label_1 = QLabel("Point 1:", self)
        label_2 = QLabel("Point 2:", self)
        label_3 = QLabel("Point 3:", self)
        label_4 = QLabel("Angle:", self)
        label_5 = QLabel("Result", self)

        #user input
        self.point1 = QLineEdit()
        self.point2 = QLineEdit()
        self.point3 = QLineEdit()
        self.angle = QLineEdit()
        self.result = QLineEdit()

        self.result.readonly = True
        self.result.setToolTip('Insert number and choose action...')

        Layout = QGridLayout()
        Layout.addWidget(label_1, 0, 0)
        Layout.addWidget(label_2, 0, 2)
        Layout.addWidget(label_3, 0, 4)
        Layout.addWidget(label_4, 1, 0)
        Layout.addWidget(label_5, 1, 2)
        Layout.addWidget(self.point1, 0, 1)
        Layout.addWidget(self.point2, 0, 3)
        Layout.addWidget(self.point3, 0, 5)
        Layout.addWidget(self.angle, 1, 1)
        Layout.addWidget(self.result, 1, 3)

        #Buttons
        azimuth_button = QPushButton("Azimuth", self)
        length_button = QPushButton("Length", self)
        grad_button = QPushButton("Grad", self)
        degree_button = QPushButton("Degree", self)
        horizontal_angle_button = QPushButton("Horizontal Angle", self)
        gauss_area_button = QPushButton("Gauss Area", self)
        import_data = QPushButton("Import coordinates", self)
        end_button = QPushButton("Finish work on today", self)
        radian_button = QPushButton("Radian", self)
        end_button.resize(end_button.sizeHint())

        # adding buttons to layout
        Layout2 = QHBoxLayout()
        Layout2.addWidget(azimuth_button)
        Layout2.addWidget(length_button)
        Layout2.addWidget(grad_button)
        Layout2.addWidget(degree_button)
        Layout2.addWidget(radian_button)
        Layout2.addWidget(horizontal_angle_button)
        Layout2.addWidget(gauss_area_button)
        Layout2.addWidget(import_data)

        Layout.addLayout(Layout2, 2, 0, 2, 3)
        self.setLayout(Layout)
        self.setGeometry(20, 20, 400, 100)
        self.setWindowIcon(QIcon('surveyor.jpg'))
        Layout.addWidget(end_button, 3, 0, 2, 3)

        end_button.clicked.connect(self.end)
        azimuth_button.clicked.connect(self.perform_an_action)
        length_button.clicked.connect(self.perform_an_action)
        grad_button.clicked.connect(self.perform_an_action)
        degree_button.clicked.connect(self.perform_an_action)
        horizontal_angle_button.clicked.connect(self.perform_an_action)
        gauss_area_button.clicked.connect(self.perform_an_action)
        radian_button.clicked.connect(self.perform_an_action)

    def end(self) -> None:
        """
        closes program
        :return:
        """
        self.close()

    def closeEvent(self, event) -> None:
        """
        :param event:
        :return: None
        """
        answer = QMessageBox.question(
            self, 'Alert',
            "Are you sure to exit?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if answer == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def perform_an_action(self):
        sender_action = self.sender()
        try:
            point1 = [float(i.strip()) for i in self.point1.text().split()]
            point2 = [float(i.strip()) for i in self.point2.text().split()]
            point3 = [float(i.strip()) for i in self.point3.text().split()]
            angle = float(self.angle.text().strip())
            result = " "

            if sender_action.text() == "Azimuth":
                result = count_azimuth(point1, point2)
            elif sender_action.text() == "Length":
                result = count_length(point1, point2)
            elif sender_action.text() == "Gauss Area":
                result = count_area_with_gauss(point1, point3, point2)
            elif sender_action.text() == "Grad":
                result = convert_degree_to_grad(angle)
            elif sender_action.text() == "Degree":
                result = convert_grad_to_degree(angle)
            elif sender_action.text() == "Radian":
                result = convert_degree_to_radians(angle)
            elif sender_action.text() == "Horizontal Angle":
                result = count_horizontal_angle
            else:
                result = 0

            return self.result.setText(str(result))

        except ValueError:
            QMessageBox.warning(self, "Error", "Incorrrect Data", QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec_())
