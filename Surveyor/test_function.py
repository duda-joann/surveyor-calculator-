import unittest

from function import (
                        count_length,
                        convert_degree_to_radians,
                        convert_degree_to_grad,
                        convert_grad_to_radians,
                        count_azimuth,
                        count_horizontal_angle,
                        count_area_with_gauss,
                        convert_grad_to_degree, )
from exception import AzimuthError


class TestLength(unittest.TestCase):

    def test_count_length(self):
        self.assertAlmostEqual(count_length([50, 0], [0, 50]), 70.710678, 6)

    def test_count_length2(self):
        self.assertEqual(count_length([50, 50], [50, 50]), 0)

    def test_count_length3(self):
        self.assertAlmostEqual(count_length([0, 50], [50, 0]), 70.710678, 6)


class TestDegreeToRadians(unittest.TestCase):

    def test_convert_degree_to_radians(self):
        self.assertAlmostEqual(convert_degree_to_radians(180), 3.1416, 4)

    def test_convert_degree_to_radians2(self):
        self.assertAlmostEqual(convert_degree_to_radians(0), 0.0000, 4)

    def test_convert_degree_to_radians3(self):
        self.assertAlmostEqual(convert_degree_to_radians(90), 1.5708, 4)


class TestDegreeToGrad(unittest.TestCase):

    def test_convert_degree_to_grad(self):
        self.assertEqual(convert_degree_to_grad(180), 200)

    def test_convert_degree_to_grad2(self):
        self.assertEqual(convert_degree_to_grad(0), 0)

    def test_convert_degree_to_grad3(self):
        self.assertAlmostEqual(convert_degree_to_grad(56), 62.2222, 4)


class TestGradTORadians(unittest.TestCase):
    def test_convert_grad_to_radians(self):
        self.assertAlmostEqual(convert_grad_to_radians(200), 3.4907, 4)

    def test_convert_grad_to_radians2(self):
        self.assertEqual(convert_grad_to_radians(0), 0)

    def test_convert_grad_to_radians3(self):
        self.assertAlmostEqual(convert_grad_to_radians(500), 8.7266, 4)


class TestAzimuth(unittest.TestCase):
    def test_count_azimuth(self):
        self.assertRaises(AzimuthError, count_azimuth, [100, 100], [100, 100])

    def test_count_azimuth2(self):
        self.assertAlmostEqual(count_azimuth([0, 0], [0, 5]), 200.0000, 4)

    def test_count_azimuth3(self):
        self.assertAlmostEqual(count_azimuth([10, 10], [45, 45]), 200.0137, 4)


class TestHorizontalAngle(unittest.TestCase):
    def count_horizontal_angle(self):
        self.assertEqual(count_horizontal_angle([0,10], [0,0], [10,0]), 100)

    def count_horizontal_angle2(self):
        self.assertAlmostEqual(count_horizontal_angle([-6, 6], [-7, 18], [19, 60]), 178)

    def count_horizontal_angle3(self):
        self.assertAlmostEqual(count_horizontal_angle([-34, 5], [34, 6], [56, -8]), 123,4)


class TestArea(unittest.TestCase):
    def test_count_area_with_gauss(self):
        self.assertAlmostEqual(count_area_with_gauss([0,50], [0,0], [10,0], [50,40]), 1450)

    def test_count_area_with_gauss2(self):
        self.assertAlmostEqual(count_area_with_gauss([0,0], [10, 10], [10,0], [10,0]), 50)

    def test_count_area_with_gauss3(self):
        self.assertAlmostEqual(count_area_with_gauss([0, 0], [5, 25],[10, 50], [12, 18], [14, 10]), 276.00, 2)


class TestGradToDegree(unittest.TestCase):
    def test_convert_grad_to_degree(self):
        self.assertEqual(convert_grad_to_degree(200), 180,)

    def test_convert_grad_to_degree2(self):
        self.assertEqual(convert_grad_to_degree(0), 0)

    def test_convert_grad_to_degree3(self):
        self.assertAlmostEqual(convert_grad_to_degree(55), 49.50, 2)


if __name__ == '__main__':
    unittest.main()