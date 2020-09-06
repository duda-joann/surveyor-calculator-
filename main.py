import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt


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
        end_button = QPushButton("Finish work on today", self)
        end_button.resize(end_button.sizeHint())

        # adding buttons to layout
        Layout2 = QHBoxLayout()
        Layout2.addWidget(azimuth_button)
        Layout2.addWidget(length_button)
        Layout2.addWidget(grad_button)
        Layout2.addWidget(degree_button)
        Layout2.addWidget(horizontal_angle_button)
        Layout2.addWidget(gauss_area_button)

        Layout.addLayout(Layout2, 2, 0, 2, 3)
        self.setLayout(Layout)
        self.setGeometry(20, 20, 300, 100)
        self.setWindowIcon(QIcon('surveyor.jpg'))
        Layout.addWidget(end_button, 3, 0, 2, 3)

        end_button.clicked.connect(self.end)
        azimuth_button.clicked.connect(self.perform_an_action)
        length_button.clicked.connect(self.perform_an_action)
        grad_button.clicked.connect(self.perform_an_action)
        degree_button.clicked.connect(self.perform_an_action)
        horizontal_angle_button.clicked.connect(self.perform_an_action)
        gauss_area_button.clicked.connect(self.perform_an_action)

    @staticmethod
    def count_difference(end, start):
        """
        :param end:
        :param start:
        :return:
        """
        return end - start

    @staticmethod
    def count_length(end_point: (tuple), start_point: (tuple)) -> float:
        """
        :param end_point: tuple contains: point number, coordinate x, coordinate y
        :param start_point: tuple contains: point number, coordinate x, coordinate y
        :return: return length  of section
        """
        dx = end_point[1] - start_point[1]
        dy = end_point[2] - start_point[2]
        return math.sqrt(dx ** 2 + dy ** 2)

    def convert_degree_to_grad (self, degree: float) -> float:
        """
        :param degree:  value provides by user
        :return:  value in grad
        """
        return degree * 10 / 9

    def convert_grad_to_degree(self, grad: float) -> float:
        """
        :param grad: value provides by user
        :return: value in  degree
        """
        return grad * 10 / 9

    def convert_degree_to_radians(self, degree: float) -> float:
        """
        :param degree: value  provides by user
        :return:
        """
        return degree * math.pi / 180

    def convert_grad_to_radians (self, grad: float) -> float:
        """
        :param grad:
        :return:
        """
        return grad * math.pi / 180

    def count_azimuth(self, end_point, start_point) -> float:
        """
        azimuth - angle measures clockwise between north and line; always positive

        :param end_point: tuple contains: point number, coordinate x, coordinate y
        :param start_point: tuple contains: point number, coordinate x, coordinate y
        :return: value of azimuth in grad
        """

        coordinate_increment_by_axxis_x = end_point[1] - start_point[1]
        coordinate_increment_by_axxis_y = end_point[2] - start_point[2]
        angle = math.degrees(math.atan(coordinate_increment_by_axxis_y / coordinate_increment_by_axxis_x))* 10/9

        if coordinate_increment_by_axxis_x > 0 and coordinate_increment_by_axxis_y > 0:
            return angle
        elif coordinate_increment_by_axxis_x == 0 and coordinate_increment_by_axxis_y > 0:
            return 100
        elif coordinate_increment_by_axxis_x < 0 and coordinate_increment_by_axxis_y == 0:
            return 200
        elif coordinate_increment_by_axxis_x == 0 and coordinate_increment_by_axxis_y < 0:
            return 300
        elif coordinate_increment_by_axxis_x == 0 and coordinate_increment_by_axxis_y == 0:
            return 0
        elif coordinate_increment_by_axxis_x < 0 and coordinate_increment_by_axxis_y > 0:
            return 200 + angle
        elif coordinate_increment_by_axxis_x < 0 and coordinate_increment_by_axxis_y < 0:
            return angle + 200
        else:
            return 400 + angle

    def count_horizontal_angle(self, left_point: tuple, centre_point: tuple, right_point: tuple) -> float:
        """
        counts horizontal angle between three points
        :param left_point:
        :param centre_point:
        :param right_point:
        :return: horizontal angle
        """
        return self.count_azimuth(left_point, centre_point) - self.count_azimuth(right_point, centre_point)

    def count_area_with_gauss(self, *points: list) -> float:
        """
        :param points: list contains  breakpoints of borders,
        a breakpoint  has got attributtes as  value  on x-axxis, y-xxis and  height; unit of measure: meter
        :return: area, unit [square meter]
        """
        area = 0
        for count, point in enumerate(points):
            coordinate_increment = (points[count + 1][1] - points[count - 1][1]) * points[count][2]
            area += coordinate_increment
            return area / 2

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
            point1 = [float(i) for i in self.point1.text().split()]
            point2 = [float(i) for i in self.point1.text().split()]
            point3 = [float(i) for i in self.point1.text().split()]
            result = " "

            if sender_action.text() == "Azimuth":
                result = self.count_azimuth(point1, point2)

            else:
                result = 0

            self.result.setText(str(result))

        except ValueError:
            QMessageBox.warning(self, "Error", "Incorrrect Data", QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec_())
