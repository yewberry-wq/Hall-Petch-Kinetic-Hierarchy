"""diffusivity_inversion.py -- Eq. (22): invert a measured crossover size
into the operative grain-boundary diffusivity.

D_gb^eff = k_B * T * eps_dot * d_c^(7/2) / (k_HP * A_Coble * Omega * delta)

For Cu at 300 K, eps_dot = 1e-3 s^-1, d_c = 180 nm this returns
D_gb^eff ~= 8e-17 m^2/s, i.e. an enhancement of ~7e5 over the equilibrium
tracer value 1.11e-22 m^2/s -- the diagnostic of grain-boundary
non-equilibrium developed in Sec. 4.4 (data behind Fig. 4c).
"""
kB = 1.380649e-23
K_HP, A_CO, OMEGA, DELTA = 0.146e6, 150.0, 1.18e-29, 0.5e-9
D_EQ = 1.11e-22

def D_eff(d_c, T=300.0, eps_dot=1e-3):
    return kB*T*eps_dot * d_c**3.5 / (K_HP*A_CO*OMEGA*DELTA)

if __name__ == "__main__":
    for dc in [5e-9, 50e-9, 180e-9]:
        D = D_eff(dc)
        print(f"d_c={dc*1e9:6.0f} nm -> D_gb^eff = {D:.2e} m^2/s "
              f"(enhancement over D_gb^eq: {D/D_EQ:.1e})")
