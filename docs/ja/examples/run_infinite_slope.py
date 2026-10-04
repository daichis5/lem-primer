"""実践1の数値を表示する．"""

import math

from infinite_slope import (
    GAMMA_W,
    base_stresses,
    column_weight,
    factor_of_safety,
    pore_pressure,
)

C, PHI = 10.0, 30.0  # c' [kPa], phi' [度]
GAMMA, GAMMA_SAT = 18.0, 20.0  # [kN/m³]

print("1. dry slope, beta = 30 deg, z = 5 m")
sigma_n, tau = base_stresses(30.0, column_weight(5.0, GAMMA))
fs = factor_of_safety(sigma_n, tau, 0.0, C, PHI)
print(f"   sigma_n = {sigma_n:.2f} kPa, tau = {tau:.2f} kPa, Fs = {fs:.3f}")

print("2. the base of Chapter 1, Section 6")
beta = math.degrees(math.atan(0.3))
w = 100.0 / math.cos(math.radians(beta)) ** 2
sigma_n, tau = base_stresses(beta, w)
print(f"   beta = {beta:.2f} deg, w = {w:.1f} kPa:", end=" ")
print(f"sigma_n = {sigma_n:.2f} kPa, tau = {tau:.2f} kPa")
for u in (40.0, 60.0):
    print(f"   u = {u:.0f} kPa: Fs = {factor_of_safety(sigma_n, tau, u, C, PHI):.3f}")

print("3. water table at the ground surface, beta = 30 deg, z = 5 m")
w = column_weight(5.0, GAMMA, h_w=5.0, gamma_sat=GAMMA_SAT)
sigma_n, tau = base_stresses(30.0, w)
print(f"   sigma_n = {sigma_n:.2f} kPa, tau = {tau:.2f} kPa")
for rule in ("parallel", "vertical"):
    u = pore_pressure(5.0, 30.0, rule)
    fs = factor_of_safety(sigma_n, tau, u, C, PHI)
    print(f"   {rule:8s}: u = {u:.2f} kPa,", end=" ")
    print(f"sigma_n - u = {sigma_n - u:6.2f} kPa, Fs = {fs:.3f}")

print("4. effective normal stress with the water table at the surface, z = 5 m [kPa]")
print("   beta  parallel  vertical")
for beta in (30.0, 40.0, 45.0, 50.0):
    sigma_n, _ = base_stresses(beta, w)
    parallel = sigma_n - pore_pressure(5.0, beta, "parallel")
    vertical = sigma_n - pore_pressure(5.0, beta, "vertical")
    print(f"   {beta:4.0f}  {parallel:8.2f}  {vertical:8.2f}")
beta_zero = math.degrees(math.acos(math.sqrt(GAMMA_W / GAMMA_SAT)))
print(f"   vertical rule: sigma_n - u = 0 at beta = {beta_zero:.1f} deg")

print("5. depth of the slip plane, beta = 30 deg, water table 2 m below the surface")
print("   z [m]   dry   parallel  vertical")
for z in (1.0, 2.0, 3.0, 5.0, 7.0, 10.0):
    dry = factor_of_safety(*base_stresses(30.0, column_weight(z, GAMMA)), 0.0, C, PHI)
    h_w = max(z - 2.0, 0.0)
    sigma_n, tau = base_stresses(
        30.0, column_weight(z, GAMMA, h_w=h_w, gamma_sat=GAMMA_SAT)
    )
    wet = [
        factor_of_safety(sigma_n, tau, pore_pressure(h_w, 30.0, r), C, PHI)
        for r in ("parallel", "vertical")
    ]
    print(f"   {z:5.1f}  {dry:5.3f}  {wet[0]:8.3f}  {wet[1]:8.3f}")
