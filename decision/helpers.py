import re
from math import acos, sqrt, pow, fabs


def parse_coords(polygon_input: str) -> list:
    """
    Method parse coordinates of dots into list of int pairs.
    (1,2)(3,4)(5,6) -> [[1,2], [3,4], [5,6]]
    :param polygon_input: string
    :return: list of int pairs
    """
    ready_pattern = re.compile("-?\d{1,5},-?\d{1,5}")
    # find all numbers with format {number,number}
    dots_str_tuples = re.findall(ready_pattern, polygon_input)
    # go through all founded strings, split it by , and transform it into int
    coords = [list(map(int, dot_str_tuple.split(','))) for dot_str_tuple in dots_str_tuples]
    return coords


def are_polygons_identical(polygon1: list, polygon2: list) -> int:
    """
    Method define are polygons identical.
    First assert polygons have same number of points.
    Second assert they have same angles.
    Third assert polygons have same sides.
    :param polygon1: list of coord pars
    :param polygon2: list of coord pars
    :return: 1 if polygons edintical, 0 if not
    """
    if len(polygon1) != len(polygon2):
        return 0
    elif set(calc_polygon_angles(polygon1)) != set(calc_polygon_angles(polygon2)):
        return 0
    elif set(calc_polygon_sides(polygon1)) != set(calc_polygon_sides(polygon2)):
        return 0
    return 1


def calc_polygon_angles(polygon: list) -> list:
    """
    Method calc polygon angles.
    :param polygon: list of coord pairs
    :return: list of angles
    """
    angles = []
    for i in range(len(polygon)):
        base_point = polygon[i]
        left_point = polygon[i - 1]
        right_point = polygon[i + 1 if i < len(polygon) - 1 else 0]
        angle = calc_angle(base_point, left_point, right_point)
        angles.append(angle)
    return angles


def calc_angle(point: list, left_point: list, right_point: list) -> float:
    """
    Method calc angle by using (scalar vector multiplication) / (multiplication of vector`s length).
    :param point: list, coords of base point
    :param left_point: list, coords of left point of the angle
    :param right_point: list, coords of the right point of the angle
    :return: angle in radians
    """
    left_vector = calc_vector_coords(point, left_point)
    right_vector = calc_vector_coords(point, right_point)
    angle_cos = (calc_scalar_vector_mult(left_vector, right_vector)) / \
                (calc_vector_length(left_vector) * calc_vector_length(right_vector))
    return acos(angle_cos)


def calc_vector_coords(start_point: list, finish_point: list) -> list:
    """
    Method calc vector coordinates.
    :param start_point: list, coords of the start point
    :param finish_point: list, coords of the end point
    :return: list, coords of the vector
    """
    return [finish_coord - start_coord for start_coord, finish_coord in zip(start_point, finish_point)]


def calc_scalar_vector_mult(vector1: list, vector2: list) -> int:
    """
    Method calc scalar vector multiplication.
    (x1, y1) * (x2, y2) = x1 * x2 + y1 * y2
    :param vector1: list, coords of the vector
    :param vector2: list, coords of the vector
    :return: int valur of the scalar multiplication.
    """
    return sum([start_coord * finish_coord for start_coord, finish_coord in zip(vector1, vector2)])


def calc_vector_length(vector: list) -> float:
    """
    Method calc length of the vector.
    :param vector: list, coords of the vector
    :return: float value of the length
    """
    coord_diff_squares = (pow(coord, 2) for coord in vector)
    return fabs(sqrt(sum(coord_diff_squares)))


def calc_polygon_sides(polygon: list) -> list:
    """
    Method calc polygon sides.
    :param polygon: list, vector coords
    :return: list of the sides
    """
    sides = []
    for i in range(len(polygon)):
        start_point = polygon[i - 1]
        finish_point = polygon[i]
        side = calc_vector_length(calc_vector_coords(start_point, finish_point))
        sides.append(side)
    return sides


filename = input("Please, enter the filename\n")
with open(filename, "rt") as source:
    input_text = source.readlines()
polygon_fst_str, polygon_sec_str = input_text
polygon_fst = parse_coords(polygon_fst_str)
polygon_sec = parse_coords(polygon_sec_str)

print(are_polygons_identical(polygon_fst, polygon_sec))
