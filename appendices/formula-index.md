# Formula Index

**Basis:** latest technical audit (`Technical-Audit-Formulas(20261011-003235).csv`), 5,996 parsed display formulas across 206 audited chapters.

This appendix is an **index of governing and reusable relations**, not a dump of every displayed equation. Intermediate arithmetic substitutions, boxed numeric answers, and repeated worked-example calculations are intentionally omitted. Audit formula numbers are retained so each entry can be traced to the technical-audit output.

**Indexed formulas:** 1,323 selected canonical/reusable relations.

## Selection rule

- Prefer symbolic governing equations, identities, distributions, constitutive relations, and reusable design/check equations.
- Exclude display blocks that are primarily numeric substitution, arithmetic simplification, or a boxed numeric answer.
- Retain at most 12 indexed formulas per chapter to keep this appendix usable as an index rather than a second textbook.

## Layer 1 — Mathematical and Analytical Foundations

### 01-01 — Numbers, Magnitude, and Metric Prefixes

- **01-01:F1** — $\frac{a + b}{c + d}$
- **01-01:F13** — $(N_1 \times 10^{x_1})(N_2 \times 10^{x_2}) = (N_1 N_2) \times 10^{x_1 + x_2}$
- **01-01:F14** — $\frac{N_1 \times 10^{x_1}}{N_2 \times 10^{x_2}} = \left(\frac{N_1}{N_2}\right) \times 10^{x_1 - x_2}$
- **01-01:F21** — $N_1 \times 10^{x} + N_2 \times 10^{x} = (N_1 + N_2) \times 10^{x}$
- **01-01:F39** — $4.7 \text{ k}\Omega = 4.7 \times 10^3 \; \Omega$
- **01-01:F66** — $N \times 10^x, \qquad 1 \le \lvert N \rvert < 10$

### 01-02 — Units, Dimensions, and the Pound Problem

- **01-02:F6** — $F = ma$
- **01-02:F8** — $[T_p] = T$
- **01-02:F11** — $T \;\ne\; \frac{L}{T}$
- **01-02:F29** — $F = ma \qquad \text{(N, kg, m/s²)}$
- **01-02:F30** — $F = ma \qquad \text{(lbf, slug, ft/s²)}$
- **01-02:F32** — $\boxed{g_c = 32.174 \; \frac{\text{lbm} \cdot \text{ft}}{\text{lbf} \cdot \text{s}^2}}$
- **01-02:F33** — $\boxed{F = \frac{ma}{g_c}}$
- **01-02:F35** — $a = \frac{F g_c}{m}$
- **01-02:F48** — $\boxed{F_W = \frac{mg}{g_c}} \qquad \text{(USCS)} \qquad\qquad \boxed{F_W = mg} \qquad \text{(SI)}$
- **01-02:F98** — $R = \frac{\bar{R}}{MW}$
- **01-02:F124** — $p = \frac{\rho g h}{g_c} \qquad SW = \frac{\rho g}{g_c} \qquad \tau = \frac{\mu}{g_c}\frac{dv}{dy}$
- **01-02:F125** — $\frac{F}{F_W} = \frac{a}{g}$

### 01-03 — Accuracy, Precision, and Significant Figures

- **01-03:F1** — $\boxed{E_{abs} = \lvert x_{meas} - x_{true} \rvert}$
- **01-03:F2** — $\boxed{E_{rel} = \frac{\lvert x_{meas} - x_{true} \rvert}{x_{true}}}$
- **01-03:F3** — $\boxed{E_{\%} = \frac{\lvert x_{meas} - x_{true} \rvert}{x_{true}} \times 100\%}$
- **01-03:F24** — $\frac{X}{A-B},\qquad A\approx B$
- **01-03:F27** — $\tau = \frac{T_q \cdot c}{J}$
- **01-03:F43** — $E_{abs} = \lvert x_{meas} - x_{true} \rvert \qquad E_{rel} = \frac{E_{abs}}{x_{true}} \qquad E_{\%} = E_{rel} \times 100\%$

### 01-04 — Expressions, Equations, and Inequalities

- **01-04:F8** — $a(b + c + d) = ab + ac + ad$
- **01-04:F9** — $(a + b)(c + d) = ac + ad + bc + bd$
- **01-04:F10** — $\boxed{a^2 - b^2 = (a+b)(a-b)}$
- **01-04:F27** — $V_{out} R_1 = R_2(V_{in} - V_{out})$
- **01-04:F28** — $\boxed{R_1 = \frac{R_2(V_{in} - V_{out})}{V_{out}}}$
- **01-04:F36** — $pV = mRT$
- **01-04:F37** — $T = \frac{pV}{mR}$
- **01-04:F41** — $\lvert f(x) \rvert = a \implies f(x) = a \quad \text{or} \quad f(x) = -a$
- **01-04:F60** — $F_W = SW \cdot V$
- **01-04:F65** — $\boxed{F_{work} \le 2{,}125 \text{ lbf}}$
- **01-04:F70** — $\boxed{T_H = \frac{T_L}{1 - \eta}}$
- **01-04:F71** — $\boxed{R_2 = \frac{V_{out}R_1}{V_{in} - V_{out}}}$

### 01-05 — Exponents, Radicals, and Logarithms

- **01-05:F10** — $\boxed{b^{m/n} = \left(\sqrt[n]{b}\right)^m = \sqrt[n]{b^m}}$
- **01-05:F15** — $\omega_n = \sqrt{\frac{k_s}{m}}$
- **01-05:F20** — $\frac{d}{dx}\left(e^x\right) = e^x$
- **01-05:F21** — $f(t) = A \, e^{-t/\tau}$
- **01-05:F22** — $\boxed{\log_b x = y \quad \Longleftrightarrow \quad b^y = x}$
- **01-05:F25** — $\log_b b^x = x \quad\text{(inverse function, cancels)}$
- **01-05:F26** — $b^{\log_b x} = x \quad\text{(inverse function, cancels)}$
- **01-05:F28** — $\log_e x = \ln x$
- **01-05:F29** — $\boxed{\log_b(xy) = \log_b x + \log_b y}$
- **01-05:F30** — $\boxed{\log_b\frac{x}{y} = \log_b x - \log_b y}$
- **01-05:F31** — $\boxed{\log_b(x^r) = r \log_b x}$
- **01-05:F35** — $\frac{\log_b x}{\log_b y} \ne \log_b\frac{x}{y} \qquad \text{(quotient rule is subtraction, not division)}$

### 01-06 — Functions, Graphs, and Transformations

- **01-06:F1** — $4 - x^2 \ge 0 \implies x^2 \le 4 \implies -2 \le x \le 2$
- **01-06:F3** — $(f \circ g)(x) = f(g(x))$
- **01-06:F4** — $f^{-1}(f(x)) = x \qquad\text{and}\qquad f(f^{-1}(x)) = x$
- **01-06:F5** — $y = \frac{3x - 2}{x + 1}$
- **01-06:F6** — $x = \frac{3y - 2}{y + 1}$
- **01-06:F8** — $xy + x = 3y - 2$
- **01-06:F9** — $xy - 3y = -2 - x$
- **01-06:F10** — $y(x - 3) = -(2 + x)$
- **01-06:F12** — $\boxed{f^{-1}(x) = \frac{x + 2}{3 - x}, \quad x \ne 3}$
- **01-06:F15** — $g(x) = a \cdot f(b(x - h)) + k$
- **01-06:F17** — $V(t) = V_{max}\left(1 - e^{-t/\tau}\right)$
- **01-06:F18** — $f(x) = \begin{cases} x^2 & x < 0 \\ 2x + 1 & 0 \le x \le 3 \\ 10 & x > 3 \end{cases}$

### 01-07 — Polynomials and Their Roots

- **01-07:F2** — $P(x) = a_n x^n + a_{n-1}x^{n-1} + \cdots + a_1 x + a_0$
- **01-07:F3** — $(3x^3 - 2x + 5) + (x^3 + 4x^2 - 3x - 1) = 4x^3 + 4x^2 - 5x + 4$
- **01-07:F4** — $(x^2 + 2)(x - 3) = x^3 - 3x^2 + 2x - 6$
- **01-07:F6** — $P(x) = (x-2)(2x^2 + x + 3) + 1$
- **01-07:F8** — $ax^2 + bx + c = 0, \quad a \ne 0$
- **01-07:F16** — $x + 3 = \pm 2$
- **01-07:F18** — $\boxed{x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}}$
- **01-07:F19** — $\Delta = b^2 - 4ac$
- **01-07:F32** — $P(x) = (x-1)\left(2x^2 + x - 6\right)$
- **01-07:F36** — $P(x) = -2(x+3)(x-1)^2(x-4)$
- **01-07:F46** — $P(x) = a(x - r_1)(x - r_2) \cdots (x - r_n)$
- **01-07:F54** — $y(x) = k \cdot x(L - x)(x^2 - Lx - L^2)$

### 01-08 — Systems of Linear Equations

- **01-08:F2** — $y = 7 - 2x$
- **01-08:F5** — $x = 3$
- **01-08:F8** — $3F_1 - 2F_2 = 6 \qquad \text{(horizontal, kN)} \quad (1)$
- **01-08:F9** — $F_1 + 4F_2 = 16 \qquad \text{(vertical, kN)} \quad (2)$
- **01-08:F18** — $R_2 \leftarrow 2R_2 + 3R_1$
- **01-08:F20** — $R_3 \leftarrow R_3 + R_1$
- **01-08:F23** — $R_3 \leftarrow R_3 - 2R_2$
- **01-08:F35** — $\begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc$
- **01-08:F40** — $\boxed{x = \frac{D_x}{D} \qquad y = \frac{D_y}{D}}$
- **01-08:F55** — $5I_1 + 2I_3 = 12 \quad \text{(loop 1)} \quad (1)$
- **01-08:F99** — $T_A = T_B - 6$
- **01-08:F115** — $D_x = \begin{vmatrix} e & b \\ f & d \end{vmatrix} = ed - fb$

### 01-09 — Analytic Geometry

- **01-09:F1** — $\boxed{y = mx + b}$
- **01-09:F2** — $\boxed{y - y_1 = m(x - x_1)}$
- **01-09:F3** — $\boxed{Ax + By + C = 0}$
- **01-09:F30** — $\boxed{(x - h)^2 = 4p(y - k)}$
- **01-09:F31** — $\boxed{(y - k)^2 = 4p(x - h)}$
- **01-09:F32** — $x^2 = 4py$
- **01-09:F34** — $\boxed{x^2 = 960y}$
- **01-09:F39** — $A = \pi a b$
- **01-09:F52** — $\boxed{e = \frac{c}{a}}$
- **01-09:F60** — $\boxed{y = -2x + 1}$
- **01-09:F87** — $\boxed{x^2 = 20y}$
- **01-09:F94** — $\boxed{x^2 = -40y}$

### 01-10 — Areas, Volumes, and Mensuration

- **01-10:F1** — $s = \frac{a+b+c}{2} \quad \text{(semi-perimeter)}$
- **01-10:F2** — $A = \sqrt{s(s-a)(s-b)(s-c)}$
- **01-10:F6** — $\boxed{\bar{x} = \frac{\sum A_i \bar{x}_i}{\sum A_i} \qquad \bar{y} = \frac{\sum A_i \bar{y}_i}{\sum A_i}}$
- **01-10:F7** — $\bar{x} = \frac{\Sigma A_i\bar{x}_i}{\Sigma A_i} \qquad \bar{y} = \frac{\Sigma A_i\bar{y}_i}{\Sigma A_i}$
- **01-10:F9** — $\boxed{\bar{x} = 60 \text{ mm}, \quad \bar{y} = 30 \text{ mm from bottom}}$
- **01-10:F13** — $\boxed{V = 2\pi \bar{r} A}$
- **01-10:F18** — $V_{hollow\,cyl} = \pi(r_o^2-r_i^2)h$
- **01-10:F20** — $\bar{x} = \frac{\sum A_i\bar{x}_i}{\sum A_i} \qquad \bar{y} = \frac{\sum A_i\bar{y}_i}{\sum A_i}$
- **01-10:F21** — $V = 2\pi\bar{r}A$

### 01-11 — Trigonometry

- **01-11:F2** — $\boxed{\cos\theta = x\text{-coordinate on the unit circle} \qquad \sin\theta = y\text{-coordinate}}$
- **01-11:F3** — $\tan\theta = \frac{\sin\theta}{\cos\theta} \qquad \cot\theta = \frac{\cos\theta}{\sin\theta}$
- **01-11:F14** — $\sin\theta = \frac{a}{c} \qquad \cos\theta = \frac{b}{c} \qquad \tan\theta = \frac{a}{b}$
- **01-11:F18** — $\boxed{\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C}}$
- **01-11:F28** — $\sin(\alpha \pm \beta) = \sin\alpha\cos\beta \pm \cos\alpha\sin\beta$
- **01-11:F29** — $\cos(\alpha \pm \beta) = \cos\alpha\cos\beta \mp \sin\alpha\sin\beta$
- **01-11:F30** — $\tan(\alpha \pm \beta) = \frac{\tan\alpha \pm \tan\beta}{1 \mp \tan\alpha\tan\beta}$
- **01-11:F31** — $\sin(2\theta) = 2\sin\theta\cos\theta$
- **01-11:F39** — $\theta = \arcsin(x) = \sin^{-1}(x) \implies \sin\theta = x$
- **01-11:F42** — $\boxed{\tan\alpha = m}$
- **01-11:F56** — $F_x = F\cos\theta \qquad F_y = F\sin\theta$
- **01-11:F73** — $\sin\theta = \frac{y}{r} \qquad \cos\theta = \frac{x}{r} \qquad \tan\theta = \frac{y}{x}$

### 01-12 — Complex Numbers

- **01-12:F4** — $\boxed{z = a + jb}$
- **01-12:F5** — $(a + jb) \pm (c + jd) = (a \pm c) + j(b \pm d)$
- **01-12:F7** — $z = a + jb \implies z^* = a - jb$
- **01-12:F13** — $a = r\cos\theta \qquad b = r\sin\theta$
- **01-12:F16** — $\boxed{e^{j\theta} = \cos\theta + j\sin\theta}$
- **01-12:F19** — $z = re^{j\theta} = r(\cos\theta + j\sin\theta) = r\angle\theta$
- **01-12:F22** — $\boxed{(r\angle\theta)^n = r^n\angle(n\theta)}$
- **01-12:F23** — $(\cos\theta + j\sin\theta)^n = \cos(n\theta) + j\sin(n\theta)$
- **01-12:F27** — $v(t) = V_m \cos(\omega t + \phi)$
- **01-12:F28** — $\mathbf{V} = V_m \angle\phi$
- **01-12:F39** — $z = r\angle\theta = r(\cos\theta + j\sin\theta) = re^{j\theta}$
- **01-12:F42** — $v(t) = V_m\cos(\omega t+\phi) \;\longleftrightarrow\; \mathbf{V} = V_m\angle\phi$

### 01-13 — Vectors and Vector Operations

- **01-13:F1** — $\vec{A} = A_x\hat{\imath} + A_y\hat{\jmath} + A_z\hat{k}$
- **01-13:F2** — $\vec{A} + \vec{B} = (A_x+B_x)\hat{\imath} + (A_y+B_y)\hat{\jmath} + (A_z+B_z)\hat{k}$
- **01-13:F3** — $\vec{A} - \vec{B} = (A_x-B_x)\hat{\imath} + (A_y-B_y)\hat{\jmath} + (A_z-B_z)\hat{k}$
- **01-13:F4** — $c\vec{A} = cA_x\hat{\imath} + cA_y\hat{\jmath} + cA_z\hat{k}$
- **01-13:F7** — $\cos\alpha = \frac{A_x}{A} \qquad \cos\beta = \frac{A_y}{A} \qquad \cos\gamma = \frac{A_z}{A}$
- **01-13:F9** — $\boxed{\vec{A} \cdot \vec{B} = A_xB_x + A_yB_y + A_zB_z}$
- **01-13:F11** — $\cos\theta = \frac{\vec{A}\cdot\vec{B}}{\lvert\vec{A}\rvert\lvert\vec{B}\rvert}$
- **01-13:F12** — $\text{comp}_{\vec{A}}\vec{B} = \frac{\vec{A}\cdot\vec{B}}{\lvert\vec{A}\rvert} = \lvert\vec{B}\rvert\cos\theta$
- **01-13:F16** — $\vec{A} \times \vec{B} = \begin{vmatrix} \hat{\imath} & \hat{\jmath} & \hat{k} \\ A_x & A_y & A_z \\ B_x & B_y & B_z \end{vmatrix}$
- **01-13:F17** — $\boxed{\vec{A} \times \vec{B} = (A_yB_z - A_zB_y)\hat{\imath} - (A_xB_z - A_zB_x)\hat{\jmath} + (A_xB_y - A_yB_x)\hat{k}}$
- **01-13:F25** — $\vec{A}\cdot(\vec{B}\times\vec{C}) = \begin{vmatrix} A_x & A_y & A_z \\ B_x & B_y & B_z \\ C_x & C_y & C_z \end{vmatrix}$
- **01-13:F27** — $\vec{R} = \sum_i \vec{F}_i = \left(\sum_i F_{ix}\right)\hat{\imath} + \left(\sum_i F_{iy}\right)\hat{\jmath}$

### 01-14 — Matrices, Determinants, and Eigenvalues

- **01-14:F5** — $A + B = B + A \qquad (A+B)+C = A+(B+C)$
- **01-14:F6** — $\underbrace{A}_{m \times n} \; \underbrace{B}_{n \times p} = \underbrace{AB}_{m \times p}$
- **01-14:F11** — $A(BC) = (AB)C \quad \text{(associative)}$
- **01-14:F12** — $A(B+C) = AB + AC \quad \text{(distributive)}$
- **01-14:F16** — $(A^T)_{ij} = a_{ji}$
- **01-14:F18** — $(A^T)^T = A$
- **01-14:F19** — $(A+B)^T = A^T + B^T$
- **01-14:F20** — $\boxed{(AB)^T = B^T A^T \quad \text{— note the order reversal}}$
- **01-14:F21** — $(cA)^T = cA^T$
- **01-14:F59** — $x_i = \frac{\det A_i}{\det A}$
- **01-14:F69** — $\boxed{\sum_i \lambda_i = \text{tr}(A) \qquad \prod_i \lambda_i = \det A}$
- **01-14:F125** — $(AB)_{ij} = \sum_k a_{ik}b_{kj} \qquad AB \ne BA$

### 01-15 — Sequences, Series, and Progressions

- **01-15:F5** — $\boxed{\sum_{k=1}^{n} c\,a_k = c\sum_{k=1}^{n} a_k}$
- **01-15:F7** — $\boxed{\sum_{k=1}^{n} c = nc \qquad (c \text{ constant, no } k)}$
- **01-15:F11** — $\boxed{d = a_{n+1} - a_n \quad \text{(same for every } n)}$
- **01-15:F12** — $\boxed{a_n = a_1 + (n-1)d}$
- **01-15:F23** — $\boxed{r = \frac{a_{n+1}}{a_n} \quad \text{(same for every } n)}$
- **01-15:F24** — $\boxed{a_n = a_1 r^{\,n-1}}$
- **01-15:F25** — $\boxed{S_n = \frac{a_1\left(1 - r^n\right)}{1 - r} \qquad (r \ne 1)}$
- **01-15:F51** — $n! = n \cdot (n-1)!$
- **01-15:F66** — $(0.72)^n \le 0.161290$
- **01-15:F68** — $\boxed{n = 6 \text{ stages}}$
- **01-15:F74** — $\sum_{k=m}^{n} a_k \qquad \text{number of terms} = n - m + 1$
- **01-15:F75** — $\sum c\,a_k = c\sum a_k \qquad \sum(a_k \pm b_k) = \sum a_k \pm \sum b_k \qquad \sum_{k=1}^{n} c = nc$

### 01-16 — Limits and Continuity

- **01-16:F3** — $\lim_{x \to a}f(x) \quad \text{and} \quad f(a) \quad \text{are different questions.}$
- **01-16:F4** — $\lim_{x \to a^-}f(x) \quad \text{approach from the left } (x < a)$
- **01-16:F5** — $\lim_{x \to a^+}f(x) \quad \text{approach from the right } (x > a)$
- **01-16:F6** — $\boxed{\lim_{x\to a}f(x) = L \iff \lim_{x\to a^-}f(x) = L \;\text{ and }\; \lim_{x\to a^+}f(x) = L}$
- **01-16:F10** — $\boxed{\lim_{x\to 1}f(x) \text{ does not exist (DNE)}}$
- **01-16:F11** — $\boxed{\text{For any polynomial } p(x): \quad \lim_{x\to a}p(x) = p(a)}$
- **01-16:F12** — $\lim_{x\to a}\frac{p(x)}{q(x)} = \frac{p(a)}{q(a)} \qquad \text{provided } q(a) \ne 0$
- **01-16:F22** — $\lim_{x\to\infty}f(x) = L \quad \text{means } f(x) \text{ approaches } L \text{ as } x \text{ increases without bound}$
- **01-16:F27** — $\lim_{x\to\infty}e^{-x} = 0 \qquad \lim_{x\to\infty}e^{x} = \infty \;(\text{unbounded})$
- **01-16:F28** — $v(t) = v_\infty\left(1 - e^{-t/\tau}\right)$
- **01-16:F87** — $\lim_{x\to a}f(x) = L \iff \lim_{x\to a^-}f(x) = \lim_{x\to a^+}f(x) = L$
- **01-16:F90** — $f(a) \text{ exists} \quad\wedge\quad \lim_{x\to a}f(x) \text{ exists} \quad\wedge\quad \lim_{x\to a}f(x) = f(a)$

### 01-17 — The Derivative

- **01-17:F2** — $m_{\text{sec}} = \frac{f(a+h) - f(a)}{h} = \frac{\Delta y}{\Delta x}$
- **01-17:F21** — $\boxed{\left[\frac{dy}{dx}\right] = \frac{[y]}{[x]}}$
- **01-17:F33** — $\boxed{\frac{d}{dx}\left[c\,f(x)\right] = c\,f'(x)}$
- **01-17:F34** — $\boxed{\frac{d}{dx}\left[f(x) \pm g(x)\right] = f'(x) \pm g'(x)}$
- **01-17:F40** — $\boxed{\frac{d}{dx}(uv) = u'v + uv'}$
- **01-17:F42** — $\boxed{\frac{dy}{dx} = f'\big(g(x)\big)\cdot g'(x)}$
- **01-17:F43** — $\boxed{\frac{dy}{dx} = \frac{dy}{du}\cdot\frac{du}{dx}}$
- **01-17:F44** — $\frac{dy}{dx} = \frac{dy}{du}\cdot\frac{du}{dv}\cdot\frac{dv}{dx}$
- **01-17:F63** — $\boxed{\frac{d}{dx}\sin x = \cos x \qquad \frac{d}{dx}\cos x = -\sin x}$
- **01-17:F64** — $\frac{\sin(x+h) - \sin x}{h} = \frac{\sin x\cos h + \cos x\sin h - \sin x}{h}$
- **01-17:F69** — $\boxed{\frac{d}{dx}e^x = e^x}$
- **01-17:F72** — $\boxed{\frac{d}{dx}a^x = a^x\ln a}$

### 01-18 — Applications of the Derivative

- **01-18:F1** — $f'(c) = \frac{f(b) - f(a)}{b - a}$
- **01-18:F24** — $A = x^2 + 4xh$
- **01-18:F47** — $\frac{dP}{dt} = -\frac{P}{V}\cdot\frac{dV}{dt}$
- **01-18:F50** — $\lim_{x\to a}\frac{f(x)}{g(x)} = \lim_{x\to a}\frac{f'(x)}{g'(x)}$
- **01-18:F58** — $\boxed{dy = f'(x)\,dx}$
- **01-18:F59** — $dy = f'(x)\,dx$
- **01-18:F60** — $\frac{dy}{y} = \frac{f'(x)}{f(x)}\,dx$
- **01-18:F61** — $\boxed{\frac{dy}{y} = n\,\frac{dx}{x}}$
- **01-18:F132** — $f'(c) = \frac{f(b)-f(a)}{b-a} \quad \text{for some } c \in (a,b)$
- **01-18:F136** — $\frac{dV}{dh} = \text{liquid surface area} \quad \text{(tank check)}$
- **01-18:F139** — $dy = f'(x)\,dx \qquad \frac{dy}{y} = \frac{f'(x)}{f(x)}dx$
- **01-18:F140** — $\boxed{y = kx^n \implies \frac{dy}{y} = n\frac{dx}{x}}$

### 01-19 — Antiderivatives and the Definite Integral

- **01-19:F2** — $\boxed{\int f(x)\,dx = F(x) + C}$
- **01-19:F6** — $\boxed{\int c\,f(x)\,dx = c\int f(x)\,dx \qquad \int \big[f(x) \pm g(x)\big]\,dx = \int f(x)\,dx \pm \int g(x)\,dx}$
- **01-19:F15** — $\Delta x = \frac{b-a}{n}$
- **01-19:F26** — $\boxed{\int_a^b f(x)\,dx = F(b) - F(a)}$
- **01-19:F27** — $\int_a^b f(x)\,dx = \Big[F(x)\Big]_a^b = F(b) - F(a)$
- **01-19:F28** — $G(x) = \int_a^x f(t)\,dt$
- **01-19:F29** — $\boxed{\frac{d}{dx}\int_a^x f(t)\,dt = f(x)}$
- **01-19:F30** — $\frac{d}{dx}\int_a^{g(x)} f(t)\,dt = f\big(g(x)\big)\cdot g'(x)$
- **01-19:F38** — $\boxed{\int f\big(g(x)\big)g'(x)\,dx = \int f(u)\,du}$
- **01-19:F42** — $= \int\frac{-du}{u} = -\ln\lvert u\rvert + C = \boxed{-\ln\lvert\cos x\rvert + C}$
- **01-19:F43** — $\int\frac{g'(x)}{g(x)}\,dx = \ln\lvert g(x)\rvert + C$
- **01-19:F50** — $\bar{f}\cdot(b-a) = \int_a^b f(x)\,dx$

### 01-20 — Applications of the Definite Integral

- **01-20:F1** — $dA = \big[\,y_{\text{top}} - y_{\text{bottom}}\,\big]\,dx$
- **01-20:F2** — $\boxed{A = \int_a^b \big[\,f(x) - g(x)\,\big]\,dx \qquad \text{where } f \ge g \text{ on } [a,b]}$
- **01-20:F11** — $\boxed{A = \int_c^d \big[\,x_{\text{right}} - x_{\text{left}}\,\big]\,dy}$
- **01-20:F22** — $dV = A(x)\,dx \implies \boxed{V = \int_a^b A(x)\,dx}$
- **01-20:F48** — $\boxed{Q_x = \int y\,dA \qquad Q_y = \int x\,dA}$
- **01-20:F49** — $\boxed{\bar{x} = \frac{Q_y}{A} = \frac{\int x\,dA}{A} \qquad \bar{y} = \frac{Q_x}{A} = \frac{\int y\,dA}{A}}$
- **01-20:F70** — $dW = F(x)\,dx \implies \boxed{W = \int_a^b F(x)\,dx}$
- **01-20:F75** — $\boxed{W = \gamma\int \big(y_{\text{dest}} - y\big)A(y)\,dy}$
- **01-20:F172** — $A = \int_a^b\big[y_{\text{top}} - y_{\text{bottom}}\big]dx \qquad A = \int_c^d\big[x_{\text{right}} - x_{\text{left}}\big]dy$
- **01-20:F173** — $\text{net} = \int v\,dt \qquad \text{total} = \int\lvert v\rvert\,dt$
- **01-20:F175** — $Q_x = \int y\,dA = A\bar{y} \qquad Q_y = \int x\,dA = A\bar{x}$
- **01-20:F179** — $\text{pumping: } W = \gamma\int\big(y_{\text{dest}} - y\big)A(y)\,dy$

### 01-21 — Techniques of Integration

- **01-21:F2** — $uv = \int u\,dv + \int v\,du$
- **01-21:F3** — $\boxed{\int u\,dv = uv - \int v\,du}$
- **01-21:F5** — $dv = e^x dx \implies v = e^x$
- **01-21:F9** — $u = \ln x \implies du = \frac{dx}{x}$
- **01-21:F11** — $\int\ln x\,dx = x\ln x - \int x\cdot\frac{dx}{x} = x\ln x - \int dx$
- **01-21:F24** — $dv = e^x dx, \quad v = e^x$
- **01-21:F25** — $I = e^x\sin x - \int e^x\cos x\,dx$
- **01-21:F28** — $\int e^x\cos x\,dx = e^x\cos x + \int e^x\sin x\,dx = e^x\cos x + I$
- **01-21:F29** — $I = e^x\sin x - \Big[e^x\cos x + I\Big] = e^x\sin x - e^x\cos x - I$
- **01-21:F33** — $\boxed{\int_a^b u\,dv = \Big[uv\Big]_a^b - \int_a^b v\,du}$
- **01-21:F75** — $\boxed{\int_a^{\infty}f(x)\,dx = \lim_{b\to\infty}\int_a^b f(x)\,dx}$
- **01-21:F76** — $\int_a^b f(x)\,dx = \lim_{t\to a^+}\int_t^b f(x)\,dx$

### 01-22 — Infinite Series and Taylor Expansions

- **01-22:F1** — $\sin x = x - \frac{x^3}{6} + \frac{x^5}{120} - \cdots$
- **01-22:F3** — $\boxed{\sum_{n=1}^{\infty}a_n = \lim_{n\to\infty}S_n = S}$
- **01-22:F6** — $\lim_{n\to\infty}\frac{1}{\sqrt{n}} = 0$
- **01-22:F11** — $\boxed{\sum_{n=1}^{\infty}a_n \text{ and } \int_1^{\infty}f(x)\,dx \text{ both converge or both diverge}}$
- **01-22:F17** — $L = \lim_{n\to\infty}\left\lvert\frac{a_{n+1}}{a_n}\right\rvert$
- **01-22:F25** — $\boxed{\lvert S - S_n\rvert \le b_{n+1}}$
- **01-22:F31** — $\boxed{f(x) = \sum_{n=0}^{\infty}\frac{f^{(n)}(a)}{n!}(x-a)^n}$
- **01-22:F34** — $P_1(x) = f(a) + f'(a)(x-a)$
- **01-22:F35** — $f^{(n)}(0) = 1 \quad \text{for all } n$
- **01-22:F43** — $E_n(x) = f(x) - P_n(x)$
- **01-22:F54** — $T_0 = 2\pi\sqrt{\frac{L}{g}}$
- **01-22:F75** — $\sum_{n=1}^{\infty}a_n = \lim_{n\to\infty}S_n$

### 01-23 — Partial Derivatives and Vector Calculus

- **01-23:F8** — $f_{xx} = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial x}\right) \qquad f_{yy} = \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial y}\right)$
- **01-23:F9** — $f_{xy} = \frac{\partial}{\partial y}\left(\frac{\partial f}{\partial x}\right) \qquad f_{yx} = \frac{\partial}{\partial x}\left(\frac{\partial f}{\partial y}\right)$
- **01-23:F10** — $\boxed{f_{xy} = f_{yx}}$
- **01-23:F13** — $\boxed{f_{xy} = f_{yx} \;\checkmark}$
- **01-23:F14** — $\boxed{df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy + \frac{\partial f}{\partial z}dz + \cdots}$
- **01-23:F15** — $\boxed{z = f(a,b) + f_x(a,b)(x-a) + f_y(a,b)(y-b)}$
- **01-23:F16** — $\boxed{\lvert df\rvert \le \left\lvert\frac{\partial f}{\partial x}\right\rvert\lvert dx\rvert + \left\lvert\frac{\partial f}{\partial y}\right\rvert\lvert dy\rvert + \cdots}$
- **01-23:F17** — $f = C\,x^{a}y^{b}z^{c}$
- **01-23:F18** — $\boxed{\frac{\lvert df\rvert}{f} \le \lvert a\rvert\frac{\lvert dx\rvert}{x} + \lvert b\rvert\frac{\lvert dy\rvert}{y} + \lvert c\rvert\frac{\lvert dz\rvert}{z}}$
- **01-23:F34** — $\boxed{\frac{df}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt} + \cdots}$
- **01-23:F39** — $\boxed{\nabla f = \frac{\partial f}{\partial x}\hat{\imath} + \frac{\partial f}{\partial y}\hat{\jmath} + \frac{\partial f}{\partial z}\hat{k}}$
- **01-23:F48** — $\mathbf{F} = F_x\hat{\imath} + F_y\hat{\jmath} + F_z\hat{k}$

### 01-24 — Multiple Integration

- **01-24:F1** — $\sum_i f(x_i^*,y_i^*)\,\Delta A_i$
- **01-24:F4** — $\boxed{\iint_D f\,dA =\int_a^b\int_c^d f(x,y)\,dy\,dx =\int_c^d\int_a^b f(x,y)\,dx\,dy.}$
- **01-24:F5** — $\int_a^b\left[\int_c^d f(x,y)\,dy\right]dx,$
- **01-24:F27** — $\boxed{A(D)=\iint_D1\,dA.}$
- **01-24:F28** — $\boxed{V=\iint_D f(x,y)\,dA.}$
- **01-24:F40** — $dM=\rho_A(x,y)\,dA.$
- **01-24:F41** — $\boxed{M=\iint_D\rho_A(x,y)\,dA.}$
- **01-24:F42** — $\boxed{\bar x=\frac1M\iint_Dx\rho_A\,dA, \qquad \bar y=\frac1M\iint_Dy\rho_A\,dA.}$
- **01-24:F43** — $\bar x=\frac1A\iint_Dx\,dA, \qquad \bar y=\frac1A\iint_Dy\,dA.$
- **01-24:F53** — $\text{total}=\iint_D(\text{quantity per area})\,dA.$
- **01-24:F69** — $\boxed{V(E)=\iiint_E1\,dV}$
- **01-24:F90** — $\boxed{dA= \left|\frac{\partial(x,y)}{\partial(u,v)}\right|du\,dv}$

### 01-25 — Differential Equations

- **01-25:F6** — $\frac{dy}{dt}=p(t)q(y)$
- **01-25:F7** — $\frac{dy}{q(y)}=p(t)\,dt.$
- **01-25:F8** — $\frac{dy}{dt}=ky$
- **01-25:F16** — $\boxed{y'+p(t)y=q(t).}$
- **01-25:F17** — $\boxed{\mu(t)=e^{\int p(t)\,dt}.}$
- **01-25:F18** — $\mu y'+\mu p y=\frac{d}{dt}(\mu y).$
- **01-25:F25** — $y'+ay=b$
- **01-25:F42** — $\boxed{y=y_h+y_p}$
- **01-25:F46** — $y_p=At\sin2t.$
- **01-25:F80** — $\boxed{y=e^{-t}\sin3t}.$
- **01-25:F93** — $\frac{dy}{dt}=p(t)q(y) \quad\Longrightarrow\quad \frac{dy}{q(y)}=p(t)dt.$
- **01-25:F94** — $y'+p(t)y=q(t),\qquad \mu=e^{\int p(t)dt},\qquad (\mu y)'=\mu q.$

### 01-26 — Numerical Methods

- **01-26:F1** — $\boxed{e_a=|x_{\text{approx}}-x^\*|}$
- **01-26:F4** — $\boxed{R_k=f(x_k).}$
- **01-26:F11** — $f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}.$
- **01-26:F31** — $y=f(x_k)+f'(x_k)(x-x_k).$
- **01-26:F46** — $\frac{f(x_k)}{f'(x_k)}$
- **01-26:F52** — $H\Delta\mathbf x=-\nabla h$
- **01-26:F71** — $x_k=a+k\Delta x,$
- **01-26:F72** — $\boxed{\Delta x=\frac{b-a}{n}}.$
- **01-26:F188** — $e_a=|x_{\text{approx}}-x^\*|,$
- **01-26:F189** — $e_r=\frac{e_a}{|x^\*|}\quad(x^\*\ne0).$
- **01-26:F190** — $R_k=f(x_k).$
- **01-26:F202** — $\Delta x=\frac{b-a}{n}.$

### 01-27 — Algorithm and Logic Development

- **01-27:F1** — $x_{k+1}=x_k-\frac{f(x_k)}{f'(x_k)}.$
- **01-27:F4** — $r\ge0,\qquad h\ge0.$
- **01-27:F5** — $V=\pi r^2h.$
- **01-27:F6** — $V\ge0$
- **01-27:F11** — $x=x+2.$
- **01-27:F12** — $\boxed{\texttt{sum}=30}.$
- **01-27:F19** — $N=\frac{t_f-t_0}{\Delta t}$
- **01-27:F21** — $\boxed{f(a_k)f(b_k)\le0}$
- **01-27:F22** — $0\le\texttt{count}\le k$
- **01-27:F35** — $\boxed{\texttt{product}=120}.$
- **01-27:F38** — $y_1=1.4,$
- **01-27:F39** — $y_2=0.98,$

### 01-28 — Probability Fundamentals

- **01-28:F11** — $\boxed{ P(A)=\frac{\text{number of outcomes in }A} {\text{number of outcomes in }S}. }$
- **01-28:F16** — $\boxed{ P(n,r)=\frac{n!}{(n-r)!}. }$
- **01-28:F17** — $\boxed{ C(n,r)=\frac{n!}{r!(n-r)!}. }$
- **01-28:F27** — $\boxed{ (A\cup B)^c=A^c\cap B^c. }$
- **01-28:F28** — $\boxed{ (A\cap B)^c=A^c\cup B^c. }$
- **01-28:F43** — $\boxed{ P(A\mid B)=P(A) }$
- **01-28:F65** — $P(B\mid F) = \frac{P(F\mid B)P(B)}{P(F)}$
- **01-28:F73** — $P(+) = P(+\mid D)P(D) + P(+\mid D^c)P(D^c).$
- **01-28:F103** — $S=\{PP,PF,FP,FF\}.$
- **01-28:F118** — $P(B\mid D) = \frac{P(D\mid B)P(B)}{P(D)}$
- **01-28:F128** — $\boxed{ P(A)=\frac{N(A)}{N(S)}. }$
- **01-28:F130** — $\boxed{ P(n,r)=\frac{n!}{(n-r)!} }$

### 01-29 — Random Variables and Probability Distributions

- **01-29:F6** — $S=\{PP,PF,FP,FF\}.$
- **01-29:F8** — $\boxed{ f(x_k)=P(X=x_k). }$
- **01-29:F9** — $\boxed{f(x_k)\ge0}$
- **01-29:F19** — $\boxed{ P(a\le X\le b) = \int_a^b f(x)\,dx. }$
- **01-29:F29** — $\boxed{ F(x)=\sum_{x_k\le x}P(X=x_k). }$
- **01-29:F30** — $\boxed{ F(x)=\int_{-\infty}^{x}f(t)\,dt. }$
- **01-29:F31** — $\boxed{ f(x)=\frac{dF}{dx}. }$
- **01-29:F32** — $\boxed{ P(a<X\le b)=F(b)-F(a). }$
- **01-29:F37** — $\boxed{ E[X] = \mu = \sum_k x_k f(x_k). }$
- **01-29:F38** — $\boxed{ E[X] = \mu = \int_{-\infty}^{\infty}x f(x)\,dx. }$
- **01-29:F39** — $\boxed{ E[g(X)] = \sum_k g(x_k)f(x_k) }$
- **01-29:F40** — $\boxed{ E[g(X)] = \int_{-\infty}^{\infty}g(x)f(x)\,dx. }$

### 01-30 — The Normal Distribution and the Central Limit Theorem

- **01-30:F2** — $\boxed{x=\mu-\sigma,\qquad x=\mu+\sigma.}$
- **01-30:F9** — $\boxed{z=\frac{x-\mu}{\sigma}.}$
- **01-30:F38** — $E[X_i]=\mu$
- **01-30:F43** — $\boxed{\sigma_Y=\sigma\sqrt n.}$
- **01-30:F47** — $\boxed{\sigma_{\bar X}=\frac{\sigma}{\sqrt n}.}$
- **01-30:F55** — $\boxed{\mu_{\bar X}=\mu}$
- **01-30:F70** — $E[\bar X]=\mu,\qquad \sigma_{\bar X}=\frac{\sigma}{\sqrt n}$
- **01-30:F71** — $E[Y]=n\mu,\qquad \sigma_Y=\sigma\sqrt n$
- **01-30:F73** — $\boxed{z=\frac{x-\mu}{\sigma}}$
- **01-30:F89** — $\boxed{\mu_Y=n\mu}$
- **01-30:F90** — $\boxed{\sigma_Y=\sigma\sqrt n}$
- **01-30:F92** — $\boxed{\sigma_{\bar X}=\frac{\sigma}{\sqrt n}}$

### 01-31 — Sampling Distributions, Student's t, and Chi-Square

- **01-31:F1** — $\frac{\sigma}{\sqrt n}.$
- **01-31:F2** — $Z= \frac{\bar X-\mu}{\sigma/\sqrt n},$
- **01-31:F3** — $T= \frac{\bar X-\mu}{s/\sqrt n},$
- **01-31:F25** — $Z = \frac{\bar X-\mu}{\sigma/\sqrt n}.$
- **01-31:F26** — $\boxed{ T = \frac{\bar X-\mu}{s/\sqrt n}. }$
- **01-31:F38** — $\boxed{ P(T>t_{\alpha,\nu})=\alpha. }$
- **01-31:F40** — $\boxed{ P(T<-t_{\alpha,\nu})=\alpha. }$
- **01-31:F90** — $\boxed{ Z = \frac{\bar X-\mu}{\sigma/\sqrt n}. }$
- **01-31:F154** — $\boxed{ Z = \frac{\bar X-\mu}{\sigma/\sqrt n} }$
- **01-31:F155** — $\boxed{ T = \frac{\bar X-\mu}{s/\sqrt n} }$
- **01-31:F157** — $\boxed{ P(T>t_{\alpha,\nu})=\alpha }$
- **01-31:F158** — $\boxed{ P(T<-t_{\alpha,\nu})=\alpha }$

### 01-32 — Estimation and Confidence Intervals

- **01-32:F16** — $Z = \frac{\bar X-\mu}{\sigma/\sqrt n}$
- **01-32:F19** — $\boxed{ \bar X - z_{\alpha/2}\frac{\sigma}{\sqrt n} \le \mu \le \bar X + z_{\alpha/2}\frac{\sigma}{\sqrt n}. }$
- **01-32:F20** — $\boxed{ \mu: \quad \bar x \pm z_{\alpha/2} \frac{\sigma}{\sqrt n}. }$
- **01-32:F21** — $\boxed{ E = z_{\alpha/2} \frac{\sigma}{\sqrt n}. }$
- **01-32:F23** — $\sigma=12\text{ g}.$
- **01-32:F31** — $E = z_{\alpha/2} \frac{\sigma}{\sqrt n},$
- **01-32:F32** — $T = \frac{\bar X-\mu}{s/\sqrt n}$
- **01-32:F33** — $\nu=n-1.$
- **01-32:F34** — $\boxed{ \mu: \quad \bar x \pm t_{\alpha/2,n-1} \frac{s}{\sqrt n}. }$
- **01-32:F35** — $\boxed{ E = t_{\alpha/2,n-1} \frac{s}{\sqrt n}. }$
- **01-32:F49** — $\boxed{ E_t>E_z. }$
- **01-32:F72** — $\boxed{ \sqrt{L_{\sigma^2}} < \sigma < \sqrt{U_{\sigma^2}}. }$

### 01-33 — Hypothesis Testing and Statistical Decisions

- **01-33:F1** — $\boxed{ H_0:\mu=\mu_0 }$
- **01-33:F4** — $\boxed{ H_1:\mu<\mu_0. }$
- **01-33:F6** — $\boxed{ H_1:\mu>\mu_0. }$
- **01-33:F7** — $H_0:\mu=5.00\text{ V}$
- **01-33:F13** — $\boxed{ \alpha=P(\text{Type I error}). }$
- **01-33:F15** — $\boxed{ \beta=P(\text{Type II error}). }$
- **01-33:F19** — $H_0:\mu=\mu_0$
- **01-33:F42** — $\boxed{ t_0 = \frac{\bar X-\mu_0}{s/\sqrt n} }$
- **01-33:F79** — $\nu=n-1.$
- **01-33:F144** — $H_0:\mu=2.00$
- **01-33:F176** — $\boxed{ \alpha=P(\text{Type I error}) }$
- **01-33:F177** — $\boxed{ \beta=P(\text{Type II error}) }$

### 01-34 — Analysis of Variance and Design of Experiments

- **01-34:F2** — $\boxed{ SS_{\text{total}} = SS_{\text{treatments}} + SS_{\text{error}}. }$
- **01-34:F3** — $\boxed{ F = \frac{MS_{\text{treatments}}} {MS_{\text{error}}}. }$
- **01-34:F41** — $\boxed{ SS_{\text{total}} = SS_{\text{treatments}} + SS_{\text{blocks}} + SS_{\text{error}}. }$
- **01-34:F45** — $\boxed{ SS_{\text{error}} = SS_{\text{total}} - SS_{\text{treatments}} - SS_{\text{blocks}}. }$
- **01-34:F46** — $\boxed{ F_{\text{treatments}} = \frac{MST}{MSE}. }$
- **01-34:F47** — $\boxed{ F_{\text{blocks}} = \frac{MSB}{MSE}. }$
- **01-34:F66** — $\boxed{ SS_{\text{total}} = SSA+SSB+SSAB+SS_{\text{error}}. }$
- **01-34:F73** — $\boxed{ F_A=\frac{MSA}{MSE} }$
- **01-34:F74** — $\boxed{ F_B=\frac{MSB}{MSE} }$
- **01-34:F75** — $\boxed{ F_{AB}=\frac{MSAB}{MSE}. }$
- **01-34:F103** — $e_{ij} = y_{ij}-\bar y_i.$
- **01-34:F108** — $SS_{\text{total}} = SS_{\text{treatments}} + SS_{\text{error}}.$

### 01-35 — Linear Regression and Goodness of Fit

- **01-35:F1** — $\boxed{ e_i=y_i-\hat y_i. }$
- **01-35:F2** — $\boxed{ \hat y=\hat a+\hat b x. }$
- **01-35:F7** — $\boxed{ \hat y_i=\hat a+\hat b x_i. }$
- **01-35:F17** — $S_{xy} = \sum x_i y_i - \frac{(\sum x_i)(\sum y_i)}{n}.$
- **01-35:F18** — $\boxed{ \hat b = \frac{S_{xy}}{S_{xx}}. }$
- **01-35:F31** — $\hat y_i = \hat a+\hat b x_i$
- **01-35:F32** — $e_i = y_i-\hat y_i.$
- **01-35:F47** — $\boxed{ R = \frac{S_{xy}} {\sqrt{S_{xx}S_{yy}}}. }$
- **01-35:F57** — $\boxed{ SE_{\hat b} = \frac{S_e}{\sqrt{S_{xx}}}. }$
- **01-35:F86** — $y=Ae^{bx}$
- **01-35:F87** — $y=Ax^b.$
- **01-35:F96** — $\boxed{ R = \frac{S_{xy}} {\sqrt{S_{xx}S_{yy}}} }$

### 01-36 — Measurement Uncertainty and Statistical Error Propagation

- **01-36:F1** — $\left|\Delta y\right| \lesssim \sum_i \left| \frac{\partial f}{\partial x_i} \right| \left|\Delta x_i\right|.$
- **01-36:F3** — $\boxed{ e_x=x-x_{\text{ref}}. }$
- **01-36:F5** — $\boxed{ x = x_{\text{ref}} + d_{\text{systematic}} + d_{\text{random}}. }$
- **01-36:F13** — $\boxed{ c_i = \frac{\partial f}{\partial x_i}. }$
- **01-36:F14** — $\frac{\text{output units}} {\text{input }i\text{ units}}.$
- **01-36:F27** — $\frac{\partial y}{\partial x_i} = a_i\frac{y}{x_i}.$
- **01-36:F28** — $\left( \frac{\partial y}{\partial x_i} \right)u_{x_i} = a_i y\frac{u_{x_i}}{x_i}.$
- **01-36:F48** — $\boxed{ U=ku_y, }$
- **01-36:F59** — $\boxed{ s_{\bar x} = \frac{s}{\sqrt n}. }$
- **01-36:F60** — $x=x_{\text{ref}}+d_{\text{systematic}}+d_{\text{random}}$
- **01-36:F70** — $\frac{s}{\sqrt n}\rightarrow0.$
- **01-36:F73** — $\boxed{ \eta_i = \frac{q_i} {\sum_j q_j}. }$

### 01-37 — Expected Value, Decision Trees, and Risk

- **01-37:F5** — $\boxed{ EV = \sum_i p_i C_i. }$
- **01-37:F13** — $\boxed{ EL = \sum_i p_i L_i. }$
- **01-37:F14** — $\boxed{ R_{ij} = \text{best payoff in state }j - \text{payoff from decision }i. }$
- **01-37:F15** — $R_{ij}\ge0.$
- **01-37:F16** — $\boxed{ EOL_i = \sum_j p_j R_{ij}. }$
- **01-37:F26** — $\boxed{ EV_{\text{chance}} = \sum_i p_i C_i. }$
- **01-37:F54** — $\boxed{ EV_{\text{PI}} = \sum_j p_j \left( \max_i C_{ij} \right). }$
- **01-37:F55** — $\boxed{ EV_{\text{current}} = \max_i \sum_j p_j C_{ij}. }$
- **01-37:F56** — $\boxed{ EVPI = EV_{\text{PI}} - EV_{\text{current}}. }$
- **01-37:F76** — $EV_X=EV_Y.$
- **01-37:F134** — $\boxed{ EV = \sum_i p_iC_i }$
- **01-37:F136** — $EC=\sum_i p_iC_i$

### 01-38 — Common Engineering Probability Distributions

- **01-38:F8** — $\boxed{ P(X=x) = \frac{ \binom{r}{x} \binom{N-r}{n-x} }{ \binom{N}{n} }. }$
- **01-38:F9** — $\boxed{ \mu = \frac{nr}{N}. }$
- **01-38:F43** — $\boxed{ \mu=\frac1p. }$
- **01-38:F48** — $\boxed{ \mu=\frac rp. }$
- **01-38:F61** — $\boxed{ f(x) = \frac1{b-a}. }$
- **01-38:F65** — $\boxed{ P(c\le X\le d) = \frac{d-c}{b-a}. }$
- **01-38:F66** — $a\le m\le b.$
- **01-38:F89** — $\boxed{ S(x) = P(X>x) = e^{-x/\beta}. }$
- **01-38:F90** — $\boxed{ h=\frac1\beta. }$
- **01-38:F103** — $\boxed{ S(x) = e^{-(x/\beta)^\alpha}. }$
- **01-38:F110** — $S(x) = e^{-(x/\beta)}$
- **01-38:F111** — $f(x) = \frac1\beta e^{-x/\beta}.$

### 01-39 — Statistical Process Control and Control Charts

- **01-39:F6** — $n=\text{subgroup size}$
- **01-39:F9** — $\boxed{ R_i = X_{i,\max} - X_{i,\min}. }$
- **01-39:F18** — $\boxed{CL_R=\bar R}$
- **01-39:F21** — $\boxed{CL_{\bar X}=\bar{\bar X}}$
- **01-39:F41** — $\boxed{CL_S=\bar S}$
- **01-39:F63** — $\boxed{CL+\frac d3}$
- **01-39:F65** — $CL-\frac d3$
- **01-39:F113** — $LCL_R = \boxed0.$
- **01-39:F121** — $LCL_S = \boxed0.$
- **01-39:F133** — $\bar X_i=\frac1n\sum_jX_{ij}, \qquad R_i=X_{\max}-X_{\min}.$
- **01-39:F134** — $\bar{\bar X} = \frac1k\sum_i\bar X_i, \qquad \bar R = \frac1k\sum_iR_i, \qquad \bar S = \frac1k\sum_iS_i.$
- **01-39:F136** — $CL_{\bar X}=\bar{\bar X},$

### 01-40 — Process Capability and Specification Performance

- **01-40:F1** — $LSL\le X\le USL.$
- **01-40:F7** — $\boxed{ C_p = \frac{USL-LSL}{6\sigma}. }$
- **01-40:F9** — $\boxed{ W_{\text{spec}} = USL-LSL. }$
- **01-40:F23** — $\boxed{ C_{pu} = \frac{USL-\mu}{3\sigma}. }$
- **01-40:F25** — $\boxed{ C_{pk} = \min(C_{pl},C_{pu}). }$
- **01-40:F35** — $\mu=m,$
- **01-40:F38** — $\boxed{ C_{pk}=C_p. }$
- **01-40:F39** — $\boxed{ C_{pk}<C_p }$
- **01-40:F40** — $\boxed{ C_{pk}\le C_p. }$
- **01-40:F160** — $\boxed{ W_{\text{spec}} = USL-LSL }$
- **01-40:F164** — $\boxed{ C_{pk} = \min(C_{pl},C_{pu}) }$
- **01-40:F165** — $\boxed{ \mu=m \Rightarrow C_{pk}=C_p. }$

### 01-41 — Acceptance Sampling and Operating Characteristic Curves

- **01-41:F1** — $X=\text{number of nonconforming units found in the sample}.$
- **01-41:F3** — $\boxed{X\le c}$
- **01-41:F4** — $\boxed{X>c}.$
- **01-41:F9** — $\boxed{ X\le c \Rightarrow \text{accept lot} }$
- **01-41:F10** — $\boxed{ X>c \Rightarrow \text{reject lot}. }$
- **01-41:F20** — $X\le c.$
- **01-41:F37** — $P(X=x) = \frac{ \binom Dx \binom{N-D}{n-x} }{ \binom Nn }.$
- **01-41:F51** — $\frac nN$
- **01-41:F64** — $\boxed{ \beta = P_a(\text{RQL}). }$
- **01-41:F111** — $\beta=P_a(\text{RQL}).$
- **01-41:F173** — $P_a=\text{probability of acceptance}.$
- **01-41:F175** — $\boxed{ \beta = P_a(\text{RQL}) }$

## Layer 2 — Common Engineering Fundamentals

### 02-01 — Engineering Ethics, Public Welfare, and Professional Judgment

_No reusable display formula selected; this chapter is primarily conceptual/procedural or its displayed math was example-specific._

### 02-02 — Licensure, Model Law, Model Rules, and Responsible Charge

_No reusable display formula selected; this chapter is primarily conceptual/procedural or its displayed math was example-specific._

### 02-03 — Contracts, Professional Liability, and Intellectual Property

_No reusable display formula selected; this chapter is primarily conceptual/procedural or its displayed math was example-specific._

### 02-04 — Cash Flows, Interest, and Economic Equivalence

- **02-04:F1** — $F=P(1+i)^n.$
- **02-04:F2** — $P=F(1+i)^{-n}.$
- **02-04:F3** — $i_e=\left(1+\frac{r}{m}\right)^m-1.$
- **02-04:F5** — $P=\sum_{t=0}^{n}\frac{C_t}{(1+i)^t}.$

### 02-05 — Present Worth and Future Worth

- **02-05:F1** — $P=F(P/F,i,n)=F(1+i)^{-n}.$
- **02-05:F2** — $F=P(F/P,i,n)=P(1+i)^n.$
- **02-05:F3** — $F=A(F/A,i,n)=A\frac{(1+i)^n-1}{i}.$
- **02-05:F5** — $PW=\sum P_k.$

### 02-06 — Annual Worth, Capital Recovery, and Gradient Series

- **02-06:F1** — $A=P(A/P,i,n).$
- **02-06:F3** — $A=F(A/F,i,n) =F\frac{i}{(1+i)^n-1}.$
- **02-06:F5** — $EAC=CR+O\&M+\text{other annual equivalents}.$

### 02-07 — Rate of Return and Minimum Attractive Rate of Return

_No reusable display formula selected; this chapter is primarily conceptual/procedural or its displayed math was example-specific._

### 02-08 — Breakeven, Benefit-Cost, and Payback Analysis

- **02-08:F1** — $EC_A(x)=EC_B(x).$
- **02-08:F2** — $C=F+vQ,$
- **02-08:F3** — $F_A+v_AQ=F_B+v_BQ,$
- **02-08:F4** — $Q_{BE}=\frac{F_B-F_A}{v_A-v_B},$
- **02-08:F5** — $pQ=F+vQ,$
- **02-08:F6** — $Q_{BE}=\frac{F}{p-v}.$
- **02-08:F7** — $B-C\ge0$
- **02-08:F8** — $\frac{B}{C}\ge1.$

### 02-09 — Inflation, Depreciation, Taxes, and Replacement

- **02-09:F1** — $i_e=\left(1+\frac{r}{m}\right)^m-1.$
- **02-09:F2** — $D_j=\frac{C-S_n}{n},$
- **02-09:F3** — $D_j=(\text{factor})C$
- **02-09:F4** — $BV_j=C-\sum_{k=1}^{j}D_k.$
- **02-09:F5** — $Tax=t(\text{taxable income}),$
- **02-09:F6** — $P=\frac{A}{i}.$

### 02-10 — Economic Decision-Making, Project Selection, and Risk

- **02-10:F1** — $EV=\sum p_i C_i.$

### 02-11 — Atomic Structure, Bonding, and the Periodic Table

- **02-11:F1** — $A=Z+N$

### 02-12 — Chemical Quantities, Stoichiometry, and Reaction Balancing

- **02-12:F2** — $M_{H_2O}=2M_H+M_O.$
- **02-12:F3** — $n=\frac{m}{M},$
- **02-12:F4** — $w_i=\frac{\text{mass of element }i\text{ in one mole of compound}}{\text{molar mass of compound}}.$
- **02-12:F6** — $\frac{n_A}{a}=\frac{n_B}{b}=\frac{n_C}{c}=\frac{n_D}{d}$
- **02-12:F7** — $\%Y=\frac{\text{actual yield}}{\text{theoretical yield}}\times100\%.$
- **02-12:F9** — $V=n(22.4\ \text{L/mol}).$

### 02-13 — Solutions, Concentration, Acids, Bases, and pH

- **02-13:F1** — $M=\frac{\text{mol solute}}{\text{L solution}}.$
- **02-13:F2** — $m=\frac{\text{mol solute}}{\text{kg solvent}}.$
- **02-13:F3** — $M_1V_1=M_2V_2.$
- **02-13:F4** — $M_f=\frac{\sum M_iV_i}{V_f}.$
- **02-13:F5** — $pH=-\log_{10}[H^+].$
- **02-13:F6** — $[H^+][OH^-]=10^{-14},$
- **02-13:F7** — $pH+pOH=14.$
- **02-13:F9** — $K_a=\frac{[H^+][A^-]}{[HA]}$
- **02-13:F10** — $pK_a=-\log_{10}K_a.$
- **02-13:F11** — $pH=pK_a+\log\frac{[A^-]}{[HA]},$
- **02-13:F13** — $K_{sp}=[A^{n+}]^m[B^{m-}]^n.$

### 02-14 — Chemical Equilibrium, Electrochemistry, and Corrosion

- **02-14:F2** — $K=\frac{[C]^c[D]^d}{[A]^a[B]^b}.$
- **02-14:F3** — $E=E^\circ-\frac{RT}{nF}\ln Q,$
- **02-14:F4** — $m=\frac{QM}{zF},$
- **02-14:F5** — $F=96{,}485\ \text{C/mol e}^-.$
- **02-14:F6** — $m=\frac{ItM}{zF}.$

### 02-15 — Organic Chemistry and Biological Systems

_No reusable display formula selected; this chapter is primarily conceptual/procedural or its displayed math was example-specific._

### 02-16 — Materials Classes, Structure, and Bonding

- **02-16:F1** — $\rho_c=\sum f_i\rho_i.$
- **02-16:F2** — $E_c=\sum f_iE_i$

### 02-17 — Material Properties and Engineering Selection

- **02-17:F1** — $\varepsilon=\frac{\Delta L}{L_0}.$
- **02-17:F2** — $\varepsilon_T=\ln(1+\varepsilon).$
- **02-17:F3** — $\rho=\frac{RA}{L}$
- **02-17:F4** — $R=\rho\frac{L}{A}.$
- **02-17:F5** — $\sigma_e=\frac{1}{\rho}.$
- **02-17:F6** — $C=\frac{\varepsilon A}{d}.$
- **02-17:F7** — $\varepsilon=\alpha\Delta T,$
- **02-17:F8** — $\text{specific strength}=\frac{\text{strength}}{\rho},$

### 02-18 — Diffusion, Phase Change, Heat Treatment, and Processing

- **02-18:F1** — $D=D_0e^{-Q/(RT)},$
- **02-18:F2** — $\ln\frac{D_2}{D_1} =-\frac{Q}{R}\left(\frac1{T_2}-\frac1{T_1}\right).$
- **02-18:F3** — $w_\alpha=\frac{x_\beta-x}{x_\beta-x_\alpha}, \qquad w_\beta=\frac{x-x_\alpha}{x_\beta-x_\alpha}.$
- **02-18:F4** — $w_\alpha+w_\beta=1.$

### 02-19 — Safety Systems, Hazard Communication, and Personal Protective Equipment

- **02-19:F1** — $Risk=Hazard\times Probability$
- **02-19:F2** — $Risk=Hazard\times Exposure.$

### 02-20 — Fire, Explosion, Electrical, and Confined-Space Hazards

- **02-20:F1** — $LFL_m=\frac{100}{\sum_i C_{fi}/LFL_i},$

### 02-21 — Toxicology, Exposure Limits, Risk, and Chemical Compatibility

- **02-21:F1** — $Risk=CDI\times CSF,$
- **02-21:F2** — $HI=\frac{CDI}{RfD}.$
- **02-21:F3** — $RfD=\frac{NOAEL}{UF},$

### 02-22 — Constructing a Free-Body Diagram

- **02-22:F1** — $\mathbf F=F_x\hat{\mathbf i}+F_y\hat{\mathbf j}$
- **02-22:F3** — $F_x=F\cos\theta,\qquad F_y=F\sin\theta$
- **02-22:F5** — $W=mg$
- **02-22:F6** — $\mathbf F_A=-\mathbf F_B,\qquad \mathbf F_A\parallel AB$

### 02-23 — Equilibrium Equations for a 2D Concurrent Force System

- **02-23:F1** — $\sum \mathbf F=\mathbf 0$
- **02-23:F2** — $F_x=F\cos\theta,\qquad F_y=F\sin\theta$
- **02-23:F3** — $\sum F_x=0,\qquad \sum F_y=0$
- **02-23:F4** — $\begin{bmatrix}a&b\\c&d\end{bmatrix}\begin{bmatrix}F_1\\F_2\end{bmatrix}=\begin{bmatrix}r_1\\r_2\end{bmatrix}$
- **02-23:F5** — $\mathbf R=\sum_i\mathbf F_i,\qquad \mathbf F_{\rm eq}=-\mathbf R$
- **02-23:F7** — $\left|\sum F_x\right|\approx0,\qquad\left|\sum F_y\right|\approx0$

### 02-24 — Method of Joints for Planar Trusses

- **02-24:F2** — $m+r=2j$
- **02-24:F3** — $\text{unloaded joint + geometry rules}\Rightarrow F=0$
- **02-24:F5** — $\sum F_x=0,\qquad\sum F_y=0$
- **02-24:F6** — $F>0:\text{ tension (assumed)}\qquad F<0:\text{ compression}$
- **02-24:F7** — $\sum\mathbf F_{\rm joint}=\mathbf0$

### 02-25 — Moments, Couples, and Equivalent Force Systems

- **02-25:F1** — $\mathbf M_O=\mathbf r\times\mathbf F,\qquad M_O=F d_\perp$
- **02-25:F2** — $M_z=xF_y-yF_x$
- **02-25:F3** — $M_c=F d$
- **02-25:F5** — $\mathbf R=\sum\mathbf F_i,\qquad \mathbf M_O=\sum(\mathbf r_i\times\mathbf F_i)+\sum\mathbf M_i$
- **02-25:F6** — $M_O(\mathbf F)=M_O(F_x)+M_O(F_y)$
- **02-25:F7** — $[M]=\text{force}\times\text{length}$

### 02-26 — Rigid-Body Equilibrium and Support Reactions

- **02-26:F3** — $\sum M_A=0$
- **02-26:F4** — $\sum M_A=0\rightarrow B_y,\qquad \sum F_y=0\rightarrow A_y$
- **02-26:F5** — $\sum\mathbf F=\mathbf0,\qquad\sum\mathbf M=\mathbf0$
- **02-26:F7** — $\sum F_x=\sum F_y=\sum M_O=0$

### 02-27 — Method of Sections, Frames, and Machines

- **02-27:F2** — $\sum M_P=0\Rightarrow \text{one cut-member force}$
- **02-27:F3** — $F_{\rm assumed\ tension}<0\Rightarrow\text{compression}$
- **02-27:F4** — $\text{frame member: }\sum F_x=\sum F_y=\sum M=0$
- **02-27:F5** — $\mathbf F_{A\to B}=-\mathbf F_{B\to A}$
- **02-27:F6** — $A_x,A_y\text{ on member 1}\leftrightarrow -A_x,-A_y\text{ on member 2}$
- **02-27:F7** — $\sum\mathbf F=\mathbf0,\qquad\sum M=0\text{ for each isolated member}$

### 02-28 — Distributed Loads, Centroids, and Centers of Gravity

- **02-28:F1** — $R=\int_a^b w(x)\,dx,\qquad x_R=\frac{\int_a^b xw(x)\,dx}{R}$
- **02-28:F2** — $R_{\rm uniform}=wL,\qquad R_{\rm triangle}=\tfrac12 w_0L$
- **02-28:F3** — $\bar x=\frac{\sum A_i x_i}{\sum A_i},\qquad \bar y=\frac{\sum A_i y_i}{\sum A_i}$
- **02-28:F4** — $ar x=\frac1A\int_A x\,dA,\qquad ar y=\frac1A\int_A y\,dA.$
- **02-28:F5** — $A=\int_A dA$
- **02-28:F6** — $\mathbf r_G=\frac{\sum m_i\mathbf r_i}{\sum m_i}$
- **02-28:F7** — $\bar x=\frac{\sum V_i x_i}{\sum V_i}\quad(\rho=\text{constant})$
- **02-28:F8** — $R=\int w\,dx,\qquad Rx_R=\int xw\,dx.$

### 02-29 — Area Moments of Inertia and the Parallel-Axis Theorem

- **02-29:F1** — $I_x=\int_A y^2\,dA,\qquad I_y=\int_A x^2\,dA.$
- **02-29:F2** — $I_x=\int y^2dA,\qquad I_y=\int x^2dA$
- **02-29:F4** — $I_{x,c}=\frac{bh^3}{12}$
- **02-29:F5** — $I=I_c+Ad^2$
- **02-29:F6** — $I=\sum_i\left(I_{c,i}+A_i d_i^2\right)$
- **02-29:F7** — $J=I_x+I_y.$
- **02-29:F8** — $J=I_x+I_y$
- **02-29:F9** — $r_x=\sqrt{\frac{I_x}{A}},\qquad r_y=\sqrt{\frac{I_y}{A}}$
- **02-29:F10** — $I_{xy}=\int_A xy\,dA.$
- **02-29:F11** — $I_{xy}=\int xy\,dA$

### 02-30 — Static Friction

- **02-30:F1** — $|F|\le\mu_sN.$
- **02-30:F2** — $|F|\le\mu_sN$
- **02-30:F3** — $F=\mu_sN\quad\text{at impending slip}$
- **02-30:F4** — $F_k=\mu_kN.$
- **02-30:F5** — $F_k=\mu_kN$
- **02-30:F6** — $N=W\cos heta.$
- **02-30:F7** — $W_\parallel=W\sin\theta,\qquad W_\perp=W\cos\theta$
- **02-30:F8** — $P_{\rm slide}=\mu_sN,\qquad \sum M_{\rm edge}=0\text{ for tipping}$
- **02-30:F9** — $F_1=F_2e^{\mu heta},$
- **02-30:F10** — $\frac{F_1}{F_2}=e^{\mu\theta}$
- **02-30:F11** — $M=Pr\tan(\alpha\pm\phi),\qquad \mu=\tan\phi$

### 02-31 — Particle Kinematics — Rectilinear Motion

- **02-31:F1** — $v=\frac{ds}{dt},\qquad a=\frac{dv}{dt}=\frac{d^2s}{dt^2}$
- **02-31:F3** — $a_y=-g\quad(\text{upward positive})$
- **02-31:F5** — $a=v\frac{dv}{ds}.$
- **02-31:F6** — $a=v\frac{dv}{ds}$
- **02-31:F7** — $\Delta s=\int v\,dt,\qquad \Delta v=\int a\,dt$
- **02-31:F8** — $s_{A/B}=s_A-s_B,\qquad v_{A/B}=v_A-v_B$

### 02-32 — Particle Kinematics — Curvilinear and Relative Motion

- **02-32:F1** — $\mathbf r=x\hat i+y\hat j,\quad\mathbf v=\dot x\hat i+\dot y\hat j,\quad\mathbf a=\ddot x\hat i+\ddot y\hat j$
- **02-32:F3** — $a_t=\frac{dv}{dt},\qquad a_n=\frac{v^2}{\rho}$
- **02-32:F4** — $\mathbf v=\dot r\,\mathbf e_r+r\dot\theta\,\mathbf e_\theta$
- **02-32:F5** — $\mathbf a=(\ddot r-r\dot\theta^2)\mathbf e_r+(r\ddot\theta+2\dot r\dot\theta)\mathbf e_\theta$
- **02-32:F6** — $v=r\omega,\qquad a_t=r\alpha,\qquad a_n=r\omega^2$
- **02-32:F7** — $\mathbf r_A=\mathbf r_B+\mathbf r_{A/B}$
- **02-32:F8** — $\mathbf v_A=\mathbf v_B+\mathbf v_{A/B},\qquad \mathbf a_A=\mathbf a_B+\mathbf a_{A/B}$

### 02-33 — Particle Kinetics — Force and Acceleration

- **02-33:F1** — $\sum\mathbf F=m\mathbf a$
- **02-33:F2** — $W=mg.$
- **02-33:F3** — $W=mg$
- **02-33:F4** — $\sum F_x=ma_x,\qquad \sum F_y=ma_y$
- **02-33:F5** — $\sum F_t=m\frac{dv}{dt},\qquad\sum F_n=m\frac{v^2}{\rho}$
- **02-33:F6** — $L=\text{constant}\Rightarrow \dot L=0,\ \ddot L=0$
- **02-33:F7** — $|F_s|\le\mu_sN,\qquad F_k=\mu_kN$
- **02-33:F8** — $\text{FBD}\rightarrow\text{kinematics}\rightarrow\sum F=ma\rightarrow\text{check}$

### 02-34 — Work, Energy, and Power

- **02-34:F1** — $U=\int \mathbf F\cdot d\mathbf r.$
- **02-34:F2** — $U_{1\to2}=\int_1^2\mathbf F\cdot d\mathbf r$
- **02-34:F3** — $T=\frac12mv^2.$
- **02-34:F4** — $T_{\rm particle}=\tfrac12mv^2$
- **02-34:F5** — $V_g=mgh$
- **02-34:F6** — $V_e=\frac12ks^2$
- **02-34:F7** — $F_s=ks,\qquad V_e=\tfrac12ks^2$
- **02-34:F8** — $T_2+V_2=T_1+V_1+U_{1\to2}^{\rm nonconservative}$
- **02-34:F9** — $P=\mathbf F\cdot\mathbf v.$
- **02-34:F10** — $P=\frac{dU}{dt}=\mathbf F\cdot\mathbf v,\qquad \eta=\frac{P_{\rm out}}{P_{\rm in}}$

### 02-35 — Impulse, Momentum, and Impact

- **02-35:F1** — $\mathbf p=m\mathbf v,\qquad \mathbf P=\sum_i m_i\mathbf v_i$
- **02-35:F2** — $m\mathbf v_2=m\mathbf v_1+\int_{t_1}^{t_2}\mathbf F\,dt$
- **02-35:F3** — $\sum m_i\mathbf v_{i1}=\sum m_i\mathbf v_{i2}\quad(\text{zero external impulse})$
- **02-35:F4** — $\mathbf H_{O2}=\mathbf H_{O1}+\int_{t_1}^{t_2}\mathbf M_O\,dt$
- **02-35:F5** — $m_1v_1+m_2v_2=m_1v_1'+m_2v_2'$
- **02-35:F6** — $e=\frac{v_2'-v_1'}{v_1-v_2}\quad\text{for chosen 1D orientation}$
- **02-35:F7** — $e=1:\text{ elastic},\qquad e=0:\text{ no rebound}$

### 02-36 — Rigid-Body Planar Kinematics and Kinetics

- **02-36:F1** — $\mathbf v_B=\mathbf v_A+\boldsymbol\omega\times\mathbf r_{B/A}$
- **02-36:F2** — $\mathbf a_B=\mathbf a_A+oldsymbollpha imes\mathbf r_{B/A}+oldsymbol\omega imes(oldsymbol\omega imes\mathbf r_{B/A}).$
- **02-36:F3** — $\mathbf a_B=\mathbf a_A+\boldsymbol\alpha\times\mathbf r_{B/A}-\omega^2\mathbf r_{B/A}$
- **02-36:F5** — $v_P=\omega r_{P/IC}$
- **02-36:F6** — $I=\int r^2\,dm,\qquad I_O=I_G+md^2$
- **02-36:F7** — $\sum F_x=ma_{Gx},\quad \sum F_y=ma_{Gy},\quad \sum M_G=I_Glpha.$
- **02-36:F8** — $\sum\mathbf F=m\mathbf a_G,\qquad \sum M_G=I_G\alpha$
- **02-36:F9** — $T=\tfrac12mv_G^2+\tfrac12I_G\omega^2$

### 02-37 — Stress, Strain, and Axial/Thermal Deformation

- **02-37:F1** — $\sigma=\frac{P}{A}.$
- **02-37:F2** — $\sigma=\frac{P}{A}$
- **02-37:F3** — $\varepsilon=\frac{\delta}{L},\qquad \sigma=E\varepsilon$
- **02-37:F4** — $\delta=\frac{PL}{AE},\qquad \delta=\int\frac{P(x)}{A(x)E(x)}dx$
- **02-37:F5** — $\nu=-\frac{\varepsilon_{\rm lateral}}{\varepsilon_{\rm longitudinal}},\qquad G=\frac{E}{2(1+\nu)}$
- **02-37:F6** — $\delta_T=lpha L\Delta T.$
- **02-37:F7** — $\varepsilon_T=\alpha\Delta T,\qquad \delta_T=\alpha L\Delta T$
- **02-37:F9** — $\sigma_h=\frac{pr}{t},\qquad \sigma_a=\frac{pr}{2t}$

### 02-38 — Torsion

- **02-38:F1** — $\sum M_{\rm axis}=0\Rightarrow T_{\rm internal}$
- **02-38:F3** — $J=\int r^2dA$
- **02-38:F4** — $au(r)=\frac{Tr}{J}.$
- **02-38:F5** — $\tau_{\max}=\frac{Tc}{J}$
- **02-38:F6** — $\phi=\frac{TL}{GJ}.$
- **02-38:F7** — $\phi=\int\frac{T(x)}{G(x)J(x)}dx$
- **02-38:F8** — $k_t=\frac{T}{\phi}=\frac{GJ}{L}.$
- **02-38:F9** — $k_t=\frac{GJ}{L}$
- **02-38:F10** — $P=T\omega.$
- **02-38:F11** — $P=T\omega$
- **02-38:F12** — $\tau=\frac{T}{2A_m t}$

### 02-39 — Beams — Shear, Moment, Bending, and Deflection

- **02-39:F1** — $\sum F_y=0\Rightarrow V,\qquad \sum M_{\rm cut}=0\Rightarrow M$
- **02-39:F2** — $\frac{dV}{dx}=-w(x),\qquad \frac{dM}{dx}=V(x)$
- **02-39:F3** — $\Delta V=-P,\qquad \Delta M=M_{\rm applied}$
- **02-39:F4** — $\sigma_x=-\frac{My}{I}.$
- **02-39:F5** — $\sigma_{\max}=\frac{Mc}{I}=\frac{M}{S}$
- **02-39:F6** — $au=\frac{VQ}{Ib}.$
- **02-39:F7** — $\tau=\frac{VQ}{Ib},\qquad q=\frac{VQ}{I}$
- **02-39:F8** — $EI\,y''=M(x)$
- **02-39:F9** — $EI\frac{d^2y}{dx^2}=M(x)$
- **02-39:F10** — $n=\frac{E_1}{E_2}$

### 02-40 — Combined Stress, Principal Stress, and Mohr's Circle

- **02-40:F1** — $\sigma_x=\sum \sigma_{x,i},\qquad \tau_{xy}=\sum\tau_{xy,i}$
- **02-40:F2** — $\sigma_{x'}=\frac{\sigma_x+\sigma_y}{2}+\frac{\sigma_x-\sigma_y}{2}\cos2\theta+\tau_{xy}\sin2\theta$
- **02-40:F3** — $\sigma_{1,2}=\frac{\sigma_x+\sigma_y}{2}\pm\sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2+\tau_{xy}^2}$
- **02-40:F4** — $\tau_{\max,\rm in}=\sqrt{\left(\frac{\sigma_x-\sigma_y}{2}\right)^2+\tau_{xy}^2}$
- **02-40:F6** — $an2 heta_p=\frac{2 au_{xy}}{\sigma_x-\sigma_y}.$
- **02-40:F7** — $\tan2\theta_p=\frac{2\tau_{xy}}{\sigma_x-\sigma_y}$
- **02-40:F8** — $\tau_{\max,3D}=\frac{\sigma_{\max}-\sigma_{\min}}{2}$

### 02-41 — Fluid Properties, Pressure, and Hydrostatics

- **02-41:F1** — $\rho=\frac{m}{V},\qquad v=\frac1\rho,\qquad \gamma=\rho g,\qquad SG=\frac{\rho}{\rho_w}$
- **02-41:F2** — $P_{\rm abs}=P_{\rm atm}+P_{\rm gage},\qquad P_{\rm abs}=P_{\rm atm}-P_{\rm vacuum}$
- **02-41:F3** — $\tau=\mu\frac{dv}{dy},\qquad \nu=\frac{\mu}{\rho}$
- **02-41:F4** — $\tau=K\left(\frac{dv}{dy}\right)^n$
- **02-41:F5** — $\sigma=\frac{F}{L},\qquad h=\frac{4\sigma\cos\beta}{\gamma d}$
- **02-41:F7** — $\text{static fluid}\Rightarrow \frac{dP}{dz}=-\rho g$

### 02-42 — Buoyancy, Manometry, and Forces on Submerged Surfaces

- **02-42:F1** — $\Delta P=\sum (\pm \rho_i g\,\Delta h_i)$
- **02-42:F2** — $P_{\rm atm}=P_v+\rho gh$
- **02-42:F3** — $F_B=\rho_f gV_{\rm displaced}=\gamma_fV_{\rm displaced}$
- **02-42:F4** — $W=\sum_i \rho_i gV_i$
- **02-42:F5** — $F_R=P_CA=\rho g h_C A$
- **02-42:F6** — $y_{CP}=y_C+\frac{I_{xC}}{y_CA}$
- **02-42:F7** — $\sum F=0,\qquad \sum M=0$

### 02-43 — Continuity, Velocity Fields, and Flow Kinematics

- **02-43:F1** — $Q=\int_A\mathbf v\cdot\mathbf n\,dA\approx Av$
- **02-43:F2** — $\dot m=\rho Q=\rho Av$
- **02-43:F4** — $\mathbf a=\frac{\partial\mathbf v}{\partial t}+(\mathbf v\cdot\nabla)\mathbf v$
- **02-43:F5** — $\frac{dx}{u}=\frac{dy}{v}=\frac{dz}{w}\quad\text{along a streamline}$
- **02-43:F6** — $\frac{dm_{CV}}{dt}=\sum\dot m_{\rm in}-\sum\dot m_{\rm out}$
- **02-43:F7** — $\sum\dot m_{\rm in}=\sum\dot m_{\rm out}\quad(\text{steady})$

### 02-44 — Bernoulli and Mechanical-Energy Equations

- **02-44:F1** — $H=\frac{P}{\gamma}+\frac{v^2}{2g}+z$
- **02-44:F2** — $\frac{P_1}{\gamma}+\frac{v_1^2}{2g}+z_1=\frac{P_2}{\gamma}+\frac{v_2^2}{2g}+z_2$
- **02-44:F3** — $HGL=\frac{P}{\gamma}+z,\qquad EGL=HGL+\frac{v^2}{2g}$
- **02-44:F4** — $\frac{P_1}{\gamma}+\frac{v_1^2}{2g}+z_1+h_p-h_t-h_L=\frac{P_2}{\gamma}+\frac{v_2^2}{2g}+z_2$
- **02-44:F6** — $\Delta P+\gamma\Delta z+\rho a_x\Delta x=0\quad\text{(stated 1D model)}$

### 02-45 — Internal Flow — Reynolds Number, Friction, and Head Loss

- **02-45:F1** — $Re=\frac{\rho vD}{\mu}=\frac{vD}{\nu}$
- **02-45:F2** — $v(r)=v_{\max}\left[1-\left(\frac rR\right)^2\right]$
- **02-45:F3** — $h_f=f\frac LD\frac{v^2}{2g}$
- **02-45:F4** — $f_{\rm Darcy}=4f_{\rm Fanning}$
- **02-45:F6** — $D_h=\frac{4A}{P_w}$
- **02-45:F7** — $Q=\frac{\pi D^4\Delta P}{128\mu L}$

### 02-46 — Momentum, Flow Measurement, Pumps, and Turbines

- **02-46:F1** — $\sum\mathbf F=\sum_{\rm out}\dot m\,\mathbf v-\sum_{\rm in}\dot m\,\mathbf v$
- **02-46:F2** — $\mathbf F_{\rm fluid\ on\ hardware}=-\mathbf F_{\rm hardware\ on\ fluid}$
- **02-46:F3** — $v=\sqrt{\frac{2(P_0-P_s)}{\rho}}$
- **02-46:F4** — $Q=C_vA_2\sqrt{\frac{2\Delta P/\rho}{1-(A_2/A_1)^2}}\quad\text{(level incompressible form)}$
- **02-46:F5** — $\dot W_{\rm in}=\frac{\rho gQH}{\eta_{\rm total}}$

### 02-47 — Thermodynamic Systems, Properties, Work, and Heat

- **02-47:F1** — $\text{closed system: }\dot m_{\rm boundary}=0$
- **02-47:F2** — $v=\frac Vm,\qquad u=\frac Um,\qquad h=\frac Hm,\qquad s=\frac Sm$
- **02-47:F3** — $H=U+PV,\qquad h=u+Pv$
- **02-47:F4** — $Q>0:\text{ into system},\qquad W>0:\text{ out of system}$
- **02-47:F5** — $w_b=\int_1^2P\,dv$
- **02-47:F6** — $Pv^n=\text{constant}\quad\text{(polytropic ideal-gas process)}$

### 02-48 — Pure Substances, Phase Diagrams, and Property Tables

- **02-48:F1** — $P=P_{\rm sat}(T)\quad\text{on the saturation line}$
- **02-48:F2** — $x=0:\text{ saturated liquid},\qquad x=1:\text{ saturated vapor}$
- **02-48:F3** — $x=\frac{m_g}{m_f+m_g},\qquad y=y_f+xy_{fg}$
- **02-48:F4** — $y_{fg}=y_g-y_f$
- **02-48:F5** — $T>T_{\rm sat}(P)\Rightarrow\text{superheated vapor}$
- **02-48:F6** — $q_{\rm rev}=\int T\,ds$

### 02-49 — Ideal Gases, Gas Mixtures, and Psychrometrics

- **02-49:F1** — $Pv=RT,\qquad PV=mRT,\qquad R=\frac{\bar R}{M}$
- **02-49:F2** — $\Delta u=c_v\Delta T,\quad\Delta h=c_p\Delta T,\quad c_p-c_v=R$
- **02-49:F3** — $\frac{T_2}{T_1}=\left(\frac{P_2}{P_1}\right)^{(k-1)/k}$
- **02-49:F4** — $x_i=\frac{N_i}{N},\quad y_i=\frac{m_i}{m},\quad P=\sum P_i,\quad M=\sum x_iM_i$
- **02-49:F5** — $Pv=ZRT$
- **02-49:F6** — $\omega=0.622\frac{P_v}{P-P_v},\qquad \phi=\frac{P_v}{P_g(T)}$
- **02-49:F7** — $\dot m_a\omega_1+\dot m_w=\dot m_a\omega_2$

### 02-50 — First Law — Closed Systems

- **02-50:F1** — $Q-W=\Delta U+\Delta KE+\Delta PE$
- **02-50:F2** — $\Delta E=\Delta U+\frac m2(V_2^2-V_1^2)+mg(z_2-z_1)$
- **02-50:F3** — $W_b=P(V_2-V_1)$
- **02-50:F4** — $W_b=0,\qquad Q=\Delta U\quad\text{(if other terms negligible)}$
- **02-50:F5** — $W_b=mRT\ln\frac{V_2}{V_1}$
- **02-50:F6** — $W_b=\frac{P_2V_2-P_1V_1}{1-n}$
- **02-50:F7** — $\text{state 1}\rightarrow\text{process}\rightarrow\text{state 2}\rightarrow Q-W=\Delta E$

### 02-51 — First Law — Control Volumes

- **02-51:F1** — $\frac{dE_{CV}}{dt}=\dot Q-\dot W+\sum_{\rm in}\dot m\left(h+\frac{V^2}{2}+gz\right)-\sum_{\rm out}\dot m\left(h+\frac{V^2}{2}+gz\right)$
- **02-51:F2** — $\dot Q-\dot W=\dot m\left[(h_2-h_1)+\frac{V_2^2-V_1^2}{2}+g(z_2-z_1)\right]$
- **02-51:F3** — $h_1+\frac{V_1^2}{2}=h_2+\frac{V_2^2}{2}$
- **02-51:F6** — $h_1=h_2$
- **02-51:F7** — $\sum\dot m_{\rm in}h_{\rm in}=\sum\dot m_{\rm out}h_{\rm out}\quad\text{(adiabatic mixer, negligible KE/PE)}$

### 02-52 — Second Law, Entropy, and Isentropic Processes

- **02-52:F1** — $\eta_{\rm engine}<1\quad\text{for finite-temperature heat engines}$
- **02-52:F2** — $ds=\frac{\delta q_{\rm rev}}{T}$
- **02-52:F3** — $\Delta S_{\rm system}=\int\frac{\delta Q}{T_b}+S_{\rm gen},\qquad S_{\rm gen}\ge0$
- **02-52:F5** — $\Delta s=c_p\ln\frac{T_2}{T_1}-R\ln\frac{P_2}{P_1}$
- **02-52:F6** — $\Delta s\approx c\ln\frac{T_2}{T_1}$
- **02-52:F7** — $I=T_0S_{\rm gen}$

### 02-53 — Power Cycles

- **02-53:F1** — $\eta=\frac{W_{\rm net}}{Q_H}=1-\frac{Q_L}{Q_H}$
- **02-53:F2** — $\eta_C=1-\frac{T_L}{T_H}$
- **02-53:F3** — $\eta_{\rm Otto}=1-\frac{1}{r^{k-1}}$
- **02-53:F4** — $w_{\rm net}=w_t-w_c$
- **02-53:F5** — $\eta_{\rm Rankine}=\frac{(h_3-h_4)-(h_2-h_1)}{h_3-h_2}$

### 02-54 — Refrigeration and Heat Pumps

- **02-54:F1** — $COP_R=\frac{Q_L}{W_{in}},\qquad COP_{HP}=\frac{Q_H}{W_{in}}=COP_R+1$
- **02-54:F2** — $COP_{R,C}=\frac{T_L}{T_H-T_L},\qquad COP_{HP,C}=\frac{T_H}{T_H-T_L}$
- **02-54:F3** — $1\to2:\text{compression},\ 2\to3:\text{condensation},\ 3\to4:h=\text{const},\ 4\to1:\text{evaporation}$
- **02-54:F4** — $COP_R=\frac{h_1-h_4}{h_2-h_1}$
- **02-54:F5** — $\dot Q_L=\dot m(h_1-h_4)$
- **02-54:F6** — $COP_{HP}=COP_R+1$

### 02-55 — Conduction and Thermal Resistance

- **02-55:F1** — $\dot Q=-kA\frac{dT}{dx}$
- **02-55:F2** — $\dot Q=\frac{kA(T_1-T_2)}{L}$
- **02-55:F3** — $\dot Q=\frac{2\pi kL(T_1-T_2)}{\ln(r_2/r_1)}$
- **02-55:F4** — $\dot Q=\frac{\Delta T}{R_{\rm total}},\qquad R_{\rm cond,plane}=\frac{L}{kA},\qquad R_{\rm conv}=\frac1{hA}$
- **02-55:F5** — $R_{\rm total}=\frac1{h_1A}+\sum_i\frac{L_i}{k_iA}+\frac1{h_2A}$
- **02-55:F6** — $r_{\rm cr}=\frac{k_{\rm insulation}}{h_\infty}$

### 02-56 — Extended Surfaces and Transient Conduction

- **02-56:F1** — $Bi=\frac{hV}{kA_s}=\frac{hL_c}{k}$
- **02-56:F2** — $\frac{T-T_\infty}{T_i-T_\infty}=\exp\left(-\frac{hA_s}{\rho Vc_p}t\right)$
- **02-56:F3** — $Q_{\rm body}=m c_p(T-T_i)$
- **02-56:F4** — $Fo=\frac{\alpha t}{L^2},\qquad \alpha=\frac{k}{\rho c_p}$
- **02-56:F6** — $m=\sqrt{\frac{hP}{kA_c}}$
- **02-56:F7** — $\varepsilon_f=\frac{\dot Q_{\rm fin}}{hA_b(T_b-T_\infty)}$

### 02-57 — Convection and Thermal Radiation

- **02-57:F1** — $\dot Q=hA(T_s-T_\infty)$
- **02-57:F2** — $Nu=\frac{hL}{k},\qquad Re=\frac{\rho VL}{\mu},\qquad Pr=\frac{c_p\mu}{k}$
- **02-57:F3** — $Nu=CRe^mPr^n\quad\text{(correlation form)}$
- **02-57:F4** — $Nu_D=4.36\ \text{(laminar, uniform heat flux)},\qquad Nu_D=3.66\ \text{(laminar, const. }T_s)$
- **02-57:F5** — $Ra=Gr\,Pr$
- **02-57:F6** — $\dot Q_{\rm emit}=\varepsilon\sigma AT^4$
- **02-57:F7** — $A_iF_{ij}=A_jF_{ji},\qquad \sum_jF_{ij}=1$

### 02-58 — Heat Exchangers — LMTD and Effectiveness-NTU

- **02-58:F1** — $\dot Q=C_H(T_{Hi}-T_{Ho})=C_C(T_{Co}-T_{Ci})$
- **02-58:F2** — $\Delta T(x)=T_H(x)-T_C(x)$
- **02-58:F3** — $\Delta T_{lm}=\frac{\Delta T_1-\Delta T_2}{\ln(\Delta T_1/\Delta T_2)}$
- **02-58:F4** — $\dot Q=UA F\Delta T_{lm}$
- **02-58:F5** — $\dot Q=UA\,F\Delta T_{lm}$
- **02-58:F6** — $\varepsilon=\frac{\dot Q}{\dot Q_{\max}},\qquad \dot Q_{\max}=C_{\min}(T_{Hi}-T_{Ci})$
- **02-58:F7** — $NTU=\frac{UA}{C_{\min}},\qquad C_r=\frac{C_{\min}}{C_{\max}}$

### 02-59 — Electrical Quantities, Ohm's Law, and DC Power

- **02-59:F1** — $i(t)=\frac{dq(t)}{dt}$
- **02-59:F2** — $V=\frac{W}{Q}$
- **02-59:F3** — $R=\rho\frac{L}{A},\qquad G=\frac{1}{R}$
- **02-59:F4** — $V=IR,\qquad p=vi$
- **02-59:F5** — $R=R_0\left[1+\alpha(T-T_0)\right]$
- **02-59:F6** — $P=VI=I^2R=\frac{V^2}{R}$
- **02-59:F7** — $E=\int p(t)\,dt,\qquad E=Pt\ \text{for constant DC power}$

### 02-60 — Kirchhoff's Laws and Resistive Circuit Analysis

- **02-60:F1** — $R_s=\sum_iR_i,\qquad \frac1{R_p}=\sum_i\frac1{R_i}$
- **02-60:F2** — $\sum I_{\rm in}=\sum I_{\rm out}\qquad\text{or}\qquad\sum_k i_k=0$
- **02-60:F3** — $\sum V_{\rm rises}=\sum V_{\rm drops}\qquad\text{or}\qquad\sum_k v_k=0$
- **02-60:F4** — $V_k=V_T\frac{R_k}{\sum R},\qquad I_k=I_T\frac{G_k}{\sum G}$
- **02-60:F5** — $\sum_j\frac{V_k-V_j}{R_{kj}}=I_{\rm injected,k}$
- **02-60:F6** — $\sum R\,I_{\rm mesh}+\sum R(I_{\rm mesh}-I_{\rm adjacent})=\sum V_{\rm sources}$
- **02-60:F7** — $V_{Th}=V_{oc},\qquad I_N=I_{sc},\qquad R_{Th}=R_N,\qquad R_L=R_{Th}\ \text{for max }P_L$

### 02-61 — Capacitance, Inductance, and First-Order Transients

- **02-61:F1** — $q=Cv_C,\qquad i_C=C\frac{dv_C}{dt}$
- **02-61:F2** — $W_C=\frac12Cv_C^2,\qquad C_p=\sum C_i,\qquad \frac1{C_s}=\sum\frac1{C_i}$
- **02-61:F3** — $v_L=L\frac{di_L}{dt}$
- **02-61:F4** — $W_L=\frac12Li_L^2,\qquad L_s=\sum L_i,\qquad \frac1{L_p}=\sum\frac1{L_i}$
- **02-61:F6** — $v_C(t)=v_C(\infty)+\big[v_C(0^+)-v_C(\infty)\big]e^{-t/\tau},\qquad \tau=R_{eq}C$
- **02-61:F7** — $i_L(t)=i_L(\infty)+\big[i_L(0^+)-i_L(\infty)\big]e^{-t/\tau},\qquad \tau=\frac{L}{R_{eq}}$

### 02-62 — Sinusoids, Phasors, Impedance, and Resonance

- **02-62:F1** — $x(t)=X_{\max}\cos(\omega t+\phi),\qquad f=\frac1T=\frac{\omega}{2\pi}$
- **02-62:F2** — $X_{\rm rms}=\sqrt{\frac1T\int_0^T x^2(t)\,dt},\qquad X_{\rm rms}=\frac{X_{\max}}{\sqrt2}\ \text{for a sinusoid}$
- **02-62:F3** — $\underline V=V_{\rm rms}\angle\phi_V,\qquad \underline I=I_{\rm rms}\angle\phi_I$
- **02-62:F4** — $Z_R=R,\qquad Z_L=j\omega L,\qquad Z_C=\frac1{j\omega C},\qquad Y=\frac1Z$
- **02-62:F5** — $Z_s=\sum Z_i,\qquad Y_p=\sum Y_i,\qquad \underline I=\frac{\underline V}{Z_{eq}}$
- **02-62:F7** — $Z_L=Z_{Th}^{*}$

### 02-63 — AC Power, Power Factor, and Three-Phase Systems

- **02-63:F1** — $\underline S=\underline V\underline I^*=P+jQ,\qquad P=VI\cos\theta,\qquad Q=VI\sin\theta$
- **02-63:F2** — $pf=\cos\theta=\frac{P}{|S|}$
- **02-63:F3** — $Q_C=P\left(\tan\theta_1-\tan\theta_2\right)$
- **02-63:F4** — $\underline V_{an}=V_P\angle0^\circ,\quad \underline V_{bn}=V_P\angle-120^\circ,\quad \underline V_{cn}=V_P\angle120^\circ$
- **02-63:F5** — $I_L=I_P,\qquad V_L=\sqrt3\,V_P$
- **02-63:F6** — $V_L=V_P,\qquad I_L=\sqrt3\,I_P,\qquad Z_\Delta=3Z_Y$

### 02-64 — Magnetics and Transformers

- **02-64:F1** — $\mathbf B=\mu\mathbf H,\qquad \Phi=\int_S\mathbf B\cdot d\mathbf S$
- **02-64:F2** — $\mathbf F=I\mathbf L\times\mathbf B,\qquad F=ILB\sin\theta$
- **02-64:F3** — $v=-N\frac{d\Phi}{dt}$
- **02-64:F4** — $\mathcal R=\frac{\ell}{\mu A},\qquad L=\frac{N^2}{\mathcal R}$
- **02-64:F5** — $\frac{V_P}{V_S}=a=\frac{N_P}{N_S},\qquad \frac{I_P}{I_S}=\frac1a$
- **02-64:F6** — $Z_P=a^2Z_S$

### 02-65 — Motors, Generators, and Electromechanical Energy Conversion

- **02-65:F1** — $\eta=\frac{P_{out}}{P_{in}},\qquad P_{out}=P_{in}-P_{loss}$
- **02-65:F2** — $P_m=T\omega_m,\qquad \omega_m=\frac{2\pi n}{60}$
- **02-65:F3** — $n_s=\frac{120f}{p}\ \text{rpm}$
- **02-65:F4** — $P_d\approx 3\frac{E_aV_a}{X_s}\sin\delta$
- **02-65:F5** — $s=\frac{n_s-n}{n_s}$
- **02-65:F6** — $V_a=K_an\Phi,\qquad P_m=V_aI_a,\qquad T_m=\frac{60}{2\pi}K_a\Phi I_a$
- **02-65:F7** — $V=IR+K_E\omega,\qquad T=K_TI,\qquad K_T=K_E\ \text{in consistent SI units}$

### 02-66 — Measurement Systems, Calibration, Accuracy, and Uncertainty

- **02-66:F3** — $S=\frac{\Delta(\text{electrical output})}{\Delta(\text{physical input})}$
- **02-66:F5** — $w_R=\sqrt{\sum_i\left(\frac{\partial R}{\partial x_i}w_i\right)^2}$

### 02-67 — Sensors, Transducers, Bridges, and Signal Conditioning

- **02-67:F1** — $R_T=R_0\left[1+\alpha(T-T_0)\right]$
- **02-67:F2** — $R=R_0\exp\left[\beta\left(\frac1T-\frac1{T_0}\right)\right]$
- **02-67:F4** — $GF=\frac{\Delta R/R}{\varepsilon}$
- **02-67:F6** — $E_{el}=E_0-S(pH_a-pH_i)$

### 02-68 — Data Acquisition, Sampling, Dynamic Response, and Frequency Response

- **02-68:F1** — $f_s=\frac1{\Delta t}$
- **02-68:F2** — $f_s>2f_N$
- **02-68:F3** — $f_{\rm alias}=|f_{\rm signal}-k f_s|\quad\text{for an integer }k\text{ chosen into the observed band}$
- **02-68:F4** — $\Delta V=\frac{V_H-V_L}{2^n},\qquad V=V_L+N\Delta V$
- **02-68:F7** — $G(j\omega)=|G(j\omega)|\angle\phi(\omega)$

### 02-69 — Transfer Functions and Feedback Control Fundamentals

- **02-69:F1** — $G(s)=\frac{Y(s)}{X(s)}=K\frac{\prod_m(s-z_m)}{\prod_n(s-p_n)}$
- **02-69:F2** — $Y(s)=G(s)X(s)\quad\text{for a single block}$
- **02-69:F4** — $\frac{Y(s)}{L_d(s)}=\frac{G_2(s)}{1+G_1(s)G_2(s)H(s)}\quad\text{for the Handbook diagram}$
- **02-69:F5** — $1+L(s)=0$
- **02-69:F6** — $G(0)=\lim_{s\to0}G(s)$

### 02-70 — PID Control, Stability, and Control-Loop Hardware

- **02-70:F1** — $u_P(t)=K_Pe(t)$
- **02-70:F2** — $u_I(t)=K_I\int_0^t e(\tau)\,d\tau$
- **02-70:F3** — $u_D(t)=K_D\frac{de(t)}{dt}$
- **02-70:F4** — $G_C(s)=K\left(1+\frac1{T_Is}+T_Ds\right)=K_P+\frac{K_I}{s}+K_Ds$
- **02-70:F6** — $G_C(s)=K\frac{1+sT_1}{1+sT_2}$

## Layer 3 — Chemical

### 03-01 — Material and Energy Balances — Single Units and Process Flowsheets

- **03-01:F1** — $\dot n_i=y_i\dot n,\qquad \sum_i y_i=1$
- **03-01:F2** — $\sum \dot m_{\rm in}=\sum \dot m_{\rm out},\qquad \sum \dot n_{i,\rm in}=\sum \dot n_{i,\rm out}$
- **03-01:F4** — $\dot n_{\rm feed}=\sum_j\dot n_j,\qquad y_{i,j}=y_{i,\rm feed}\ \text{for an ideal splitter}$
- **03-01:F6** — $\dot Q-\dot W_s=\sum_{\rm out}\dot n_i\hat H_i-\sum_{\rm in}\dot n_i\hat H_i\quad\text{when KE/PE are negligible}$

### 03-02 — Recycle, Bypass, Purge, and Unsteady Material Balances

- **03-02:F2** — $R=\frac{\dot n_{\rm recycle}}{\dot n_{\rm fresh}},\qquad X_{\rm overall}=\frac{\text{fresh reactant consumed}}{\text{fresh reactant fed}}$
- **03-02:F3** — $\dot n_{\rm feed}=\dot n_{\rm processed}+\dot n_{\rm bypass}$
- **03-02:F4** — $\dot n_{I,\rm fresh}=\dot n_{I,\rm purge}+\dot n_{I,\rm product}$
- **03-02:F5** — $\frac{dN_i}{dt}=\sum \dot n_{i,\rm in}-\sum \dot n_{i,\rm out}+r_{i,\rm gen}V$
- **03-02:F6** — $V\frac{dC}{dt}=Q_{\rm in}C_{\rm in}-Q_{\rm out}C$

### 03-03 — Reactive Material Balances, Combustion, and Heats of Reaction

- **03-03:F1** — $N_{i,out}=N_{i,in}+\nu_i\xi$
- **03-03:F2** — $\dot n_{i,out}=\dot n_{i,in}+\sum_r\nu_{i,r}\dot\xi_r$
- **03-03:F3** — $\%\text{ excess}=\frac{n_{\rm actual}-n_{\rm stoich}}{n_{\rm stoich}}\times100\%$
- **03-03:F4** — $\%\text{ excess air}=\frac{(A/F)_{\rm actual}-(A/F)_{\rm stoich}}{(A/F)_{\rm stoich}}\times100\%$
- **03-03:F5** — $\Delta H_r^\circ=\sum_i\nu_i\Delta H_{f,i}^\circ$
- **03-03:F6** — $\Delta H_r(T)=\Delta H_r^\circ(T_{ref})+\int_{T_{ref}}^T\Delta C_p\,dT$
- **03-03:F7** — $0=\sum_{\rm out}\dot n_i\hat H_i-\sum_{\rm in}\dot n_i\hat H_i-\dot Q+\dot W_s$

### 03-04 — Phase Equilibrium, Raoult's Law, Fugacity, Activity, and Chemical Equilibrium

- **03-04:F1** — $P+F=C+2$
- **03-04:F2** — $p_i=y_iP=H_i x_i$
- **03-04:F3** — $p_i=x_iP_i^{sat},\qquad y_iP=x_iP_i^{sat}$
- **03-04:F4** — $K_i=\frac{y_i}{x_i},\qquad \sum_iK_ix_i=1\ \text{(bubble)},\qquad \sum_i\frac{y_i}{K_i}=1\ \text{(dew)}$
- **03-04:F5** — $\hat f_i^V=\hat f_i^L,\qquad \hat f_i^V=y_i\phi_iP,\qquad \hat f_i^L=x_i\gamma_i f_i^L$
- **03-04:F6** — $\hat f_i^L=x_i\gamma_i f_i^L$
- **03-04:F7** — $\Delta G^\circ=-RT\ln K,\qquad K=\prod_i a_i^{\nu_i}$

### 03-05 — Molecular Diffusion and Convective Mass Transfer

- **03-05:F1** — $J_A=-D_{AB}\frac{dC_A}{dx}$
- **03-05:F2** — $\frac{\partial C}{\partial t}=D\frac{\partial^2C}{\partial x^2}$
- **03-05:F3** — $N_A=\frac{D_{AB}P}{RT(z_2-z_1)}\frac{p_{A1}-p_{A2}}{(p_B)_{lm}}$
- **03-05:F4** — $N_A=-N_B=\frac{D_{AB}}{RT}\frac{p_{A1}-p_{A2}}{z_2-z_1}$
- **03-05:F5** — $N_A=k_G'(p_{AG}-p_{Ai})=k_L'(C_{Ai}-C_{AL})$
- **03-05:F6** — $\frac1{K_G'}=\frac1{k_G'}+\frac{H}{k_L'},\qquad \frac1{K_L'}=\frac1{Hk_G'}+\frac1{k_L'}$
- **03-05:F7** — $Sh=\frac{k_mD}{D_{AB}},\qquad Sc=\frac{\mu}{\rho D_{AB}}$

### 03-06 — Distillation and Equilibrium-Stage Methods

- **03-06:F1** — $F=V+L,\qquad Fz_i=Vy_i+Lx_i$
- **03-06:F2** — $\ln\frac{W}{W_0}=\int_{x_0}^{x}\frac{dx}{y-x}$
- **03-06:F3** — $F=D+B,\qquad Fz_F=Dx_D+Bx_B$
- **03-06:F4** — $y_{n+1}=\frac{R_D}{R_D+1}x_n+\frac{x_D}{R_D+1}$
- **03-06:F5** — $\text{slope}_{q}=\frac{q}{q-1}$
- **03-06:F7** — $E_{MV}=\frac{y_n-y_{n+1}}{y_n^*-y_{n+1}}$

### 03-07 — Absorption, Extraction, Adsorption, and Membrane Separations

- **03-07:F1** — $Z=NTU_G\,HTU_G=NTU_L\,HTU_L=N_{EQ}HETP$
- **03-07:F2** — $N_A=K_G'(p_A-p_A^*)=K_L'(C_A^*-C_A)$
- **03-07:F3** — $K_D=\frac{y_A}{x_A},\qquad Fz_A+Sx_{A,S}=R x_A+E y_A$
- **03-07:F4** — $q=q^*(C)$
- **03-07:F5** — $J_i=\frac{P_i}{\delta}\,\Delta(\text{driving force})$
- **03-07:F7** — $Z=N_{EQ}HETP=NTU\cdot HTU$

### 03-08 — Humidification, Drying, and Evaporation

- **03-08:F1** — $\omega=0.622\frac{P_v}{P-P_v}$
- **03-08:F2** — $\dot m_w=\dot m_a(\omega_2-\omega_1)$
- **03-08:F3** — $X_{db}=\frac{m_w}{m_{dry}},\qquad X_{wb}=\frac{m_w}{m_w+m_{dry}}$
- **03-08:F4** — $dt=\frac{m_{dry}}{A}\frac{-dX}{N(X)}$
- **03-08:F5** — $X^*=X^*(RH,T,\text{material})$
- **03-08:F6** — $\dot m_F x_F=\dot m_P x_P,\qquad \dot m_V=\dot m_F-\dot m_P$

### 03-09 — Particle Characterization, Solids Handling, Size Reduction, and Crystallization

- **03-09:F1** — $F(x)=\int_0^x f(\xi)\,d\xi$
- **03-09:F2** — $d_{32}=\frac{\sum n_i d_i^3}{\sum n_i d_i^2}$
- **03-09:F4** — $\text{reduction ratio}\approx \frac{d_{\rm feed}}{d_{\rm product}}$
- **03-09:F6** — $\tan\theta_r=\frac{h}{r}\quad\text{for a simple conical pile geometry}$

### 03-10 — Reaction Kinetics, Rate Laws, and Arrhenius Behavior

- **03-10:F1** — $-r_A=-\frac1V\frac{dN_A}{dt}$
- **03-10:F2** — $-r_A=kC_A^xC_B^y,\qquad n=x+y$
- **03-10:F5** — $r_{\rm net}=r_f-r_r,\qquad r_{\rm net}=0\ \text{at equilibrium}$
- **03-10:F6** — $r=\frac{V_{\max}C_S}{K_m+C_S}$
- **03-10:F7** — $S_{D/U}=\frac{\text{moles desired product formed}}{\text{moles undesired product formed}}$

### 03-11 — Reactor Design — Batch, CSTR, PFR, Multiple Reactions, and Catalysis

- **03-11:F1** — $t=C_{A0}\int_0^{X_A}\frac{dX_A}{-r_A}$
- **03-11:F3** — $V_{PFR}=F_{A0}\int_0^{X_A}\frac{dX_A}{-r_A}$
- **03-11:F4** — $V_{CSTR}=\frac{F_{A0}X_A}{(-r_A)_{\rm exit}}$
- **03-11:F5** — $\frac{C_{AN}}{C_{A0}}=\left(\frac1{1+k\tau}\right)^N$

### 03-12 — Process Flow Diagrams, P&IDs, Equipment Sizing, Scale-Up, and Cost Estimation

- **03-12:F5** — $C_{\rm current}=C_{\rm old}\frac{I_{\rm current}}{I_{\rm old}}$
- **03-12:F6** — $\frac{C_2}{C_1}=\left(\frac{S_2}{S_1}\right)^n$

### 03-13 — Process Optimization, Advanced Control, and Process Safety

- **03-13:F1** — $\min/\max\ f(\mathbf x)\quad\text{subject to}\quad g_j(\mathbf x)\le0,\ h_k(\mathbf x)=0$
- **03-13:F3** — $\text{ratio setpoint: }\dot m_2=R\,\dot m_1$
- **03-13:F4** — $G_p(s)\approx \frac{Ke^{-\theta s}}{\tau s+1}\quad\text{for a common first-order-plus-dead-time approximation}$

## Layer 3 — Civil

### 03-14 — Civil Materials — Concrete, Asphalt, Aggregates, Wood, and Testing

- **03-14:F1** — $\text{w/c}=\frac{W_w}{W_c}$
- **03-14:F2** — $V_a=100\left(1-\frac{G_{mb}}{G_{mm}}\right)$
- **03-14:F3** — $\%\,\text{passing}=100\frac{W_{\text{passing}}}{W_{\text{total}}}$
- **03-14:F4** — $f_c=\frac{P}{A}$
- **03-14:F5** — $\sigma=\frac{P}{A}$
- **03-14:F6** — $E=\frac{\sigma}{\varepsilon}$

### 03-15 — Surveying, Leveling, Coordinates, Grades, Earthwork, and Volumes

- **03-15:F2** — $\Delta N=L\cos\theta,\qquad \Delta E=L\sin\theta$
- **03-15:F3** — $d=\sqrt{(\Delta E)^2+(\Delta N)^2}$
- **03-15:F4** — $\mathrm{HI}=E_{\text{known}}+\mathrm{BS},\qquad E_{\text{next}}=\mathrm{HI}-\mathrm{FS}$
- **03-15:F5** — $\%G=100\frac{\Delta z}{L}$
- **03-15:F6** — $A=\frac12\left|\sum x_i y_{i+1}-y_i x_{i+1}\right|$

### 03-16 — Hydrology — Rainfall, Infiltration, Runoff, Watersheds, and Hydrographs

- **03-16:F1** — $P+Q_{in}+Q_g-Q_{out}-E-T-I=\Delta S$
- **03-16:F2** — $i=i(T_r,t_d)$
- **03-16:F3** — $P_e=P-I_a-F$
- **03-16:F4** — $Q=CIA$
- **03-16:F6** — $Q(t)=Q_b(t)+Q_d(t)$
- **03-16:F7** — $E_L=P_cE_p$

### 03-17 — Open-Channel Flow — Manning Equation, Specific Energy, and Hydraulic Jumps

- **03-17:F1** — $R=\frac{A}{P_w}$
- **03-17:F2** — $Q=\frac{1.49}{n}AR^{2/3}S^{1/2}\quad\text{(USCS)}$
- **03-17:F3** — $\mathrm{Fr}=\frac{V}{\sqrt{gD_h}}$
- **03-17:F4** — $E=y+\frac{V^2}{2g}$
- **03-17:F5** — $Q=C\,L\,H^{3/2}$

### 03-18 — Pipe Networks, Water Distribution, Pumps, and Collection Systems

- **03-18:F1** — $\frac{p_1}{\gamma}+z_1+\frac{V_1^2}{2g}+h_p=\frac{p_2}{\gamma}+z_2+\frac{V_2^2}{2g}+h_L+h_t$
- **03-18:F2** — $h_L=f\frac{L}{D}\frac{V^2}{2g}+\sum K\frac{V^2}{2g}$
- **03-18:F3** — $h_f\propto \frac{LQ^{1.852}}{C^{1.852}D^{4.87}}$
- **03-18:F4** — $\sum Q_{\text{node}}=0,\qquad \sum h_L{}_{\text{loop}}=0$
- **03-18:F5** — $P_{\text{in}}=\frac{\gamma QH_p}{\eta}$
- **03-18:F6** — $p=\gamma h$
- **03-18:F7** — $Q=VA$

### 03-19 — Flood Control, Stormwater Detention, Routing, and Spillways

- **03-19:F1** — $P_{\text{annual exceedance}}=\frac{1}{T_r}$
- **03-19:F2** — $\frac{dS}{dt}=I-O$
- **03-19:F4** — $\Delta S=\int (I-O)\,dt$
- **03-19:F5** — $Q=C\,L\,H^{3/2}$
- **03-19:F6** — $\text{freeboard}=z_{\text{crest}}-z_{\text{design water surface}}$
- **03-19:F7** — $\text{load}=Q\,C$

### 03-20 — Groundwater Flow, Aquifer Properties, Wells, and Drawdown

- **03-20:F1** — $Q=K\,i\,A$
- **03-20:F2** — $K=\frac{Q}{iAt}$
- **03-20:F3** — $T=Kb$
- **03-20:F4** — $h=z+\frac{p}{\gamma}$
- **03-20:F5** — $s=h_0-h(r)$
- **03-20:F6** — $s_{\text{total}}\approx \sum s_i$
- **03-20:F7** — $i=\frac{\Delta h}{L}$

### 03-21 — Water Quality and Water/Wastewater Treatment for Civil Applications

- **03-21:F1** — $\dot m=QC$
- **03-21:F2** — $\mathrm{pH}=-\log_{10}[H^+]$
- **03-21:F3** — $\bar C=\frac{1}{n}\sum C_i$
- **03-21:F7** — $\text{required removal}=C_{\text{in}}-C_{\text{target}}$

### 03-22 — Structural Determinacy, Stability, Loads, Load Paths, and Influence Lines

- **03-22:F3** — $m+r\stackrel{?}{=}2j$
- **03-22:F4** — $w_{\text{total}}=\sum w_i$
- **03-22:F5** — $P=qA_t$
- **03-22:F6** — $\text{response}=\sum P_i\,y_i$
- **03-22:F7** — $U=\sum \gamma_i Q_i$

### 03-23 — Structural Analysis — Beams, Trusses, Frames, and Deflections

- **03-23:F1** — $\frac{dV}{dx}=-w,\qquad \frac{dM}{dx}=V$
- **03-23:F2** — $\sum F_x=0,\qquad \sum F_y=0$
- **03-23:F3** — $\sum M=0$
- **03-23:F5** — $EI\,v''(x)=M(x)$
- **03-23:F6** — $\delta=\sum \frac{N\,n\,L}{AE}$
- **03-23:F7** — $\delta=\sum \int \frac{M\,m}{EI}\,dx$

### 03-24 — Columns, Buckling, and Elementary Indeterminate Structures

- **03-24:F1** — $P_{cr}=\frac{\pi^2EI}{(KL)^2}$
- **03-24:F2** — $\lambda=\frac{KL}{r},\qquad r=\sqrt{\frac{I}{A}}$
- **03-24:F3** — $\text{column strength}=f\!\left(\frac{KL}{r},F_y,E\right)$
- **03-24:F5** — $\delta_{\text{load}}+R\,f=0$
- **03-24:F6** — $\text{distribution factor}=\frac{K_i}{\sum K}$

### 03-25 — Steel Design — Tension Members, Beams, Columns, and Connections

- **03-25:F1** — $\phi R_n\ge U$
- **03-25:F2** — $\phi T_n=\min(\phi F_yA_g,\ \phi F_uA_e)$
- **03-25:F4** — $\phi M_n\ge M_u$
- **03-25:F5** — $\phi V_n\ge V_u$
- **03-25:F6** — $\phi P_n=\phi F_{cr}A_g$

### 03-26 — Reinforced Concrete Design — Beams and Columns

- **03-26:F1** — $C=T$
- **03-26:F2** — $M_n=A_sf_y\left(d-\frac{a}{2}\right)$
- **03-26:F3** — $\phi M_n\ge M_u$
- **03-26:F4** — $\phi(V_c+V_s)\ge V_u$
- **03-26:F5** — $\text{available development length}\ge l_d$

### 03-27 — Soil Classification, Phase Relations, Compaction, and Effective Stress

- **03-27:F1** — $e=\frac{V_v}{V_s},\quad n=\frac{V_v}{V},\quad w=\frac{W_w}{W_s}$
- **03-27:F2** — $S=\frac{V_w}{V_v}\times100\%$
- **03-27:F4** — $PI=LL-PL$
- **03-27:F6** — $RC=\frac{\gamma_{d,\text{field}}}{\gamma_{d,\max}}\times100\%$
- **03-27:F7** — $\sigma'=\sigma-u$

### 03-28 — Shear Strength, Earth Pressure, Bearing Capacity, Foundations, Settlement, and Slope Stability

- **03-28:F1** — $\tau_f=c'+\sigma'\tan\phi'$
- **03-28:F2** — $\sigma_h=K\,\sigma'_v$
- **03-28:F3** — $FS=\frac{\text{resisting effect}}{\text{driving effect}}$
- **03-28:F4** — $q_{allow}=\frac{q_{ult}}{FS}$
- **03-28:F5** — $q=\frac{P}{A}$
- **03-28:F6** — $S=S_i+S_c+S_s$
- **03-28:F7** — $FS=\frac{\text{available shear resistance}}{\text{mobilized shear demand}}$

### 03-29 — Transportation Engineering — Geometric Design, Pavements, Traffic Flow, and Planning

- **03-29:F1** — $SSD=\text{perception-reaction distance}+\text{braking distance}$
- **03-29:F2** — $\frac{V^2}{gR}\sim e+f$
- **03-29:F3** — $A=|g_2-g_1|$
- **03-29:F4** — $\text{performance}=f(\text{traffic},\text{subgrade},\text{materials},\text{drainage})$
- **03-29:F5** — $q=kv$
- **03-29:F6** — $v/c=\frac{\text{demand flow}}{\text{capacity}}$
- **03-29:F7** — $\text{trips}=r\,(\text{land-use units})$

### 03-30 — Construction Engineering — Administration, Operations, Scheduling, Estimating, and Drawings

- **03-30:F4** — $\text{total float}=LS-ES=LF-EF$
- **03-30:F5** — $CV=EV-AC,\qquad SV=EV-PV$

## Layer 3 — Electrical & Computer

### 03-31 — Semiconductor Materials, Energy Bands, Doping, and p-n Junctions

- **03-31:F1** — $\sigma=q(n\mu_n+p\mu_p),\qquad \rho=\frac{1}{\sigma}$
- **03-31:F2** — $E_g=E_C-E_V$
- **03-31:F4** — $np=n_i^2$
- **03-31:F5** — $J_n=q n\mu_n E+qD_n\frac{dn}{dx}$
- **03-31:F6** — $V_0=\frac{kT}{q}\ln\!\left(\frac{N_A N_D}{n_i^2}\right)$
- **03-31:F7** — $V_T=\frac{kT}{q}\approx 0.026\text{ V at 300 K}$

### 03-32 — Diodes, Rectifiers, Thyristors, and Device Models

- **03-32:F1** — $i_D\approx I_S\!\left(e^{v_D/(\eta V_T)}-1\right)$
- **03-32:F2** — $V_S=i_D R+v_D$
- **03-32:F3** — $V_{\text{avg,full-wave}}=\frac{2V_m}{\pi},\qquad V_{\text{rms,full-wave}}=\frac{V_m}{\sqrt2}$
- **03-32:F4** — $\Delta V\approx \frac{I_L}{f_r C}$
- **03-32:F5** — $I_Z=\frac{V_S-V_Z}{R}-I_L$

### 03-33 — BJT and MOSFET Biasing and Small-Signal Models

- **03-33:F1** — $I_C\approx \beta I_B,\qquad I_E=I_B+I_C$
- **03-33:F2** — $V_{CE}=V_{CC}-I_C R_C$
- **03-33:F3** — $g_m\approx \frac{I_{CQ}}{V_T},\qquad r_\pi\approx \frac{\beta}{g_m}$
- **03-33:F4** — $I_D=I_{DSS}\left(1-\frac{V_{GS}}{V_P}\right)^2$
- **03-33:F5** — $I_D=K(V_{GS}-V_t)^2\quad\text{in saturation under the Handbook model}$
- **03-33:F6** — $g_m=2K(V_{GS}-V_t)$

### 03-34 — Single-Stage, Differential, and Operational Amplifiers

- **03-34:F2** — $A_v\lesssim 1$
- **03-34:F4** — $i_+=i_-=0,\qquad v_+\approx v_-\text{ in linear negative feedback}$
- **03-34:F5** — $A_{v,\text{inv}}=-\frac{R_f}{R_{in}},\qquad A_{v,\text{noninv}}=1+\frac{R_f}{R_g}$
- **03-34:F6** — $\mathrm{CMRR}=\frac{A_d}{A_{cm}},\qquad \mathrm{CMRR}_{dB}=20\log_{10}\!\frac{A_d}{A_{cm}}$

### 03-35 — Power Electronics — Rectifiers, Converters, Inverters, and Switching

- **03-35:F2** — $\overline V_o=\text{rectifier average determined by pulse number and input RMS}$
- **03-35:F3** — $\frac{V_o}{V_{in}}=D$
- **03-35:F5** — $\Delta i_L\approx \frac{V_L\Delta t}{L},\qquad \Delta v_C\approx \frac{I_C\Delta t}{C}$
- **03-35:F7** — $\eta=\frac{P_o}{P_{in}}=\frac{P_o}{P_o+P_{\text{loss}}}$

### 03-36 — Power Systems — Transmission, Distribution, Losses, and Voltage Regulation

- **03-36:F1** — $S=VI^*=P+jQ,\qquad |S|=VI$
- **03-36:F2** — $P=\sqrt3\,V_L I_L\cos\theta$
- **03-36:F3** — $\Delta V\approx I(R+jX),\qquad P_{\text{loss}}=I^2R$
- **03-36:F4** — $Q_c=P(\tan\theta_1-\tan\theta_2)$
- **03-36:F6** — $n_s=\frac{120f}{p},\qquad s=\frac{n_s-n}{n_s}$
- **03-36:F7** — $\%\mathrm{VR}=100\frac{V_{NL}-V_{FL}}{V_{FL}}$

### 03-37 — Electromagnetic Fields — Electrostatics, Magnetostatics, and Maxwell Foundations

- **03-37:F1** — $\mathbf E=\frac{Q}{4\pi\varepsilon r^2}\mathbf a_r,\qquad \mathbf F=Q_t\mathbf E$
- **03-37:F2** — $\oint_S \mathbf D\cdot d\mathbf S=Q_{\text{encl}},\qquad \mathbf D=\varepsilon\mathbf E$
- **03-37:F4** — $\mathbf H=\frac{I}{2\pi r}\mathbf a_\phi,\qquad \mathbf F=I\mathbf L\times\mathbf B$
- **03-37:F5** — $N\Phi=Li,\qquad W_H=\frac12Li^2$
- **03-37:F6** — $v=-N\frac{d\Phi}{dt}$
- **03-37:F7** — $\nabla\times\mathbf E=-\frac{\partial\mathbf B}{\partial t},\qquad \nabla\times\mathbf H=\mathbf J+\frac{\partial\mathbf D}{\partial t}$

### 03-38 — Electromagnetic Waves and Transmission Lines

- **03-38:F1** — $\lambda=\frac{u}{f},\qquad \beta=\frac{2\pi}{\lambda}$
- **03-38:F2** — $Z_0=\sqrt{\frac{L'}{C'}}$
- **03-38:F3** — $\Gamma_L=\frac{Z_L-Z_0}{Z_L+Z_0}$
- **03-38:F5** — $Z_{in}=Z_0\frac{Z_L+jZ_0\tan(\beta l)}{Z_0+jZ_L\tan(\beta l)}$
- **03-38:F6** — $Z_L=Z_0\Rightarrow \Gamma=0$
- **03-38:F7** — $\theta=\beta l=\frac{2\pi l}{\lambda}$

### 03-39 — Signals and Linear Systems — Fourier Methods, Convolution, Filtering, and Transform Models

- **03-39:F1** — $y(t)=x(t)*h(t)=\int_{-\infty}^{\infty}x(\tau)h(t-\tau)\,d\tau$
- **03-39:F2** — $Y(f)=H(f)X(f)$
- **03-39:F3** — $x(t)=\sum_{n=-\infty}^{\infty}X_n e^{j2\pi n f_0t}$
- **03-39:F4** — $H(s)=\frac{Y(s)}{X(s)}$
- **03-39:F5** — $\mathrm{dB}=20\log_{10}|H(j\omega)|$
- **03-39:F6** — $f_s>2W$
- **03-39:F7** — $H(z)=\frac{Y(z)}{X(z)}$

### 03-40 — Communications — AM, FM, PM, PCM, Bandwidth, and Noise

- **03-40:F1** — $s(t)=A(t)\cos(2\pi f_ct+\phi(t))$
- **03-40:F3** — $B_{DSB}=2W,\qquad B_{SSB}=W$
- **03-40:F4** — $\omega_i(t)=\frac{d\theta(t)}{dt}$
- **03-40:F6** — $q=2^n,\qquad R_b\ge 2nW$
- **03-40:F7** — $C=B\log_2(1+S/N)$

### 03-41 — Multiplexing and Digital Communications

- **03-41:F2** — $R_b=R_s\log_2 M$
- **03-41:F4** — $\frac{T(x)+E(x)}{G(x)}\rightarrow 0\text{ remainder for a valid CRC check}$
- **03-41:F6** — $d_{trans}=\frac{L}{R},\qquad d_{prop}=\frac{d}{s}$
- **03-41:F7** — $U_{\text{stop-wait}}\approx \frac{d_{trans}}{D}$

### 03-42 — Digital Logic — Number Systems, Boolean Algebra, Gates, and Minimization

- **03-42:F1** — $\text{two's complement}(M)=2^N-M$
- **03-42:F2** — $C=A\cdot B,\qquad C=A+B,\qquad C=A\oplus B$
- **03-42:F3** — $\overline{AB}=\bar A+\bar B,\qquad \overline{A+B}=\bar A\bar B$
- **03-42:F4** — $F=\sum m(\cdots),\qquad G=\prod M(\cdots)$
- **03-42:F6** — $\mathbf y=f(\mathbf x)$
- **03-42:F7** — $t_{pd,\text{path}}\approx\sum t_{pd,\text{gates}}$

### 03-43 — Sequential Logic — Flip-Flops, Counters, State Machines, Timing, and PLDs

- **03-43:F1** — $Q_{n+1}=f(Q_n,\text{inputs})$
- **03-43:F2** — $\text{state}_{n+1}=\text{shifted state}_n+\text{new input bit}$
- **03-43:F3** — $N_{\text{states}}\le 2^n$
- **03-43:F6** — $T_{clk}\ge t_{CQ}+t_{comb,\max}+t_{setup}$

### 03-44 — Computer Systems — Microprocessors, Memory, and Interfacing

- **03-44:F4** — $C=SAB,\quad b_{\text{offset}}=\log_2 B,\quad b_{\text{index}}=\log_2 S$

### 03-45 — Computer Networks — Routing, Switching, Topologies, and TCP/IP

- **03-45:F5** — $d_{trans}=\frac{L}{R}$
- **03-45:F7** — $d_{total}=d_{proc}+d_{queue}+d_{trans}+d_{prop}$

### 03-46 — Cybersecurity — Security Triad, Firewalls, Detection, Scanning, and Vulnerability Testing

- **03-46:F1** — $\text{security objectives}=\{C,I,A\}$

### 03-47 — Software Engineering — Data Structures, Algorithms, Complexity, Control Flow, and Testing

_No reusable display formula selected; this chapter is primarily conceptual/procedural or its displayed math was example-specific._

## Layer 3 — Environmental

### 03-48 — Population, Demand, Environmental Mass Balances, and Reactor Models

- **03-48:F1** — $P_t=P_0(1+r)^t,\qquad D=P_t\,d_{pc}$
- **03-48:F2** — $\frac{dM}{dt}=\sum \dot M_{in}-\sum \dot M_{out}+rV$
- **03-48:F3** — $\dot m=QC$
- **03-48:F4** — $r=-kC^n$
- **03-48:F5** — $\theta=\frac{V}{Q}\quad\text{for flowing reactors}$
- **03-48:F6** — $C=\frac{C_0}{1+k\theta}\quad\text{for first-order steady decay}$

### 03-49 — Environmental Chemistry — Equilibrium, Kinetics, Partitioning, and pC-pH

- **03-49:F1** — $\text{moles}=\frac{m}{MW}$
- **03-49:F2** — $\mathrm{pH}=-\log_{10}[H^+],\qquad K_a=\frac{[H^+][A^-]}{[HA]}$
- **03-49:F4** — $K_{sp}=\prod a_i^{\nu_i}$
- **03-49:F5** — $pC=-\log_{10}C$
- **03-49:F6** — $K_{ow}=\frac{C_o}{C_w},\qquad K_d=K_{oc}f_{oc}$
- **03-49:F7** — $k_T=k_{20}\theta^{T-20}$

### 03-50 — Health Hazards, Exposure Pathways, Toxicology, and Risk Assessment

- **03-50:F2** — $\mathrm{CDI}=\frac{C\,IR\,EF\,ED}{BW\,AT}$
- **03-50:F3** — $HQ=\frac{\mathrm{CDI}}{\mathrm{RfD}},\qquad HI=\sum HQ_i$
- **03-50:F4** — $\text{Risk}=\mathrm{LADD}\times SF$
- **03-50:F5** — $\text{response}=f(\text{dose})$

### 03-51 — Environmental Hydraulics — Conduits, Open Channels, Pumps, Blowers, and Flow Measurement

- **03-51:F1** — $p=\gamma h$
- **03-51:F2** — $h_f=f\frac{L}{D}\frac{V^2}{2g}$
- **03-51:F3** — $h_f\propto \frac{LQ^{1.852}}{C^{1.852}D^{4.87}}$
- **03-51:F4** — $Q=\frac{1}{n}AR^{2/3}S^{1/2}\quad\text{SI}$
- **03-51:F5** — $P_{in}=\frac{\gamma QH}{\eta}$
- **03-51:F6** — $P\approx \frac{Q\,\Delta p}{\eta}$
- **03-51:F7** — $Q=C\,H^n$

### 03-52 — Surface-Water Hydrology — Runoff, Infiltration, Water Budgets, and Storage

- **03-52:F1** — $P+Q_{in}+Q_g-Q_{out}-ET-I=\Delta S$
- **03-52:F2** — $i=i(T_r,t_d)$
- **03-52:F3** — $Q=CIA$
- **03-52:F5** — $\text{effective rainfall}=P-\text{abstractions}$
- **03-52:F6** — $\Delta S=\int(I-O)\,dt$
- **03-52:F7** — $\text{runoff volume}=\int Q(t)\,dt$

### 03-53 — Routing, Stormwater/Watershed Quality, Streeter–Phelps, and Eutrophication

- **03-53:F1** — $\frac{dS}{dt}=I-O$
- **03-53:F3** — $\dot m=QC$
- **03-53:F4** — $\text{erosion risk}=f(\text{flow shear, soil, slope, cover, duration})$
- **03-53:F5** — $\mathrm{BOD}_t=L_0(1-e^{-kt})$
- **03-53:F6** — $\mathrm{DO}=\mathrm{DO}_{sat}-D$

### 03-54 — Groundwater Flow, Aquifer Tests, Wells, and Drawdown

- **03-54:F1** — $n=\frac{V_v}{V},\qquad T=Kb$
- **03-54:F2** — $Q=KiA,\qquad v_s=\frac{Ki}{n_e}$
- **03-54:F3** — $i=\frac{\Delta h}{L}$
- **03-54:F4** — $s=h_0-h$
- **03-54:F5** — $Q\propto \frac{T(h_1-h_2)}{\ln(r_2/r_1)}$
- **03-54:F6** — $\text{drawdown}=f(Q,T,S,r,t)$
- **03-54:F7** — $\text{specific capacity}=\frac{Q}{s}$

### 03-55 — Soil and Sediment Contamination, Site Characterization, and Groundwater Remediation

- **03-55:F2** — $D=\frac{V}{A R_v}$
- **03-55:F3** — $R=1+\frac{\rho_b K_d}{n_e}$
- **03-55:F6** — $\text{remediation}=f(\text{contaminant, geology, geochemistry, access, time})$

### 03-56 — Water/Wastewater Characteristics, Loading Rates, and Physical Treatment

- **03-56:F2** — $\eta=\frac{C_{in}-C_{out}}{C_{in}}\times100\%$
- **03-56:F4** — $v_o=\frac{Q}{A_s}$
- **03-56:F5** — $\text{loading rate}=\frac{Q}{A}$
- **03-56:F6** — $q=\frac{\text{mass adsorbed}}{\text{mass adsorbent}}$
- **03-56:F7** — $\text{process selection}=f(\text{contaminant size/volatility/phase, target, fouling, energy})$

### 03-57 — Chemical Water/Wastewater Treatment — Coagulation, Softening, Disinfection, Ion Exchange, and Precipitation

- **03-57:F2** — $\mathrm{IAP}>K_{sp}\Rightarrow\text{precipitation favored}$
- **03-57:F4** — $\text{microbial inactivation}=f(C,t,\text{organism},T,\text{water quality})$
- **03-57:F6** — $\dot m_{\text{chem}}=Q\,C_{\text{dose}}$

### 03-58 — Biological Treatment — Activated Sludge, Fixed Film, Lagoons, and Nutrient Removal

- **03-58:F1** — $\mu=\mu_{max}\frac{S}{K_s+S}$
- **03-58:F2** — $Y=\frac{\text{biomass produced}}{\text{substrate consumed}}$
- **03-58:F4** — $\theta_c=\frac{\text{mass of solids in system}}{\text{mass solids wasted per time}}$

### 03-59 — Sludge/Biosolids Handling, Water Reuse, and Residuals Management

- **03-59:F2** — $\dot m_s=Q_s X_s$
- **03-59:F3** — $\%\mathrm{VS\ reduction}=\frac{VS_{in}-VS_{out}}{VS_{in}}\times100\%$
- **03-59:F4** — $\%\text{solids}=\frac{m_{\text{dry solids}}}{m_{\text{wet cake}}}\times100\%$

### 03-60 — Air Quality — Emissions, Dispersion, Indoor Air, and Gas/Particle Control

- **03-60:F1** — $C_{\mathrm{mg/m^3}}\propto \frac{\mathrm{ppb}\,MW\,P}{RT}$
- **03-60:F2** — $\dot m=EF\times \text{activity rate}$
- **03-60:F3** — $\Gamma=\frac{\Delta T}{\Delta z}$
- **03-60:F4** — $C(x,y,z)=\frac{Q}{2\pi u\sigma_y\sigma_z}(\cdots)$
- **03-60:F5** — $V\frac{dC_i}{dt}=Q(C_o-C_i)+S-kVC_i$
- **03-60:F7** — $\eta_{\mathrm{ESP}}=1-e^{-WA/Q}$

### 03-61 — Solid and Hazardous Waste, Landfills, Treatment, and Energy-Environment Impacts

- **03-61:F1** — $\text{generated}=\text{recycled}+\text{processed}+\text{disposed}+\Delta\text{storage}$
- **03-61:F2** — $\text{system cost/environmental impact}=f(\text{collection, transfer, processing, recovery, disposal})$
- **03-61:F3** — $\Delta S_{LC}=P-R-ET-PER_{sw}$
- **03-61:F7** — $\mathrm{CO_2e}=\sum m_i\,GWP_i$

## Layer 3 — Industrial & Systems

### 03-62 — Data, Logic, Databases, and Engineering Analytics

- **03-62:F5** — $z=\\frac{x-\\bar x}{s}\$

### 03-63 — Linear Programming and Optimization

- **03-63:F1** — $\\max Z=cx\\quad\\text{s.t. }Ax\\le b,\\ x\\ge0\$
- **03-63:F2** — $a_ix+s_i=b_i,\\quad s_i\\ge0\$
- **03-63:F4** — $\\max cx,Ax\\le b\\quad\\leftrightarrow\\quad\\min yb,yA\\ge c\$
- **03-63:F6** — $\\min\\sum_i\\sum_j c_{ij}x_{ij}\$

### 03-64 — Queueing Models and Service Systems

- **03-64:F1** — $\\rho=\\frac{\\lambda}{s\\mu}\$
- **03-64:F2** — $L=\\lambda W,\\qquad L_q=\\lambda W_q\$
- **03-64:F3** — $W=\\frac{1}{\\mu-\\lambda},\\quad L=\\frac{\\lambda}{\\mu-\\lambda}\$
- **03-64:F4** — $\\lambda_e=\\lambda(1-P_M)\$
- **03-64:F5** — $L_q=\\frac{\\lambda^2\\sigma_s^2+\\rho^2}{2(1-\\rho)}\$
- **03-64:F6** — $\\rho=\\frac{\\lambda}{s\\mu}<1\$

### 03-65 — Markov Processes, Stochastic Models, and Simulation

- **03-65:F1** — $P_{ij}=P(X_{n+1}=j\\mid X_n=i)\$
- **03-65:F2** — $\\mathbf p_{n+1}=\\mathbf p_nP\$
- **03-65:F3** — $\\boldsymbol\\pi=\\boldsymbol\\pi P,\\quad\\sum_i\\pi_i=1\$
- **03-65:F4** — $Z_n=(aZ_{n-1}+C)\\bmod m,\\quad U_n=Z_n/m\$
- **03-65:F5** — $X=F^{-1}(U)\$
- **03-65:F7** — $\\bar X\\pm t\\frac{s}{\\sqrt n}\$

### 03-66 — Engineering and Project Management — Organization, WBS, PERT/CPM, Earned Value, Agile, and KPIs

- **03-66:F3** — $T=\\sum_{(i,j)\\in CP}d_{ij}\$
- **03-66:F5** — $CV=EV-AC,\\quad SV=EV-PV\$

### 03-67 — Forecasting — Moving Averages, Exponential Smoothing, and Tracking Signals

- **03-67:F1** — $D_t=\\text{level}+\\text{trend}+\\text{seasonality}+\\text{noise}\$
- **03-67:F2** — $\\hat d_t=\\frac1n\\sum_{i=1}^n d_{t-i}\$
- **03-67:F3** — $\\hat d_t=\\alpha d_{t-1}+(1-\\alpha)\\hat d_{t-1}\$
- **03-67:F4** — $MAD=\\frac1n\\sum|e_t|,\\quad MSE=\\frac1n\\sum e_t^2\$
- **03-67:F5** — $TS=\\frac{RSFE}{MAD}\$
- **03-67:F6** — $\\hat D=(\\text{level}+h\\,\\text{trend})\\times\\text{seasonal factor}\$

### 03-68 — Inventory, Aggregate Planning, MRP, Sequencing, and Theory of Constraints

- **03-68:F1** — $Q^*=\\sqrt{\\frac{2AD}{h}}\$
- **03-68:F2** — $Q^*=\\sqrt{\\frac{2AD}{h(1-D/R)}}\$
- **03-68:F3** — $ROP=\\bar d_L+SS\$

### 03-69 — Manufacturing and Service Systems — Processes, Automation, Throughput, and Line Balancing

- **03-69:F1** — $\\text{process}=f(\\text{material, geometry, tolerance, volume, cost})\$
- **03-69:F2** — $WIP=Throughput\\times Flow\\ Time\$
- **03-69:F3** — $Utilization=\\frac{actual\\ output}{defined\\ capacity}\$
- **03-69:F4** — $\\text{automation decision}=f(\\text{technical, economic, safety, flexibility})\$
- **03-69:F5** — $CT=\\frac{OT}{OR},\\quad N_{min}=\\frac{\\sum t_i}{CT}\$
- **03-69:F6** — $\\eta=\\frac{\\sum t_i}{NCT}\$
- **03-69:F7** — $Energy\\ intensity=\\frac{energy\\ input}{useful\\ output}\$

### 03-70 — Lean Systems, Process Improvement, Sustainability, and Value Engineering

- **03-70:F1** — $Lead\\ time=VA\\ time+waiting+transport+rework+other\\ delay\$
- **03-70:F2** — $T_{NVA}=T_{wait}+T_{transport}+T_{motion}+T_{rework}+\\cdots\$
- **03-70:F3** — $Takt=\\frac{available\\ production\\ time}{customer\\ demand}\$
- **03-70:F5** — $V=\\frac{F}{C_{LC}}\$
- **03-70:F6** — $Resource\\ intensity=\\frac{energy/material/water/waste}{useful\\ output}\$

### 03-71 — Facility Location, Layout, Capacity, and Material Handling

- **03-71:F1** — $LD=\\sum_{i,j}F_{ij}D_{ij}\$
- **03-71:F2** — $D_E=\\sqrt{(\\Delta x)^2+(\\Delta y)^2},\\quad D_R=|\\Delta x|+|\\Delta y|\$
- **03-71:F3** — $\\text{layout}=f(\\text{volume, variety, flow, flexibility})\$
- **03-71:F4** — $\\min\\sum_jf_jx_j+\\sum_i\\sum_jc_{ij}y_{ij}\$
- **03-71:F5** — $M_j=\\sum_i\\frac{P_{ij}T_{ij}}{C_{ij}}\$
- **03-71:F6** — $A_j=\\sum_i\\frac{P_{ij}T_{ij}}{C_{ij}}\$
- **03-71:F7** — $\\text{choice}=f(\\text{load, distance, frequency, path, flexibility, safety})\$

### 03-72 — Supply Chains, Transportation Networks, Pooling, and Distribution

- **03-72:F2** — $\\min\\sum_i\\sum_j c_{ij}x_{ij}\$
- **03-72:F3** — $Total\\ cost=facility+transport+inventory+service\\ effects\$
- **03-72:F4** — $\\sigma_{pooled}=\\sqrt{\\sum_i\\sigma_i^2}\\quad\\text{for independent demand}\$
- **03-72:F5** — $Inventory\\ position=on\\ hand+on\\ order-backorders\$
- **03-72:F7** — $Var(orders\\ upstream)>Var(customer\\ demand)\\text{ can occur}\$

### 03-73 — Human Factors, Ergonomics, Work Design, Time Study, and Learning Curves

- **03-73:F1** — $\\text{performance}=f(\\text{perception, cognition, control, feedback, workload})\$
- **03-73:F3** — $Risk=f(force,posture,repetition,duration,recovery)\$
- **03-73:F6** — $ST=NT\\times AF\$
- **03-73:F7** — $T_N=KN^s,\\quad s=\\frac{\\ln(LR)}{\\ln2}\$

### 03-74 — Quality Management, SPC, Process Capability, Sampling, and DOE

- **03-74:F1** — $Quality=plan+assure+control+improve\$
- **03-74:F3** — $L(y)=k(y-T)^2\$
- **03-74:F4** — $UCL=CL+3\\sigma_{stat},\\quad LCL=CL-3\\sigma_{stat}\$
- **03-74:F6** — $P_a=P(\\text{lot accepted}\\mid p)\$
- **03-74:F7** — $E_i=\\bar Y_{i,+}-\\bar Y_{i,-}\$

### 03-75 — Systems Engineering, Reliability, FMEA, Fault Trees, and Life-Cycle Risk

- **03-75:F4** — $RPN=S\\times O\\times D\$
- **03-75:F5** — $P(A\\cap B)=P(A)P(B)\\text{ for independent events}\$
- **03-75:F6** — $R_s=\\prod_iR_i,\\quad R_p=1-\\prod_i(1-R_i)\$
- **03-75:F7** — $A=\\frac{MTBF}{MTBF+MTTR}\$

## Layer 3 — Mechanical

### 03-76 — Mechanism Kinematics and Machine Motion

- **03-76:F1** — $\mathbf v_B=\mathbf v_A+\boldsymbol\omega\times\mathbf r_{B/A}$
- **03-76:F2** — $v_P=\omega r_{P/IC}$
- **03-76:F4** — $\mathbf r_{crank}+\mathbf r_{rod}=\mathbf r_{slider}$
- **03-76:F5** — $\frac{\omega_{out}}{\omega_{in}}=-\frac{N_{in}}{N_{out}}$
- **03-76:F6** — $m_v=\frac{\prod N_{driven}}{\prod N_{driver}}$

### 03-77 — Mechanical Vibrations — Free, Forced, Damped, and Resonant Response

- **03-77:F1** — $\omega_n=\sqrt{\frac{k}{m}},\qquad f_n=\frac{\omega_n}{2\pi}$
- **03-77:F2** — $\zeta=\frac{c}{2\sqrt{km}}$
- **03-77:F3** — $\delta=\ln\!\left(\frac{x_n}{x_{n+1}}\right)$
- **03-77:F4** — $r=\frac{\omega}{\omega_n}$
- **03-77:F5** — $M=\frac{1}{\sqrt{(1-r^2)^2+(2\zeta r)^2}}$

### 03-78 — Failure Theories, Stress Concentrations, Fatigue, Fracture, and Creep

- **03-78:F1** — $\sigma_{max}=K_t\sigma_{nom}$
- **03-78:F2** — $\sigma_{vm}\le \frac{S_y}{n}$
- **03-78:F4** — $\sigma_a=\frac{\sigma_{max}-\sigma_{min}}2,\quad \sigma_m=\frac{\sigma_{max}+\sigma_{min}}2$
- **03-78:F5** — $\text{stress amplitude}=f(N)$
- **03-78:F6** — $K_I=Y\sigma\sqrt{\pi a}$
- **03-78:F7** — $\epsilon=\epsilon(t,\sigma,T)$

### 03-79 — Manufacturing Processes, Material Processing, Heat Treatment, and Selection

- **03-79:F1** — $\text{process choice}=f(\text{alloy, size, geometry, surface, quantity})$
- **03-79:F2** — $V=\pi DN,\qquad \mathrm{MRR}\sim\text{speed}\times\text{feed}\times\text{depth}$
- **03-79:F3** — $VT^n=C$
- **03-79:F5** — $\text{microstructure}=f(\text{composition, temperature, time, cooling path})$
- **03-79:F6** — $\text{specific property}=\frac{\text{property}}{\rho}$
- **03-79:F7** — $\text{selection}=f(\text{loads, environment, process, life, cost, availability})$

### 03-80 — External Flow — Drag, Lift, Boundary Layers, and Dimensional Similarity

- **03-80:F1** — $\mathrm{Re}=\frac{\rho VL}{\mu}=\frac{VL}{\nu}$
- **03-80:F2** — $\tau_w=\mu\left.\frac{\partial u}{\partial y}\right|_w$
- **03-80:F3** — $D=D_{\text{friction}}+D_{\text{pressure}}$
- **03-80:F4** — $F_D=\frac12\rho V^2 C_DA$
- **03-80:F5** — $F_L=\frac12\rho V^2 C_LA$
- **03-80:F6** — $\Pi_i=f(\Pi_1,\Pi_2,\ldots)$

### 03-81 — Compressible Flow — Mach Number, Nozzles, Isentropic Flow, and Normal Shocks

- **03-81:F1** — $M=\frac{V}{a},\qquad a=\sqrt{\gamma RT}$
- **03-81:F2** — $\frac{T_0}{T}=1+\frac{\gamma-1}{2}M^2$
- **03-81:F3** — $M=1\text{ at the minimum-area throat of an ideal choked nozzle}$
- **03-81:F4** — $\dot m=\rho AV$

### 03-82 — Combustion and Combustion Products

- **03-82:F1** — $\mathrm{C_xH_y}+\left(x+\frac y4\right)\mathrm{O_2}\rightarrow x\mathrm{CO_2}+\frac y2\mathrm{H_2O}$
- **03-82:F2** — $\%\text{excess air}=100\frac{A_{actual}-A_{theoretical}}{A_{theoretical}}$
- **03-82:F5** — $\sum H_{reactants}=\sum H_{products}$

### 03-83 — HVAC Processes, Loads, Psychrometrics, and Equipment Performance

- **03-83:F1** — $\omega=0.622\frac{P_v}{P-P_v}$
- **03-83:F2** — $\dot Q_s=\dot m_a c_p(T_2-T_1)$
- **03-83:F3** — $\dot Q=\dot m_a(h_1-h_2)$
- **03-83:F4** — $\dot m_w=\dot m_a(\omega_2-\omega_1)$
- **03-83:F5** — $\dot m_1 h_1+\dot m_2 h_2=(\dot m_1+\dot m_2)h_3$
- **03-83:F6** — $\dot Q_{load}=\dot Q_{envelope}+\dot Q_{solar}+\dot Q_{people}+\dot Q_{equipment}+\dot Q_{vent}$
- **03-83:F7** — $\mathrm{COP_R}=\frac{Q_L}{W_{in}},\qquad \mathrm{COP_{HP}}=\frac{Q_H}{W_{in}}$

### 03-84 — Mechanical Springs

- **03-84:F1** — $\tau=K_s\frac{8FD}{\pi d^3}$
- **03-84:F2** — $k=\frac{Gd^4}{8D^3N}$
- **03-84:F3** — $\frac1{k_{eq}}=\sum\frac1{k_i},\qquad k_{eq}=\sum k_i$
- **03-84:F5** — $S_{ut}=\frac{A}{d^m}$
- **03-84:F6** — $\sigma=K_i\frac{32Fr}{\pi d^3},\qquad Fr=k\theta$
- **03-84:F7** — $U=\frac12kx^2$

### 03-85 — Pressure Vessels and Piping

- **03-85:F1** — $\sigma_h=\frac{pr}{t}$
- **03-85:F2** — $\sigma_l=\frac{pr}{2t}$
- **03-85:F3** — $\sigma=\frac{pr}{2t}$
- **03-85:F4** — $t\gtrsim\frac{pr}{S_{allow}}\text{ in a simplified thin-wall screen}$
- **03-85:F5** — $\Delta L=\alpha L\Delta T,\qquad \sigma=E\alpha\Delta T\text{ if fully restrained elastically}$

### 03-86 — Bearings and Lubrication

- **03-86:F1** — $\text{bearing choice}=f(\text{radial load, thrust, speed, life, stiffness, environment})$
- **03-86:F2** — $C=P L^{1/a}$
- **03-86:F3** — $P_{eq}=XVF_r+YF_a$
- **03-86:F4** — $L_{rev}=60n\,L_h$

### 03-87 — Power Screws, Threaded Fasteners, and Mechanical Joints

- **03-87:F1** — $T_R=\frac{Fd_m}{2}\frac{\pi\mu d_m+l}{\pi d_m-\mu l}+\frac{F\mu_cd_c}{2}$
- **03-87:F2** — $\eta=\frac{Fl}{2\pi T_R}$
- **03-87:F3** — $C=\frac{k_b}{k_b+k_m}$
- **03-87:F4** — $F_b=CP+F_i,\qquad F_m=(1-C)P-F_i$
- **03-87:F5** — $n_s=\frac{F_i}{P(1-C)}$
- **03-87:F6** — $\tau=\frac FA,\qquad \sigma_{bearing}=\frac{F}{dt}$
- **03-87:F7** — $F_{2i}=\frac{Mr_i}{\sum r_i^2}$

### 03-88 — Shafts, Keys, Couplings, Gears, Belts, Chains, and Power Transmission

- **03-88:F1** — $\tau_{max}\sim \frac{16T}{\pi d^3},\qquad \sigma_b\sim\frac{32M}{\pi d^3}$
- **03-88:F2** — $d^3\propto n\sqrt{\left(\frac{K_fM_a}{S_e}+\frac{M_m}{S_y}\right)^2+\left(\frac{K_{fs}T_a}{S_e}+\frac{T_m}{S_y}\right)^2}$
- **03-88:F4** — $p_c=\frac{\pi d}{N},\qquad m=\frac dN$
- **03-88:F5** — $W_r=W_t\tan\phi,\qquad T=\frac{W_td}{2}$
- **03-88:F6** — $W_t=F Y\frac{1}{P}\sigma_{allow}\text{ in equivalent form}$

### 03-89 — Hydraulic, Pneumatic, and Electromechanical Components

- **03-89:F1** — $F=pA$
- **03-89:F2** — $P_h=pQ,\qquad v=\frac QA$
- **03-89:F5** — $P=T\omega$

### 03-90 — Fits, Tolerances, GD&T, Manufacturability, Quality, and Reliability

- **03-90:F1** — $\Delta D=D_{max}-D_{min}$
- **03-90:F2** — $\text{clearance}=D_{hole}-d_{shaft}$
- **03-90:F6** — $\Delta_{worst}\approx\sum |\Delta_i|$

## Layer 3 — Other Disciplines

### 03-91 — Other Disciplines Mechanics and Materials Integration

- **03-91:F5** — $\text{response}=f(E,G,\nu,S_y,S_u,K_{IC},\alpha,\rho,\text{environment})$
- **03-91:F6** — $P_{cr}=\frac{\pi^2EI}{(KL)^2}$
- **03-91:F7** — $[\mathrm{LHS}]=[\mathrm{RHS}],\qquad \mathbf R_F=\sum\mathbf F-m\mathbf a,\qquad R_M=\sum M_G-I_G\alpha$

### 03-92 — Other Disciplines Thermal, Fluid, Heat-Transfer, and HVAC Integration

- **03-92:F1** — $\frac{dE_{CV}}{dt}=\dot Q-\dot W+\sum\dot m\left(h+\frac{V^2}{2}+gz\right)_{in}-\sum\dot m\left(h+\frac{V^2}{2}+gz\right)_{out}$
- **03-92:F2** — $\mathrm{Re}=\frac{\rho VD}{\mu}$
- **03-92:F3** — $\frac{p_1}{\gamma}+z_1+\frac{V_1^2}{2g}+h_p=\frac{p_2}{\gamma}+z_2+\frac{V_2^2}{2g}+h_L$
- **03-92:F4** — $\dot Q=hA(T_s-T_\infty),\qquad \mathrm{Nu}=f(\mathrm{Re},\mathrm{Pr},\text{geometry})$
- **03-92:F5** — $\dot Q=\frac{\Delta T}{R_{th}},\qquad R_{conv}=\frac1{hA}$
- **03-92:F6** — $\eta_{th}=\frac{W_{net}}{Q_{in}},\qquad \mathrm{COP_R}=\frac{Q_L}{W_{in}}$
- **03-92:F7** — $\sum \dot m_{da,in}=\sum \dot m_{da,out},\qquad \sum \dot m_{da}\omega_{in}+\dot m_{w,in}=\sum \dot m_{da}\omega_{out}+\dot m_{w,out},\qquad \dot Q-\dot W+\sum \dot m h_{in}-\sum \dot m h_{out}=0$

### 03-93 — Other Disciplines Electrical, Instrumentation, and Control Integration

- **03-93:F1** — $V=IR,\qquad P=VI$
- **03-93:F2** — $\sum V=0,\qquad \sum I=0,\qquad Z=R+jX$
- **03-93:F3** — $P=\sqrt3\,V_LI_L\cos\phi$
- **03-93:F5** — $f_s>2f_{max},\qquad \Delta=\frac{V_{FS}}{2^N}$
- **03-93:F6** — $T(s)=\frac{G(s)}{1+G(s)H(s)}$

### 03-94 — Other Disciplines Safety, Economics, and Cross-Domain Engineering Decisions

- **03-94:F2** — $\text{dose/exposure}=f(C,t,\text{route},\text{frequency})$
- **03-94:F4** — $PW=\sum_t\frac{CF_t}{(1+i)^t}$
- **03-94:F5** — $E[X]=\sum p_ix_i$

### 03-95 — Other Disciplines Mixed FE Synthesis and Handbook Strategy

- **03-95:F4** — $\rho_x=\frac{x_{calc}}{x_{est}},\qquad \lim_{u\to u_0}x(u)=x_0$
- **03-95:F5** — $y=f(x),\qquad z=g(y)\quad\Rightarrow\quad z=g\!\left(f(x)\right)$
