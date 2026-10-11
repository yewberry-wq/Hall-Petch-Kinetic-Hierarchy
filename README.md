# Emergence of Hall–Petch and Inverse Hall–Petch Scaling from a Dislocation Kinetic Hierarchy — Data & Code

This repository accompanies the manuscript

> F. Yang, "Emergence of Hall–Petch and Inverse Hall–Petch Scaling from a
> Dislocation Kinetic Hierarchy," submitted to *Computational Materials Science*
> (Manuscript No. COMMAT-D-26-04353).

It contains every numerical quantity reported in the paper and the scripts that
reproduce them. No fitted parameters are used anywhere: the Hall–Petch
coefficients follow from DFT/NEB transmission stresses via Eq. (17), and the
crossover size and inverted diffusivities follow from Eqs. (2) and (22).

## Repository structure

```
data/
  table1_dft_neb_hall_petch.csv   DFT/NEB emission barriers, activation volumes,
                                  transmission stresses, and k_HP (main-text Table 1)
  tableS1_taylor_factors.csv      Kröner/Taylor orientation factors M (Table S1)
  tableS2_parameters.csv          All parameters entering Eqs. (17) and (2) (Table S2)
code/
  k_hp_from_neb.py                k_HP from DFT/NEB stresses, Eq. (17) -> reproduces
                                  Table 1 last column and the squares of Fig. 2
                                  (Cu 0.146, Ni 0.35, Al 0.16, Fe 0.35 MPa*m^0.5)
  crossover_scaling.py            Crossover size d_c(T, eps_dot), Eq. (2) -> data
                                  behind Figs. 4a/4b; equilibrium chain gives
                                  d_c = 3.8 nm at 300 K, 1e-3 s^-1
  diffusivity_inversion.py        D_gb^eff from a measured d_c, Eq. (22) -> data
                                  behind Fig. 4c; d_c = 180 nm -> D_gb^eff ~ 8e-17 m^2/s
  requirements.txt                (standard library only, Python >= 3.8)
figures/                          The four manuscript figures (PNG)
```

## How to run

```bash
python3 code/k_hp_from_neb.py
python3 code/crossover_scaling.py
python3 code/diffusivity_inversion.py
```

Each script prints the values quoted in the manuscript; no installation beyond a
standard Python 3 interpreter is required.

## Data provenance

- `table1_dft_neb_hall_petch.csv`: emission barriers and activation volumes are
  DFT/NEB saddle-point results for the listed grain boundaries; transmission
  stresses tau_c and the audit trail tau = dH x f / V* are given in the
  manuscript caption of Table 1.
- `tableS1_taylor_factors.csv`: computed from the Kröner self-consistent
  elastoplastic constraint (Ref. [30] of the manuscript); convergence verified
  against a 1000-grain orientation-distribution-function ensemble.
- Experimental comparison windows (Cu: 0.11–0.15 MPa*m^0.5 etc.) are literature
  compilations, Refs. [31,32] of the manuscript; the equilibrium boundary tracer
  diffusivity is from Ref. [33].

## License

Code: MIT. Data and figures: CC BY 4.0.

## Contact

Feng Yang, School of Integrated Circuit Science and Engineering,
Southwest Jiaotong University, Chengdu 610031, China — yf@home.swjtu.edu.cn
