import math

import numpy as np
import pytest

import infinite_slope
import slices


def test_the_slice_table_by_hand():
    s = slices.make_slices(slices.Circle(), 6)
    assert s.b == pytest.approx(np.full(6, (slices.Circle().x1 + 1.0) / 6))
    # 3本目のスライス：幅の中央 x = 9.24 m の底面と地表の高さから重さを求める
    x = s.x[2]
    z = 18.0 - math.sqrt(slices.Circle().radius ** 2 - (x - 6.0) ** 2)
    assert s.W[2] == pytest.approx(18.0 * s.b[2] * (float(slices.ground(x)) - z))
    assert math.degrees(s.alpha[2]) == pytest.approx(9.66, abs=0.01)


def test_on_a_circle_every_normal_passes_through_the_centre():
    s = slices.make_slices(slices.Circle(), 6)
    r = np.stack([s.x - 6.0, s.z - 18.0], axis=1)
    assert np.allclose(slices.cross(r, s.n), 0.0, atol=1e-12)


def test_the_three_formulas_on_the_circle_of_figure_1():
    s = slices.make_slices(slices.Circle(), 50)
    assert slices.fellenius(s) == pytest.approx(1.888, abs=1e-3)
    assert slices.bishop(s) == pytest.approx(2.063, abs=1e-3)
    assert slices.janbu(s) == pytest.approx(1.868, abs=1e-3)


def test_theta_zero_gives_simplified_bishop_and_janbu():
    s = slices.make_slices(slices.Circle(), 50)
    assert slices.fs_moment(s, 0.0, (6.0, 18.0)) == pytest.approx(
        slices.bishop(s), abs=1e-9
    )
    assert slices.fs_force(s, 0.0) == pytest.approx(slices.janbu(s), abs=1e-9)


def test_spencer_satisfies_both_force_and_moment_equilibrium():
    s = slices.make_slices(slices.Circle(), 50)
    fs, theta = slices.spencer(s, (6.0, 18.0))
    assert fs == pytest.approx(2.059, abs=1e-3)
    assert math.degrees(theta) == pytest.approx(18.3, abs=0.1)
    force, moment = slices.residuals(s, fs, theta, (6.0, 18.0))
    assert abs(force) < 1e-6 and abs(moment) < 1e-6


def test_a_plane_under_a_planar_slope_gives_the_infinite_slope():
    line = slices.Line(30.0, 5.0)
    s = slices.make_slices(line, 8, ground=line.ground)
    sigma_n, tau = infinite_slope.base_stresses(30.0, 18.0 * 5.0)
    expected = infinite_slope.factor_of_safety(sigma_n, tau, 0.0, 10.0, 30.0)
    for fs in (slices.fellenius(s), slices.bishop(s), slices.janbu(s)):
        assert fs == pytest.approx(expected)


def test_fellenius_about_the_centre_of_a_circle_is_the_formula():
    s = slices.make_slices(slices.Circle(), 50)
    assert slices.fellenius_about(s, (6.0, 18.0)) == pytest.approx(slices.fellenius(s))


def test_the_moment_centre_matters_only_where_force_equilibrium_is_missing():
    s = slices.make_slices(slices.Ellipse(), 50)
    o, up, right = (6.0, 18.0), (6.0, 25.0), (10.0, 18.0)
    # 全体の力のつり合いを満たさない Fellenius法は，上にも右にも移動させると値が変わる
    assert slices.fellenius_about(s, up) != pytest.approx(
        slices.fellenius_about(s, o), abs=1e-3
    )
    assert slices.fellenius_about(s, right) != pytest.approx(
        slices.fellenius_about(s, o), abs=1e-3
    )
    # 鉛直方向のつり合いを満たす簡易Bishop法は，横に移動させても変わらない
    bishop_o = slices.fs_moment(s, 0.0, o)
    assert slices.fs_moment(s, 0.0, up) != pytest.approx(bishop_o, abs=1e-3)
    assert slices.fs_moment(s, 0.0, right) == pytest.approx(bishop_o, abs=1e-9)
    # 力とモーメントのつり合いをともに満たす Spencer法は，どこに移動させても変わらない
    spencer_o = slices.spencer(s, o)[0]
    assert slices.spencer(s, up)[0] == pytest.approx(spencer_o, abs=1e-6)
    assert slices.spencer(s, right)[0] == pytest.approx(spencer_o, abs=1e-6)
