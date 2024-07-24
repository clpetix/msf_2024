# Import package, test suite, and other packages as needed
import sys

import pytest
import numpy

import msf_2024

def test_angle():
    rA = numpy.array([0, 0, -1])
    rB = numpy.array([0, 0, 0])
    rC = numpy.array([1, 0, 0])

    calc_angle_radian = msf_2024.measure.calculate_angle(rA, rB, rC)
    expected_radian = numpy.pi / 2
    assert numpy.isclose(calc_angle_radian, expected_radian)

    calc_angle_degree = msf_2024.measure.calculate_angle(rA, rB, rC, degrees=True)
    expected_degree = 90
    assert calc_angle_degree == expected_degree
