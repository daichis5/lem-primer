import numpy as np
import pytest

import columns
import infinite_slope
import slices

D = np.array([-1.0, 0.0, 0.0])
AXIS = np.array([0.0, 1.0, 0.0])
CENTRE = np.array([6.0, 0.0, 18.0])
R = slices.Circle().radius


def test_the_column_table_by_hand():
    col = columns.make_columns(columns.Ellipsoid(CENTRE, (R, R, R)), 0.5)
    i = 0
    x, y, z = col.base[i]
    assert (x - 6.0) ** 2 + y**2 + (z - 18.0) ** 2 == pytest.approx(R**2)
    assert col.n[i] == pytest.approx((col.base[i] - CENTRE) / R)
    assert col.A[i] == pytest.approx(0.25 / abs(col.n[i, 2]))
    assert col.W[i] == pytest.approx(18.0 * 0.25 * (float(slices.ground(x)) - z))


def test_both_local_directions_lie_in_the_base():
    col = columns.make_columns(columns.Ellipsoid(CENTRE, (R, R, R)), 0.5)
    for m in (columns.dip_directions(col, D), columns.projected_directions(col, D)):
        assert np.allclose(np.linalg.norm(m, axis=1), 1.0)
        assert np.allclose(np.sum(m * col.n, axis=1), 0.0, atol=1e-12)
        assert np.all(m @ D > 0.0)


def test_a_plane_under_a_planar_slope_gives_the_infinite_slope():
    plane = columns.Plane(30.0, 5.0)
    col = columns.make_columns(plane, 0.5, ground=plane.ground)
    sigma_n, tau = infinite_slope.base_stresses(30.0, 18.0 * 5.0)
    expected = infinite_slope.factor_of_safety(sigma_n, tau, 0.0, 10.0, 30.0)
    centre = np.array([10.0, 10.0, 30.0])
    assert columns.hovland(col, columns.dip_directions(col, D)) == pytest.approx(
        expected
    )
    assert columns.hovland_moment(col, centre, AXIS) == pytest.approx(expected)
    assert columns.bishop(col, centre, AXIS) == pytest.approx(expected)


def test_a_cylinder_gives_the_2d_values():
    col = columns.make_columns(columns.Cylinder(10.0), 0.25)
    s = slices.make_slices(slices.Circle(), 200)
    assert columns.hovland(col, columns.dip_directions(col, D)) == pytest.approx(
        slices.fellenius(s), abs=5e-3
    )
    assert columns.hovland_moment(col, CENTRE, AXIS) == pytest.approx(
        slices.fellenius(s), abs=5e-3
    )
    assert columns.bishop(col, CENTRE, AXIS) == pytest.approx(
        slices.bishop(s), abs=5e-3
    )


def test_the_sphere():
    col = columns.make_columns(columns.Ellipsoid(CENTRE, (R, R, R)), 0.25)
    assert columns.hovland(col, columns.dip_directions(col, D)) == pytest.approx(
        1.816, abs=1e-3
    )
    assert columns.hovland(col, columns.projected_directions(col, D)) == pytest.approx(
        2.122, abs=1e-3
    )
    assert columns.bishop(col, CENTRE, AXIS) == pytest.approx(2.142, abs=1e-3)


def test_a_symmetric_slip_surface_is_least_stable_straight_down_the_slope():
    col = columns.make_columns(columns.Ellipsoid(CENTRE, (R, R, R)), 0.5)
    fs = []
    for deg in (-15.0, 0.0, 15.0):
        t = np.radians(deg)
        d = np.array([-np.cos(t), np.sin(t), 0.0])
        fs.append(columns.hovland(col, columns.dip_directions(col, d)))
    assert fs[1] < fs[0] and fs[1] < fs[2]
    assert fs[0] == pytest.approx(fs[2])


def test_the_saved_table(tmp_path):
    col = columns.make_columns(columns.Ellipsoid(CENTRE, (R, 2 * R, R)), 1.0)
    columns.save_columns(tmp_path / "columns.npz", col, CENTRE, AXIS)
    saved = np.load(tmp_path / "columns.npz")
    assert np.array_equal(saved["normal"], col.n)
    assert np.array_equal(saved["center"], CENTRE)
    assert saved["friction_angle_deg"] == pytest.approx(np.full(len(col.W), 30.0))
