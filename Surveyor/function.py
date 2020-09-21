import math
from exception import AzimuthError


def count_length(end_point: list, start_point: list) -> float:
    """
    :param end_point: tuple contains: point number, coordinate x, coordinate y
    :param start_point: tuple contains: point number, coordinate x, coordinate y
    :return: return length  of section
    """
    dx = end_point[0] - start_point[0]
    dy = end_point[1] - start_point[1]
    return math.sqrt(dx ** 2 + dy ** 2)


def convert_degree_to_grad(degree: float) -> float:
    """
    :param degree:  value provides by user
    :return:  value in grad
    """
    return degree * 10 / 9


def convert_grad_to_degree(grad: float) -> float:
    """
    :param grad: value provides by user
    :return: value in  degree
    """
    return grad * 9/10


def convert_degree_to_radians(degree: float) -> float:
    """
    :param degree: value  provides by user
    :return:
    """
    return degree * math.pi / 180


def convert_grad_to_radians(grad: float) -> float:
    """
    :param grad:
    :return:
    """
    return grad * math.pi / 180


def count_azimuth(end_point: list, start_point: list) -> float:
    """
    azimuth - angle measures clockwise between north and line; always positive

    :param end_point: tuple contains:  coordinate x, coordinate y
    :param start_point: tuple contains:  coordinate x, coordinate y
    :return: value of azimuth in grad
    """

    coordinate_increment_by_axxis_x = end_point[0] - start_point[0]
    coordinate_increment_by_axxis_y = end_point[1] - start_point[1]

    if coordinate_increment_by_axxis_x == 0 and coordinate_increment_by_axxis_y == 0:
        raise AzimuthError
    else:
        if coordinate_increment_by_axxis_x == 0 and coordinate_increment_by_axxis_y > 0:
            return 0
        elif coordinate_increment_by_axxis_x > 0 and coordinate_increment_by_axxis_y == 0:
            return 100
        elif coordinate_increment_by_axxis_x == 0 and coordinate_increment_by_axxis_y < 0:
            return 200
        elif coordinate_increment_by_axxis_x < 0 and coordinate_increment_by_axxis_y == 0:
            return 300
        else:
            angle_degrees = math.atan(coordinate_increment_by_axxis_y / coordinate_increment_by_axxis_x)
            angle = convert_degree_to_radians(angle_degrees)


        if coordinate_increment_by_axxis_x > 0 and coordinate_increment_by_axxis_y > 0:
            return angle
        elif coordinate_increment_by_axxis_x < 0 and coordinate_increment_by_axxis_y > 0:
            return 200 + angle
        elif coordinate_increment_by_axxis_x < 0 and coordinate_increment_by_axxis_y < 0:
            return angle + 200
        else:
            return 400 + angle


def count_horizontal_angle(left_point: list, centre_point: list, right_point: list) -> float:
    """
    counts horizontal angle between three points
    :param left_point:
    :param centre_point:
    :param right_point:
    :return: horizontal angle
    """
    return count_azimuth(left_point, centre_point) - count_azimuth(right_point, centre_point)


def count_area_with_gauss(*args) -> float:
    """
    :param points: list contains  breakpoints of borders,
    a breakpoint  has got attributtes as  value  on x-axxis, y-xxis and  height; unit of measure: meter
    :return: area, unit [square meter]
    """
    points = [item for item in args]
    area = 0
    for count, point in enumerate(points):
        if 1 <= count <= len(points)-2:
            coordinate_increment = (points[count + 1][0] - points[count - 1][0]) * points[count][1]
            area += coordinate_increment
        elif count == 0:
            coordinate_increment = (points[1][0] - points[-1][0]) * points[0][1]
            area += coordinate_increment

        elif count == len(points) -1:
                coordinate_increment = (points[0][0] - points[count - 1][0]) * points[count][1]
                area += coordinate_increment

    return abs(area / 2)




