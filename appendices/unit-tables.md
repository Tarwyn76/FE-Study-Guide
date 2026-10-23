# Unit Tables

**Primary project sources:** Chapters 01-01 and 01-02, `meta/notation.md`, and the FE Reference Handbook 10.6 locations cited by those files.

This appendix is a compact study-guide unit reference. It does not replace the FE Reference Handbook conversion table.

## SI base units

| Quantity | Unit | Symbol |
|---|---|---|
| Mass | kilogram | kg |
| Length | metre | m |
| Time | second | s |
| Thermodynamic temperature | kelvin | K |
| Electric current | ampere | A |
| Amount of substance | mole | mol |
| Luminous intensity | candela | cd |

## Common SI derived units

| Quantity | Unit | Symbol | Base-unit form | Dimensions |
|---|---|---|---|---|
| Force | newton | N | kg·m/s² | $MLT^{-2}$ |
| Pressure, stress | pascal | Pa | kg/(m·s²) | $ML^{-1}T^{-2}$ |
| Energy, work | joule | J | kg·m²/s² | $ML^2T^{-2}$ |
| Power | watt | W | kg·m²/s³ | $ML^2T^{-3}$ |
| Frequency | hertz | Hz | 1/s | $T^{-1}$ |
| Electric charge | coulomb | C | A·s | $IT$ |
| Voltage | volt | V | kg·m²/(A·s³) | $ML^2T^{-3}I^{-1}$ |
| Resistance | ohm | Ω | kg·m²/(A²·s³) | $ML^2T^{-3}I^{-2}$ |
| Capacitance | farad | F | A²·s⁴/(kg·m²) | $M^{-1}L^{-2}T^4I^2$ |

## Common USCS derived units

| Quantity | Unit / expression |
|---|---|
| Pressure, stress | lbf/in² (psi); also lbf/ft² (psf) |
| Energy, work | ft·lbf; Btu for heat |
| Power | ft·lbf/s; horsepower (hp) |
| Density | lbm/ft³ |
| Specific weight | lbf/ft³ |

## Metric prefixes

| Multiple | Prefix | Symbol |
|---:|---|---|
| $10^{18}$ | exa | E |
| $10^{15}$ | peta | P |
| $10^{12}$ | tera | T |
| $10^{9}$ | giga | G |
| $10^{6}$ | mega | M |
| $10^{3}$ | kilo | k |
| $10^{2}$ | hecto | h |
| $10^{1}$ | deka | da |
| $10^{-1}$ | deci | d |
| $10^{-2}$ | centi | c |
| $10^{-3}$ | milli | m |
| $10^{-6}$ | micro | µ |
| $10^{-9}$ | nano | n |
| $10^{-12}$ | pico | p |
| $10^{-15}$ | femto | f |
| $10^{-18}$ | atto | a |

## Landmark conversions

| From | To | Multiply by |
|---|---|---:|
| in | mm | 25.4 |
| ft | m | 0.3048 |
| mile | ft | 5,280 |
| lbf | N | 4.448 |
| lbm | kg | 0.4536 |
| slug | kg | 14.59 |
| psi | kPa | 6.895 |
| psi | lbf/ft² | 144 |
| atm | kPa | 101.3 |
| atm | psi | 14.70 |
| ft·lbf | J | 1.356 |
| Btu | ft·lbf | 778 |
| Btu | J | 1,055 |
| hp | W | 745.7 |

## Temperature values and differences

$$^\circ\mathrm{F}=1.8(^\circ\mathrm{C})+32$$

$$^\circ\mathrm{C}=\frac{^\circ\mathrm{F}-32}{1.8}$$

$$^\circ\mathrm{R}=^\circ\mathrm{F}+459.69$$

$$\mathrm{K}=^\circ\mathrm{C}+273.15$$

$$\mathrm{K}=\frac{^\circ\mathrm{R}}{1.8}$$

| Temperature difference equivalence |
|---|
| $\Delta T$ of 1 °C = 1 K |
| $\Delta T$ of 1 °F = 1 °R |
| $\Delta T$ of 1 °C = 1.8 °F |

Use an absolute scale whenever absolute $T$ appears in a ratio, power, thermodynamic state relation, or radiation relation.

## Pound-mass / pound-force relations

$$g_c=32.174\;\frac{\mathrm{lbm}\cdot\mathrm{ft}}{\mathrm{lbf}\cdot\mathrm{s}^2}$$

$$F=\frac{ma}{g_c}\quad\text{(USCS with lbm)}$$

$$F_W=\frac{mg}{g_c}\quad\text{(USCS)},\qquad F_W=mg\quad\text{(SI)}$$

Standard gravity: $g=9.807\,\mathrm{m/s^2}=32.174\,\mathrm{ft/s^2}$.

## Universal gas constant forms

| Value | Units |
|---:|---|
| 8,314 | J/(kmol·K) |
| 8,314 | kPa·m³/(kmol·K) |
| 1,545 | ft·lbf/(lb mole·°R) |
| 0.08206 | L·atm/(mol·K) |

$$R=\frac{\bar R}{MW}$$

## Verified constants used by the notation contract

| Symbol | Quantity | Value |
|---|---|---|
| $e_{charge}$ | electron charge | $1.6022\times10^{-19}$ C |
| $F_{faraday}$ | Faraday constant | 96,485 C/mol |
| $G$ | gravitation constant | $6.673\times10^{-11}$ m³/(kg·s²) |
| $g$ | standard gravity | 9.807 m/s²; 32.174 ft/s² |
| $c$ | speed of light, exact | 299,792,458 m/s |
| $\sigma_{SB}$ | Stefan–Boltzmann constant | $5.67\times10^{-8}$ W/(m²·K⁴) |
| $V_m$ | ideal-gas molar volume at 273.15 K and 101.3 kPa | 22,414 L/kmol |

## Chapter-supplied SI/USCS quantity units

These entries come directly from notation banners whose table explicitly contains SI and USCS columns.

| Chapter | Symbol | Meaning | SI | USCS |
|---|---|---|---|---|
| 01-01 | $N$ | mantissa (coefficient) in scientific notation, $1 \le \lvert N \rvert < 10$ | — | — |
| 01-01 | $x$ | exponent, a power of ten | — | — |
| 01-01 | $\lvert a \rvert$ | absolute value of $a$ | — | — |
| 01-02 | $m$ | mass | kg | lbm or slug |
| 01-02 | $F$ | force | N | lbf |
| 01-02 | $a$ | acceleration | m/s² | ft/s² |
| 01-02 | $F_W$ | weight (a force) | N | lbf |
| 01-02 | $g$ | local gravitational acceleration | m/s² | ft/s² |
| 01-02 | $g_c$ | force unit conversion constant | — | 32.174 lbm·ft/(lbf·s²) |
| 01-02 | $\rho$ | density | kg/m³ | lbm/ft³ |
| 01-02 | $SW$ | specific weight | N/m³ | lbf/ft³ |
| 01-02 | $p$ | pressure | Pa | lbf/ft² or psi |
| 01-02 | $h$ | height or depth | m | ft |
| 01-02 | $v$ | speed | m/s | ft/s |
| 01-02 | $T$ | temperature | K or °C | °R or °F |
| 01-02 | $\Delta T$ | temperature difference | K or °C | °R or °F |
| 01-02 | $\bar{R}$ | universal gas constant | see §1.8 | see §1.8 |
| 01-02 | $KE$, $PE$ | kinetic, potential energy | J | ft·lbf |
| 01-24 | $D$ | two-dimensional integration region | m² as an area when coordinates are lengths | ft² or in² |
| 01-24 | $E$ | three-dimensional integration region | m³ as a volume when coordinates are lengths | ft³ or in³ |
| 01-24 | $dA$ | differential area element | m² | ft² or in² |
| 01-24 | $dV$ | differential volume element | m³ | ft³ or in³ |
| 01-24 | $f(x,y)$ | scalar field or surface height | problem-dependent | problem-dependent |
| 01-24 | $A(D)$ | area of region $D$ | m² | ft² or in² |
| 01-24 | $V(E)$ | volume of region $E$ | m³ | ft³ or in³ |
| 01-24 | $\rho_A(x,y)$ | mass per unit area of a lamina | kg/m² | slug/ft² or lbm/ft² as specified |
| 01-24 | $\rho_V(x,y,z)$ | mass per unit volume | kg/m³ | slug/ft³ or lbm/ft³ as specified |
| 01-24 | $M$ | total mass | kg | slug or lbm as specified |
| 01-24 | $\bar x,\bar y,\bar z$ | centroid or center-of-mass coordinates | m | ft or in |
| 01-24 | $r,\theta$ | polar/cylindrical radius and azimuth angle | m; rad | ft or in; rad |
| 01-24 | $\varrho,\phi,\theta$ | spherical radius, polar angle from $+z$, azimuth angle | m; rad; rad | ft or in; rad; rad |
| 01-24 | $u,v,w$ | generic transformed coordinates | problem-dependent | problem-dependent |
| 01-24 | $J$ | Jacobian determinant or its absolute value as stated | coordinate-scale dependent | same dimensional role |
| 01-25 | $t$ | independent variable, usually time | s when time | s when time |
| 01-25 | $y(t)$ | unknown dependent variable | problem-dependent | problem-dependent |
| 01-25 | $y',y'',y^{(n)}$ | first, second, and $n$th derivatives of $y$ | $[y]/[t]$, $[y]/[t]^2$, ... | same dimensional pattern |
| 01-25 | $g(t)$ | forcing or source term | must match the equation's derivative terms | same dimensional requirement |
| 01-25 | $a,b,b_0,b_1,b_n$ | constant coefficients | coefficient units make all terms compatible | same rule |
| 01-25 | $C,C_1,C_2$ | constants selected by conditions | whatever units make $y$ consistent | same rule |
| 01-25 | $r$ | characteristic root | inverse independent-variable unit when exponent is dimensional | same dimensional role |
| 01-25 | $\alpha,\beta$ | real and imaginary parts of $r=\alpha\pm j\beta$ | inverse independent-variable unit | same |
| 01-25 | $\tau$ | first-order time constant | s | s |
| 01-25 | $K$ | gain in a supplied first-order model | output/input | output/input |
| 01-25 | $u(t)$ | unit-step function | 1 | 1 |
| 01-25 | $\delta(t)$ | unit impulse | $1/\mathrm{s}$ when $t$ is time | $1/\mathrm{s}$ |
| 01-25 | $s$ | unilateral Laplace-transform variable | $1/\mathrm{s}$ when $t$ is time | $1/\mathrm{s}$ |
| 01-25 | $Y(s)$ | Laplace transform of $y(t)$ | $[y]\cdot\mathrm s$ under the usual time transform | same dimensional role |
| 01-25 | $a_n$ | coefficient in a power-series solution | chosen so each term has units of $y$ | same rule |

## Presentation rules

- Every numeric result carries a unit unless the result is dimensionless.
- Variables are italicized in typeset math; unit symbols are not.
- Use a middle dot for multiplication in units: `N·m`.
- Prefer one solidus: `W/(m·K)` rather than `W/m/K`.
- For temperature differences, state the scale when ambiguity is possible.
- Use factor-label dimensional analysis for conversions; cancel units explicitly.
