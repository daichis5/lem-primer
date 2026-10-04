import math

import numpy as np
import pytest

import infinite_slope


def test_traction_splits_into_normal_and_shear():
    n, m = infinite_slope.plane_vectors(30.0)
    t = -50.0 * n + 20.0 * (-m)  # pushes with 50 kPa and resists sliding with 20 kPa
    sigma_n, shear = infinite_slope.split_traction(t, n)
    assert sigma_n == pytest.approx(50.0)
    assert np.allclose(shear, 20.0 * (-m))
    assert shear @ n == pytest.approx(0.0, abs=1e-12)


def test_stresses_on_the_slip_plane_by_hand():
    sigma_n, tau = infinite_slope.base_stresses(30.0, 18.0 * 5.0)
    assert sigma_n == pytest.approx(90.0 * math.cos(math.radians(30.0)) ** 2)
    assert tau == pytest.approx(
        90.0 * math.sin(math.radians(30.0)) * math.cos(math.radians(30.0))
    )


def test_dry_sand_at_its_friction_angle_is_just_stable():
    sigma_n, tau = infinite_slope.base_stresses(35.0, 18.0 * 2.0)
    assert infinite_slope.factor_of_safety(
        sigma_n, tau, 0.0, 0.0, 35.0
    ) == pytest.approx(1.0)


def test_the_base_of_section_6_of_document_1():
    beta = math.degrees(math.atan(0.3))
    w = 100.0 / math.cos(math.radians(beta)) ** 2
    sigma_n, tau = infinite_slope.base_stresses(beta, w)
    assert (sigma_n, tau) == pytest.approx((100.0, 30.0))
    assert infinite_slope.factor_of_safety(
        sigma_n, tau, 40.0, 10.0, 30.0
    ) == pytest.approx(1.488, abs=1e-3)
    assert infinite_slope.factor_of_safety(
        sigma_n, tau, 60.0, 10.0, 30.0
    ) == pytest.approx(1.103, abs=1e-3)


def test_the_two_water_rules_differ_by_cos_squared():
    parallel = infinite_slope.pore_pressure(5.0, 30.0, "parallel")
    vertical = infinite_slope.pore_pressure(5.0, 30.0, "vertical")
    assert vertical == pytest.approx(9.81 * 5.0)
    assert parallel == pytest.approx(vertical * math.cos(math.radians(30.0)) ** 2)


def test_only_the_vertical_rule_makes_the_effective_stress_negative():
    w = infinite_slope.column_weight(5.0, 18.0, h_w=5.0, gamma_sat=20.0)
    sigma_n, _ = infinite_slope.base_stresses(50.0, w)
    assert sigma_n - infinite_slope.pore_pressure(5.0, 50.0, "parallel") > 0.0
    assert sigma_n - infinite_slope.pore_pressure(5.0, 50.0, "vertical") < 0.0


def test_a_deeper_plane_is_less_stable():
    fs = []
    for z in (2.0, 5.0, 10.0):
        sigma_n, tau = infinite_slope.base_stresses(
            30.0, infinite_slope.column_weight(z, 18.0)
        )
        fs.append(infinite_slope.factor_of_safety(sigma_n, tau, 0.0, 10.0, 30.0))
    assert fs[0] > fs[1] > fs[2]
