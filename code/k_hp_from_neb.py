"""k_hp_from_neb.py -- Reproduce Table 1 (last column) and Fig. 2 of the manuscript.

Computes the Hall-Petch coefficient k_HP from DFT/NEB transmission stresses
via Eq. (17):  k_HP = M * sqrt(2*G*b*<tau_c^poly> / (pi*(1-nu))).
No fitted parameters: G, b, nu are standard elastic data; <tau_c^poly> is the
orientational average of the DFT/NEB transmission stresses in
data/table1_dft_neb_hall_petch.csv; M from data/tableS1_taylor_factors.csv.
"""
import csv, math, os

DATA = os.path.join(os.path.dirname(__file__), "..", "data")

# elastic inputs: G [Pa], b [m], nu [-], M [-] (Kroner random-fcc for fcc; Fe: bcc orientation factor M = 2.6 as stated in the text)
ELASTIC = {
    "Cu":      dict(G=48e9,  b=0.255e-9, nu=0.34, M=2.75),
    "Ni":      dict(G=76e9,  b=0.249e-9, nu=0.31, M=2.75),
    "Al":      dict(G=26e9,  b=0.286e-9, nu=0.33, M=2.75),
    "Fe(bcc)": dict(G=82e9,  b=0.248e-9, nu=0.29, M=2.60),
}

def k_hp(G, b, nu, M, tau_poly):
    return M * math.sqrt(2*G*b*tau_poly / (math.pi*(1-nu)))  # Pa*m^0.5

def main():
    rows = list(csv.DictReader(open(os.path.join(DATA, "table1_dft_neb_hall_petch.csv"))))
    metals = {}
    for r in rows:
        metals.setdefault(r["metal"], []).append(float(r["tau_c_0K_GPa"]))
    print(f"{'metal':8s} {'<tau_c^poly> [GPa]':>18s} {'k_HP [MPa m^0.5]':>18s}")
    for m, taus in metals.items():
        tau_poly = sum(taus)/len(taus) * 1e9          # simple Sigma3/5/7 average as in text
        e = ELASTIC[m]
        k = k_hp(e["G"], e["b"], e["nu"], e["M"], tau_poly) / 1e6
        print(f"{m:8s} {tau_poly/1e9:18.2f} {k:18.3f}")

if __name__ == "__main__":
    main()
