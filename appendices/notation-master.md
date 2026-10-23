# Notation Master

**Source of truth:** `meta/notation.md` plus chapter `Notation Used Here` banners available in the current project Library.

The guide intentionally allows discipline-local symbol meanings while enforcing a global collision contract. This appendix records that contract first, then provides a chapter-local cross-reference. If a local chapter banner conflicts with the frozen notation contract, the contract governs and the chapter should be corrected.

## Handbook alignment

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

## Collision table

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

## Structural conventions

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

## Subscript reservations

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

## Unit presentation

- Every numeric result carries a unit. No exceptions.
- SI first, USCS in parentheses, on first statement of a result:
  `9.807 m/s² (32.174 ft/sec²)`
- Unit symbols are never italicized. Variables always are.
- Multiplication in units uses a middle dot: `N·m`, not `Nm`.
- Division uses a solidus with at most one: `W/(m·K)`, not `W/m/K`.
- Temperature difference uses `ΔT` with the scale named, since a
  difference of 1 K equals 1 °C but a difference of 1 °R equals 1 °F.

## Verified constants

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

## Chapter-local notation cross-reference

Entries below are transcribed from chapter notation banners in the current Library snapshots. The third and fourth fields preserve the banner's own unit columns or local-convention notes without reinterpretation.

| Symbol | Meaning | SI / local convention | USCS / additional convention | Chapter(s) |
|---|---|---|---|---|
| $(a, b)$ | open interval, $a < x < b$ | endpoints excluded |  | 01-04 |
| $(a, b]$ | half-open, $a < x \le b$ | — |  | 01-04 |
| $(a,b)$ | open interval, endpoints excluded | — |  | 01-18 |
| $(h, k)$ | centre of a circle or ellipse; vertex of a parabola | — |  | 01-09 |
| $(x_1, y_1)$, $(x_2, y_2)$ | specific named points | — |  | 01-09 |
| $1-\alpha$ | confidence level | e.g. 0.95 |  | 01-32 |
| $1-\beta$ | power | probability of rejecting $H_0$ when the specified alternative is true |  | 01-33 |
| $[A \mid b]$ | augmented matrix | coefficients, a rule, then constants |  | 01-08 |
| $[a, b]$ | closed interval, $a \le x \le b$ | endpoints included |  | 01-04 |
| $[a,b]$ | closed interval, endpoints included | required for the closed-interval method |  | 01-18 |
| $[a_k,b_k]$ | bracketing interval | endpoints have opposite function signs |  | 01-26 |
| `<, <=, >, >=` | comparison operators | result is Boolean |  | 01-27 |
| `and`, `or` | logical conjunction / disjunction | evaluate conditions, not arithmetic |  | 01-27 |
| `count` | number of qualifying events | initialize deliberately |  | 01-27 |
| `do ... while` | post-test loop | executes at least once |  | 01-27 |
| `else` | alternate branch | paired with an `if` |  | 01-27 |
| `for` | count-controlled loop | preferred when iteration count is known |  | 01-27 |
| `if ... then` | conditional branch | executes only when condition is true |  | 01-27 |
| `k` | loop or iteration index | local meaning |  | 01-27 |
| `maxIter` | maximum allowed iterations | prevents uncontrolled looping |  | 01-27 |
| `status` | outcome flag or label | e.g. `"converged"` or `"failed"` |  | 01-27 |
| `sum` | accumulator | initialize before the loop |  | 01-27 |
| `tol` | numerical tolerance | must be positive |  | 01-27 |
| `while` | pre-test loop | may execute zero times |  | 01-27 |
| `x <> y` | not-equal comparison | Handbook pseudocode convention |  | 01-27 |
| `x = expression` | assignment | store the value of the expression in `x` |  | 01-27 |
| `x == y` | equality comparison | Boolean result |  | 01-27 |
| $a$ | acceleration | m/s² | ft/s² | 01-02 |
| $A$ | area | m², ft², in², mm² |  | 01-10 |
| $a$ | real part of $z$, $\text{Re}(z)$ | — |  | 01-12 |
| $a$ | semi-major axis (ellipse) or semi-transverse axis (hyperbola) | always the larger for an ellipse |  | 01-09 |
| $a$ | the **centre** of a Taylor expansion | not a series term here |  | 01-22 |
| $a$ | the constant in $\sqrt{a^2 \pm x^2}$ | always taken positive |  | 01-21 |
| $A$ | uniform end-of-period amount |  |  | 02-04, 02-05, 02-06, 02-07, 02-08, 02-09, 02-10 |
| $a \to b$ | direction of integration | reversing it flips the sign |  | 01-19 |
| $A(D)$ | area of region $D$ | m² | ft² or in² | 01-24 |
| $A$, $B$, $C$ | angles of a triangle | $A + B + C = 180°$ |  | 01-11 |
| $a, b, c$ | constants or known coefficients | — |  | 01-04 |
| $a$, $b$, $c$ | side lengths of a triangle | $c$ opposite angle $C$ |  | 01-11 |
| $A$, $B$, $C$ | unknown constants in a partial fraction decomposition | solved for |  | 01-21 |
| $A, B, C, D, E, F$ | coefficients of the general second-degree equation | §9.9 |  | 01-09 |
| $A$, $B$, $M$ | matrices | capital letters, no decoration |  | 01-14 |
| $A$, $V$ | total area, total volume | — |  | 01-20 |
| $a,b$ | levels of Factors A and B | two-factor factorial design |  | 01-34 |
| $a,b$ | lower and upper bounds | uniform / triangular |  | 01-38 |
| $a,b,b_0,b_1,b_n$ | constant coefficients | coefficient units make all terms compatible | same rule | 01-25 |
| $A,B,C$ | events | subsets of $S$ |  | 01-28 |
| $A^{-1}$ | inverse of $A$ | exists only if $\det A \ne 0$ |  | 01-14 |
| $a_0$ | constant term | value when $x = 0$ |  | 01-07 |
| $a_1$ | the first term | some texts index from $a_0$; watch for it |  | 01-15 |
| $A_2,D_3,D_4$ | Handbook constants | $\bar X$-$R$ charts |  | 01-39 |
| $A_3,B_3,B_4$ | Handbook constants | $\bar X$-$S$ charts |  | 01-39 |
| $A^c$ | complement of $A$ | outcomes in $S$ that are not in $A$ |  | 01-28 |
| $A\cap B$ | intersection | both $A$ and $B$ |  | 01-28 |
| $A\cup B$ | union | $A$ or $B$ or both |  | 01-28 |
| $A_i$ | area of component $i$ | for composite shapes |  | 01-10 |
| $a_{ij}$ | coefficient in row $i$, column $j$ | first index is the row |  | 01-08 |
| $a_{ij}$ | element of $A$ in row $i$, column $j$ | row index first, always |  | 01-14 |
| $\alpha$ | angle of inclination of a line | measured counterclockwise from the positive $x$-axis, $0° \le \alpha < 180°$ |  | 01-11 |
| $\alpha$ | producer's risk | probability of rejection at the stated AQL |  | 01-41 |
| $\alpha$ | significance level | probability of Type I error under the test design |  | 01-33 |
| $\alpha$ | total probability outside a two-sided confidence region | split into two tails for symmetric intervals |  | 01-32 |
| $\alpha$ | Weibull shape parameter | positive |  | 01-38 |
| $\alpha,\beta$ | real and imaginary parts of $r=\alpha\pm j\beta$ | inverse independent-variable unit | same | 01-25 |
| $a_n$ | coefficient in a power-series solution | chosen so each term has units of $y$ | same rule | 01-25 |
| $a_n$ | leading coefficient | coefficient of $x^n$ |  | 01-07 |
| $a_n$ | the $n$th term of a sequence | $n$ is a positive integer |  | 01-15 |
| $a_n$ | the $n$th term of a sequence or series | — |  | 01-22 |
| AQL | acceptable quality level | guide-developed quality-engineering design point |  | 01-41 |
| $A^T$ | transpose of $A$ | rows and columns exchanged |  | 01-14 |
| $A_x, A_y, A_z$ | scalar components of $\vec{A}$ | may be negative |  | 01-13 |
| $b$ | base width | — |  | 01-10 |
| $B$ | benefit |  |  | 02-04, 02-05, 02-06, 02-07, 02-08, 02-09, 02-10 |
| $b$ | imaginary part of $z$, $\text{Im}(z)$ | — |  | 01-12 |
| $b$ | semi-minor axis (ellipse) or semi-conjugate axis (hyperbola) | — |  | 01-09 |
| $\bar R$ | average subgroup range | center line of $R$ chart |  | 01-39 |
| $\bar S$ | average subgroup standard deviation | center line of $S$ chart |  | 01-39 |
| $\bar x$ | average of repeated measurements | sample mean |  | 01-36 |
| $\bar x$ | observed sample mean | numerical result from one sample |  | 01-32 |
| $\bar x$ | realized sample mean | numerical value from one sample |  | 01-31 |
| $\bar X$ | sample mean | average of $n$ observations |  | 01-30 |
| $\bar X$ | sample mean | random statistic before sampling |  | 01-31 |
| $\bar X$ | sample mean statistic | random before sampling |  | 01-32 |
| $\bar x,\bar y$ | sample means | centers of the observed data |  | 01-35 |
| $\bar x,\bar y,\bar z$ | centroid or center-of-mass coordinates | m | ft or in | 01-24 |
| $\bar X_i$ | mean of subgroup $i$ | plotted on average chart |  | 01-39 |
| $\bar y$ | grand mean | mean of all observations |  | 01-34 |
| $\bar y_i$ | mean response for treatment $i$ | one-way |  | 01-34 |
| $\bar{\bar X}$ | average of subgroup means | center line of $\bar X$ chart |  | 01-39 |
| $\bar{f}$ | average value of $f$ over an interval | a single number |  | 01-19 |
| $\bar{I}$ | second moment about a **centroidal** axis | the tabulated value |  | 01-20 |
| $\bar{R}$ | universal gas constant | see §1.8 | see §1.8 | 01-02 |
| $\bar{x}$, $\bar{y}$ | centroid coordinates | read "x-bar", "y-bar" |  | 01-20 |
| $\bar{x}, \bar{y}$ | centroid coordinates | $\bar{x}$ is $x$-coordinate of centroid |  | 01-10 |
| $\bar{x}_i, \bar{y}_i$ | centroid of component $i$ | — |  | 01-10 |
| $\begin{vmatrix} a & b \\ c & d \end{vmatrix}$ | determinant of a 2×2 array | a single number, $ad - bc$ |  | 01-08 |
| $\beta$ | consumer's risk | probability of acceptance at the stated RQL |  | 01-41 |
| $\beta$ | probability of Type II error | depends on the true alternative value |  | 01-33 |
| $\beta$ | scale parameter | exponential and Weibull Handbook notation |  | 01-38 |
| $\big[F(x)\big]_a^b$ | evaluation notation | means $F(b) - F(a)$ |  | 01-19 |
| $\big[uv\big]_a^b$ | boundary term in definite integration by parts | evaluated, not integrated |  | 01-21 |
| $b^x$ | $b$ raised to power $x$ | $b > 0$, $b \ne 1$ for exponential/log purposes |  | 01-05 |
| $c$ | acceptance number | accept if $X\le c$ |  | 01-41 |
| $C$ | constant of integration | never optional on an indefinite integral |  | 01-19 |
| $C$ | cost |  |  | 02-04, 02-05, 02-06, 02-07, 02-08, 02-09, 02-10 |
| $c$ | focal distance from centre | $c^2 = a^2 - b^2$ ellipse, $c^2 = a^2 + b^2$ hyperbola |  | 01-09 |
| $c$ | the point guaranteed by the Mean Value Theorem | not a constant here |  | 01-18 |
| $c$ | the unknown interior point in the Lagrange remainder | not a constant |  | 01-22 |
| $C(n,r)$ | combinations | order does not matter |  | 01-28 |
| $C,C_1,C_2$ | constants selected by conditions | whatever units make $y$ consistent | same rule | 01-25 |
| $\chi_0^2$ | observed chi-square statistic | variance test |  | 01-33 |
| $\chi^2$ | chi-square statistic | nonnegative |  | 01-31 |
| $\chi^2_{\alpha,\nu}$ | chi-square critical value | upper-tail area $\alpha$, df $\nu$ |  | 01-31 |
| $\chi^2_{\alpha,\nu}$ | chi-square upper-tail critical value | Handbook-style tail convention |  | 01-32 |
| $C_i$ | consequence of outcome $i$ | benefit, cost, loss, or net value |  | 01-37 |
| $c_i$ | sensitivity coefficient | $c_i=\partial f/\partial x_i$ |  | 01-36 |
| $C_{ij}$ | cofactor of element $a_{ij}$ | $(-1)^{i+j}M_{ij}$ |  | 01-14 |
| CL | center line | baseline central statistic |  | 01-39 |
| CL, UCL, LCL | control-chart center and limits | process-monitoring quantities, not specifications |  | 01-40 |
| converges / diverges | the improper integral has a finite value / does not | — |  | 01-21 |
| $C_p$ | potential capability | assumes centered process |  | 01-40 |
| $C_{pk}$ | actual capability | includes current centering |  | 01-40 |
| $C_{pl}$ | lower-side capability | distance from LSL to mean in $3\sigma$ units |  | 01-40 |
| $C_{pu}$ | upper-side capability | distance from mean to USL in $3\sigma$ units |  | 01-40 |
| critical point | a point where $f' = 0$ or $f'$ is undefined | interior to the domain |  | 01-18 |
| $\csc\theta$, $\sec\theta$, $\cot\theta$ | reciprocal trig functions | — |  | 01-11 |
| $d$ | common difference (arithmetic) | $d = a_{n+1} - a_n$ |  | 01-15 |
| $D$ | discriminant $f_{xx}f_{yy} - f_{xy}^2$ | second-derivative test |  | 01-23 |
| $d$ | distance | — |  | 01-09 |
| $D$ | number of nonconforming units in lot | finite-lot model |  | 01-41 |
| $d$ | perpendicular distance between parallel axes | parallel axis theorem |  | 01-20 |
| $D$ | two-dimensional integration region | m² as an area when coordinates are lengths | ft² or in² | 01-24 |
| $D$, $D_x$, $D_y$ | the three determinants of Cramer's rule | defined in §8.5 |  | 01-08 |
| $d_2,c_4$ | Handbook approximation constants | used to estimate process $\sigma$ |  | 01-39 |
| $dA$ | area of one thin slice | $= (\text{height})\,dx$ or $(\text{width})\,dy$ |  | 01-20 |
| $dA$ | differential area element | m² | ft² or in² | 01-24 |
| $\Delta$ | discriminant, $b^2 - 4ac$ | determines root type |  | 01-07 |
| $\Delta T$ | temperature difference | K or °C | °R or °F | 01-02 |
| $\Delta t$ | time step | Euler marching step |  | 01-26 |
| $\Delta x$ | width of a subinterval | $= \dfrac{b-a}{n}$ for equal subdivisions |  | 01-19 |
| $\Delta x$, $\Delta y$ | actual finite changes | measured or exact |  | 01-18 |
| $\Delta y$ | the corresponding increment in $y$ | $= f(x+h) - f(x)$ |  | 01-17 |
| $\delta(t)$ | unit impulse | $1/\mathrm{s}$ when $t$ is time | $1/\mathrm{s}$ | 01-25 |
| $\det A$ or $\lvert A \rvert$ | determinant of $A$ | scalar; square matrices only |  | 01-14 |
| $D_f$ | domain of $f$ | set of valid inputs |  | 01-06 |
| $df$ | total differential of $f$ | sum of all partial contributions |  | 01-23 |
| $\dfrac{d}{dx}[\;\cdot\;]$ | "take the derivative with respect to $x$ of" | operator form |  | 01-17 |
| $\dfrac{dy}{dx}$ | derivative of $y$ with respect to $x$ | Leibniz notation |  | 01-17 |
| $\dfrac{dy}{y}$ | relative (fractional) change | multiply by 100 for percent |  | 01-18 |
| $\dfrac{\partial f}{\partial x}$, $f_x$ | partial derivative with respect to $x$ | other variables held constant |  | 01-23 |
| $D_hf$ | finite-difference derivative estimate | notation local to this chapter |  | 01-26 |
| $\displaystyle\int f(x)\,dx$ | indefinite integral (antiderivative family) | result is a **family** of functions |  | 01-19 |
| $\displaystyle\int_a^b f(x)\,dx$ | definite integral from $a$ to $b$ | result is a **number** |  | 01-19 |
| $\displaystyle\lim_{b\to\infty}$ | the limit defining an improper integral | improper integrals are limits, not integrals |  | 01-21 |
| $\displaystyle\lim_{x \to a}f(x)$ | the limit of $f$ as $x$ approaches $a$ | $x$ never equals $a$ |  | 01-16 |
| $\displaystyle\sum_{n=1}^{\infty}a_n$ | infinite series | from Chapter 01-15 |  | 01-22 |
| $D_{\mathbf{u}}f$ | directional derivative of $f$ in direction $\mathbf{u}$ | $\mathbf{u}$ must be a **unit** vector |  | 01-23 |
| DNE | does not exist | the correct answer when no limit exists |  | 01-16 |
| $\dot{y}$, $\ddot{y}$ | first and second derivative **with respect to time** | Newton/dot notation |  | 01-17 |
| $d_{\text{random}}$ | random disturbance | noise-type contribution |  | 01-36 |
| $d_{\text{systematic}}$ | systematic disturbance | bias/drift-type contribution |  | 01-36 |
| $du$, $v$ | the results of that differentiation and integration | — |  | 01-21 |
| $dV$ | differential volume element | m³ | ft³ or in³ | 01-24 |
| $dV$ | volume of one thin slice | disc, washer, or shell |  | 01-20 |
| $dx$ | differential of the integration variable | tells you *what* you are integrating with respect to |  | 01-19 |
| $dx$, $dy$ | differentials | the linear estimate of the change |  | 01-18 |
| $e$ | eccentricity, $c/a$ | **not** Euler's number here |  | 01-09 |
| $e$ | Euler's number, $\approx 2.71828...$ | irrational, defined precisely in §5.3 |  | 01-05 |
| $E$ | margin of error | half-width for symmetric intervals |  | 01-32 |
| $E$ | three-dimensional integration region | m³ as a volume when coordinates are lengths | ft³ or in³ | 01-24 |
| $E_{\%}$ | percent error | % |  | 01-03 |
| $E[g(X)]$ | expected value of a function of $X$ | weighted sum or integral |  | 01-29 |
| $e_a$ | absolute error | $ | x_{\text{approx}}-x^\* | 01-26 |
| $E_{abs}$ | absolute error | same as $x$ |  | 01-03 |
| $EC$ | expected cost | lower is preferred in a cost-only model |  | 01-37 |
| $e_i$ | residual | $y_i-\hat y_i$ |  | 01-35 |
| $EL$ | expected loss | lower is preferred |  | 01-37 |
| $E_n(x)$ | truncation error, $f(x) - P_n(x)$ | written $R_n$ in many texts |  | 01-22 |
| $EOL_i$ | expected opportunity loss of decision $i$ | probability-weighted regret |  | 01-37 |
| $e_r$ | relative error | $e_a/ | x^\* | 01-26 |
| $E_{rel}$ | relative error | dimensionless |  | 01-03 |
| $EV$ | expected value | probability-weighted average consequence |  | 01-37 |
| $EVPI$ | expected value of perfect information | $EV_{\text{PI}}-\max EV$ for benefit/net-value problems |  | 01-37 |
| $EV_{\text{PI}}$ | expected value with perfect information | best decision chosen after state is known |  | 01-37 |
| $\exp(x)$ | same as $e^x$ | used when exponent is complex expression |  | 01-05 |
| $F$ | force | N | lbf | 01-02 |
| $F$ | future worth/value |  |  | 02-04, 02-05, 02-06, 02-07, 02-08, 02-09, 02-10 |
| $F$ | ratio of mean squares | compared with an $F$ critical value |  | 01-34 |
| $f \circ g$ | composite function, $f(g(x))$ | read "f of g" |  | 01-06 |
| $f''(x)$, $\dfrac{d^2y}{dx^2}$ | second derivative | — |  | 01-17 |
| $f'(x)$ | derivative of $f$ with respect to $x$ | Lagrange notation |  | 01-17 |
| $f'(x)$ | exact first derivative | when an analytic derivative exists |  | 01-26 |
| $f'$, $f''$ | first and second derivatives | as in Chapter 01-17 |  | 01-18 |
| $f(a)$ | the **value** of $f$ at $a$ | may differ from the limit, or not exist |  | 01-16 |
| $f^{(n)}(a)$ | $n$th derivative of $f$ evaluated at $a$ | $f^{(0)} = f$ |  | 01-22 |
| $f^{(n)}(x)$, $\dfrac{d^ny}{dx^n}$ | $n$th derivative | primes get unreadable past three |  | 01-17 |
| $F(x)$ | an antiderivative of $f(x)$ | so $F'(x) = f(x)$ |  | 01-19 |
| $F(x)$ | cumulative distribution function | $P(X\le x)$ |  | 01-38 |
| $F(x)$ | cumulative distribution function | $F(x)=P(X\le x)$ |  | 01-29 |
| $F(x)$ | force as a function of position | — |  | 01-20 |
| $f(x)$ | function $f$ evaluated at $x$ | $f$ is the function; $f(x)$ is its value |  | 01-06 |
| $f(x)$ | PMF or PDF depending on context | identify discrete vs continuous first |  | 01-29 |
| $f(x,y)$ | scalar field or surface height | problem-dependent | problem-dependent | 01-24 |
| $f(x,y)$, $f(x,y,z)$ | scalar function of several variables | output is a number |  | 01-23 |
| $F(z)$ | left-tail unit-normal probability | Handbook: area from $-\infty$ to $z$ |  | 01-30 |
| $f^{-1}(x)$ | inverse function of $f$ | not $1/f(x)$ |  | 01-06 |
| $F_0$ | observed $F$ statistic | ratio of sample variances |  | 01-33 |
| $f_{\text{rms}}$ | root-mean-square value of $f$ | — |  | 01-20 |
| $F_W$ | weight (a force) | N | lbf | 01-02 |
| $f_{xx}$, $f_{yy}$ | second partials in the same variable | — |  | 01-23 |
| $f_{xy}$, $f_{yx}$ | **mixed** second partials | equal for well-behaved $f$ |  | 01-23 |
| $G$ | arithmetic gradient amount |  |  | 02-04, 02-05, 02-06, 02-07, 02-08, 02-09, 02-10 |
| $g$ | local gravitational acceleration | m/s² | ft/s² | 01-02 |
| $g(t)$ | forcing or source term | must match the equation's derivative terms | same dimensional requirement | 01-25 |
| $g(x,y) = k$ | constraint equation | — |  | 01-23 |
| $\gamma = \rho g$ | weight density (specific weight) | N/m³; 9810 N/m³ for water |  | 01-20 |
| $\Gamma(\cdot)$ | gamma function | used in Weibull mean and variance |  | 01-38 |
| $g_c$ | force unit conversion constant | — | 32.174 lbm·ft/(lbf·s²) | 01-02 |
| $h$ | height | — |  | 01-10 |
| $h$ | height or depth | m | ft | 01-02 |
| $H$ | Hessian matrix | matrix of second partial derivatives |  | 01-26 |
| $h$ | spatial or independent-variable step size | also written $\Delta x$ |  | 01-26 |
| $h$ or $\Delta x$ | the increment in the independent variable | shrinks to zero in the limit |  | 01-17 |
| $H_0$ | null hypothesis | reference claim used to build the test statistic |  | 01-33 |
| $H_1$ | alternative hypothesis | claim supported when $H_0$ is rejected |  | 01-33 |
| $\hat a$ | fitted intercept | predicted $y$ at $x=0$ |  | 01-35 |
| $\hat b$ | fitted slope | change in fitted $y$ per unit $x$ |  | 01-35 |
| $\hat y_i$ | fitted response at $x_i$ | value on fitted line |  | 01-35 |
| $\hat{A}$ | unit vector in direction of $\vec{A}$ | $\lvert\hat{A}\rvert = 1$ |  | 01-13 |
| $\hat{\imath}$, $\hat{\jmath}$, $\hat{k}$ | unit vectors along $x$, $y$, $z$ axes | right-hand coordinate system |  | 01-13 |
| $\hat\sigma$ | estimated process standard deviation | may come from $\bar R/d_2$ or $\bar S/c_4$ |  | 01-40 |
| $\hat\theta$ | point estimator / point estimate | statistic used to estimate $\theta$ |  | 01-32 |
| $I$ | exact integral | numerical rules produce approximations to it |  | 01-26 |
| $I$ | identity matrix | 1's on the diagonal, 0's elsewhere |  | 01-14 |
| $i$ | imaginary unit, $i^2 = -1$ | complex roots in §7.5 |  | 01-07 |
| $i$ | interest rate per period |  |  | 02-04, 02-05, 02-06, 02-07, 02-08, 02-09, 02-10 |
| $I$ | the unknown integral, treated as an algebraic quantity | used in the cyclic case |  | 01-21 |
| $\in$ | "is an element of" | $x \in \mathbb{R}$ means $x$ is a real number |  | 01-04 |
| $\infty$ | infinity | not a number; used in interval notation |  | 01-04 |
| $\infty$, $-\infty$ | unbounded growth, positive or negative | not a number |  | 01-16 |
| $I_x$, $I_y$ | second moment of area about the $x$- and $y$-axis | also called moment of inertia of the area |  | 01-20 |
| $j$ | imaginary unit, $j^2 = -1$ | Handbook convention; physics uses $i$ |  | 01-12 |
| $J$ | Jacobian determinant or its absolute value as stated | coordinate-scale dependent | same dimensional role | 01-24 |
| $k$ | coverage factor | Handbook notes $k=2$ is typically used for approximately 95% |  | 01-36 |
| $K$ | gain in a supplied first-order model | output/input | output/input | 01-25 |
| $k$ | number of subgroups | baseline groups |  | 01-39 |
| $k$ | number of treatments | one-way / block design |  | 01-34 |
| $k$ | spring constant | N/m |  | 01-20 |
| $k$ | summation index (dummy variable) | also $i$, $j$; never reused as a real quantity |  | 01-15 |
| $KE$, $PE$ | kinetic, potential energy | J | ft·lbf | 01-02 |
| $L$ | arc length | — |  | 01-20 |
| $l$ | slant height | for cones and pyramids |  | 01-10 |
| $L$ | the limit computed in the ratio test | — |  | 01-22 |
| $L$ | the limiting value | a finite number, when it exists |  | 01-16 |
| $L_1$, $L_2$ | labels for two lines | — |  | 01-11 |
| $\lambda$ | eigenvalue | scalar |  | 01-14 |
| $\lambda$ | Lagrange multiplier | — |  | 01-23 |
| $\lambda$ | Poisson mean event count | also Poisson variance |  | 01-38 |
| LCL | lower control limit | lower three-sigma-type boundary |  | 01-39 |
| $\ln x$ | natural logarithm of $x$, base $e$ | — |  | 01-05 |
| $\log x$ or $\log_{10} x$ | common logarithm, base 10 | Handbook uses $\log_{10}$ |  | 01-05 |
| $\log_b x$ | logarithm of $x$ to base $b$ | — |  | 01-05 |
| $LSL$ | lower specification limit | engineering/customer/design requirement |  | 01-40 |
| $\lvert a \rvert$ | absolute value of $a$ | — | — | 01-01 |
| $\lvert x \rvert$ | absolute value of $x$ | introduced in 01-01 |  | 01-04 |
| $\lvert z \rvert$ or $r$ | modulus (magnitude) of $z$ | — |  | 01-12 |
| $\lvert\vec{A}\rvert$ or $A$ | magnitude of $\vec{A}$ | scalar, always $\ge 0$ |  | 01-13 |
| $m$ | mass | kg | lbm or slug | 01-02 |
| $m$ | midpoint of specification band | $(USL+LSL)/2$ |  | 01-40 |
| $m$ | mode of triangular distribution | $a\le m\le b$ |  | 01-38 |
| $m$ | number of independent equations | — |  | 01-08 |
| $m$ | slope of a line | — |  | 01-09 |
| $M$ | total mass | kg | slug or lbm as specified | 01-24 |
| $m \times n$ | dimensions: $m$ rows, $n$ columns | rows first, always |  | 01-14 |
| $m$, $m_1$, $m_2$ | slopes of lines | from 01-09 §9.1 |  | 01-11 |
| $\mathbb{R}$ | all real numbers | $(-\infty, +\infty)$ |  | 01-06 |
| $\mathbb{R}$ | the set of all real numbers | — |  | 01-04 |
| $\mathbf{F}$ | vector field, $\mathbf{F} = F_x\hat{\imath} + F_y\hat{\jmath} + F_z\hat{k}$ | — |  | 01-23 |
| $\mathbf{v}$ | eigenvector | column vector |  | 01-14 |
| $\mathbf{x}$, $\mathbf{b}$ | column vectors | $n \times 1$ matrices |  | 01-14 |
| $M_{ij}$ | minor of element $a_{ij}$ | determinant with row $i$, col $j$ deleted |  | 01-14 |
| $MS$ | mean square | $SS$ divided by its df |  | 01-34 |
| $MSB$ | block mean square | randomized block design |  | 01-34 |
| $MSE$ | error mean square | denominator for ANOVA $F$ tests |  | 01-34 |
| $MSE$ | residual mean square | $SSE/(n-2)$ for simple linear regression |  | 01-35 |
| $MST$ | treatment mean square | one-way / block design |  | 01-34 |
| $m_{\text{tan}}$, $m_{\text{norm}}$ | slopes of the tangent and normal lines | — |  | 01-17 |
| $\mu$ | population mean | center of the normal curve |  | 01-30 |
| $\mu$ | population mean | target parameter in mean intervals |  | 01-32 |
| $\mu$ | population mean | fixed but often unknown |  | 01-31 |
| $\mu$ | population mean / expected value | $\mu=E[X]$ |  | 01-29 |
| $\mu$ | stable process mean | process center |  | 01-40 |
| $\mu_0$ | hypothesized population mean | value stated in $H_0$ |  | 01-33 |
| $n$ | degree of the polynomial | highest power of $x$ |  | 01-07 |
| $N$ | finite population size | hypergeometric |  | 01-38 |
| $N$ | lot size | finite-lot model |  | 01-41 |
| $N$ | mantissa (coefficient) in scientific notation, $1 \le \lvert N \rvert < 10$ | — | — | 01-01 |
| $n$ | number of binomial trials | fixed before the experiment |  | 01-29 |
| $n$ | number of periods |  |  | 02-04, 02-05, 02-06, 02-07, 02-08, 02-09, 02-10 |
| $n$ | number of significant figures | — |  | 01-03 |
| $n$ | number of subintervals | Simpson requires even $n$ |  | 01-26 |
| $n$ | number of subintervals | driven to infinity in the limit |  | 01-19 |
| $n$ | number of unknowns | — |  | 01-08 |
| $n$ | observations per subgroup | Handbook table uses $n=2$ through 10 |  | 01-39 |
| $n$ | repetitions per factor combination | two-factor factorial design |  | 01-34 |
| $n$ | sample size | units inspected |  | 01-41 |
| $n$ | sample size | number of observations |  | 01-30, 01-31 |
| $n$ | sample size | positive integer |  | 01-32 |
| $n$ | sample size / fixed number of draws | hypergeometric |  | 01-38 |
| $n$ | term number, or number of terms | context distinguishes them |  | 01-15 |
| $n$ | total number of objects or trials | context dependent |  | 01-28 |
| $N$ | total number of observations | $N=\sum_i n_i$ |  | 01-34 |
| $n!$ | $n$ factorial | $n! = n(n-1)(n-2)\cdots(1)$ |  | 01-15 |
| $n!$ | factorial | $n(n-1)\cdots2\cdot1$ |  | 01-28 |
| $n!$ | factorial, $n(n-1)\cdots(1)$, with $0! = 1$ | from Chapter 01-15 |  | 01-22 |
| $\nabla$ | del operator, $\left(\frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z}\right)$ | pronounced "del" or "nabla" |  | 01-23 |
| $\nabla f$ | **gradient** of a scalar field | a **vector** |  | 01-23 |
| $\nabla\cdot\mathbf{F}$ | **divergence** of a vector field | a **scalar** |  | 01-23 |
| $\nabla\times\mathbf{F}$ | **curl** of a vector field | a **vector** |  | 01-23 |
| $n_i$ | sample size for treatment $i$ | may differ by treatment |  | 01-34 |
| $\nu$ | degrees of freedom | often $n-1$ |  | 01-32 |
| $\nu$ | degrees of freedom | often $n-1$ in one-sample problems |  | 01-31 |
| $\nu$ | degrees of freedom | depends on the procedure |  | 01-33 |
| $\nu$ | residual degrees of freedom | $n-2$ in simple linear regression |  | 01-35 |
| $O(g(n))$ | order of growth | asymptotic scaling, not an exact runtime |  | 01-27 |
| OC curve | operating characteristic curve | plots $P_a$ versus lot quality |  | 01-41 |
| $p$ | directed distance from parabola vertex to focus | **not** pressure here |  | 01-09 |
| $p$ | exponent in a $p$-series $\sum n^{-p}$ | — |  | 01-22 |
| $p$ | fraction/probability nonconforming | binomial model |  | 01-41 |
| $p$ | p-value | tail probability at least as extreme as the observed statistic under $H_0$ |  | 01-33 |
| $P$ | present worth/value |  |  | 02-04, 02-05, 02-06, 02-07, 02-08, 02-09, 02-10 |
| $p$ | pressure | Pa | lbf/ft² or psi | 01-02 |
| $p$ | probability of success per trial | constant for a binomial model |  | 01-29 |
| $p$ | success probability on each Bernoulli trial | geometric / negative binomial |  | 01-38 |
| $p$ | the exponent in the convergence test $\int x^{-p}dx$ | — |  | 01-21 |
| $P(A)$ | probability of event $A$ | between 0 and 1 |  | 01-28 |
| $P(A\mid B)$ | conditional probability | probability of $A$ given $B$ occurred |  | 01-28 |
| $P(n,r)$ | permutations | order matters |  | 01-28 |
| $P(x)$ | polynomial in variable $x$ | — |  | 01-07 |
| $P(X=x)$ | point probability | meaningful for discrete variables |  | 01-29 |
| $P_a$ | probability of accepting the lot | function of lot quality and plan |  | 01-41 |
| $\partial$ | "partial" — the curly $d$ | signals that other variables are frozen |  | 01-23 |
| $p_i$ | probability of outcome $i$ | $0\le p_i\le1$ |  | 01-37 |
| $P_n(x)$ | Taylor polynomial of degree $n$ | the truncated series |  | 01-22 |
| $q$ | failure probability | $q=1-p$ |  | 01-38 |
| $q$ | probability of failure | $q=1-p$ |  | 01-29 |
| $Q_x$, $Q_y$ | first moment of area about the $x$- and $y$-axis | $Q_x = \int y\,dA$ |  | 01-20 |
| $r$ | characteristic root | inverse independent-variable unit when exponent is dimensional | same dimensional role | 01-25 |
| $r$ | common ratio (geometric) | $r = a_{n+1}/a_n$ |  | 01-15 |
| $r$ | common ratio of a geometric series | converges iff $\lvert r\rvert < 1$ |  | 01-22 |
| $r$ | number of successes in population, or target success count | meaning depends on distribution |  | 01-38 |
| $r$ | number selected | for permutations/combinations |  | 01-28 |
| $r$ | radius | not a correlation coefficient here |  | 01-10 |
| $r$ | radius of a circle | **not** resistance or correlation here |  | 01-09 |
| $R$ | radius of convergence of a power series | a distance in $x$ |  | 01-22 |
| $r$ | root (zero) of $P(x)$ | value where $P(r) = 0$ |  | 01-07 |
| $R$ | sample correlation coefficient | between $-1$ and $+1$ |  | 01-35 |
| $R(z)$ | right-tail unit-normal probability | Handbook: area from $z$ to $\infty$ |  | 01-30 |
| $r,\theta$ | polar/cylindrical radius and azimuth angle | m; rad | ft or in; rad | 01-24 |
| $R^2$ | coefficient of determination | fraction of sample response variation explained by the fitted line |  | 01-35 |
| rad | radians | — |  | 01-11 |
| $R_f$ | range of $f$ | set of possible outputs |  | 01-06 |
| $\rho$ | density | kg/m³ | lbm/ft³ | 01-02 |
| $\rho$ | mass density | kg/m³ |  | 01-20 |
| $\rho_A(x,y)$ | mass per unit area of a lamina | kg/m² | slug/ft² or lbm/ft² as specified | 01-24 |
| $\rho_V(x,y,z)$ | mass per unit volume | kg/m³ | slug/ft³ or lbm/ft³ as specified | 01-24 |
| $R_i$ | range of subgroup $i$ | maximum minus minimum |  | 01-39 |
| $R_i$ | row $i$ of an augmented matrix | — |  | 01-08 |
| $R_i \leftarrow R_i + cR_j$ | replace row $i$ with itself plus $c$ times row $j$ | row operation |  | 01-08 |
| $R_{ij}$ | regret/opportunity loss for decision $i$ under state $j$ | nonnegative when defined against best state-specific choice |  | 01-37 |
| $R_k$ | residual | value of the governing equation evaluated at $x_k$ |  | 01-26 |
| RQL | rejectable quality level | guide-developed quality-engineering design point |  | 01-41 |
| $S$ | sample space | set of all possible outcomes |  | 01-28 |
| $s$ | sample standard deviation | random scatter estimate |  | 01-36 |
| $s$ | sample standard deviation | used in a $t$ interval |  | 01-32 |
| $s$ | sample standard deviation | $\sqrt{s^2}$ |  | 01-31 |
| $S$ | surface area | same units as area |  | 01-10 |
| $S$ | surface area of revolution | — |  | 01-20 |
| $S$ | the sum of the series, $\lim_{n\to\infty}S_n$ | exists only if convergent |  | 01-22 |
| $s$ | unilateral Laplace-transform variable | $1/\mathrm{s}$ when $t$ is time | $1/\mathrm{s}$ | 01-25 |
| $S(x)$ | survival probability | $P(X>x)=1-F(x)$ |  | 01-38 |
| $s^2$ | sample variance | uses denominator $n-1$ |  | 01-31 |
| $s_{\bar x}$ | standard error of the mean | $s/\sqrt n$ |  | 01-36 |
| $S_e$ | standard error of estimate | $\sqrt{MSE}$ |  | 01-35 |
| $S_i$ | sample standard deviation of subgroup $i$ | plotted on $S$ chart |  | 01-39 |
| $\sigma$ | population standard deviation | positive scale parameter |  | 01-30 |
| $\sigma$ | population standard deviation | known in a $z$ interval |  | 01-32 |
| $\sigma$ | population standard deviation | square root of $\sigma^2$ |  | 01-31 |
| $\sigma$ | population standard deviation | $\sqrt{V[X]}$ |  | 01-29 |
| $\sigma$ | stable process standard deviation | process spread |  | 01-40 |
| $\sigma_0^2$ | hypothesized population variance | variance stated in $H_0$ |  | 01-33 |
| $\sigma^2$ | population variance | $\sigma^2=V[X]$ |  | 01-30 |
| $\sigma^2$ | population variance | fixed population parameter |  | 01-31 |
| $\sigma^2$ | population variance | $V[X]$ |  | 01-29 |
| $\sigma_{\bar X}$ | standard deviation of $\bar X$ | $\sigma/\sqrt n$ for independent observations |  | 01-30 |
| $\sigma_{x_i}$ | standard deviation/standard uncertainty notation | Handbook probability/statistics form |  | 01-36 |
| $\sigma_y$ | standard uncertainty of output | Handbook probability/statistics notation |  | 01-36 |
| $S_\infty$ | sum of an infinite series | exists only when it converges |  | 01-15 |
| $\sin\theta$, $\cos\theta$, $\tan\theta$ | primary trig functions | — |  | 01-11 |
| $S_n$ | $n$th partial sum, $a_1 + \cdots + a_n$ | a finite number |  | 01-22 |
| $S_n$ | sum of the first $n$ terms (partial sum) | a finite number always |  | 01-15 |
| $\sqrt[n]{x}$ | $n$th root of $x$ | same as $x^{1/n}$ |  | 01-05 |
| $SS$ | sum of squares | measure of variation |  | 01-34 |
| $SSA,SSB$ | main-effect sums of squares | two-factor design |  | 01-34 |
| $SSAB$ | interaction sum of squares | two-factor design |  | 01-34 |
| $SSE$ | residual/error sum of squares | $\sum e_i^2$ |  | 01-35 |
| $\sum$ | summation operator | "sigma" |  | 01-15 |
| $SW$ | specific weight | N/m³ | lbf/ft³ | 01-02 |
| $S_{xx}$ | predictor corrected sum of squares | $\sum(x_i-\bar x)^2$ |  | 01-35 |
| $S_{xy}$ | corrected cross-product sum | $\sum(x_i-\bar x)(y_i-\bar y)$ |  | 01-35 |
| $S_{yy}$ | response corrected sum of squares | $\sum(y_i-\bar y)^2$ |  | 01-35 |
| $t$ | independent variable, usually time | s when time | s when time | 01-25 |
| $T$ | period of a periodic function | — |  | 01-20 |
| $T$ | Student's $t$ statistic | typically when $\sigma$ is unknown and replaced by $s$ |  | 01-31 |
| $T$ | temperature | K or °C | °R or °F | 01-02 |
| $t_0$ | observed Student's $t$ statistic | Handbook notation |  | 01-33 |
| $t_{\alpha,\nu}$ | $t$ critical value | upper-tail area $\alpha$, df $\nu$ |  | 01-31 |
| $t_{\alpha/2,\nu}$ | Student's $t$ upper-tail critical value | $\nu$ degrees of freedom |  | 01-32 |
| $\tau$ | first-order time constant | s | s | 01-25 |
| $\tau$ | time constant of an exponential | introduced here; used throughout Tier 2 |  | 01-05 |
| $\tau$ | time constant of an exponential decay | seconds |  | 01-21 |
| $\text{tr}(A)$ | trace of $A$ | sum of diagonal elements |  | 01-14 |
| $\theta$ | angle, **in radians** | non-negotiable in this chapter |  | 01-22 |
| $\theta$ | generic population parameter | fixed but usually unknown |  | 01-32 |
| $\theta$ | the substitution variable in a trigonometric substitution | — |  | 01-21 |
| $\theta$ or $\angle\theta$ | argument (angle) of $z$ | in radians or degrees |  | 01-12 |
| $\theta$, $\phi$, $\beta$ | angles | radians or degrees |  | 01-11 |
| $U$ | expanded uncertainty | $U=ku_y$ |  | 01-36 |
| $u$ | substitution variable | $u = g(x)$ |  | 01-19 |
| $u(t)$ | unit-step function | 1 | 1 | 01-25 |
| $u$, $dv$ | the two parts chosen in integration by parts | $u$ gets differentiated, $dv$ gets integrated |  | 01-21 |
| $u$, $v$ | intermediate functions in product, quotient, chain rules | — |  | 01-17 |
| $u,v,w$ | generic transformed coordinates | problem-dependent | problem-dependent | 01-24 |
| UCL | upper control limit | upper three-sigma-type boundary |  | 01-39 |
| $USL$ | upper specification limit | engineering/customer/design requirement |  | 01-40 |
| USL, LSL | upper/lower specification limits | engineering/customer limits, not control limits |  | 01-39 |
| $u_{x_i}$ | standard uncertainty of input $x_i$ | guide notation |  | 01-36 |
| $u_y$ | combined standard uncertainty of $y$ | guide notation |  | 01-36 |
| $v$ | speed | m/s | ft/s | 01-02 |
| $V$ | volume | m³, ft³, in³ |  | 01-10 |
| $V(E)$ | volume of region $E$ | m³ | ft³ or in³ | 01-24 |
| $\varepsilon$, $\delta$ | tolerance and window in the formal definition | mentioned, not used computationally |  | 01-16 |
| $\varrho,\phi,\theta$ | spherical radius, polar angle from $+z$, azimuth angle | m; rad; rad | ft or in; rad; rad | 01-24 |
| $\vec{A} \cdot \vec{B}$ | dot product | result is a scalar |  | 01-13 |
| $\vec{A} \times \vec{B}$ | cross product | result is a vector |  | 01-13 |
| $\vec{A}$, $\mathbf{A}$ | vector $A$ | both notations used; bold preferred in display |  | 01-13 |
| $W$ | work | joules, N·m |  | 01-20 |
| $W(z)$ | central unit-normal probability | Handbook: area from $-z$ to $+z$ for $z\ge0$ |  | 01-30 |
| $w_i$ | input uncertainty | Handbook instrumentation form |  | 01-36 |
| $w_R$ | uncertainty of calculated result $R$ | Handbook instrumentation notation |  | 01-36 |
| $x$ | exponent, a power of ten | — | — | 01-01 |
| $x$ | measured quantity value | Handbook measurement-error model |  | 01-36 |
| $X$ | normal random variable | original engineering units |  | 01-30 |
| $X$ | number nonconforming in sample | discrete random variable |  | 01-41 |
| $x$ | number of successes in a binomial model | integer $0,\ldots,n$ |  | 01-29 |
| $x$ | one observed or threshold value | same units as $X$ |  | 01-30 |
| $x$ | one possible numerical value of $X$ | lowercase denotes a value |  | 01-29 |
| $X$ | random variable | uppercase denotes the variable |  | 01-29 |
| $x$ | realized count | discrete models |  | 01-38 |
| $x \to a$ | "$x$ approaches $a$" | from both sides |  | 01-16 |
| $x \to a^+$ | approach from the **right**, $x > a$ | right-hand limit |  | 01-16 |
| $x \to a^-$ | approach from the **left**, $x < a$ | left-hand limit |  | 01-16 |
| $x^\*$ | exact or target value | usually unknown in a real numerical problem |  | 01-26 |
| $x, y, z$ | unknown variables | — |  | 01-04 |
| $x_i$ | predictor value for observation $i$ | horizontal-axis variable |  | 01-35 |
| $X_{ij}$ | observation $j$ in subgroup $i$ | individual measurement |  | 01-39 |
| $x_k$ | numerical estimate at iteration $k$ | $k=0$ is the starting estimate |  | 01-26 |
| $x_k$, $x_k^*$ | subinterval endpoint; sample point in subinterval $k$ | — |  | 01-19 |
| $x_{meas}$ | measured value | same as $x$ |  | 01-03 |
| $x_{\text{ref}}$ | reference quantity value | comparison value |  | 01-36 |
| $x_{true}$ | true value of a quantity | same as $x$ |  | 01-03 |
| $y$ | trial count to the $r$th success | negative binomial |  | 01-38 |
| $y',y'',y^{(n)}$ | first, second, and $n$th derivatives of $y$ | $[y]/[t]$, $[y]/[t]^2$, ... | same dimensional pattern | 01-25 |
| $Y(s)$ | Laplace transform of $y(t)$ | $[y]\cdot\mathrm s$ under the usual time transform | same dimensional role | 01-25 |
| $y(t)$ | unknown dependent variable | problem-dependent | problem-dependent | 01-25 |
| $y=f(x_1,\ldots,x_n)$ | calculated result | depends on measured inputs |  | 01-36 |
| $Y=\sum a_iX_i$ | linear combination | coefficients $a_i$ are constants |  | 01-29 |
| $y_i$ | observed response for observation $i$ | vertical-axis variable |  | 01-35 |
| $y_{ij}$ | observation $j$ under treatment $i$ | one-way notation |  | 01-34 |
| $y_{ijk}$ | observation $k$ at factor combination $(i,j)$ | two-factor notation |  | 01-34 |
| $y_k$ | numerical ODE solution at $t_k$ | $t_k=t_0+k\Delta t$ |  | 01-26 |
| $z$ | a complex number | — |  | 01-12 |
| $z$ | one standardized value | dimensionless |  | 01-30 |
| $Z$ | standard normal random variable | mean 0, standard deviation 1 |  | 01-30 |
| $Z$ | standard normal statistic | typically when population $\sigma$ is known |  | 01-31 |
| $z^*$ or $\bar{z}$ | complex conjugate of $z$ | — |  | 01-12 |
| $Z_0$ | observed $z$ test statistic | Handbook notation |  | 01-33 |
| $z_{\alpha/2}$ | standard-normal upper-tail critical value | leaves $\alpha/2$ to the right |  | 01-32 |

## Scope note

Global collision rules, structural conventions, reserved subscripts, unit-presentation rules, and verified constants are systemwide. Chapter-local variables remain defined locally unless they are promoted into the global contract. This keeps discipline-specific notation from being falsely universalized.
