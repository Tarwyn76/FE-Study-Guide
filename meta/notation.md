# Notation Contract

**Status: FROZEN.** Changes require updating every affected chapter and
rerunning `lint_forward_refs.py` and `check_reference_backlinks.py`.

## Why this file exists

FE material spans seven disciplines that reuse the same Greek and Latin
letters for unrelated quantities. A reader who skips Tier C and lands in
Tier E must never encounter a symbol whose meaning was silently
established in a tier they skipped. Two mechanisms prevent that:

1. **Global disambiguation** — collisions resolved once, here.
2. **Per-chapter notation banner** — every chapter opens with a table of
   only the symbols it uses. A skipping reader gets an unambiguous local
   reading with no backtracking.

## Rule 1 — Handbook alignment

Where the *FE Reference Handbook* 10.6 uses a symbol, this guide uses the
same symbol. When the guide must disambiguate and the Handbook does not,
the chapter states the difference explicitly in section 3.

Confirmed alignments:

| Symbol | Meaning | Handbook |
|--------|---------|----------|
| `j` | imaginary unit | p.38 — "some disciplines use i" |
| `g_c` | unit conversion constant, 32.174 lbm-ft/(lbf-sec²) | p.1 |
| `R̄` | universal gas constant | p.2 — "some disciplines, notably chemical engineering, often use R" |
| `σ` | Stefan-Boltzmann constant, 5.67×10⁻⁸ W/(m²·K⁴) | p.2 |

The `R̄` and `σ` cases are both collisions. Resolved below.

## Rule 2 — Collision table

Any symbol in this table requires a **mandatory notation banner** in every
chapter that uses it. The linter enforces presence of the banner.

| Symbol | Competing meanings | Resolution |
|--------|-------------------|------------|
| `ρ` | density · resistivity · correlation coefficient | `ρ` density (unqualified) · `ρ_e` resistivity · `r` sample correlation |
| `σ` | normal stress · standard deviation · conductivity · Stefan-Boltzmann | `σ` normal stress in Tier 2C · `s` sample std dev, `σ_pop` population std dev · `σ_e` conductivity · `σ_SB` Stefan-Boltzmann |
| `τ` | shear stress · time constant | `τ` shear stress · `τ_c` time constant |
| `μ` | friction coefficient · dynamic viscosity · population mean · magnetic permeability · SI micro- prefix | `μ_s`/`μ_k` static/kinetic friction · `μ` dynamic viscosity in Tier 2D · `μ_pop` population mean (prefer `x̄` for sample) · `μ_m` permeability · micro- prefix never standalone |
| `ν` | kinematic viscosity · Poisson's ratio · frequency | `ν` kinematic viscosity · `ν_p` Poisson's ratio · `f` frequency |
| `k` | thermal conductivity · spring constant · reaction rate constant · specific heat ratio · Boltzmann constant | `k` thermal conductivity in Tier 2D · `k_s` spring constant · `k_r` rate constant · `γ` specific heat ratio · `k_B` Boltzmann |
| `E` | elastic modulus · energy · electric field · expected value · EMF | `E` elastic modulus · `U` internal energy, `KE`/`PE` kinetic/potential · `Ē` electric field · `E[X]` expectation · `ℰ` EMF |
| `P` | pressure · power · probability · present worth · perimeter | `P` pressure in Tier 2D · `Ẇ` or `P_w` power · `P(A)` probability · `PW` present worth · `P` perimeter in mensuration only |
| `V` | volume · voltage · velocity · shear force | `V` volume · `V` voltage in Tier 2E only · `v` velocity · `V_s` shear force |
| `Q` | heat · volumetric flow rate · electric charge · first moment | `Q` heat · `Q_v` volumetric flow · `q` charge · `Q_a` first moment of area |
| `R` | universal gas constant · specific gas constant · resistance · radius · thermal resistance | `R̄` universal · `R` specific gas constant · `R` resistance in Tier 2E only · `r` radius · `R_θ` thermal resistance |
| `A` | area · amplitude · availability | `A` area · `A_m` amplitude · `A_v` availability |
| `T` | temperature · torque · period · tension | `T` temperature · `T_q` torque · `T_p` period · `F_T` tension |
| `I` | current · moment of inertia · impulse | `I` current in Tier 2E only · `I` area moment of inertia in Tier 2C · `I_m` mass moment of inertia · `J_i` impulse |
| `W` | work · weight · watt (unit) | `W` work · `F_W` weight · watt as unit symbol only |
| `α` | angular acceleration · thermal expansion coefficient · significance level | `α` angular acceleration · `α_T` thermal expansion · `α` significance level in Tier 1F only |
| `β` | Type II error rate · thermal coefficient | `β` Type II error in Tier 1F only · `β_T` elsewhere |
| `η` | efficiency · similarity variable | `η` efficiency |
| `λ` | wavelength · failure rate · eigenvalue · Poisson parameter | `λ` wavelength · `λ_f` failure rate · `λ_i` eigenvalue · `λ` Poisson parameter in Tier 1F only |
| `ω` | angular velocity · angular frequency | `ω` both; identical concept, different context |
| `θ` | plane angle | reserved for plane angle throughout |
| `φ` | plane angle · phase angle · porosity | `φ` plane angle in geometry · `φ_p` phase angle · `n_p` porosity |

**"in Tier X only" means** the symbol carries that meaning inside that
tier and the chapter banner states it. A reader who skipped the competing
tier is never exposed to the other meaning.

## Rule 3 — Structural conventions

| Convention | Form | Example |
|-----------|------|---------|
| Vector | overbar in prose, bold in display | `v̄` or **v** |
| Unit vectors | `î`, `ĵ`, `k̂` | — |
| Time derivative | overdot | `ẋ` |
| Rate quantity | overdot | `ṁ`, `Q̇`, `Ẇ` |
| Average over space or time | overbar | `T̄` |
| Sample mean | `x̄` | preferred over `μ` |
| Per-mole quantity | overbar | `h̄` |
| Estimated value | circumflex | `ŷ` |
| Change in quantity | `Δ` | `ΔT` |
| Differential | `d` | `dx` |
| Partial derivative | `∂` | `∂T/∂x` |
| Complex quantity | underline in prose | `Z` for impedance |
| Phasor | angle notation | `V∠θ` |
| Matrix | uppercase bold | **A** |
| Transpose | superscript T | **A**ᵗ |
| Determinant | vertical bars | `|A|` |

## Rule 4 — Subscript reservations

| Subscript | Meaning | Never means |
|-----------|---------|-------------|
| `0` | initial or reference state | zero-valued |
| `i` | index | initial |
| `f` | final | fluid or friction |
| `s` | static or isentropic | surface |
| `k` | kinetic | index |
| `avg` | average | — |
| `max` `min` | extremum | — |
| `sat` | saturated | — |
| `abs` `gage` | absolute / gage pressure | — |
| `net` | net quantity | — |
| `in` `out` | crossing a boundary | inner/outer diameter — use `ID`/`OD` |
| `crit` | critical | — |
| `allow` | allowable | — |

## Rule 5 — Unit presentation

- Every numeric result carries a unit. No exceptions.
- SI first, USCS in parentheses, on first statement of a result:
  `9.807 m/s² (32.174 ft/sec²)`
- Unit symbols are never italicized. Variables always are.
- Multiplication in units uses a middle dot: `N·m`, not `Nm`.
- Division uses a solidus with at most one: `W/(m·K)`, not `W/m/K`.
- Temperature difference uses `ΔT` with the scale named, since a
  difference of 1 K equals 1 °C but a difference of 1 °R equals 1 °F.

## Rule 6 — Per-chapter banner format

Mandatory in every chapter. Generated from the ledger's
`introduces_symbols` and `uses_symbols` fields, so it cannot drift.

```markdown
## Notation used here

| Symbol | Meaning in this chapter | SI | USCS |
|--------|------------------------|-----|------|
| *F* | force | N | lbf |
| *θ* | plane angle | rad | rad |
| *g_c* | unit conversion constant | — | 32.174 lbm·ft/(lbf·s²) |

> **Collision note.** In this chapter *σ* means normal stress.
> In Tier 1F it means population standard deviation, written *σ_pop*
> there. See [Notation Contract](../../meta/notation.md).
```

The collision note appears only when a symbol from Rule 2 is present, and
the linter fails the build if it is missing.

## Rule 7 — Verified constants

Values per Handbook 10.6 p.2, transcription verified.

| Symbol | Quantity | Value |
|--------|----------|-------|
| `e_charge` | electron charge | 1.6022×10⁻¹⁹ C |
| `F_faraday` | Faraday constant | 96,485 C/mol |
| `R̄` | universal gas constant | 8,314 J/(kmol·K) |
| `R̄` | universal gas constant | 8,314 kPa·m³/(kmol·K) |
| `R̄` | universal gas constant | 1,545 ft·lbf/(lb mole·°R) |
| `R̄` | universal gas constant | 0.08206 L·atm/(mol·K) |
| `G_grav` | gravitation constant | 6.673×10⁻¹¹ m³/(kg·s²) |
| `g` | standard gravity | 9.807 m/s² · 32.174 ft/sec² |
| `g_c` | unit conversion constant | 32.174 lbm·ft/(lbf·sec²) |
| `V_m` | molar volume, ideal gas at 273.15 K and 101.3 kPa | 22,414 L/kmol |
| `c_light` | speed of light, exact | 299,792,458 m/s |
| `σ_SB` | Stefan-Boltzmann constant | 5.67×10⁻⁸ W/(m²·K⁴) |