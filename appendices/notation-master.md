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

## Chapter coverage cross-reference

This table establishes publication-level notation coverage for every canonical chapter. Symbol definitions remain centralized above; a chapter marked local banner contains its own Notation Used Here section, while master only relies on the global contract unless a local ambiguity requires a banner.

| Chapter | Title | Source | Coverage |
|---|---|---|---|
| 00-01 | Chapter 00-01: How to Use This Guide | [layer-0-orientation/00-01-how-to-use-this-guide.md](../layer-0-orientation/00-01-how-to-use-this-guide.md) | master only |
| 00-02 | Chapter 00-02: The Exam and the CBT Format | [layer-0-orientation/00-02-the-exam-and-the-cbt-format.md](../layer-0-orientation/00-02-the-exam-and-the-cbt-format.md) | master only |
| 00-03 | Chapter 00-03: Navigating the FE Reference Handbook | [layer-0-orientation/00-03-navigating-the-fe-reference-book.md](../layer-0-orientation/00-03-navigating-the-fe-reference-book.md) | master only |
| 01-01 | Chapter 01-01: Numbers, Magnitude, and Metric Prefixes | [layer-1-substrate/01-01-numbers-magnitude-and-metric-prefixes.md](../layer-1-substrate/01-01-numbers-magnitude-and-metric-prefixes.md) | local banner |
| 01-02 | Chapter 01-02: Units, Dimensions, and the Pound Problem | [layer-1-substrate/01-02-units-dimensions-and-the-pound-problem.md](../layer-1-substrate/01-02-units-dimensions-and-the-pound-problem.md) | local banner |
| 01-03 | Chapter 01-03: Accuracy, Precision, and Significant Figures | [layer-1-substrate/01-03-Accuracy-Precision-and-Significant-Figures.md](../layer-1-substrate/01-03-Accuracy-Precision-and-Significant-Figures.md) | local banner |
| 01-04 | Chapter 01-04: Expressions, Equations, and Inequalities | [layer-1-substrate/01-04-Expressions-Equations-and-Inequalities.md](../layer-1-substrate/01-04-Expressions-Equations-and-Inequalities.md) | local banner |
| 01-05 | Chapter 01-05: Exponents, Radicals, and Logarithms | [layer-1-substrate/01-05-Exponents-Radicals-and-Logarithms.md](../layer-1-substrate/01-05-Exponents-Radicals-and-Logarithms.md) | local banner |
| 01-06 | Chapter 01-06: Functions, Graphs, and Transformations | [layer-1-substrate/01-06-Functions-Graphs-and-Transformations.md](../layer-1-substrate/01-06-Functions-Graphs-and-Transformations.md) | local banner |
| 01-07 | Chapter 01-07: Polynomials and Their Roots | [layer-1-substrate/01-07-Polynomials-and-Their-Roots.md](../layer-1-substrate/01-07-Polynomials-and-Their-Roots.md) | local banner |
| 01-08 | Chapter 01-08: Systems of Linear Equations | [layer-1-substrate/01-08-Systems-of-Linear-Equations.md](../layer-1-substrate/01-08-Systems-of-Linear-Equations.md) | local banner |
| 01-09 | Chapter 01-09: Analytic Geometry | [layer-1-substrate/01-09-Analytic-Geometry.md](../layer-1-substrate/01-09-Analytic-Geometry.md) | local banner |
| 01-10 | Chapter 01-10: Areas, Volumes, and Mensuration | [layer-1-substrate/01-10-Areas-Volumes-and-Mensuration.md](../layer-1-substrate/01-10-Areas-Volumes-and-Mensuration.md) | local banner |
| 01-11 | Chapter 01-11: Trigonometry | [layer-1-substrate/01-11-Trigonometry.md](../layer-1-substrate/01-11-Trigonometry.md) | local banner |
| 01-12 | Chapter 01-12: Complex Numbers | [layer-1-substrate/01-12-Complex-Numbers.md](../layer-1-substrate/01-12-Complex-Numbers.md) | local banner |
| 01-13 | Chapter 01-13: Vectors and Vector Operations | [layer-1-substrate/01-13-Vectors-and-Vector-Operations.md](../layer-1-substrate/01-13-Vectors-and-Vector-Operations.md) | local banner |
| 01-14 | Chapter 01-14: Matrices, Determinants, and Eigenvalues | [layer-1-substrate/01-14-Matrices-Determinants-and-Eigenvalues.md](../layer-1-substrate/01-14-Matrices-Determinants-and-Eigenvalues.md) | local banner |
| 01-15 | Chapter 01-15: Sequences, Series, and Progressions | [layer-1-substrate/01-15-Sequences-Series-and-Progressions.md](../layer-1-substrate/01-15-Sequences-Series-and-Progressions.md) | local banner |
| 01-16 | Chapter 01-16: Limits and Continuity | [layer-1-substrate/01-16-Limits-and-Continuity.md](../layer-1-substrate/01-16-Limits-and-Continuity.md) | local banner |
| 01-17 | Chapter 01-17: The Derivative | [layer-1-substrate/01-17-The-Derivative.md](../layer-1-substrate/01-17-The-Derivative.md) | local banner |
| 01-18 | Chapter 01-18: Applications of the Derivative | [layer-1-substrate/01-18-Applications-of-the-Derivative.md](../layer-1-substrate/01-18-Applications-of-the-Derivative.md) | local banner |
| 01-19 | Chapter 01-19: Antiderivatives and the Definite Integral | [layer-1-substrate/01-19-Antiderivatives-and-the-Definite-Integral.md](../layer-1-substrate/01-19-Antiderivatives-and-the-Definite-Integral.md) | local banner |
| 01-20 | Chapter 01-20: Applications of the Definite Integral | [layer-1-substrate/01-20-Applications-of-the-Definite Integral.md](../layer-1-substrate/01-20-Applications-of-the-Definite Integral.md) | local banner |
| 01-21 | Chapter 01-21: Techniques of Integration | [layer-1-substrate/01-21-Techniques-of-Integration.md](../layer-1-substrate/01-21-Techniques-of-Integration.md) | local banner |
| 01-22 | Chapter 01-22: Infinite Series and Taylor Expansions | [layer-1-substrate/01-22-Infinite-Series-and-Taylor-Expansions.md](../layer-1-substrate/01-22-Infinite-Series-and-Taylor-Expansions.md) | local banner |
| 01-23 | Chapter 01-23: Partial Derivatives and Vector Calculus | [layer-1-substrate/01-23-Partial-Derivatives-and-Vector-Calculus.md](../layer-1-substrate/01-23-Partial-Derivatives-and-Vector-Calculus.md) | local banner |
| 01-24 | Chapter 01-24: Multiple Integration | [layer-1-substrate/01-24-Multiple-Integration.md](../layer-1-substrate/01-24-Multiple-Integration.md) | local banner |
| 01-25 | Chapter 01-25: Differential Equations | [layer-1-substrate/01-25-Differential-Equations.md](../layer-1-substrate/01-25-Differential-Equations.md) | local banner |
| 01-26 | Chapter 01-26: Numerical Methods | [layer-1-substrate/01-26-Numerical-Methods.md](../layer-1-substrate/01-26-Numerical-Methods.md) | local banner |
| 01-27 | Chapter 01-27: Algorithm and Logic Development | [layer-1-substrate/01-27-Algorithm-and-Logic-Development.md](../layer-1-substrate/01-27-Algorithm-and-Logic-Development.md) | local banner |
| 01-28 | Chapter 01-28: Probability Fundamentals | [layer-1-substrate/01-28-Probability-Fundamentals.md](../layer-1-substrate/01-28-Probability-Fundamentals.md) | local banner |
| 01-29 | Chapter 01-29: Random Variables and Probability Distributions | [layer-1-substrate/01-29-Random-Variables-and-Probability-Distributions.md](../layer-1-substrate/01-29-Random-Variables-and-Probability-Distributions.md) | local banner |
| 01-30 | Chapter 01-30: The Normal Distribution and the Central Limit Theorem | [layer-1-substrate/01-30-The-Normal-Distribution-and-the-Central-Limit-Theorem.md](../layer-1-substrate/01-30-The-Normal-Distribution-and-the-Central-Limit-Theorem.md) | local banner |
| 01-31 | Chapter 01-31: Sampling Distributions, Student's t, and Chi-Square | [layer-1-substrate/01-31-Sampling-Distributions-Students-t-and-Chi-Square.md](../layer-1-substrate/01-31-Sampling-Distributions-Students-t-and-Chi-Square.md) | local banner |
| 01-32 | Chapter 01-32: Estimation and Confidence Intervals | [layer-1-substrate/01-32-Estimation-and-Confidence-Intervals.md](../layer-1-substrate/01-32-Estimation-and-Confidence-Intervals.md) | local banner |
| 01-33 | Chapter 01-33: Hypothesis Testing and Statistical Decisions | [layer-1-substrate/01-33-Hypothesis-Testing-and-Statistical-Decisions.md](../layer-1-substrate/01-33-Hypothesis-Testing-and-Statistical-Decisions.md) | local banner |
| 01-34 | Chapter 01-34: Analysis of Variance and Design of Experiments | [layer-1-substrate/01-34-Analysis-of-Variance-and-Design-of-Experiments.md](../layer-1-substrate/01-34-Analysis-of-Variance-and-Design-of-Experiments.md) | local banner |
| 01-35 | Chapter 01-35: Linear Regression and Goodness of Fit | [layer-1-substrate/01-35-Linear-Regression-and-Goodness-of-Fit.md](../layer-1-substrate/01-35-Linear-Regression-and-Goodness-of-Fit.md) | local banner |
| 01-36 | Chapter 01-36: Measurement Uncertainty and Statistical Error Propagation | [layer-1-substrate/01-36-Measurement-Uncertainty-and-Statistical-Error-Propagation.md](../layer-1-substrate/01-36-Measurement-Uncertainty-and-Statistical-Error-Propagation.md) | local banner |
| 01-37 | Chapter 01-37: Expected Value, Decision Trees, and Risk | [layer-1-substrate/01-37-Expected-Value-Decision-Trees-and-Risk.md](../layer-1-substrate/01-37-Expected-Value-Decision-Trees-and-Risk.md) | local banner |
| 01-38 | Chapter 01-38: Common Engineering Probability Distributions | [layer-1-substrate/01-38-Common-Engineering-Probability-Distributions.md](../layer-1-substrate/01-38-Common-Engineering-Probability-Distributions.md) | local banner |
| 01-39 | Chapter 01-39: Statistical Process Control and Control Charts | [layer-1-substrate/01-39-Statistical-Process-Control-and-Control-Charts.md](../layer-1-substrate/01-39-Statistical-Process-Control-and-Control-Charts.md) | local banner |
| 01-40 | Chapter 01-40: Process Capability and Specification Performance | [layer-1-substrate/01-40-Process-Capability-and-Specification-Performance.md](../layer-1-substrate/01-40-Process-Capability-and-Specification-Performance.md) | local banner |
| 01-41 | Chapter 01-41: Acceptance Sampling and Operating Characteristic Curves | [layer-1-substrate/01-41-Acceptance-Sampling-and-Operating-Characteristic-Curves.md](../layer-1-substrate/01-41-Acceptance-Sampling-and-Operating-Characteristic-Curves.md) | local banner |
| 02-01 | Chapter 02-01: Engineering Ethics, Public Welfare, and Professional Judgment | [layer-2-core/a-professional/02-01-Engineering-Ethics-Public-Welfare-and-Professional-Judgment.md](../layer-2-core/a-professional/02-01-Engineering-Ethics-Public-Welfare-and-Professional-Judgment.md) | local banner |
| 02-02 | Chapter 02-02: Licensure, Model Law, Model Rules, and Responsible Charge | [layer-2-core/a-professional/02-02-Licensure-Model-Law-Model-Rules-and-Responsible-Charge.md](../layer-2-core/a-professional/02-02-Licensure-Model-Law-Model-Rules-and-Responsible-Charge.md) | local banner |
| 02-03 | Chapter 02-03: Contracts, Professional Liability, and Intellectual Property | [layer-2-core/a-professional/02-03-Contracts-Professional-Liability-and-Intellectual-Property.md](../layer-2-core/a-professional/02-03-Contracts-Professional-Liability-and-Intellectual-Property.md) | local banner |
| 02-04 | Chapter 02-04: Cash Flows, Interest, and Economic Equivalence | [layer-2-core/a-professional/02-04-Cash-Flows-Interest-and-Economic-Equivalence.md](../layer-2-core/a-professional/02-04-Cash-Flows-Interest-and-Economic-Equivalence.md) | local banner |
| 02-05 | Chapter 02-05: Present Worth and Future Worth | [layer-2-core/a-professional/02-05-Present-Worth-and-Future-Worth.md](../layer-2-core/a-professional/02-05-Present-Worth-and-Future-Worth.md) | local banner |
| 02-06 | Chapter 02-06: Annual Worth, Capital Recovery, and Gradient Series | [layer-2-core/a-professional/02-06-Annual-Worth-Capital-Recovery-and-Gradient-Series.md](../layer-2-core/a-professional/02-06-Annual-Worth-Capital-Recovery-and-Gradient-Series.md) | local banner |
| 02-07 | Chapter 02-07: Rate of Return and Minimum Attractive Rate of Return | [layer-2-core/a-professional/02-07-Rate-of-Return-and-Minimum-Attractive-Rate-of-Return.md](../layer-2-core/a-professional/02-07-Rate-of-Return-and-Minimum-Attractive-Rate-of-Return.md) | local banner |
| 02-08 | Chapter 02-08: Breakeven, Benefit-Cost, and Payback Analysis | [layer-2-core/a-professional/02-08-Breakeven-Benefit-Cost-and-Payback-Analysis.md](../layer-2-core/a-professional/02-08-Breakeven-Benefit-Cost-and-Payback-Analysis.md) | local banner |
| 02-09 | Chapter 02-09: Inflation, Depreciation, Taxes, and Replacement | [layer-2-core/a-professional/02-09-Inflation-Depreciation-Taxes-and-Replacement.md](../layer-2-core/a-professional/02-09-Inflation-Depreciation-Taxes-and-Replacement.md) | local banner |
| 02-10 | Chapter 02-10: Economic Decision-Making, Project Selection, and Risk | [layer-2-core/a-professional/02-10-Economic-Decision-Making-Project-Selection-and-Risk.md](../layer-2-core/a-professional/02-10-Economic-Decision-Making-Project-Selection-and-Risk.md) | local banner |
| 02-11 | Chapter 02-11: Atomic Structure, Bonding, and the Periodic Table | [layer-2-core/b-physical-science/02-11-Atomic-Structure-Bonding-and-the-Periodic-Table.md](../layer-2-core/b-physical-science/02-11-Atomic-Structure-Bonding-and-the-Periodic-Table.md) | local banner |
| 02-12 | Chapter 02-12: Chemical Quantities, Stoichiometry, and Reaction Balancing | [layer-2-core/b-physical-science/02-12-Chemical-Quantities-Stoichiometry-and-Reaction-Balancing.md](../layer-2-core/b-physical-science/02-12-Chemical-Quantities-Stoichiometry-and-Reaction-Balancing.md) | local banner |
| 02-13 | Chapter 02-13: Solutions, Concentration, Acids, Bases, and pH | [layer-2-core/b-physical-science/02-13-Solutions-Concentration-Acids-Bases-and-pH.md](../layer-2-core/b-physical-science/02-13-Solutions-Concentration-Acids-Bases-and-pH.md) | local banner |
| 02-14 | Chapter 02-14: Chemical Equilibrium, Electrochemistry, and Corrosion | [layer-2-core/b-physical-science/02-14-Chemical-Equilibrium-Electrochemistry-and-Corrosion.md](../layer-2-core/b-physical-science/02-14-Chemical-Equilibrium-Electrochemistry-and-Corrosion.md) | local banner |
| 02-15 | Chapter 02-15: Organic Chemistry and Biological Systems | [layer-2-core/b-physical-science/02-15-Organic-Chemistry-and-Biological-Systems.md](../layer-2-core/b-physical-science/02-15-Organic-Chemistry-and-Biological-Systems.md) | local banner |
| 02-16 | Chapter 02-16: Materials Classes, Structure, and Bonding | [layer-2-core/b-physical-science/02-16-Materials-Classes-Structure-and-Bonding.md](../layer-2-core/b-physical-science/02-16-Materials-Classes-Structure-and-Bonding.md) | local banner |
| 02-17 | Chapter 02-17: Material Properties and Engineering Selection | [layer-2-core/b-physical-science/02-17-Material-Properties-and-Engineering-Selection.md](../layer-2-core/b-physical-science/02-17-Material-Properties-and-Engineering-Selection.md) | local banner |
| 02-18 | Chapter 02-18: Diffusion, Phase Change, Heat Treatment, and Processing | [layer-2-core/b-physical-science/02-18-Diffusion-Phase-Change-Heat-Treatment-and-Processing.md](../layer-2-core/b-physical-science/02-18-Diffusion-Phase-Change-Heat-Treatment-and-Processing.md) | local banner |
| 02-19 | Chapter 02-19: Safety Systems, Hazard Communication, and Personal Protective Equipment | [layer-2-core/b-physical-science/02-19-Safety-Systems-Hazard-Communication-and-Personal-Protective-Equipment.md](../layer-2-core/b-physical-science/02-19-Safety-Systems-Hazard-Communication-and-Personal-Protective-Equipment.md) | local banner |
| 02-20 | Chapter 02-20: Fire, Explosion, Electrical, and Confined-Space Hazards | [layer-2-core/b-physical-science/02-20-Fire-Explosion-Electrical-and-Confined-Space-Hazards.md](../layer-2-core/b-physical-science/02-20-Fire-Explosion-Electrical-and-Confined-Space-Hazards.md) | local banner |
| 02-21 | Chapter 02-21: Toxicology, Exposure Limits, Risk, and Chemical Compatibility | [layer-2-core/b-physical-science/02-21-Toxicology-Exposure-Limits-Risk-and-Chemical-Compatibility.md](../layer-2-core/b-physical-science/02-21-Toxicology-Exposure-Limits-Risk-and-Chemical-Compatibility.md) | local banner |
| 02-22 | Chapter 02-22: Constructing a Free-Body Diagram | [layer-2-core/c-mechanics/02-22-Constructing-a-Free-Body-Diagram.md](../layer-2-core/c-mechanics/02-22-Constructing-a-Free-Body-Diagram.md) | local banner |
| 02-23 | Chapter 02-23: Equilibrium Equations for a 2D Concurrent Force System | [layer-2-core/c-mechanics/02-23-Equilibrium-Equations-for-a-2D-Concurrent-Force-System.md](../layer-2-core/c-mechanics/02-23-Equilibrium-Equations-for-a-2D-Concurrent-Force-System.md) | local banner |
| 02-24 | Chapter 02-24: Method of Joints for Planar Trusses | [layer-2-core/c-mechanics/02-24-Method-of-Joints-for-Planar-Trusses.md](../layer-2-core/c-mechanics/02-24-Method-of-Joints-for-Planar-Trusses.md) | local banner |
| 02-25 | Chapter 02-25: Moments, Couples, and Equivalent Force Systems | [layer-2-core/c-mechanics/02-25-Moments-Couples-and-Equivalent-Force-Systems.md](../layer-2-core/c-mechanics/02-25-Moments-Couples-and-Equivalent-Force-Systems.md) | local banner |
| 02-26 | Chapter 02-26: Rigid-Body Equilibrium and Support Reactions | [layer-2-core/c-mechanics/02-26-Rigid-Body-Equilibrium-and-Support-Reactions.md](../layer-2-core/c-mechanics/02-26-Rigid-Body-Equilibrium-and-Support-Reactions.md) | local banner |
| 02-27 | Chapter 02-27: Method of Sections, Frames, and Machines | [layer-2-core/c-mechanics/02-27-Method-of-Sections-Frames-and-Machines.md](../layer-2-core/c-mechanics/02-27-Method-of-Sections-Frames-and-Machines.md) | local banner |
| 02-28 | Chapter 02-28: Distributed Loads, Centroids, and Centers of Gravity | [layer-2-core/c-mechanics/02-28-Distributed-Loads-Centroids-and-Centers-of-Gravity.md](../layer-2-core/c-mechanics/02-28-Distributed-Loads-Centroids-and-Centers-of-Gravity.md) | local banner |
| 02-29 | Chapter 02-29: Area Moments of Inertia and the Parallel-Axis Theorem | [layer-2-core/c-mechanics/02-29-Area-Moments-of-Inertia-and-the-Parallel-Axis-Theorem.md](../layer-2-core/c-mechanics/02-29-Area-Moments-of-Inertia-and-the-Parallel-Axis-Theorem.md) | local banner |
| 02-30 | Chapter 02-30: Static Friction | [layer-2-core/c-mechanics/02-30-Static-Friction.md](../layer-2-core/c-mechanics/02-30-Static-Friction.md) | local banner |
| 02-31 | Chapter 02-31: Particle Kinematics — Rectilinear Motion | [layer-2-core/c-mechanics/02-31-Particle-Kinematics-Rectilinear-Motion.md](../layer-2-core/c-mechanics/02-31-Particle-Kinematics-Rectilinear-Motion.md) | local banner |
| 02-32 | Chapter 02-32: Particle Kinematics — Curvilinear and Relative Motion | [layer-2-core/c-mechanics/02-32-Particle-Kinematics-Curvilinear-and-Relative-Motion.md](../layer-2-core/c-mechanics/02-32-Particle-Kinematics-Curvilinear-and-Relative-Motion.md) | local banner |
| 02-33 | Chapter 02-33: Particle Kinetics — Force and Acceleration | [layer-2-core/c-mechanics/02-33-Particle-Kinetics-Force-and-Acceleration.md](../layer-2-core/c-mechanics/02-33-Particle-Kinetics-Force-and-Acceleration.md) | local banner |
| 02-34 | Chapter 02-34: Work, Energy, and Power | [layer-2-core/c-mechanics/02-34-Work-Energy-and-Power.md](../layer-2-core/c-mechanics/02-34-Work-Energy-and-Power.md) | local banner |
| 02-35 | Chapter 02-35: Impulse, Momentum, and Impact | [layer-2-core/c-mechanics/02-35-Impulse-Momentum-and-Impact.md](../layer-2-core/c-mechanics/02-35-Impulse-Momentum-and-Impact.md) | local banner |
| 02-36 | Chapter 02-36: Rigid-Body Planar Kinematics and Kinetics | [layer-2-core/c-mechanics/02-36-Rigid-Body-Planar-Kinematics-and-Kinetics.md](../layer-2-core/c-mechanics/02-36-Rigid-Body-Planar-Kinematics-and-Kinetics.md) | local banner |
| 02-37 | Chapter 02-37: Stress, Strain, and Axial/Thermal Deformation | [layer-2-core/c-mechanics/02-37-Stress-Strain-and-Axial-Thermal-Deformation.md](../layer-2-core/c-mechanics/02-37-Stress-Strain-and-Axial-Thermal-Deformation.md) | local banner |
| 02-38 | Chapter 02-38: Torsion | [layer-2-core/c-mechanics/02-38-Torsion.md](../layer-2-core/c-mechanics/02-38-Torsion.md) | local banner |
| 02-39 | Chapter 02-39: Beams — Shear, Moment, Bending, and Deflection | [layer-2-core/c-mechanics/02-39-Beams-Shear-Moment-Bending-and-Deflection.md](../layer-2-core/c-mechanics/02-39-Beams-Shear-Moment-Bending-and-Deflection.md) | local banner |
| 02-40 | Chapter 02-40: Combined Stress, Principal Stress, and Mohr's Circle | [layer-2-core/c-mechanics/02-40-Combined-Stress-Principal-Stress-and-Mohr-s-Circle.md](../layer-2-core/c-mechanics/02-40-Combined-Stress-Principal-Stress-and-Mohr-s-Circle.md) | local banner |
| 02-41 | Chapter 02-41: Fluid Properties, Pressure, and Hydrostatics | [layer-2-core/d-thermal-fluids/02-41-Fluid-Properties-Pressure-and-Hydrostatics.md](../layer-2-core/d-thermal-fluids/02-41-Fluid-Properties-Pressure-and-Hydrostatics.md) | local banner |
| 02-42 | Chapter 02-42: Buoyancy, Manometry, and Forces on Submerged Surfaces | [layer-2-core/d-thermal-fluids/02-42-Buoyancy-Manometry-and-Forces-on-Submerged-Surfaces.md](../layer-2-core/d-thermal-fluids/02-42-Buoyancy-Manometry-and-Forces-on-Submerged-Surfaces.md) | local banner |
| 02-43 | Chapter 02-43: Continuity, Velocity Fields, and Flow Kinematics | [layer-2-core/d-thermal-fluids/02-43-Continuity-Velocity-Fields-and-Flow-Kinematics.md](../layer-2-core/d-thermal-fluids/02-43-Continuity-Velocity-Fields-and-Flow-Kinematics.md) | local banner |
| 02-44 | Chapter 02-44: Bernoulli and Mechanical-Energy Equations | [layer-2-core/d-thermal-fluids/02-44-Bernoulli-and-Mechanical-Energy-Equations.md](../layer-2-core/d-thermal-fluids/02-44-Bernoulli-and-Mechanical-Energy-Equations.md) | local banner |
| 02-45 | Chapter 02-45: Internal Flow — Reynolds Number, Friction, and Head Loss | [layer-2-core/d-thermal-fluids/02-45-Internal-Flow-Reynolds-Number-Friction-and-Head-Loss.md](../layer-2-core/d-thermal-fluids/02-45-Internal-Flow-Reynolds-Number-Friction-and-Head-Loss.md) | local banner |
| 02-46 | Chapter 02-46: Momentum, Flow Measurement, Pumps, and Turbines | [layer-2-core/d-thermal-fluids/02-46-Momentum-Flow-Measurement-Pumps-and-Turbines.md](../layer-2-core/d-thermal-fluids/02-46-Momentum-Flow-Measurement-Pumps-and-Turbines.md) | local banner |
| 02-47 | Chapter 02-47: Thermodynamic Systems, Properties, Work, and Heat | [layer-2-core/d-thermal-fluids/02-47-Thermodynamic-Systems-Properties-Work-and-Heat.md](../layer-2-core/d-thermal-fluids/02-47-Thermodynamic-Systems-Properties-Work-and-Heat.md) | local banner |
| 02-48 | Chapter 02-48: Pure Substances, Phase Diagrams, and Property Tables | [layer-2-core/d-thermal-fluids/02-48-Pure-Substances-Phase-Diagrams-and-Property-Tables.md](../layer-2-core/d-thermal-fluids/02-48-Pure-Substances-Phase-Diagrams-and-Property-Tables.md) | local banner |
| 02-49 | Chapter 02-49: Ideal Gases, Gas Mixtures, and Psychrometrics | [layer-2-core/d-thermal-fluids/02-49-Ideal-Gases-Gas-Mixtures-and-Psychrometrics.md](../layer-2-core/d-thermal-fluids/02-49-Ideal-Gases-Gas-Mixtures-and-Psychrometrics.md) | local banner |
| 02-50 | Chapter 02-50: First Law — Closed Systems | [layer-2-core/d-thermal-fluids/02-50-First-Law-Closed-Systems.md](../layer-2-core/d-thermal-fluids/02-50-First-Law-Closed-Systems.md) | local banner |
| 02-51 | Chapter 02-51: First Law — Control Volumes | [layer-2-core/d-thermal-fluids/02-51-First-Law-Control-Volumes.md](../layer-2-core/d-thermal-fluids/02-51-First-Law-Control-Volumes.md) | local banner |
| 02-52 | Chapter 02-52: Second Law, Entropy, and Isentropic Processes | [layer-2-core/d-thermal-fluids/02-52-Second-Law-Entropy-and-Isentropic-Processes.md](../layer-2-core/d-thermal-fluids/02-52-Second-Law-Entropy-and-Isentropic-Processes.md) | local banner |
| 02-53 | Chapter 02-53: Power Cycles | [layer-2-core/d-thermal-fluids/02-53-Power-Cycles.md](../layer-2-core/d-thermal-fluids/02-53-Power-Cycles.md) | local banner |
| 02-54 | Chapter 02-54: Refrigeration and Heat Pumps | [layer-2-core/d-thermal-fluids/02-54-Refrigeration-and-Heat-Pumps.md](../layer-2-core/d-thermal-fluids/02-54-Refrigeration-and-Heat-Pumps.md) | local banner |
| 02-55 | Chapter 02-55: Conduction and Thermal Resistance | [layer-2-core/d-thermal-fluids/02-55-Conduction-and-Thermal-Resistance.md](../layer-2-core/d-thermal-fluids/02-55-Conduction-and-Thermal-Resistance.md) | local banner |
| 02-56 | Chapter 02-56: Extended Surfaces and Transient Conduction | [layer-2-core/d-thermal-fluids/02-56-Extended-Surfaces-and-Transient-Conduction.md](../layer-2-core/d-thermal-fluids/02-56-Extended-Surfaces-and-Transient-Conduction.md) | local banner |
| 02-57 | Chapter 02-57: Convection and Thermal Radiation | [layer-2-core/d-thermal-fluids/02-57-Convection-and-Thermal-Radiation.md](../layer-2-core/d-thermal-fluids/02-57-Convection-and-Thermal-Radiation.md) | local banner |
| 02-58 | Chapter 02-58: Heat Exchangers — LMTD and Effectiveness-NTU | [layer-2-core/d-thermal-fluids/02-58-Heat-Exchangers-LMTD-and-Effectiveness-NTU.md](../layer-2-core/d-thermal-fluids/02-58-Heat-Exchangers-LMTD-and-Effectiveness-NTU.md) | local banner |
| 02-59 | Chapter 02-59: Electrical Quantities, Ohm's Law, and DC Power | [layer-2-core/e-electrical/02-59-Electrical-Quantities-Ohm-s-Law-and-DC-Power.md](../layer-2-core/e-electrical/02-59-Electrical-Quantities-Ohm-s-Law-and-DC-Power.md) | local banner |
| 02-60 | Chapter 02-60: Kirchhoff's Laws and Resistive Circuit Analysis | [layer-2-core/e-electrical/02-60-Kirchhoff-s-Laws-and-Resistive-Circuit-Analysis.md](../layer-2-core/e-electrical/02-60-Kirchhoff-s-Laws-and-Resistive-Circuit-Analysis.md) | local banner |
| 02-61 | Chapter 02-61: Capacitance, Inductance, and First-Order Transients | [layer-2-core/e-electrical/02-61-Capacitance-Inductance-and-First-Order-Transients.md](../layer-2-core/e-electrical/02-61-Capacitance-Inductance-and-First-Order-Transients.md) | local banner |
| 02-62 | Chapter 02-62: Sinusoids, Phasors, Impedance, and Resonance | [layer-2-core/e-electrical/02-62-Sinusoids-Phasors-Impedance-and-Resonance.md](../layer-2-core/e-electrical/02-62-Sinusoids-Phasors-Impedance-and-Resonance.md) | local banner |
| 02-63 | Chapter 02-63: AC Power, Power Factor, and Three-Phase Systems | [layer-2-core/e-electrical/02-63-AC-Power-Power-Factor-and-Three-Phase-Systems.md](../layer-2-core/e-electrical/02-63-AC-Power-Power-Factor-and-Three-Phase-Systems.md) | local banner |
| 02-64 | Chapter 02-64: Magnetics and Transformers | [layer-2-core/e-electrical/02-64-Magnetics-and-Transformers.md](../layer-2-core/e-electrical/02-64-Magnetics-and-Transformers.md) | local banner |
| 02-65 | Chapter 02-65: Motors, Generators, and Electromechanical Energy Conversion | [layer-2-core/e-electrical/02-65-Motors-Generators-and-Electromechanical-Energy-Conversion.md](../layer-2-core/e-electrical/02-65-Motors-Generators-and-Electromechanical-Energy-Conversion.md) | local banner |
| 02-66 | Chapter 02-66: Measurement Systems, Calibration, Accuracy, and Uncertainty | [layer-2-core/f-measurement-control/02-66-Measurement-Systems-Calibration-Accuracy-and-Uncertainty.md](../layer-2-core/f-measurement-control/02-66-Measurement-Systems-Calibration-Accuracy-and-Uncertainty.md) | local banner |
| 02-67 | Chapter 02-67: Sensors, Transducers, Bridges, and Signal Conditioning | [layer-2-core/f-measurement-control/02-67-Sensors-Transducers-Bridges-and-Signal-Conditioning.md](../layer-2-core/f-measurement-control/02-67-Sensors-Transducers-Bridges-and-Signal-Conditioning.md) | local banner |
| 02-68 | Chapter 02-68: Data Acquisition, Sampling, Dynamic Response, and Frequency Response | [layer-2-core/f-measurement-control/02-68-Data-Acquisition-Sampling-Dynamic-Response-and-Frequency-Response.md](../layer-2-core/f-measurement-control/02-68-Data-Acquisition-Sampling-Dynamic-Response-and-Frequency-Response.md) | local banner |
| 02-69 | Chapter 02-69: Transfer Functions and Feedback Control Fundamentals | [layer-2-core/f-measurement-control/02-69-Transfer-Functions-and-Feedback-Control-Fundamentals.md](../layer-2-core/f-measurement-control/02-69-Transfer-Functions-and-Feedback-Control-Fundamentals.md) | local banner |
| 02-70 | Chapter 02-70: PID Control, Stability, and Control-Loop Hardware | [layer-2-core/f-measurement-control/02-70-PID-Control-Stability-and-Control-Loop-Hardware.md](../layer-2-core/f-measurement-control/02-70-PID-Control-Stability-and-Control-Loop-Hardware.md) | local banner |
| 03-01 | Chapter 03-01: Material and Energy Balances — Single Units and Process Flowsheets | [layer-3-tracks/chemical/03-01-Material-and-Energy-Balances-Single-Units-and-Process-Flowsheets.md](../layer-3-tracks/chemical/03-01-Material-and-Energy-Balances-Single-Units-and-Process-Flowsheets.md) | local banner |
| 03-02 | Chapter 03-02: Recycle, Bypass, Purge, and Unsteady Material Balances | [layer-3-tracks/chemical/03-02-Recycle-Bypass-Purge-and-Unsteady-Material-Balances.md](../layer-3-tracks/chemical/03-02-Recycle-Bypass-Purge-and-Unsteady-Material-Balances.md) | local banner |
| 03-03 | Chapter 03-03: Reactive Material Balances, Combustion, and Heats of Reaction | [layer-3-tracks/chemical/03-03-Reactive-Material-Balances-Combustion-and-Heats-of-Reaction.md](../layer-3-tracks/chemical/03-03-Reactive-Material-Balances-Combustion-and-Heats-of-Reaction.md) | local banner |
| 03-04 | Chapter 03-04: Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium | [layer-3-tracks/chemical/03-04-Phase-Equilibrium-Raoult-s-Law-Fugacity-Activity-and-Chemical-Equilibrium.md](../layer-3-tracks/chemical/03-04-Phase-Equilibrium-Raoult-s-Law-Fugacity-Activity-and-Chemical-Equilibrium.md) | local banner |
| 03-05 | Chapter 03-05: Molecular Diffusion and Convective Mass Transfer | [layer-3-tracks/chemical/03-05-Molecular-Diffusion-and-Convective-Mass-Transfer.md](../layer-3-tracks/chemical/03-05-Molecular-Diffusion-and-Convective-Mass-Transfer.md) | local banner |
| 03-06 | Chapter 03-06: Distillation and Equilibrium-Stage Methods | [layer-3-tracks/chemical/03-06-Distillation-and-Equilibrium-Stage-Methods.md](../layer-3-tracks/chemical/03-06-Distillation-and-Equilibrium-Stage-Methods.md) | local banner |
| 03-07 | Chapter 03-07: Absorption, Extraction, Adsorption, and Membrane Separations | [layer-3-tracks/chemical/03-07-Absorption-Extraction-Adsorption-and-Membrane-Separations.md](../layer-3-tracks/chemical/03-07-Absorption-Extraction-Adsorption-and-Membrane-Separations.md) | local banner |
| 03-08 | Chapter 03-08: Humidification, Drying, and Evaporation | [layer-3-tracks/chemical/03-08-Humidification-Drying-and-Evaporation.md](../layer-3-tracks/chemical/03-08-Humidification-Drying-and-Evaporation.md) | local banner |
| 03-09 | Chapter 03-09: Particle Characterization, Solids Handling, Size Reduction, and Crystallization | [layer-3-tracks/chemical/03-09-Particle-Characterization-Solids-Handling-Size-Reduction-and-Crystallization.md](../layer-3-tracks/chemical/03-09-Particle-Characterization-Solids-Handling-Size-Reduction-and-Crystallization.md) | local banner |
| 03-10 | Chapter 03-10: Reaction Kinetics, Rate Laws, and Arrhenius Behavior | [layer-3-tracks/chemical/03-10-Reaction-Kinetics-Rate-Laws-and-Arrhenius-Behavior.md](../layer-3-tracks/chemical/03-10-Reaction-Kinetics-Rate-Laws-and-Arrhenius-Behavior.md) | local banner |
| 03-11 | Chapter 03-11: Reactor Design — Batch, CSTR, PFR, Multiple Reactions, and Catalysis | [layer-3-tracks/chemical/03-11-Reactor-Design-Batch-CSTR-PFR-Multiple-Reactions-and-Catalysis.md](../layer-3-tracks/chemical/03-11-Reactor-Design-Batch-CSTR-PFR-Multiple-Reactions-and-Catalysis.md) | local banner |
| 03-12 | Chapter 03-12: Process Flow Diagrams, P&IDs, Equipment Sizing, Scale-Up, and Cost Estimation | [layer-3-tracks/chemical/03-12-Process-Flow-Diagrams-P-IDs-Equipment-Sizing-Scale-Up-and-Cost-Estimation.md](../layer-3-tracks/chemical/03-12-Process-Flow-Diagrams-P-IDs-Equipment-Sizing-Scale-Up-and-Cost-Estimation.md) | local banner |
| 03-13 | Chapter 03-13: Process Optimization, Advanced Control, and Process Safety | [layer-3-tracks/chemical/03-13-Process-Optimization-Advanced-Control-and-Process-Safety.md](../layer-3-tracks/chemical/03-13-Process-Optimization-Advanced-Control-and-Process-Safety.md) | local banner |
| 03-14 | Chapter 03-14: Civil Materials — Concrete, Asphalt, Aggregates, Wood, and Testing | [layer-3-tracks/civil/03-14-civil-materials-concrete-asphalt-aggregates-wood-and-testing.md](../layer-3-tracks/civil/03-14-civil-materials-concrete-asphalt-aggregates-wood-and-testing.md) | local banner |
| 03-15 | Chapter 03-15: Surveying, Leveling, Coordinates, Grades, Earthwork, and Volumes | [layer-3-tracks/civil/03-15-surveying-leveling-coordinates-grades-earthwork-and-volumes.md](../layer-3-tracks/civil/03-15-surveying-leveling-coordinates-grades-earthwork-and-volumes.md) | local banner |
| 03-16 | Chapter 03-16: Hydrology — Rainfall, Infiltration, Runoff, Watersheds, and Hydrographs | [layer-3-tracks/civil/03-16-hydrology-rainfall-infiltration-runoff-watersheds-and-hydrographs.md](../layer-3-tracks/civil/03-16-hydrology-rainfall-infiltration-runoff-watersheds-and-hydrographs.md) | local banner |
| 03-17 | Chapter 03-17: Open-Channel Flow — Manning Equation, Specific Energy, and Hydraulic Jumps | [layer-3-tracks/civil/03-17-open-channel-flow-manning-equation-specific-energy-and-hydraulic-jumps.md](../layer-3-tracks/civil/03-17-open-channel-flow-manning-equation-specific-energy-and-hydraulic-jumps.md) | local banner |
| 03-18 | Chapter 03-18: Pipe Networks, Water Distribution, Pumps, and Collection Systems | [layer-3-tracks/civil/03-18-pipe-networks-water-distribution-pumps-and-collection-systems.md](../layer-3-tracks/civil/03-18-pipe-networks-water-distribution-pumps-and-collection-systems.md) | local banner |
| 03-19 | Chapter 03-19: Flood Control, Stormwater Detention, Routing, and Spillways | [layer-3-tracks/civil/03-19-flood-control-stormwater-detention-routing-and-spillways.md](../layer-3-tracks/civil/03-19-flood-control-stormwater-detention-routing-and-spillways.md) | local banner |
| 03-20 | Chapter 03-20: Groundwater Flow, Aquifer Properties, Wells, and Drawdown | [layer-3-tracks/civil/03-20-groundwater-flow-aquifer-properties-wells-and-drawdown.md](../layer-3-tracks/civil/03-20-groundwater-flow-aquifer-properties-wells-and-drawdown.md) | local banner |
| 03-21 | Chapter 03-21: Water Quality and Water/Wastewater Treatment for Civil Applications | [layer-3-tracks/civil/03-21-water-quality-and-water-wastewater-treatment-for-civil-applications.md](../layer-3-tracks/civil/03-21-water-quality-and-water-wastewater-treatment-for-civil-applications.md) | local banner |
| 03-22 | Chapter 03-22: Structural Determinacy, Stability, Loads, Load Paths, and Influence Lines | [layer-3-tracks/civil/03-22-structural-determinacy-stability-loads-load-paths-and-influence-lines.md](../layer-3-tracks/civil/03-22-structural-determinacy-stability-loads-load-paths-and-influence-lines.md) | local banner |
| 03-23 | Chapter 03-23: Structural Analysis — Beams, Trusses, Frames, and Deflections | [layer-3-tracks/civil/03-23-structural-analysis-beams-trusses-frames-and-deflections.md](../layer-3-tracks/civil/03-23-structural-analysis-beams-trusses-frames-and-deflections.md) | local banner |
| 03-24 | Chapter 03-24: Columns, Buckling, and Elementary Indeterminate Structures | [layer-3-tracks/civil/03-24-columns-buckling-and-elementary-indeterminate-structures.md](../layer-3-tracks/civil/03-24-columns-buckling-and-elementary-indeterminate-structures.md) | local banner |
| 03-25 | Chapter 03-25: Steel Design — Tension Members, Beams, Columns, and Connections | [layer-3-tracks/civil/03-25-steel-design-tension-members-beams-columns-and-connections.md](../layer-3-tracks/civil/03-25-steel-design-tension-members-beams-columns-and-connections.md) | local banner |
| 03-26 | Chapter 03-26: Reinforced Concrete Design — Beams and Columns | [layer-3-tracks/civil/03-26-reinforced-concrete-design-beams-and-columns.md](../layer-3-tracks/civil/03-26-reinforced-concrete-design-beams-and-columns.md) | local banner |
| 03-27 | Chapter 03-27: Soil Classification, Phase Relations, Compaction, and Effective Stress | [layer-3-tracks/civil/03-27-soil-classification-phase-relations-compaction-and-effective-stress.md](../layer-3-tracks/civil/03-27-soil-classification-phase-relations-compaction-and-effective-stress.md) | local banner |
| 03-28 | Chapter 03-28: Shear Strength, Earth Pressure, Bearing Capacity, Foundations, Settlement, and Slope Stability | [layer-3-tracks/civil/03-28-shear-strength-earth-pressure-bearing-capacity-foundations-settlement-and-slope-stability.md](../layer-3-tracks/civil/03-28-shear-strength-earth-pressure-bearing-capacity-foundations-settlement-and-slope-stability.md) | local banner |
| 03-29 | Chapter 03-29: Transportation Engineering — Geometric Design, Pavements, Traffic Flow, and Planning | [layer-3-tracks/civil/03-29-transportation-engineering-geometric-design-pavements-traffic-flow-and-planning.md](../layer-3-tracks/civil/03-29-transportation-engineering-geometric-design-pavements-traffic-flow-and-planning.md) | local banner |
| 03-30 | Chapter 03-30: Construction Engineering — Administration, Operations, Scheduling, Estimating, and Drawings | [layer-3-tracks/civil/03-30-construction-engineering-administration-operations-scheduling-estimating-and-drawings.md](../layer-3-tracks/civil/03-30-construction-engineering-administration-operations-scheduling-estimating-and-drawings.md) | local banner |
| 03-31 | Chapter 03-31: Semiconductor Materials, Energy Bands, Doping, and p-n Junctions | [layer-3-tracks/electrical/03-31-semiconductor-materials-energy-bands-doping-and-pn-junctions.md](../layer-3-tracks/electrical/03-31-semiconductor-materials-energy-bands-doping-and-pn-junctions.md) | local banner |
| 03-32 | Chapter 03-32: Diodes, Rectifiers, Thyristors, and Device Models | [layer-3-tracks/electrical/03-32-diodes-rectifiers-thyristors-and-device-models.md](../layer-3-tracks/electrical/03-32-diodes-rectifiers-thyristors-and-device-models.md) | local banner |
| 03-33 | Chapter 03-33: BJT and MOSFET Biasing and Small-Signal Models | [layer-3-tracks/electrical/03-33-bjt-and-mosfet-biasing-and-small-signal-models.md](../layer-3-tracks/electrical/03-33-bjt-and-mosfet-biasing-and-small-signal-models.md) | local banner |
| 03-34 | Chapter 03-34: Single-Stage, Differential, and Operational Amplifiers | [layer-3-tracks/electrical/03-34-single-stage-differential-and-operational-amplifiers.md](../layer-3-tracks/electrical/03-34-single-stage-differential-and-operational-amplifiers.md) | local banner |
| 03-35 | Chapter 03-35: Power Electronics — Rectifiers, Converters, Inverters, and Switching | [layer-3-tracks/electrical/03-35-power-electronics-rectifiers-converters-inverters-and-switching.md](../layer-3-tracks/electrical/03-35-power-electronics-rectifiers-converters-inverters-and-switching.md) | local banner |
| 03-36 | Chapter 03-36: Power Systems — Transmission, Distribution, Losses, and Voltage Regulation | [layer-3-tracks/electrical/03-36-power-systems-transmission-distribution-losses-and-voltage-regulation.md](../layer-3-tracks/electrical/03-36-power-systems-transmission-distribution-losses-and-voltage-regulation.md) | local banner |
| 03-37 | Chapter 03-37: Electromagnetic Fields — Electrostatics, Magnetostatics, and Maxwell Foundations | [layer-3-tracks/electrical/03-37-electromagnetic-fields-electrostatics-magnetostatics-and-maxwell-foundations.md](../layer-3-tracks/electrical/03-37-electromagnetic-fields-electrostatics-magnetostatics-and-maxwell-foundations.md) | local banner |
| 03-38 | Chapter 03-38: Electromagnetic Waves and Transmission Lines | [layer-3-tracks/electrical/03-38-electromagnetic-waves-and-transmission-lines.md](../layer-3-tracks/electrical/03-38-electromagnetic-waves-and-transmission-lines.md) | local banner |
| 03-39 | Chapter 03-39: Signals and Linear Systems — Fourier Methods, Convolution, Filtering, and Transform Models | [layer-3-tracks/electrical/03-39-signals-and-linear-systems-fourier-methods-convolution-filtering-and-transform-models.md](../layer-3-tracks/electrical/03-39-signals-and-linear-systems-fourier-methods-convolution-filtering-and-transform-models.md) | local banner |
| 03-40 | Chapter 03-40: Communications — AM, FM, PM, PCM, Bandwidth, and Noise | [layer-3-tracks/electrical/03-40-communications-am-fm-pm-pcm-bandwidth-and-noise.md](../layer-3-tracks/electrical/03-40-communications-am-fm-pm-pcm-bandwidth-and-noise.md) | local banner |
| 03-41 | Chapter 03-41: Multiplexing and Digital Communications | [layer-3-tracks/electrical/03-41-multiplexing-and-digital-communications.md](../layer-3-tracks/electrical/03-41-multiplexing-and-digital-communications.md) | local banner |
| 03-42 | Chapter 03-42: Digital Logic — Number Systems, Boolean Algebra, Gates, and Minimization | [layer-3-tracks/electrical/03-42-digital-logic-number-systems-boolean-algebra-gates-and-minimization.md](../layer-3-tracks/electrical/03-42-digital-logic-number-systems-boolean-algebra-gates-and-minimization.md) | local banner |
| 03-43 | Chapter 03-43: Sequential Logic — Flip-Flops, Counters, State Machines, Timing, and PLDs | [layer-3-tracks/electrical/03-43-sequential-logic-flip-flops-counters-state-machines-timing-and-plds.md](../layer-3-tracks/electrical/03-43-sequential-logic-flip-flops-counters-state-machines-timing-and-plds.md) | local banner |
| 03-44 | Chapter 03-44: Computer Systems — Microprocessors, Memory, and Interfacing | [layer-3-tracks/electrical/03-44-computer-systems-microprocessors-memory-and-interfacing.md](../layer-3-tracks/electrical/03-44-computer-systems-microprocessors-memory-and-interfacing.md) | local banner |
| 03-45 | Chapter 03-45: Computer Networks — Routing, Switching, Topologies, and TCP/IP | [layer-3-tracks/electrical/03-45-computer-networks-routing-switching-topologies-and-tcp-ip.md](../layer-3-tracks/electrical/03-45-computer-networks-routing-switching-topologies-and-tcp-ip.md) | local banner |
| 03-46 | Chapter 03-46: Cybersecurity — Security Triad, Firewalls, Detection, Scanning, and Vulnerability Testing | [layer-3-tracks/electrical/03-46-cybersecurity-security-triad-firewalls-detection-scanning-and-vulnerability-testing.md](../layer-3-tracks/electrical/03-46-cybersecurity-security-triad-firewalls-detection-scanning-and-vulnerability-testing.md) | local banner |
| 03-47 | Chapter 03-47: Software Engineering — Data Structures, Algorithms, Complexity, Control Flow, and Testing | [layer-3-tracks/electrical/03-47-software-engineering-data-structures-algorithms-complexity-control-flow-and-testing.md](../layer-3-tracks/electrical/03-47-software-engineering-data-structures-algorithms-complexity-control-flow-and-testing.md) | local banner |
| 03-48 | Chapter 03-48: Population, Demand, Environmental Mass Balances, and Reactor Models | [layer-3-tracks/environmental/03-48-population-demand-environmental-mass-balances-and-reactor-models.md](../layer-3-tracks/environmental/03-48-population-demand-environmental-mass-balances-and-reactor-models.md) | local banner |
| 03-49 | Chapter 03-49: Environmental Chemistry — Equilibrium, Kinetics, Partitioning, and pC-pH | [layer-3-tracks/environmental/03-49-environmental-chemistry-equilibrium-kinetics-partitioning-and-pc-ph.md](../layer-3-tracks/environmental/03-49-environmental-chemistry-equilibrium-kinetics-partitioning-and-pc-ph.md) | local banner |
| 03-50 | Chapter 03-50: Health Hazards, Exposure Pathways, Toxicology, and Risk Assessment | [layer-3-tracks/environmental/03-50-health-hazards-exposure-pathways-toxicology-and-risk-assessment.md](../layer-3-tracks/environmental/03-50-health-hazards-exposure-pathways-toxicology-and-risk-assessment.md) | local banner |
| 03-51 | Chapter 03-51: Environmental Hydraulics — Conduits, Open Channels, Pumps, Blowers, and Flow Measurement | [layer-3-tracks/environmental/03-51-environmental-hydraulics-conduits-open-channels-pumps-blowers-and-flow-measurement.md](../layer-3-tracks/environmental/03-51-environmental-hydraulics-conduits-open-channels-pumps-blowers-and-flow-measurement.md) | local banner |
| 03-52 | Chapter 03-52: Surface-Water Hydrology — Runoff, Infiltration, Water Budgets, and Storage | [layer-3-tracks/environmental/03-52-surface-water-hydrology-runoff-infiltration-water-budgets-and-storage.md](../layer-3-tracks/environmental/03-52-surface-water-hydrology-runoff-infiltration-water-budgets-and-storage.md) | local banner |
| 03-53 | Chapter 03-53: Routing, Stormwater/Watershed Quality, Streeter–Phelps, and Eutrophication | [layer-3-tracks/environmental/03-53-routing-stormwater-watershed-quality-streeter-phelps-and-eutrophication.md](../layer-3-tracks/environmental/03-53-routing-stormwater-watershed-quality-streeter-phelps-and-eutrophication.md) | local banner |
| 03-54 | Chapter 03-54: Groundwater Flow, Aquifer Tests, Wells, and Drawdown | [layer-3-tracks/environmental/03-54-groundwater-flow-aquifer-tests-wells-and-drawdown.md](../layer-3-tracks/environmental/03-54-groundwater-flow-aquifer-tests-wells-and-drawdown.md) | local banner |
| 03-55 | Chapter 03-55: Soil and Sediment Contamination, Site Characterization, and Groundwater Remediation | [layer-3-tracks/environmental/03-55-soil-and-sediment-contamination-site-characterization-and-groundwater-remediation.md](../layer-3-tracks/environmental/03-55-soil-and-sediment-contamination-site-characterization-and-groundwater-remediation.md) | local banner |
| 03-56 | Chapter 03-56: Water/Wastewater Characteristics, Loading Rates, and Physical Treatment | [layer-3-tracks/environmental/03-56-water-wastewater-characteristics-loading-rates-and-physical-treatment.md](../layer-3-tracks/environmental/03-56-water-wastewater-characteristics-loading-rates-and-physical-treatment.md) | local banner |
| 03-57 | Chapter 03-57: Chemical Water/Wastewater Treatment — Coagulation, Softening, Disinfection, Ion Exchange, and Precipitation | [layer-3-tracks/environmental/03-57-chemical-water-wastewater-treatment-coagulation-softening-disinfection-ion-exchange-and-precipitation.md](../layer-3-tracks/environmental/03-57-chemical-water-wastewater-treatment-coagulation-softening-disinfection-ion-exchange-and-precipitation.md) | local banner |
| 03-58 | Chapter 03-58: Biological Treatment — Activated Sludge, Fixed Film, Lagoons, and Nutrient Removal | [layer-3-tracks/environmental/03-58-biological-treatment-activated-sludge-fixed-film-lagoons-and-nutrient-removal.md](../layer-3-tracks/environmental/03-58-biological-treatment-activated-sludge-fixed-film-lagoons-and-nutrient-removal.md) | local banner |
| 03-59 | Chapter 03-59: Sludge/Biosolids Handling, Water Reuse, and Residuals Management | [layer-3-tracks/environmental/03-59-sludge-biosolids-handling-water-reuse-and-residuals-management.md](../layer-3-tracks/environmental/03-59-sludge-biosolids-handling-water-reuse-and-residuals-management.md) | local banner |
| 03-60 | Chapter 03-60: Air Quality — Emissions, Dispersion, Indoor Air, and Gas/Particle Control | [layer-3-tracks/environmental/03-60-air-quality-emissions-dispersion-indoor-air-and-gas-particle-control.md](../layer-3-tracks/environmental/03-60-air-quality-emissions-dispersion-indoor-air-and-gas-particle-control.md) | local banner |
| 03-61 | Chapter 03-61: Solid and Hazardous Waste, Landfills, Treatment, and Energy-Environment Impacts | [layer-3-tracks/environmental/03-61-solid-and-hazardous-waste-landfills-treatment-and-energy-environment-impacts.md](../layer-3-tracks/environmental/03-61-solid-and-hazardous-waste-landfills-treatment-and-energy-environment-impacts.md) | local banner |
| 03-62 | Chapter 03-62: Data, Logic, Databases, and Engineering Analytics | [layer-3-tracks/industrial/03-62-data-logic-databases-and-engineering-analytics.md](../layer-3-tracks/industrial/03-62-data-logic-databases-and-engineering-analytics.md) | local banner |
| 03-63 | Chapter 03-63: Linear Programming and Optimization | [layer-3-tracks/industrial/03-63-linear-programming-and-optimization.md](../layer-3-tracks/industrial/03-63-linear-programming-and-optimization.md) | local banner |
| 03-64 | Chapter 03-64: Queueing Models and Service Systems | [layer-3-tracks/industrial/03-64-queueing-models-and-service-systems.md](../layer-3-tracks/industrial/03-64-queueing-models-and-service-systems.md) | local banner |
| 03-65 | Chapter 03-65: Markov Processes, Stochastic Models, and Simulation | [layer-3-tracks/industrial/03-65-markov-processes-stochastic-models-and-simulation.md](../layer-3-tracks/industrial/03-65-markov-processes-stochastic-models-and-simulation.md) | local banner |
| 03-66 | Chapter 03-66: Engineering and Project Management — Organization, WBS, PERT/CPM, Earned Value, Agile, and KPIs | [layer-3-tracks/industrial/03-66-engineering-and-project-management-organization-wbs-pert-cpm-earned-value-agile-and-kpis.md](../layer-3-tracks/industrial/03-66-engineering-and-project-management-organization-wbs-pert-cpm-earned-value-agile-and-kpis.md) | local banner |
| 03-67 | Chapter 03-67: Forecasting — Moving Averages, Exponential Smoothing, and Tracking Signals | [layer-3-tracks/industrial/03-67-forecasting-moving-averages-exponential-smoothing-and-tracking-signals.md](../layer-3-tracks/industrial/03-67-forecasting-moving-averages-exponential-smoothing-and-tracking-signals.md) | local banner |
| 03-68 | Chapter 03-68: Inventory, Aggregate Planning, MRP, Sequencing, and Theory of Constraints | [layer-3-tracks/industrial/03-68-inventory-aggregate-planning-mrp-sequencing-and-theory-of-constraints.md](../layer-3-tracks/industrial/03-68-inventory-aggregate-planning-mrp-sequencing-and-theory-of-constraints.md) | local banner |
| 03-69 | Chapter 03-69: Manufacturing and Service Systems — Processes, Automation, Throughput, and Line Balancing | [layer-3-tracks/industrial/03-69-manufacturing-and-service-systems-processes-automation-throughput-and-line-balancing.md](../layer-3-tracks/industrial/03-69-manufacturing-and-service-systems-processes-automation-throughput-and-line-balancing.md) | local banner |
| 03-70 | Chapter 03-70: Lean Systems, Process Improvement, Sustainability, and Value Engineering | [layer-3-tracks/industrial/03-70-lean-systems-process-improvement-sustainability-and-value-engineering.md](../layer-3-tracks/industrial/03-70-lean-systems-process-improvement-sustainability-and-value-engineering.md) | local banner |
| 03-71 | Chapter 03-71: Facility Location, Layout, Capacity, and Material Handling | [layer-3-tracks/industrial/03-71-facility-location-layout-capacity-and-material-handling.md](../layer-3-tracks/industrial/03-71-facility-location-layout-capacity-and-material-handling.md) | local banner |
| 03-72 | Chapter 03-72: Supply Chains, Transportation Networks, Pooling, and Distribution | [layer-3-tracks/industrial/03-72-supply-chains-transportation-networks-pooling-and-distribution.md](../layer-3-tracks/industrial/03-72-supply-chains-transportation-networks-pooling-and-distribution.md) | local banner |
| 03-73 | Chapter 03-73: Human Factors, Ergonomics, Work Design, Time Study, and Learning Curves | [layer-3-tracks/industrial/03-73-human-factors-ergonomics-work-design-time-study-and-learning-curves.md](../layer-3-tracks/industrial/03-73-human-factors-ergonomics-work-design-time-study-and-learning-curves.md) | local banner |
| 03-74 | Chapter 03-74: Quality Management, SPC, Process Capability, Sampling, and DOE | [layer-3-tracks/industrial/03-74-quality-management-spc-process-capability-sampling-and-doe.md](../layer-3-tracks/industrial/03-74-quality-management-spc-process-capability-sampling-and-doe.md) | local banner |
| 03-75 | Chapter 03-75: Systems Engineering, Reliability, FMEA, Fault Trees, and Life-Cycle Risk | [layer-3-tracks/industrial/03-75-systems-engineering-reliability-fmea-fault-trees-and-life-cycle-risk.md](../layer-3-tracks/industrial/03-75-systems-engineering-reliability-fmea-fault-trees-and-life-cycle-risk.md) | local banner |
| 03-76 | Chapter 03-76: Mechanism Kinematics and Machine Motion | [layer-3-tracks/mechanical/03-76-mechanism-kinematics-and-machine-motion.md](../layer-3-tracks/mechanical/03-76-mechanism-kinematics-and-machine-motion.md) | local banner |
| 03-77 | Chapter 03-77: Mechanical Vibrations — Free, Forced, Damped, and Resonant Response | [layer-3-tracks/mechanical/03-77-mechanical-vibrations-free-forced-damped-and-resonant-response.md](../layer-3-tracks/mechanical/03-77-mechanical-vibrations-free-forced-damped-and-resonant-response.md) | local banner |
| 03-78 | Chapter 03-78: Failure Theories, Stress Concentrations, Fatigue, Fracture, and Creep | [layer-3-tracks/mechanical/03-78-failure-theories-stress-concentrations-fatigue-fracture-and-creep.md](../layer-3-tracks/mechanical/03-78-failure-theories-stress-concentrations-fatigue-fracture-and-creep.md) | local banner |
| 03-79 | Chapter 03-79: Manufacturing Processes, Material Processing, Heat Treatment, and Selection | [layer-3-tracks/mechanical/03-79-manufacturing-processes-material-processing-heat-treatment-and-selection.md](../layer-3-tracks/mechanical/03-79-manufacturing-processes-material-processing-heat-treatment-and-selection.md) | local banner |
| 03-80 | Chapter 03-80: External Flow — Drag, Lift, Boundary Layers, and Dimensional Similarity | [layer-3-tracks/mechanical/03-80-external-flow-drag-lift-boundary-layers-and-dimensional-similarity.md](../layer-3-tracks/mechanical/03-80-external-flow-drag-lift-boundary-layers-and-dimensional-similarity.md) | local banner |
| 03-81 | Chapter 03-81: Compressible Flow — Mach Number, Nozzles, Isentropic Flow, and Normal Shocks | [layer-3-tracks/mechanical/03-81-compressible-flow-mach-number-nozzles-isentropic-flow-and-normal-shocks.md](../layer-3-tracks/mechanical/03-81-compressible-flow-mach-number-nozzles-isentropic-flow-and-normal-shocks.md) | local banner |
| 03-82 | Chapter 03-82: Combustion and Combustion Products | [layer-3-tracks/mechanical/03-82-combustion-and-combustion-products.md](../layer-3-tracks/mechanical/03-82-combustion-and-combustion-products.md) | local banner |
| 03-83 | Chapter 03-83: HVAC Processes, Loads, Psychrometrics, and Equipment Performance | [layer-3-tracks/mechanical/03-83-hvac-processes-loads-psychrometrics-and-equipment-performance.md](../layer-3-tracks/mechanical/03-83-hvac-processes-loads-psychrometrics-and-equipment-performance.md) | local banner |
| 03-84 | Chapter 03-84: Mechanical Springs | [layer-3-tracks/mechanical/03-84-mechanical-springs.md](../layer-3-tracks/mechanical/03-84-mechanical-springs.md) | local banner |
| 03-85 | Chapter 03-85: Pressure Vessels and Piping | [layer-3-tracks/mechanical/03-85-pressure-vessels-and-piping.md](../layer-3-tracks/mechanical/03-85-pressure-vessels-and-piping.md) | local banner |
| 03-86 | Chapter 03-86: Bearings and Lubrication | [layer-3-tracks/mechanical/03-86-bearings-and-lubrication.md](../layer-3-tracks/mechanical/03-86-bearings-and-lubrication.md) | local banner |
| 03-87 | Chapter 03-87: Power Screws, Threaded Fasteners, and Mechanical Joints | [layer-3-tracks/mechanical/03-87-power-screws-threaded-fasteners-and-mechanical-joints.md](../layer-3-tracks/mechanical/03-87-power-screws-threaded-fasteners-and-mechanical-joints.md) | local banner |
| 03-88 | Chapter 03-88: Shafts, Keys, Couplings, Gears, Belts, Chains, and Power Transmission | [layer-3-tracks/mechanical/03-88-shafts-keys-couplings-gears-belts-chains-and-power-transmission.md](../layer-3-tracks/mechanical/03-88-shafts-keys-couplings-gears-belts-chains-and-power-transmission.md) | local banner |
| 03-89 | Chapter 03-89: Hydraulic, Pneumatic, and Electromechanical Components | [layer-3-tracks/mechanical/03-89-hydraulic-pneumatic-and-electromechanical-components.md](../layer-3-tracks/mechanical/03-89-hydraulic-pneumatic-and-electromechanical-components.md) | local banner |
| 03-90 | Chapter 03-90: Fits, Tolerances, GD&T, Manufacturability, Quality, and Reliability | [layer-3-tracks/mechanical/03-90-fits-tolerances-gdandt-manufacturability-quality-and-reliability.md](../layer-3-tracks/mechanical/03-90-fits-tolerances-gdandt-manufacturability-quality-and-reliability.md) | local banner |
| 03-91 | Chapter 03-91: Other Disciplines Mechanics and Materials Integration | [layer-3-tracks/other/03-91-other-disciplines-mechanics-and-materials-integration.md](../layer-3-tracks/other/03-91-other-disciplines-mechanics-and-materials-integration.md) | local banner |
| 03-92 | Chapter 03-92: Other Disciplines Thermal, Fluid, Heat-Transfer, and HVAC Integration | [layer-3-tracks/other/03-92-other-disciplines-thermal-fluid-heat-transfer-and-hvac-integration.md](../layer-3-tracks/other/03-92-other-disciplines-thermal-fluid-heat-transfer-and-hvac-integration.md) | local banner |
| 03-93 | Chapter 03-93: Other Disciplines Electrical, Instrumentation, and Control Integration | [layer-3-tracks/other/03-93-other-disciplines-electrical-instrumentation-and-control-integration.md](../layer-3-tracks/other/03-93-other-disciplines-electrical-instrumentation-and-control-integration.md) | local banner |
| 03-94 | Chapter 03-94: Other Disciplines Safety, Economics, and Cross-Domain Engineering Decisions | [layer-3-tracks/other/03-94-other-disciplines-safety-economics-and-cross-domain-engineering-decisions.md](../layer-3-tracks/other/03-94-other-disciplines-safety-economics-and-cross-domain-engineering-decisions.md) | local banner |
| 03-95 | Chapter 03-95: Other Disciplines Mixed FE Synthesis and Handbook Strategy | [layer-3-tracks/other/03-95-other-disciplines-mixed-fe-synthesis-and-handbook-strategy.md](../layer-3-tracks/other/03-95-other-disciplines-mixed-fe-synthesis-and-handbook-strategy.md) | local banner |
