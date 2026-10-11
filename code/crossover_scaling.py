"""crossover_scaling.py -- Crossover grain size d_c from Eq. (2) (main text).

d_c = [ k_HP * A_Coble * Omega * delta * D_gb / (k_B * T * eps_dot) ]^(2/7)

Reproduces the data behind Fig. 4a (rate scan) and Fig. 4b (Arrhenius scan).
Two diffusivity choices illustrate the point of Sec. 4: the equilibrium tracer
value D_gb^eq = 1.11e-22 m^2/s gives d_c of a few nm, while the operative
non-equilibrium value D_gb^eff ~ 8e-17 m^2/s (inverted, Eq. (22)) gives
d_c ~ 180 nm at 1e-3 s^-1, 300 K.
"""
import math

kB = 1.380649e-23          # J/K
K_HP   = 0.146e6           # Pa*m^0.5   (Cu, Table S2, computed)
A_CO   = 150.0             # Coble geometric constant
OMEGA  = 1.18e-29          # m^3
DELTA  = 0.5e-9            # m
D_EQ   = 1.11e-22          # m^2/s, equilibrium tracer
D_EFF  = 8.0e-17           # m^2/s, operative (Sec. 4.4)
Q_GB   = 0.70 * 1.602e-19  # J
D0     = D_EQ / math.exp(-Q_GB/(kB*300))   # fixes D0 from the 300 K tracer value

def d_c(T, eps_dot, D_gb):
    return (K_HP*A_CO*OMEGA*DELTA*D_gb / (kB*T*eps_dot))**(2/7)

def D_gb(T):
    return D0 * math.exp(-Q_GB/(kB*T))

if __name__ == "__main__":
    print("d_c (equilibrium vs effective diffusivity), T = 300 K:")
    for e in [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]:
        print(f"  eps={e:8.0e}  d_c^eq={d_c(300,e,D_gb(300))*1e9:8.1f} nm   "
              f"d_c^eff={d_c(300,e,D_EFF)*1e9:8.1f} nm")
    print("Arrhenius scan, eps = 1e-3 s^-1 (equilibrium chain):")
    for T in [300, 400, 500, 600, 700]:
        print(f"  T={T:4d} K   d_c^eq={d_c(T,1e-3,D_gb(T))*1e9:8.2f} nm")
