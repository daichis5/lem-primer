"""Check the values quoted in the answers to the review questions.

Readers do not download this file. CI runs it to keep the pages' answers in step
with the code.
"""

import math
import runpy
from pathlib import Path

import numpy as np
import pytest

import columns
import infinite_slope
import slices

CENTRE_3D = np.array([6.0, 0.0, 18.0])
AXIS = np.array([0.0, 1.0, 0.0])
D = np.array([-1.0, 0.0, 0.0])
R = slices.Circle().radius


def base_stresses_seismic(beta_deg, w, k):
    """Answer to Practice 1, Q3: base_stresses with a horizontal force k w downslope."""
    n, _ = infinite_slope.plane_vectors(beta_deg)
    weight = np.array([-k * w, -w])
    area = 1.0 / math.cos(math.radians(beta_deg))
    sigma_n, shear = infinite_slope.split_traction(-weight / area, n)
    return sigma_n, float(np.linalg.norm(shear))


def test_practice_1():
    sigma_n, tau = infinite_slope.base_stresses(25.0, 18.0 * 3.0)
    assert (sigma_n, tau) == pytest.approx((44.36, 20.68), abs=0.01)
    assert infinite_slope.factor_of_safety(
        sigma_n, tau, 0.0, 10.0, 30.0
    ) == pytest.approx(1.722, abs=1e-3)

    sigma_n, tau = base_stresses_seismic(30.0, 90.0, 0.2)
    assert (sigma_n, tau) == pytest.approx((59.71, 52.47), abs=0.01)
    assert infinite_slope.factor_of_safety(
        sigma_n, tau, 0.0, 10.0, 30.0
    ) == pytest.approx(0.848, abs=1e-3)
    assert infinite_slope.factor_of_safety(
        *base_stresses_seismic(30.0, 90.0, 0.1), 0.0, 10.0, 30.0
    ) == pytest.approx(1.022, abs=1e-3)

    w = infinite_slope.column_weight(5.0, 18.0, h_w=5.0, gamma_sat=20.0)
    sigma_n, tau = infinite_slope.base_stresses(50.0, w)
    u = infinite_slope.pore_pressure(5.0, 50.0, "vertical")
    assert infinite_slope.factor_of_safety(
        sigma_n, tau, u, 10.0, 30.0
    ) == pytest.approx(0.112, abs=1e-3)
    assert infinite_slope.factor_of_safety(
        sigma_n, tau, sigma_n, 10.0, 30.0
    ) == pytest.approx(0.203, abs=1e-3)

    for z in (2.0, 5.0, 10.0):
        sigma_n, tau = infinite_slope.base_stresses(30.0, 18.0 * z)
        assert infinite_slope.factor_of_safety(
            sigma_n, tau, 0.0, 0.0, 35.0
        ) == pytest.approx(1.213, abs=1e-3)


def test_practice_2():
    s = slices.make_slices(slices.Circle(), 6)
    fs = slices.bishop(s)
    m_alpha = np.cos(s.alpha) + np.sin(s.alpha) * s.tan_phi / fs
    assert m_alpha == pytest.approx(
        [0.894, 0.987, 1.033, 1.032, 0.973, 0.822], abs=1e-3
    )

    s = slices.make_slices(slices.Circle(), 50)
    assert slices.residuals(s, slices.bishop(s), 0.0, (6.0, 18.0))[0] == pytest.approx(
        86.7, abs=0.1
    )
    assert np.sum(s.W) == pytest.approx(2415.6, abs=0.1)

    s = slices.make_slices(slices.Circle(), 50, phi_deg=25.0)
    fs, theta = slices.spencer(s, (6.0, 18.0))
    assert (
        slices.fellenius(s),
        slices.bishop(s),
        slices.janbu(s),
        fs,
    ) == pytest.approx((1.594, 1.734, 1.575, 1.731), abs=1e-3)
    assert math.degrees(theta) == pytest.approx(17.9, abs=0.1)
    # Q5: the ratio to phi' = 30 deg is about 0.84, above the tan(phi') ratio of 0.81
    base = slices.make_slices(slices.Circle(), 50)
    for method in (slices.fellenius, slices.bishop, slices.janbu):
        assert method(s) / method(base) == pytest.approx(0.84, abs=5e-3)
    assert fs / slices.spencer(base, (6.0, 18.0))[0] == pytest.approx(0.84, abs=5e-3)
    assert math.tan(math.radians(25.0)) / math.tan(math.radians(30.0)) == pytest.approx(
        0.81, abs=5e-3
    )

    assert slices.bishop(
        slices.make_slices(slices.Circle((4.0, 16.0)), 50)
    ) == pytest.approx(1.790, abs=1e-3)

    # values on the circle with water, quoted by Practice 3, Q6
    s = slices.make_slices(slices.Circle(), 50, water_level=4.0)
    assert (slices.fellenius(s), slices.bishop(s)) == pytest.approx(
        (1.402, 1.540), abs=1e-3
    )
    assert np.sum(s.u * s.l) / np.sum(s.W) == pytest.approx(0.28, abs=5e-3)


def test_practice_3():
    assert 0.25**2 / math.cos(math.radians(30.0)) == pytest.approx(0.0722, abs=1e-4)

    sphere = columns.Ellipsoid(CENTRE_3D, (R, R, R))
    wet = columns.make_columns(sphere, 0.25, water_level=4.0)
    assert columns.hovland(wet, columns.section_directions(wet, D)) == pytest.approx(
        1.418, abs=1e-3
    )
    wet_bishop = columns.bishop(wet, CENTRE_3D, AXIS)
    assert wet_bishop == pytest.approx(1.699, abs=1e-3)
    assert np.sum(wet.u * wet.A) / np.sum(wet.W) == pytest.approx(0.25, abs=5e-3)

    dry = columns.make_columns(sphere, 0.25)
    dry_bishop = columns.bishop(dry, CENTRE_3D, AXIS)
    assert dry_bishop == pytest.approx(2.142, abs=1e-3)
    # Q6: simplified Bishop in 3D minus the 2D value of Practice 2
    circle = slices.Circle()
    dry_2d = slices.bishop(slices.make_slices(circle, 50))
    wet_2d = slices.bishop(slices.make_slices(circle, 50, water_level=4.0))
    assert dry_bishop - dry_2d == pytest.approx(0.079, abs=5e-4)
    assert wet_bishop - wet_2d == pytest.approx(0.159, abs=5e-4)

    raised = CENTRE_3D + np.array([0.0, 0.0, 2.0])
    assert columns.hovland(dry, columns.section_directions(dry, D)) == pytest.approx(
        1.816, abs=1e-3
    )
    assert columns.hovland_moment(dry, raised, AXIS) == pytest.approx(1.849, abs=1e-3)
    assert columns.bishop(dry, raised, AXIS) == pytest.approx(2.122, abs=1e-3)


def test_save_table(tmp_path, monkeypatch, capsys):
    """save_table.py of Practice 3, Section 8 saves the ellipsoid's column table."""
    monkeypatch.chdir(tmp_path)
    runpy.run_path(str(Path(__file__).with_name("save_table.py")))
    assert capsys.readouterr().out == "4596 columns saved to columns.npz\n"
    saved = np.load(tmp_path / "columns.npz")
    assert len(saved["weight"]) == 4596
    assert np.array_equal(saved["axis"], AXIS)
