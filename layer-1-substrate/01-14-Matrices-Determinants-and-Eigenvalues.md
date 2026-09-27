---
chapter: "01-14"
title: "Matrices, Determinants, and Eigenvalues"
layer: 1
tier: B
template: technical
ledger_ids: [MATH-1B-014-01, MATH-1B-014-02, MATH-1B-014-03, MATH-1B-014-04]
routes: [chemical, civil, electrical-computer, environmental, industrial-systems, mechanical, other-disciplines]
status: drafted
---

# Chapter 01-14: Matrices, Determinants, and Eigenvalues

> *"A matrix is a machine for turning one vector into another. Feed it a
> displacement, get back a force. Feed it a set of currents, get back a set
> of voltages. Most of the time the output points somewhere new. But every
> such machine has a few special directions where the output points exactly
> where the input did — only longer or shorter. Those directions are the
> eigenvectors, and the stretch factors are the eigenvalues. Find them and
> you have found how the system wants to behave on its own."*

---

## Before You Start

**Prerequisites:** [01-08 Systems of Linear Equations](01-08-systems-linear-equations.md) · [01-13 Vectors and Vector Operations](01-13-vectors-vector-operations.md)

**Skip if:** You pass the Tier 1B test-out quiz. Verify you can multiply
non-square matrices, expand a 3×3 determinant by cofactors, invert a 2×2,
and find eigenvalues of a 2×2 before skipping. Eigenvalues are the most
commonly rusty item in this chapter.

**Time:** ~65 min read · ~25 min review questions · ~65 min practice problems

---

## On the Board Today

Apprentice, you already know most of what a matrix does. In Chapter 01-08
you solved linear systems by Gaussian elimination and Cramer's rule, and you
wrote the coefficients in an augmented array without calling it a matrix. In
Chapter 01-13 you expanded a 3×3 determinant to compute a cross product.
This chapter names those tools, generalizes them, and adds the one genuinely
new idea: eigenvalues.

Here is the frame that makes matrices intuitive rather than mechanical.

A matrix is a **linear transformation**. Multiply a vector by a matrix and
you get a new vector. The matrix is the rule for how one set of quantities
maps to another. In structural analysis, the stiffness matrix maps
displacements to forces. In circuit analysis, the admittance matrix maps
voltages to currents. In a mass balance, the coefficient matrix maps stream
flow rates to component flow rates.

Solving $A\mathbf{x} = \mathbf{b}$ means asking: what input $\mathbf{x}$
produces the output $\mathbf{b}$? That's what you were doing in Chapter 01-08.
The matrix inverse $A^{-1}$ is the machine that runs the transformation
backward.

The **determinant** answers a single yes-or-no question with one number: is
this transformation reversible? If the determinant is zero, the matrix
collapses information — different inputs map to the same output — and no
inverse exists. In engineering terms, a zero determinant on a stiffness
matrix means the structure is unstable. A zero determinant on a system of
equilibrium equations means the structure is statically indeterminate or
improperly constrained. That single number carries real physical meaning.

**Eigenvalues** are the new idea. For most vectors, multiplying by $A$
changes both the length and the direction. But special vectors exist for
which $A$ only changes the length — the direction is preserved. Those are
eigenvectors, and the scaling factors are eigenvalues. They are how you find
natural frequencies of a vibrating structure, principal stresses in a loaded
member, buckling loads of a column, and stability of a control system.

We build all of it here.

---

## Learning Objectives

By the end of this chapter, you will be able to:

* 14.1 State the dimensions of a matrix and identify square, diagonal,
  identity, symmetric, and triangular matrices
* 14.2 Add, subtract, and scalar-multiply matrices
* 14.3 Determine whether a matrix product is defined and compute it
* 14.4 Compute the transpose and recognize symmetric matrices
* 14.5 Evaluate 2×2 and 3×3 determinants and apply determinant properties
* 14.6 Compute the inverse of a 2×2 matrix and recognize when no inverse
  exists
* 14.7 Write a linear system in matrix form $A\mathbf{x} = \mathbf{b}$ and
  solve it by matrix inversion or Cramer's rule
* 14.8 Define rank and singularity and connect them to system solvability
* 14.9 Find eigenvalues from the characteristic equation
* 14.10 Find eigenvectors corresponding to given eigenvalues
* 14.11 Verify eigenvalues using the trace and determinant checks

---

## Notation Used Here

| Symbol | Meaning in this chapter | Notes |
|---|---|---|
| $A$, $B$, $M$ | matrices | capital letters, no decoration |
| $a_{ij}$ | element of $A$ in row $i$, column $j$ | row index first, always |
| $m \times n$ | dimensions: $m$ rows, $n$ columns | rows first, always |
| $A^T$ | transpose of $A$ | rows and columns exchanged |
| $A^{-1}$ | inverse of $A$ | exists only if $\det A \ne 0$ |
| $\det A$ or $\lvert A \rvert$ | determinant of $A$ | scalar; square matrices only |
| $I$ | identity matrix | 1's on the diagonal, 0's elsewhere |
| $\mathbf{x}$, $\mathbf{b}$ | column vectors | $n \times 1$ matrices |
| $\lambda$ | eigenvalue | scalar |
| $\mathbf{v}$ | eigenvector | column vector |
| $\text{tr}(A)$ | trace of $A$ | sum of diagonal elements |
| $M_{ij}$ | minor of element $a_{ij}$ | determinant with row $i$, col $j$ deleted |
| $C_{ij}$ | cofactor of element $a_{ij}$ | $(-1)^{i+j}M_{ij}$ |

> ---
> **Mentor's Margin**
>
> Rows before columns. Always. A $3 \times 4$ matrix has three rows and four
> columns. Element $a_{23}$ is in row 2, column 3. This convention never
> varies, and it is the source of a large fraction of matrix errors when
> people work quickly. Say it out loud the first ten times: rows, then
> columns.
>
> ---

---

## 14.1 What a Matrix Is

A **matrix** is a rectangular array of numbers arranged in rows and columns.

$$A = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \end{bmatrix}$$

This is a $2 \times 3$ matrix: two rows, three columns. Its **dimensions**
or **order** are stated rows-first.

The element $a_{ij}$ sits in row $i$, column $j$.

![FIG-01-14-001: Matrix anatomy diagram showing a 3×4 matrix with rows numbered 1-3 on the left, columns numbered 1-4 across the top, and the element a_23 highlighted with arrows pointing to its row and column indices](../figures/FIG-01-14-001-matrix-anatomy.png)

### Special matrices you must recognize

| Type | Definition | Example |
|---|---|---|
| **Square** | equal rows and columns, $n \times n$ | $\begin{bmatrix} 2 & 1 \\ 4 & 3 \end{bmatrix}$ |
| **Column vector** | $n \times 1$ | $\begin{bmatrix} 3 \\ -1 \\ 5 \end{bmatrix}$ |
| **Row vector** | $1 \times n$ | $\begin{bmatrix} 3 & -1 & 5 \end{bmatrix}$ |
| **Diagonal** | square; all off-diagonal elements zero | $\begin{bmatrix} 5 & 0 \\ 0 & -2 \end{bmatrix}$ |
| **Identity** $I$ | diagonal with all 1's | $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$ |
| **Zero** | all elements zero | $\begin{bmatrix} 0 & 0 \\ 0 & 0 \end{bmatrix}$ |
| **Upper triangular** | all elements below diagonal zero | $\begin{bmatrix} 2 & 7 \\ 0 & 3 \end{bmatrix}$ |
| **Lower triangular** | all elements above diagonal zero | $\begin{bmatrix} 2 & 0 \\ 7 & 3 \end{bmatrix}$ |
| **Symmetric** | square; $A^T = A$, i.e. $a_{ij} = a_{ji}$ | $\begin{bmatrix} 2 & 5 \\ 5 & 3 \end{bmatrix}$ |

The **identity matrix** $I$ is the multiplicative identity: $AI = IA = A$
for any square $A$ of matching size. It is the matrix analogue of the number 1.

The **trace** of a square matrix is the sum of its diagonal elements:

$$\text{tr}(A) = a_{11} + a_{22} + \cdots + a_{nn}$$

> ---
> **Mentor's Margin**
>
> Symmetric matrices show up constantly in engineering, and not by accident.
> Stiffness matrices in structural analysis are symmetric because of a
> reciprocity principle: the force at point 1 caused by a unit displacement
> at point 2 equals the force at point 2 caused by a unit displacement at
> point 1. Stress and strain tensors are symmetric for the same kind of
> reason. If you build a stiffness matrix and it comes out non-symmetric,
> you have made an algebra error. That symmetry is a free error check.
>
> ---

---

## 14.2 Addition, Subtraction, and Scalar Multiplication

These operate **element by element**. Both matrices must have identical
dimensions.

$$A \pm B = \begin{bmatrix} a_{11} \pm b_{11} & a_{12} \pm b_{12} \\ a_{21} \pm b_{21} & a_{22} \pm b_{22} \end{bmatrix}$$

$$cA = \begin{bmatrix} ca_{11} & ca_{12} \\ ca_{21} & ca_{22} \end{bmatrix}$$

If the dimensions differ, the sum is **undefined**. Not zero — undefined.
There is no operation to perform.

Addition is commutative and associative, exactly as with numbers:

$$A + B = B + A \qquad (A+B)+C = A+(B+C)$$

---

## 14.3 Matrix Multiplication

This is the operation that does not behave like ordinary arithmetic, and it
is where matrices earn their usefulness.

### When is the product defined?

For $AB$ to exist, the number of **columns of $A$** must equal the number of
**rows of $B$**.

$$\underbrace{A}_{m \times n} \; \underbrace{B}_{n \times p} = \underbrace{AB}_{m \times p}$$

The inner dimensions must match and they cancel. The outer dimensions
survive as the dimensions of the product.

$$(3 \times 4)(4 \times 2) = (3 \times 2) \quad \checkmark$$

$$(3 \times 4)(2 \times 4) = \text{undefined} \quad (4 \ne 2)$$

### How to compute it

Element $(i,j)$ of the product is the **dot product** of row $i$ of $A$ with
column $j$ of $B$:

$$\boxed{(AB)_{ij} = \sum_{k=1}^{n} a_{ik}\,b_{kj}}$$

That is exactly the dot product from Chapter 01-13. Matrix multiplication is
an organized collection of dot products.

![FIG-01-14-002: Matrix multiplication diagram showing row i of matrix A highlighted horizontally and column j of matrix B highlighted vertically, with arrows converging on element (i,j) of the product matrix AB, and the dot product summation shown alongside](../figures/FIG-01-14-002-matrix-multiplication.png)

### Matrix multiplication is not commutative

$$AB \ne BA \quad \text{in general}$$

Sometimes $BA$ isn't even defined when $AB$ is. Even when both exist and have
the same dimensions, the results usually differ. Order matters.

What *does* hold:

$$A(BC) = (AB)C \quad \text{(associative)}$$

$$A(B+C) = AB + AC \quad \text{(distributive)}$$

$$AI = IA = A$$

> ---
> **Mentor's Margin**
>
> The non-commutativity is not a mathematical inconvenience — it is physically
> meaningful. Matrices represent transformations, and transformations don't
> generally commute. Rotate an object 90° about the $x$-axis then 90° about
> the $y$-axis, and you land somewhere different than if you do the $y$
> rotation first. Try it with a book. The matrices representing those two
> rotations don't commute because the physical operations don't commute.
>
> ---

### Worked Example 1 — Matrix Multiplication

**Given.**

$$A = \begin{bmatrix} 2 & -1 & 3 \\ 0 & 4 & 1 \end{bmatrix} \qquad B = \begin{bmatrix} 1 & 2 \\ -3 & 0 \\ 5 & -1 \end{bmatrix}$$

**(a)** Is $AB$ defined? What are its dimensions?
**(b)** Compute $AB$.
**(c)** Is $BA$ defined? What are its dimensions?

**Solution.**

**(a)** $A$ is $2 \times 3$, $B$ is $3 \times 2$. Inner dimensions: $3 = 3$ ✓

$AB$ is defined and is $2 \times 2$.

**(b)** Each element is a row-column dot product.

Row 1 of $A$ is $\begin{bmatrix} 2 & -1 & 3\end{bmatrix}$;
row 2 is $\begin{bmatrix} 0 & 4 & 1\end{bmatrix}$.

Column 1 of $B$ is $\begin{bmatrix} 1 \\ -3 \\ 5 \end{bmatrix}$;
column 2 is $\begin{bmatrix} 2 \\ 0 \\ -1 \end{bmatrix}$.

$(AB)_{11} = (2)(1) + (-1)(-3) + (3)(5) = 2 + 3 + 15 = 20$

$(AB)_{12} = (2)(2) + (-1)(0) + (3)(-1) = 4 + 0 - 3 = 1$

$(AB)_{21} = (0)(1) + (4)(-3) + (1)(5) = 0 - 12 + 5 = -7$

$(AB)_{22} = (0)(2) + (4)(0) + (1)(-1) = 0 + 0 - 1 = -1$

$$\boxed{AB = \begin{bmatrix} 20 & 1 \\ -7 & -1 \end{bmatrix}}$$

**(c)** $B$ is $3 \times 2$, $A$ is $2 \times 3$. Inner: $2 = 2$ ✓

$BA$ is defined and is $\boxed{3 \times 3}$ — a completely different size
from $AB$. This is the clearest possible demonstration that $AB \ne BA$.

---

## 14.4 The Transpose

The **transpose** $A^T$ exchanges rows and columns:

$$(A^T)_{ij} = a_{ji}$$

An $m \times n$ matrix transposes to an $n \times m$ matrix.

$$A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{bmatrix} \implies A^T = \begin{bmatrix} 1 & 3 & 5 \\ 2 & 4 & 6 \end{bmatrix}$$

### Transpose properties

$$(A^T)^T = A$$

$$(A+B)^T = A^T + B^T$$

$$\boxed{(AB)^T = B^T A^T \quad \text{— note the order reversal}}$$

$$(cA)^T = cA^T$$

A matrix is **symmetric** if $A^T = A$. Only square matrices can be
symmetric.

> ---
> **Mentor's Margin**
>
> The order reversal in $(AB)^T = B^T A^T$ is the property people get wrong.
> It is not $A^T B^T$. Check it with dimensions: if $A$ is $2\times 3$ and
> $B$ is $3 \times 4$, then $AB$ is $2\times 4$ and $(AB)^T$ is $4 \times 2$.
> Now $B^T$ is $4\times 3$ and $A^T$ is $3\times 2$, so $B^T A^T$ is
> $4 \times 2$ ✓. But $A^T B^T$ would be $(3\times 2)(4 \times 3)$ —
> undefined. The dimensions themselves force the order reversal.
>
> ---

---

## 14.5 Determinants

The **determinant** is a single scalar computed from a square matrix. It
answers: is this transformation invertible, and by how much does it scale
areas or volumes?

### 2×2 determinant

$$\boxed{\det\begin{bmatrix} a & b \\ c & d \end{bmatrix} = ad - bc}$$

Main diagonal product minus off-diagonal product.

### 3×3 determinant by cofactor expansion

The **minor** $M_{ij}$ is the determinant of the $2 \times 2$ matrix
remaining after deleting row $i$ and column $j$.

The **cofactor** applies a sign: $C_{ij} = (-1)^{i+j}M_{ij}$.

The signs form a checkerboard:

$$\begin{bmatrix} + & - & + \\ - & + & - \\ + & - & + \end{bmatrix}$$

Expanding along the first row:

$$\det A = a_{11}M_{11} - a_{12}M_{12} + a_{13}M_{13}$$

![FIG-01-14-003: Cofactor expansion diagram for a 3×3 determinant showing the checkerboard sign pattern, with the first row highlighted and each element's 2×2 minor extracted and shown separately to the right with its sign](../figures/FIG-01-14-003-cofactor-expansion.png)

You may expand along **any** row or column. The answer is identical. Choose
the row or column with the most zeros — every zero element kills a full
$2\times 2$ minor computation.

> ---
> **Mentor's Margin**
>
> Always look for the zeros before you start expanding. A 3×3 determinant
> expanded along a row containing two zeros takes one minor instead of three.
> That is a two-thirds reduction in work and a two-thirds reduction in
> arithmetic error opportunities. Scan the matrix first. Pick the sparsest
> line. This habit alone will save you minutes on exam day.
>
> ---

### Determinant properties

| Property | Statement |
|---|---|
| Transpose | $\det A^T = \det A$ |
| Row/column swap | swapping two rows (or columns) reverses the sign |
| Scalar multiple of a row | multiplying one row by $c$ multiplies $\det$ by $c$ |
| Scalar multiple of the matrix | $\det(cA) = c^n \det A$ for $n \times n$ |
| Duplicate row/column | if two rows (or columns) are identical, $\det A = 0$ |
| Proportional row/column | if one row is a multiple of another, $\det A = 0$ |
| Zero row/column | if any row or column is all zeros, $\det A = 0$ |
| Row addition | adding a multiple of one row to another leaves $\det$ unchanged |
| Product | $\det(AB) = (\det A)(\det B)$ |
| Triangular matrix | $\det$ = product of the diagonal elements |

The proportional-row property is the fast singularity check. Before grinding
through a cofactor expansion, look for a row that is a scalar multiple of
another. If you find one, the determinant is zero and you are done.

### Worked Example 2 — 3×3 Determinant, Two Ways

**Given.**

$$A = \begin{bmatrix} 2 & -1 & 3 \\ 1 & 4 & -2 \\ 3 & 0 & 1 \end{bmatrix}$$

**Find.** $\det A$, computed twice as a check.

**Solution — expansion along row 1.**

Signs for row 1: $+, -, +$

$$\det A = 2\begin{vmatrix} 4 & -2 \\ 0 & 1\end{vmatrix} - (-1)\begin{vmatrix} 1 & -2 \\ 3 & 1\end{vmatrix} + 3\begin{vmatrix} 1 & 4 \\ 3 & 0\end{vmatrix}$$

$$= 2\big[(4)(1) - (-2)(0)\big] + 1\big[(1)(1) - (-2)(3)\big] + 3\big[(1)(0) - (4)(3)\big]$$

$$= 2(4) + 1(1 + 6) + 3(0 - 12)$$

$$= 8 + 7 - 36 = \boxed{-21}$$

**Check — expansion along row 3** (contains a zero, so less work).

Signs for row 3: $+, -, +$

$$\det A = 3\begin{vmatrix} -1 & 3 \\ 4 & -2\end{vmatrix} - 0 + 1\begin{vmatrix} 2 & -1 \\ 1 & 4\end{vmatrix}$$

$$= 3\big[(-1)(-2) - (3)(4)\big] + 1\big[(2)(4) - (-1)(1)\big]$$

$$= 3(2 - 12) + (8 + 1)$$

$$= 3(-10) + 9 = -30 + 9 = -21 \;\checkmark$$

Both expansions agree. Note that the row-3 expansion required two minors
instead of three.

### Worked Example 3 — Detecting a Singular Matrix

**Given.**

$$A = \begin{bmatrix} 1 & 2 & 3 \\ 2 & 4 & 6 \\ 1 & 0 & 1 \end{bmatrix}$$

**Find.** $\det A$.

**Fast approach.** Inspect the rows before computing. Row 2 is exactly
$2 \times$ Row 1:

$$\begin{bmatrix} 2 & 4 & 6\end{bmatrix} = 2\begin{bmatrix} 1 & 2 & 3\end{bmatrix}$$

By the proportional-row property, $\det A = \boxed{0}$. The matrix is
singular.

**Verification by expansion along row 1.**

$$\det A = 1\begin{vmatrix} 4 & 6 \\ 0 & 1\end{vmatrix} - 2\begin{vmatrix} 2 & 6 \\ 1 & 1\end{vmatrix} + 3\begin{vmatrix} 2 & 4 \\ 1 & 0\end{vmatrix}$$

$$= 1(4 - 0) - 2(2 - 6) + 3(0 - 4)$$

$$= 4 - 2(-4) - 12 = 4 + 8 - 12 = 0 \;\checkmark$$

The inspection took five seconds; the expansion took a minute. Learn to look
first.

---

## 14.6 The Matrix Inverse

The **inverse** $A^{-1}$ satisfies:

$$A A^{-1} = A^{-1} A = I$$

It exists only if $A$ is square and $\det A \ne 0$.

### 2×2 inverse — memorize this

$$\boxed{A = \begin{bmatrix} a & b \\ c & d\end{bmatrix} \implies A^{-1} = \frac{1}{ad-bc}\begin{bmatrix} d & -b \\ -c & a\end{bmatrix}}$$

The pattern: swap the diagonal elements, negate the off-diagonal elements,
divide by the determinant.

If $ad - bc = 0$ the division is impossible and no inverse exists.

### Singular and nonsingular

| Term | Meaning |
|---|---|
| **Nonsingular** (invertible) | $\det A \ne 0$; $A^{-1}$ exists |
| **Singular** (non-invertible) | $\det A = 0$; $A^{-1}$ does not exist |

Geometrically: a nonsingular $2\times 2$ matrix maps the unit square to a
parallelogram of area $\lvert \det A\rvert$. A singular matrix collapses the
square onto a line — area zero — and that collapse cannot be undone. The
information about the second dimension is gone.

![FIG-01-14-004: Two side-by-side geometric transformations of a unit square. Left: nonsingular matrix maps the square to a parallelogram with area |det A| labeled, reversible arrow shown. Right: singular matrix collapses the square onto a line segment, area zero, with a crossed-out reverse arrow indicating irreversibility.](../figures/FIG-01-14-004-singular-vs-nonsingular.png)

### Inverse properties

$$(A^{-1})^{-1} = A \qquad (AB)^{-1} = B^{-1}A^{-1} \qquad (A^T)^{-1} = (A^{-1})^T$$

$$\det(A^{-1}) = \frac{1}{\det A}$$

Note the order reversal in $(AB)^{-1} = B^{-1}A^{-1}$, same as the transpose.

### Worked Example 4 — 2×2 Inverse with Verification

**Given.** $A = \begin{bmatrix} 3 & 5 \\ 1 & 2\end{bmatrix}$

**Find.** $A^{-1}$ and verify.

**Solution.**

$$\det A = (3)(2) - (5)(1) = 6 - 5 = 1$$

Nonzero, so the inverse exists.

$$A^{-1} = \frac{1}{1}\begin{bmatrix} 2 & -5 \\ -1 & 3\end{bmatrix} = \boxed{\begin{bmatrix} 2 & -5 \\ -1 & 3\end{bmatrix}}$$

**Verify** by computing $AA^{-1}$:

$$\begin{bmatrix} 3 & 5 \\ 1 & 2\end{bmatrix}\begin{bmatrix} 2 & -5 \\ -1 & 3\end{bmatrix}$$

$(1,1)$: $(3)(2) + (5)(-1) = 6 - 5 = 1$

$(1,2)$: $(3)(-5) + (5)(3) = -15 + 15 = 0$

$(2,1)$: $(1)(2) + (2)(-1) = 2 - 2 = 0$

$(2,2)$: $(1)(-5) + (2)(3) = -5 + 6 = 1$

$$AA^{-1} = \begin{bmatrix} 1 & 0 \\ 0 & 1\end{bmatrix} = I \;\checkmark$$

> ---
> **Mentor's Margin**
>
> Always verify a computed inverse by multiplying it back. It costs about
> twenty seconds for a 2×2 and it catches sign errors in the off-diagonal
> negation, which is the single most common mistake here. If the product
> isn't exactly $I$, you have an error — and you know it before it propagates
> into the rest of your solution.
>
> ---

---

## 14.7 Matrix Form of a Linear System

Any linear system can be written as a single matrix equation. Take the
system:

$$\begin{aligned} 2x + 3y &= 8 \\ x - y &= -1 \end{aligned}$$

In matrix form:

$$\underbrace{\begin{bmatrix} 2 & 3 \\ 1 & -1\end{bmatrix}}_{A}\underbrace{\begin{bmatrix} x \\ y\end{bmatrix}}_{\mathbf{x}} = \underbrace{\begin{bmatrix} 8 \\ -1\end{bmatrix}}_{\mathbf{b}}$$

$$A\mathbf{x} = \mathbf{b}$$

$A$ is the **coefficient matrix**, $\mathbf{x}$ the **unknown vector**,
$\mathbf{b}$ the **right-hand-side vector**.

### Solving by inversion

If $A^{-1}$ exists:

$$\boxed{\mathbf{x} = A^{-1}\mathbf{b}}$$

### Solvability, by determinant

| Condition | Conclusion |
|---|---|
| $\det A \ne 0$ | unique solution exists |
| $\det A = 0$ and $\mathbf{b} \ne \mathbf{0}$ | either no solution or infinitely many |
| $\det A = 0$ and $\mathbf{b} = \mathbf{0}$ | infinitely many solutions (nontrivial ones exist) |
| $\det A \ne 0$ and $\mathbf{b} = \mathbf{0}$ | only the trivial solution $\mathbf{x} = \mathbf{0}$ |

That last row matters for eigenvalue work, coming up in §14.9. A homogeneous
system $A\mathbf{x} = \mathbf{0}$ has a nonzero solution *only* when $A$ is
singular. Hold onto that.

### Worked Example 5 — Solve by Matrix Inversion

**Given.**

$$\begin{aligned} 2x + 3y &= 8 \\ x - y &= -1 \end{aligned}$$

**Solve** using $\mathbf{x} = A^{-1}\mathbf{b}$.

**Solution.**

$$A = \begin{bmatrix} 2 & 3 \\ 1 & -1\end{bmatrix} \qquad \mathbf{b} = \begin{bmatrix} 8 \\ -1\end{bmatrix}$$

$$\det A = (2)(-1) - (3)(1) = -2 - 3 = -5$$

Nonzero, so a unique solution exists.

$$A^{-1} = \frac{1}{-5}\begin{bmatrix} -1 & -3 \\ -1 & 2\end{bmatrix} = \begin{bmatrix} 1/5 & 3/5 \\ 1/5 & -2/5\end{bmatrix}$$

$$\mathbf{x} = A^{-1}\mathbf{b} = \begin{bmatrix} 1/5 & 3/5 \\ 1/5 & -2/5\end{bmatrix}\begin{bmatrix} 8 \\ -1\end{bmatrix}$$

$$x = \tfrac{1}{5}(8) + \tfrac{3}{5}(-1) = \tfrac{8}{5} - \tfrac{3}{5} = \tfrac{5}{5} = 1$$

$$y = \tfrac{1}{5}(8) - \tfrac{2}{5}(-1) = \tfrac{8}{5} + \tfrac{2}{5} = \tfrac{10}{5} = 2$$

$$\boxed{x = 1, \quad y = 2}$$

**Check** in the original equations:

$2(1) + 3(2) = 2 + 6 = 8$ ✓

$1 - 2 = -1$ ✓

### Cramer's rule, revisited

You met Cramer's rule in Chapter 01-08. In matrix language:

$$x_i = \frac{\det A_i}{\det A}$$

where $A_i$ is $A$ with its $i$-th column replaced by $\mathbf{b}$.

For hand computation on a $3 \times 3$ system, Cramer's rule is usually
faster than computing a full $3 \times 3$ inverse — four determinants versus
nine cofactors plus a transpose. For $2 \times 2$, inversion is fine either
way.

---

## 14.8 Rank

The **rank** of a matrix is the number of linearly independent rows
(equivalently, columns). Practically: reduce the matrix to upper triangular
form by row operations and count the nonzero rows.

For an $n \times n$ matrix:

$$\text{rank}(A) = n \iff \det A \ne 0 \iff A \text{ is nonsingular}$$

If $\text{rank}(A) < n$, the matrix is singular — some row is a combination
of the others, contributing no new information.

Rank connects directly to the solvability table in §14.7. A system with
rank deficiency has either no solution or a family of solutions, never
exactly one.

---

## 14.9 Eigenvalues

Here is the new idea.

For most vectors $\mathbf{x}$, the product $A\mathbf{x}$ points in a
different direction than $\mathbf{x}$. But for special vectors, $A$ only
scales — the direction survives.

$$\boxed{A\mathbf{v} = \lambda\mathbf{v}, \qquad \mathbf{v} \ne \mathbf{0}}$$

$\lambda$ is an **eigenvalue** of $A$; $\mathbf{v}$ is a corresponding
**eigenvector**.

![FIG-01-14-005: Eigenvector geometric interpretation. A 2D grid showing several input vectors and their images under transformation A. Most vectors change direction (shown with curved dashed arcs indicating rotation). Two special vectors along the eigenvector directions map to vectors along the same line, one stretched by λ₁ and one by λ₂, with the unchanged direction highlighted.](../figures/FIG-01-14-005-eigenvector-geometry.png)

### Deriving the characteristic equation

Rearrange:

$$A\mathbf{v} - \lambda\mathbf{v} = \mathbf{0}$$

$$A\mathbf{v} - \lambda I\mathbf{v} = \mathbf{0}$$

$$(A - \lambda I)\mathbf{v} = \mathbf{0}$$

This is a homogeneous system. From the solvability table in §14.7, a
homogeneous system has a nonzero solution *only when the coefficient matrix
is singular*. So:

$$\boxed{\det(A - \lambda I) = 0}$$

This is the **characteristic equation**. Its left side is the
**characteristic polynomial**, of degree $n$ for an $n \times n$ matrix.

By the fundamental theorem of algebra (Chapter 01-07), an $n \times n$
matrix has exactly $n$ eigenvalues, counting multiplicity. They may be
repeated, and they may be complex — which is where Chapter 01-12 pays off.

### The 2×2 characteristic equation

For $A = \begin{bmatrix} a & b \\ c & d\end{bmatrix}$:

$$\det\begin{bmatrix} a - \lambda & b \\ c & d - \lambda\end{bmatrix} = (a-\lambda)(d-\lambda) - bc = 0$$

$$\lambda^2 - (a+d)\lambda + (ad - bc) = 0$$

$$\boxed{\lambda^2 - \text{tr}(A)\,\lambda + \det A = 0}$$

Then apply the quadratic formula from Chapter 01-07.

### Two free checks

$$\boxed{\sum_i \lambda_i = \text{tr}(A) \qquad \prod_i \lambda_i = \det A}$$

The eigenvalues sum to the trace and multiply to the determinant. These hold
for any size matrix and take seconds to verify.

> ---
> **Mentor's Margin**
>
> Use both checks, every time. Compute eigenvalues, then confirm the sum
> equals the trace and the product equals the determinant. If either fails,
> you made an arithmetic error in the characteristic polynomial — and you
> catch it in ten seconds instead of carrying it into an eigenvector
> calculation and wasting five minutes. On the FE, where eigenvalue problems
> come as multiple choice, these two checks can also let you eliminate wrong
> answers without solving the polynomial at all.
>
> ---

### Special cases worth knowing

**Triangular or diagonal matrix:** the eigenvalues are the diagonal
elements. No computation needed.

$$A = \begin{bmatrix} 3 & 7 \\ 0 & -2\end{bmatrix} \implies \lambda = 3, -2$$

**Symmetric matrix with real entries:** all eigenvalues are real. This is
why structural and stress problems produce real natural frequencies and real
principal stresses.

### Worked Example 6 — Eigenvalues and Eigenvectors

**Given.** $A = \begin{bmatrix} 4 & 1 \\ 2 & 3\end{bmatrix}$

**(a)** Find the eigenvalues.
**(b)** Verify with the trace and determinant checks.
**(c)** Find an eigenvector for each eigenvalue.
**(d)** Verify each eigenvector.

**Solution.**

**(a)** $\text{tr}(A) = 4 + 3 = 7$ and $\det A = (4)(3) - (1)(2) = 12 - 2 = 10$.

$$\lambda^2 - 7\lambda + 10 = 0$$

$$(\lambda - 5)(\lambda - 2) = 0$$

$$\boxed{\lambda_1 = 5, \quad \lambda_2 = 2}$$

**(b)** Sum: $5 + 2 = 7 = \text{tr}(A)$ ✓

Product: $(5)(2) = 10 = \det A$ ✓

**(c) Eigenvector for $\lambda_1 = 5$.**

$$(A - 5I) = \begin{bmatrix} 4-5 & 1 \\ 2 & 3-5\end{bmatrix} = \begin{bmatrix} -1 & 1 \\ 2 & -2\end{bmatrix}$$

Set $(A-5I)\mathbf{v} = \mathbf{0}$:

$$-v_1 + v_2 = 0 \implies v_2 = v_1$$

(The second row, $2v_1 - 2v_2 = 0$, gives the same condition — it must, since
the matrix is singular by construction.)

Choose $v_1 = 1$:

$$\mathbf{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$$

**Eigenvector for $\lambda_2 = 2$.**

$$(A - 2I) = \begin{bmatrix} 2 & 1 \\ 2 & 1\end{bmatrix}$$

$$2v_1 + v_2 = 0 \implies v_2 = -2v_1$$

Choose $v_1 = 1$:

$$\mathbf{v}_2 = \begin{bmatrix} 1 \\ -2 \end{bmatrix}$$

**(d) Verification.**

For $\lambda_1 = 5$:

$$A\mathbf{v}_1 = \begin{bmatrix} 4 & 1 \\ 2 & 3\end{bmatrix}\begin{bmatrix} 1 \\ 1\end{bmatrix} = \begin{bmatrix} 4+1 \\ 2+3\end{bmatrix} = \begin{bmatrix} 5 \\ 5\end{bmatrix} = 5\begin{bmatrix} 1 \\ 1\end{bmatrix} \;\checkmark$$

For $\lambda_2 = 2$:

$$A\mathbf{v}_2 = \begin{bmatrix} 4 & 1 \\ 2 & 3\end{bmatrix}\begin{bmatrix} 1 \\ -2\end{bmatrix} = \begin{bmatrix} 4-2 \\ 2-6\end{bmatrix} = \begin{bmatrix} 2 \\ -4\end{bmatrix} = 2\begin{bmatrix} 1 \\ -2\end{bmatrix} \;\checkmark$$

> ---
> **Mentor's Margin**
>
> Eigenvectors are not unique. Any nonzero scalar multiple of an eigenvector
> is also an eigenvector for the same eigenvalue: if $A\mathbf{v} =
> \lambda\mathbf{v}$, then $A(3\mathbf{v}) = \lambda(3\mathbf{v})$. What is
> unique is the *direction*. So $\begin{bmatrix} 1 \\ 1\end{bmatrix}$,
> $\begin{bmatrix} 2 \\ 2\end{bmatrix}$, and
> $\begin{bmatrix} -5 \\ -5\end{bmatrix}$ are all valid answers for
> $\lambda = 5$ above. On multiple choice, look for the answer proportional
> to yours rather than identical to it.
>
> ---

### Where eigenvalues appear in engineering

You do not need these applications yet, but knowing they are coming makes
the abstraction worth the effort.

| Application | What the eigenvalue means | Chapter |
|---|---|---|
| Vibration analysis | $\lambda = \omega_n^2$; natural frequencies squared | 02-33 |
| Principal stresses | $\lambda$ = principal stress magnitudes | 02-48 |
| Column buckling | $\lambda$ relates to critical buckling load | 02-51 |
| Control system stability | eigenvalues of the system matrix are the poles | 02-72 |
| Principal moments of inertia | $\lambda$ = principal second moments | 02-27 |

> **Preview note.** Chapter 02-33 uses the eigenvalues of a
> mass-and-stiffness matrix pair to find natural frequencies of a multi-degree
> -of-freedom system, and the eigenvectors give the mode shapes. Nothing in
> this chapter depends on that; it is where the tool gets used.

---

## As the Handbook States It

> **Handbook 10.6, pp. 37–38** — *Mathematics / Matrices, Determinants,
> and Vectors*

The Handbook includes:

- Matrix definition and dimension notation
- Matrix addition and multiplication rules
- Transpose definition
- Identity matrix
- Determinant of $2\times 2$ and $3\times 3$ matrices by cofactor expansion
- Cofactor and minor definitions
- Matrix inverse via the adjugate (classical adjoint) method
- Cramer's rule for solving linear systems
- Eigenvalue definition and the characteristic equation
  $\det(A - \lambda I) = 0$

**What's in the Handbook — find it fast:**

The cofactor expansion pattern, the adjugate inverse formula, and Cramer's
rule are all tabulated. If you blank on the sign pattern for a $3\times 3$
cofactor expansion, the checkerboard is printed there.

**What's not in the Handbook — memorize:**

- The $2\times 2$ inverse shortcut $\frac{1}{ad-bc}\begin{bmatrix} d & -b \\
  -c & a\end{bmatrix}$ — the Handbook gives the general adjugate method, which
  is far slower for $2\times 2$
- The $2\times 2$ characteristic equation shortcut
  $\lambda^2 - \text{tr}(A)\lambda + \det A = 0$
- The trace and determinant checks on eigenvalues
- The dimension-compatibility rule for matrix products
- The order reversal in $(AB)^T = B^TA^T$ and $(AB)^{-1} = B^{-1}A^{-1}$
- Determinant properties (proportional row → zero determinant, etc.) as a
  fast singularity check
- Eigenvalues of a triangular matrix are its diagonal elements
- The connection between $\det A = 0$, singularity, rank deficiency, and
  nontrivial homogeneous solutions
- The procedure for finding eigenvectors once eigenvalues are known

> ---
> **Mentor's Margin**
>
> Verify the exact page numbers above against your copy of the Handbook and
> write them on your personal page map from Chapter 00-03. Section start
> pages in this guide were taken from the Handbook 10.6 table of contents,
> but the subsection where eigenvalues appear within Mathematics should be
> confirmed by you, once, before exam day. Two minutes now saves thirty
> seconds of hunting under time pressure.
>
> ---

---

## Where This Goes Wrong

**Reversing rows and columns.** A $3\times 4$ matrix has three rows. Element
$a_{23}$ is row 2, column 3. Getting this backwards corrupts every
subsequent step.

**Attempting an undefined product.** $(3\times 4)(2\times 4)$ is not a
matrix of zeros. It does not exist. Check inner dimensions before you start
multiplying.

**Assuming $AB = BA$.** They are generally different, and sometimes only one
of them is even defined. In any expression involving matrix products, order
is part of the meaning.

**Sign error in the cofactor checkerboard.** The $(1,2)$ cofactor carries a
minus sign. Forgetting it puts the wrong sign on the middle term of a
$3\times 3$ expansion. Write the sign pattern down before expanding.

**Sign error in the 2×2 inverse.** The off-diagonal elements get negated;
the diagonal elements get swapped. Not the reverse. Always verify by
multiplying $AA^{-1}$ and confirming you get $I$.

**Dividing by a zero determinant.** If $\det A = 0$, there is no inverse and
the system does not have a unique solution. Compute the determinant *first*,
then decide what to do.

**Order reversal forgotten in $(AB)^T$ and $(AB)^{-1}$.** Both reverse:
$B^TA^T$ and $B^{-1}A^{-1}$. Not $A^TB^T$ or $A^{-1}B^{-1}$.

**Sign error in $A - \lambda I$.** You subtract $\lambda$ from the *diagonal
elements only*. Writing $A - \lambda$ and subtracting from every element is
wrong — and it is not even a defined operation, since $\lambda$ is a scalar
and $A$ is a matrix.

**Expecting a unique eigenvector.** Any nonzero multiple works. If your
answer is $\begin{bmatrix} 1 \\ 1\end{bmatrix}$ and the choices list
$\begin{bmatrix} 2 \\ 2\end{bmatrix}$, that is your answer.

**Using both rows of $(A - \lambda I)\mathbf{v} = \mathbf{0}$ as
independent.** They are not. $(A - \lambda I)$ is singular by construction,
so the rows are proportional. One row gives you the whole condition. If the
two rows give you *contradictory* conditions, your eigenvalue is wrong.

**Skipping the trace and determinant checks.** They cost ten seconds and
catch most eigenvalue arithmetic errors.

---

## Key Terms

| Term | Definition |
|---|---|
| Matrix | Rectangular array of numbers arranged in rows and columns |
| Dimensions (order) | Size of a matrix, stated rows × columns |
| Element $a_{ij}$ | Entry in row $i$, column $j$ |
| Square matrix | Equal number of rows and columns |
| Diagonal matrix | Square matrix with all off-diagonal elements zero |
| Identity matrix $I$ | Diagonal matrix with all 1's; satisfies $AI = IA = A$ |
| Triangular matrix | All elements above (lower) or below (upper) the diagonal are zero |
| Symmetric matrix | Square matrix with $A^T = A$, i.e. $a_{ij} = a_{ji}$ |
| Trace | Sum of the diagonal elements of a square matrix |
| Transpose $A^T$ | Matrix with rows and columns exchanged |
| Determinant | Scalar computed from a square matrix; zero means non-invertible |
| Minor $M_{ij}$ | Determinant remaining after deleting row $i$ and column $j$ |
| Cofactor $C_{ij}$ | Signed minor, $(-1)^{i+j}M_{ij}$ |
| Cofactor expansion | Method of computing a determinant as a signed sum of element-times-minor terms |
| Inverse $A^{-1}$ | Matrix satisfying $AA^{-1} = I$; exists only if $\det A \ne 0$ |
| Singular matrix | $\det A = 0$; has no inverse; collapses information |
| Nonsingular matrix | $\det A \ne 0$; invertible |
| Rank | Number of linearly independent rows (or columns) |
| Coefficient matrix | The matrix $A$ in the system $A\mathbf{x} = \mathbf{b}$ |
| Homogeneous system | $A\mathbf{x} = \mathbf{0}$; has nonzero solutions only if $A$ is singular |
| Eigenvalue $\lambda$ | Scalar satisfying $A\mathbf{v} = \lambda\mathbf{v}$ for some $\mathbf{v} \ne \mathbf{0}$ |
| Eigenvector $\mathbf{v}$ | Nonzero vector whose direction is unchanged by $A$ |
| Characteristic equation | $\det(A - \lambda I) = 0$; its roots are the eigenvalues |
| Characteristic polynomial | The degree-$n$ polynomial on the left of the characteristic equation |

---

## Review Questions

### Conceptual

1. A matrix is $4 \times 3$ and another is $3 \times 5$. Which products are
   defined, and what are their dimensions?
2. Explain why matrix multiplication is not commutative. Give a reason
   grounded in what a matrix represents, not just an algebraic
   counterexample.
3. What does it mean physically for a stiffness matrix to be singular?
4. Explain why $(AB)^T = B^TA^T$ rather than $A^TB^T$. Use a dimension
   argument.
5. Derive the characteristic equation $\det(A - \lambda I) = 0$ starting
   from $A\mathbf{v} = \lambda\mathbf{v}$. State clearly where the
   singularity requirement enters.
6. Why are eigenvectors not unique? What *is* unique about them?
7. A real symmetric matrix always has real eigenvalues. Why does this matter
   for a vibration problem?
8. When solving $(A - \lambda I)\mathbf{v} = \mathbf{0}$, you find the two
   rows give contradictory conditions on $v_1$ and $v_2$. What does that tell
   you?

### Calculation

9. Given $A = \begin{bmatrix} 1 & -2 \\ 3 & 0\end{bmatrix}$ and
   $B = \begin{bmatrix} 4 & 1 \\ -1 & 2\end{bmatrix}$, compute:
   (a) $A + B$
   (b) $2A - 3B$
   (c) $AB$
   (d) $BA$
   (e) Confirm $AB \ne BA$

10. Find the transpose of each and state whether the original is symmetric:
    (a) $A = \begin{bmatrix} 2 & 5 & -1 \\ 5 & 0 & 3 \\ -1 & 3 & 4\end{bmatrix}$
    (b) $B = \begin{bmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6\end{bmatrix}$

11. Evaluate each determinant:
    (a) $\begin{vmatrix} 6 & -2 \\ 3 & 5\end{vmatrix}$
    (b) $\begin{vmatrix} 1 & 2 & 0 \\ 3 & -1 & 4 \\ 2 & 0 & 1\end{vmatrix}$
    (c) $\begin{vmatrix} 2 & 4 \\ 1 & 2\end{vmatrix}$ — and state whether the
    matrix is singular
    (d) $\begin{vmatrix} 3 & 8 & -1 \\ 0 & 5 & 7 \\ 0 & 0 & -2\end{vmatrix}$
    — use the fastest method

12. Find the inverse if it exists; if not, say why:
    (a) $A = \begin{bmatrix} 2 & 1 \\ 5 & 3\end{bmatrix}$
    (b) $B = \begin{bmatrix} 4 & 6 \\ 2 & 3\end{bmatrix}$

13. Solve using the matrix inverse. Verify your answer in the original
    equations.

    $$\begin{aligned} 3x + 2y &= 7 \\ x + 4y &= 9\end{aligned}$$

14. Find the eigenvalues and one eigenvector for each eigenvalue. Verify
    with the trace and determinant checks and by direct substitution.
    (a) $A = \begin{bmatrix} 5 & 2 \\ 2 & 2\end{bmatrix}$
    (b) $A = \begin{bmatrix} 3 & 0 \\ 0 & -2\end{bmatrix}$
    (c) $A = \begin{bmatrix} 1 & 4 \\ 0 & 1\end{bmatrix}$

15. **Engineering application.** A three-node system produces the following
    equations, where $x$, $y$, $z$ are unknown flow rates in kg/s:

    $$\begin{aligned} 2x + y - z &= 1 \\ x - y + 2z &= 5 \\ 3x + 2y + z &= 10\end{aligned}$$

    (a) Write the system in matrix form $A\mathbf{x} = \mathbf{b}$.
    (b) Compute $\det A$ and state whether a unique solution exists.
    (c) Solve using Cramer's rule.
    (d) Verify all three equations.

16. **Engineering application.** A two-degree-of-freedom system yields the
    matrix

    $$A = \begin{bmatrix} 2 & -1 \\ -1 & 2\end{bmatrix}$$

    (a) Confirm $A$ is symmetric and predict whether its eigenvalues will be
    real.
    (b) Find both eigenvalues.
    (c) Find an eigenvector for each.
    (d) The eigenvectors here represent mode shapes. Describe in words what
    each mode shape means about how the two coordinates move relative to
    each other.

### Multiple Choice

17. If $A$ is $3 \times 4$ and $B$ is $4 \times 2$, then $AB$ is:
    A) $3 \times 2$
    B) $4 \times 4$
    C) $2 \times 3$
    D) Undefined

18. The determinant of $\begin{bmatrix} a & b \\ c & d\end{bmatrix}$ is:
    A) $ab - cd$
    B) $ad - bc$
    C) $ac - bd$
    D) $ad + bc$

19. A square matrix has no inverse when:
    A) It is symmetric
    B) Its trace is zero
    C) Its determinant is zero
    D) It is triangular

20. The sum of the eigenvalues of a square matrix equals:
    A) Its determinant
    B) Its rank
    C) Its trace
    D) The number of rows

21. $(AB)^{-1}$ equals:
    A) $A^{-1}B^{-1}$
    B) $B^{-1}A^{-1}$
    C) $(BA)^{-1}$
    D) $A^{-1}B$

22. The eigenvalues of $\begin{bmatrix} 3 & 7 \\ 0 & -2\end{bmatrix}$ are:
    A) $3$ and $7$
    B) $3$ and $-2$
    C) $1$ and $-6$
    D) $7$ and $-2$

23. The characteristic equation of a $2\times 2$ matrix $A$ is:
    A) $\lambda^2 - \det A \cdot \lambda + \text{tr}(A) = 0$
    B) $\lambda^2 + \text{tr}(A)\lambda + \det A = 0$
    C) $\lambda^2 - \text{tr}(A)\lambda + \det A = 0$
    D) $\lambda^2 - \text{tr}(A)\lambda - \det A = 0$

24. If $\begin{bmatrix} 1 \\ 3\end{bmatrix}$ is an eigenvector of $A$, then
    which of these is also an eigenvector for the same eigenvalue?
    A) $\begin{bmatrix} 3 \\ 1\end{bmatrix}$
    B) $\begin{bmatrix} 1 \\ -3\end{bmatrix}$
    C) $\begin{bmatrix} -2 \\ -6\end{bmatrix}$
    D) $\begin{bmatrix} 0 \\ 0\end{bmatrix}$

---

## Answer Key with Explanations

**1.** $A$ is $4\times 3$, $B$ is $3\times 5$.

$AB$: inner dimensions $3 = 3$ ✓ → defined, result is $4 \times 5$.

$BA$: inner dimensions would need $5 = 4$ ✗ → **undefined**.

Only one of the two products exists. (§14.3)

**2.** A matrix represents a linear transformation, and physical
transformations generally do not commute. Rotate a book 90° about a
horizontal axis, then 90° about a vertical axis; now do the same two
rotations in the opposite order. The book ends up in a different
orientation. The matrices representing those rotations don't commute because
the physical operations don't. Order of application is part of the meaning.
(§14.3)

**3.** A singular stiffness matrix means $\det K = 0$, so $K^{-1}$ does not
exist and $K\mathbf{u} = \mathbf{F}$ has no unique solution. Physically the
structure is not adequately constrained — it can move without any applied
force (a rigid-body motion or a collapse mechanism). The mathematics is
telling you the model is unstable, not that the arithmetic failed.
(§14.6, §14.7)

**4.** Dimension argument: let $A$ be $2\times 3$ and $B$ be $3\times 4$.
Then $AB$ is $2\times 4$, so $(AB)^T$ is $4\times 2$.

$B^T$ is $4\times 3$ and $A^T$ is $3\times 2$, so $B^TA^T$ is $4\times 2$ ✓
— dimensions match.

$A^TB^T$ would be $(3\times 2)(4\times 3)$, requiring $2 = 4$ — undefined.

The dimensions alone force the order reversal. (§14.4)

**5.** Start from $A\mathbf{v} = \lambda\mathbf{v}$ with $\mathbf{v} \ne
\mathbf{0}$.

Move everything to one side: $A\mathbf{v} - \lambda\mathbf{v} = \mathbf{0}$.

Insert the identity so both terms have a matrix acting on $\mathbf{v}$:
$A\mathbf{v} - \lambda I\mathbf{v} = \mathbf{0}$.

Factor: $(A - \lambda I)\mathbf{v} = \mathbf{0}$.

This is a homogeneous system. **The singularity requirement enters here:** a
homogeneous system has a nonzero solution only if its coefficient matrix is
singular. Since we require $\mathbf{v} \ne \mathbf{0}$, we must have
$(A - \lambda I)$ singular, which means

$$\det(A - \lambda I) = 0$$

If $(A - \lambda I)$ were nonsingular, the only solution would be
$\mathbf{v} = \mathbf{0}$, which is excluded by definition. (§14.9)

**6.** If $A\mathbf{v} = \lambda\mathbf{v}$, then for any nonzero scalar $c$:

$$A(c\mathbf{v}) = c(A\mathbf{v}) = c(\lambda\mathbf{v}) = \lambda(c\mathbf{v})$$

So $c\mathbf{v}$ is also an eigenvector for the same $\lambda$. What is
unique is the **direction** — the line through the origin along which the
eigenvector lies. The magnitude is arbitrary. (§14.9)

**7.** Real eigenvalues mean real natural frequencies. In vibration analysis
$\lambda = \omega_n^2$, so a real positive eigenvalue gives a real
oscillation frequency $\omega_n = \sqrt{\lambda}$. Mass and stiffness
matrices for physical structures are symmetric (by a reciprocity principle),
which guarantees the eigenvalues come out real, which guarantees the
predicted frequencies are physically meaningful. Complex eigenvalues here
would signal a modeling error. (§14.9)

**8.** Your eigenvalue is wrong. By construction, $(A - \lambda I)$ is
singular when $\lambda$ is a genuine eigenvalue, which means its rows are
proportional and give the *same* condition. Contradictory conditions mean
$(A - \lambda I)$ is nonsingular, so $\lambda$ is not an eigenvalue. Go back
and recheck the characteristic equation — and apply the trace and
determinant checks. (§14.9)

**9.**

(a) $A + B = \begin{bmatrix} 1+4 & -2+1 \\ 3-1 & 0+2\end{bmatrix} =
\boxed{\begin{bmatrix} 5 & -1 \\ 2 & 2\end{bmatrix}}$

(b) $2A = \begin{bmatrix} 2 & -4 \\ 6 & 0\end{bmatrix}$ and
$3B = \begin{bmatrix} 12 & 3 \\ -3 & 6\end{bmatrix}$

$2A - 3B = \boxed{\begin{bmatrix} -10 & -7 \\ 9 & -6\end{bmatrix}}$

(c) $AB$:

$(1,1)$: $(1)(4) + (-2)(-1) = 4 + 2 = 6$

$(1,2)$: $(1)(1) + (-2)(2) = 1 - 4 = -3$

$(2,1)$: $(3)(4) + (0)(-1) = 12$

$(2,2)$: $(3)(1) + (0)(2) = 3$

$$AB = \boxed{\begin{bmatrix} 6 & -3 \\ 12 & 3\end{bmatrix}}$$

(d) $BA$:

$(1,1)$: $(4)(1) + (1)(3) = 4 + 3 = 7$

$(1,2)$: $(4)(-2) + (1)(0) = -8$

$(2,1)$: $(-1)(1) + (2)(3) = -1 + 6 = 5$

$(2,2)$: $(-1)(-2) + (2)(0) = 2$

$$BA = \boxed{\begin{bmatrix} 7 & -8 \\ 5 & 2\end{bmatrix}}$$

(e) $AB = \begin{bmatrix} 6 & -3 \\ 12 & 3\end{bmatrix} \ne
\begin{bmatrix} 7 & -8 \\ 5 & 2\end{bmatrix} = BA$ ✓ Confirmed.

**10.**

(a) $A^T = \begin{bmatrix} 2 & 5 & -1 \\ 5 & 0 & 3 \\ -1 & 3 & 4\end{bmatrix}
= A$. **Symmetric** ✓ (Note $a_{12} = a_{21} = 5$, $a_{13} = a_{31} = -1$,
$a_{23} = a_{32} = 3$.)

(b) $B^T = \begin{bmatrix} 1 & 3 & 5 \\ 2 & 4 & 6\end{bmatrix}$.
**Not symmetric** — $B$ is $3\times 2$, not square, so symmetry is impossible.

**11.**

(a) $(6)(5) - (-2)(3) = 30 + 6 = \boxed{36}$

(b) Expand along row 1 (signs $+, -, +$):

$$1\begin{vmatrix} -1 & 4 \\ 0 & 1\end{vmatrix} - 2\begin{vmatrix} 3 & 4 \\ 2 & 1\end{vmatrix} + 0$$

$$= 1(-1 - 0) - 2(3 - 8) + 0 = -1 + 10 = \boxed{9}$$

*Faster alternative:* expand along column 3, which has two zeros:
$0 \cdot C_{13} + 4 \cdot C_{23} + 1 \cdot C_{33}$, sign pattern
$+, -, +$ down column 3.

$= -4\begin{vmatrix} 1 & 2 \\ 2 & 0\end{vmatrix} + 1\begin{vmatrix} 1 & 2 \\ 3 & -1\end{vmatrix}
= -4(0 - 4) + (-1 - 6) = 16 - 7 = 9$ ✓

(c) $(2)(2) - (4)(1) = 4 - 4 = \boxed{0}$. **Singular.** Note that row 2 is
$\tfrac{1}{2}\times$ row 1 — the proportional-row property predicts this
without any arithmetic.

(d) Upper triangular, so the determinant is the product of the diagonal:

$$(3)(5)(-2) = \boxed{-30}$$

No expansion needed.

**12.**

(a) $\det A = (2)(3) - (1)(5) = 6 - 5 = 1 \ne 0$ → inverse exists.

$$A^{-1} = \frac{1}{1}\begin{bmatrix} 3 & -1 \\ -5 & 2\end{bmatrix} = \boxed{\begin{bmatrix} 3 & -1 \\ -5 & 2\end{bmatrix}}$$

Verify $AA^{-1}$:

$(1,1)$: $(2)(3) + (1)(-5) = 6 - 5 = 1$

$(1,2)$: $(2)(-1) + (1)(2) = -2 + 2 = 0$

$(2,1)$: $(5)(3) + (3)(-5) = 15 - 15 = 0$

$(2,2)$: $(5)(-1) + (3)(2) = -5 + 6 = 1$

$= I$ ✓

(b) $\det B = (4)(3) - (6)(2) = 12 - 12 = 0$.

**No inverse.** $B$ is singular — row 1 is $2\times$ row 2, so the rows are
linearly dependent and $B$ has rank 1, not 2.

**13.**

$$A = \begin{bmatrix} 3 & 2 \\ 1 & 4\end{bmatrix} \qquad \mathbf{b} = \begin{bmatrix} 7 \\ 9\end{bmatrix}$$

$$\det A = (3)(4) - (2)(1) = 12 - 2 = 10 \ne 0 \quad \text{→ unique solution}$$

$$A^{-1} = \frac{1}{10}\begin{bmatrix} 4 & -2 \\ -1 & 3\end{bmatrix}$$

$$x = \tfrac{1}{10}\big[(4)(7) + (-2)(9)\big] = \tfrac{1}{10}(28 - 18) = \tfrac{10}{10} = 1$$

$$y = \tfrac{1}{10}\big[(-1)(7) + (3)(9)\big] = \tfrac{1}{10}(-7 + 27) = \tfrac{20}{10} = 2$$

$$\boxed{x = 1, \quad y = 2}$$

**Verify:** $3(1) + 2(2) = 3 + 4 = 7$ ✓ and $1 + 4(2) = 1 + 8 = 9$ ✓

**14.**

**(a)** $A = \begin{bmatrix} 5 & 2 \\ 2 & 2\end{bmatrix}$

$\text{tr}(A) = 7$, $\det A = (5)(2) - (2)(2) = 10 - 4 = 6$

$$\lambda^2 - 7\lambda + 6 = 0 \implies (\lambda - 6)(\lambda - 1) = 0$$

$$\boxed{\lambda_1 = 6, \quad \lambda_2 = 1}$$

*Checks:* sum $= 6 + 1 = 7 = \text{tr}(A)$ ✓; product $= 6 = \det A$ ✓

**Eigenvector for $\lambda_1 = 6$:**

$(A - 6I) = \begin{bmatrix} -1 & 2 \\ 2 & -4\end{bmatrix}$

Row 1: $-v_1 + 2v_2 = 0 \implies v_1 = 2v_2$. Take $v_2 = 1$:

$$\mathbf{v}_1 = \begin{bmatrix} 2 \\ 1\end{bmatrix}$$

Verify: $A\mathbf{v}_1 = \begin{bmatrix} (5)(2)+(2)(1) \\ (2)(2)+(2)(1)\end{bmatrix}
= \begin{bmatrix} 12 \\ 6\end{bmatrix} = 6\begin{bmatrix} 2 \\ 1\end{bmatrix}$ ✓

**Eigenvector for $\lambda_2 = 1$:**

$(A - I) = \begin{bmatrix} 4 & 2 \\ 2 & 1\end{bmatrix}$

Row 2: $2v_1 + v_2 = 0 \implies v_2 = -2v_1$. Take $v_1 = 1$:

$$\mathbf{v}_2 = \begin{bmatrix} 1 \\ -2\end{bmatrix}$$

Verify: $A\mathbf{v}_2 = \begin{bmatrix} 5 - 4 \\ 2 - 4\end{bmatrix}
= \begin{bmatrix} 1 \\ -2\end{bmatrix} = 1 \cdot \begin{bmatrix} 1 \\ -2\end{bmatrix}$ ✓

*Note:* $A$ is symmetric, and $\mathbf{v}_1 \cdot \mathbf{v}_2 =
(2)(1) + (1)(-2) = 0$ — the eigenvectors are orthogonal, which always
happens for distinct eigenvalues of a real symmetric matrix.

**(b)** $A = \begin{bmatrix} 3 & 0 \\ 0 & -2\end{bmatrix}$ is diagonal, so
the eigenvalues are the diagonal entries:

$$\boxed{\lambda_1 = 3, \quad \lambda_2 = -2}$$

*Checks:* sum $= 1 = \text{tr}(A)$ ✓; product $= -6 = \det A$ ✓

Eigenvectors: $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 0\end{bmatrix}$ and
$\mathbf{v}_2 = \begin{bmatrix} 0 \\ 1\end{bmatrix}$ — the coordinate axes
themselves. A diagonal matrix just stretches along the axes.

**(c)** $A = \begin{bmatrix} 1 & 4 \\ 0 & 1\end{bmatrix}$ is upper
triangular, so:

$$\boxed{\lambda_1 = \lambda_2 = 1 \quad \text{(repeated, multiplicity 2)}}$$

*Checks:* sum $= 2 = \text{tr}(A)$ ✓; product $= 1 = \det A$ ✓

Eigenvector: $(A - I) = \begin{bmatrix} 0 & 4 \\ 0 & 0\end{bmatrix}$

Row 1: $4v_2 = 0 \implies v_2 = 0$. $v_1$ is free. Take $v_1 = 1$:

$$\mathbf{v} = \begin{bmatrix} 1 \\ 0\end{bmatrix}$$

Only **one** independent eigenvector exists despite the eigenvalue having
multiplicity 2. This is a *defective* matrix. Worth recognizing but not
pursued further at this tier.

**15.**

(a)

$$\underbrace{\begin{bmatrix} 2 & 1 & -1 \\ 1 & -1 & 2 \\ 3 & 2 & 1\end{bmatrix}}_{A}\begin{bmatrix} x \\ y \\ z\end{bmatrix} = \begin{bmatrix} 1 \\ 5 \\ 10\end{bmatrix}$$

(b) Expand along row 1 (signs $+, -, +$):

$$\det A = 2\begin{vmatrix} -1 & 2 \\ 2 & 1\end{vmatrix} - 1\begin{vmatrix} 1 & 2 \\ 3 & 1\end{vmatrix} + (-1)\begin{vmatrix} 1 & -1 \\ 3 & 2\end{vmatrix}$$

$$= 2(-1 - 4) - 1(1 - 6) - 1(2 + 3)$$

$$= 2(-5) - (-5) - 5 = -10 + 5 - 5 = \boxed{-10}$$

Nonzero, so a **unique solution exists**.

(c) **Cramer's rule.**

$D_x$: replace column 1 with $\mathbf{b}$:

$$D_x = \begin{vmatrix} 1 & 1 & -1 \\ 5 & -1 & 2 \\ 10 & 2 & 1\end{vmatrix} = 1(-1-4) - 1(5-20) - 1(10+10)$$

$$= -5 + 15 - 20 = -10$$

$$x = \frac{-10}{-10} = 1$$

$D_y$: replace column 2 with $\mathbf{b}$:

$$D_y = \begin{vmatrix} 2 & 1 & -1 \\ 1 & 5 & 2 \\ 3 & 10 & 1\end{vmatrix} = 2(5-20) - 1(1-6) - 1(10-15)$$

$$= -30 + 5 + 5 = -20$$

$$y = \frac{-20}{-10} = 2$$

$D_z$: replace column 3 with $\mathbf{b}$:

$$D_z = \begin{vmatrix} 2 & 1 & 1 \\ 1 & -1 & 5 \\ 3 & 2 & 10\end{vmatrix} = 2(-10-10) - 1(10-15) + 1(2+3)$$

$$= -40 + 5 + 5 = -30$$

$$z = \frac{-30}{-10} = 3$$

$$\boxed{x = 1 \text{ kg/s}, \quad y = 2 \text{ kg/s}, \quad z = 3 \text{ kg/s}}$$

(d) **Verify all three equations:**

$2(1) + 2 - 3 = 2 + 2 - 3 = 1$ ✓

$1 - 2 + 2(3) = 1 - 2 + 6 = 5$ ✓

$3(1) + 2(2) + 3 = 3 + 4 + 3 = 10$ ✓

All three flow rates are positive, which is physically sensible for a mass
flow problem.

**16.**

(a) $a_{12} = a_{21} = -1$, so $A^T = A$ — **symmetric** ✓. A real symmetric
matrix has **real eigenvalues**, so we can predict real results before
computing.

(b) $\text{tr}(A) = 4$, $\det A = (2)(2) - (-1)(-1) = 4 - 1 = 3$

$$\lambda^2 - 4\lambda + 3 = 0 \implies (\lambda - 3)(\lambda - 1) = 0$$

$$\boxed{\lambda_1 = 3, \quad \lambda_2 = 1}$$

*Checks:* sum $= 4 = \text{tr}(A)$ ✓; product $= 3 = \det A$ ✓. Both real,
as predicted.

(c) **For $\lambda_1 = 3$:**

$(A - 3I) = \begin{bmatrix} -1 & -1 \\ -1 & -1\end{bmatrix}$

Row 1: $-v_1 - v_2 = 0 \implies v_2 = -v_1$. Take $v_1 = 1$:

$$\mathbf{v}_1 = \begin{bmatrix} 1 \\ -1\end{bmatrix}$$

Verify: $A\mathbf{v}_1 = \begin{bmatrix} 2 + 1 \\ -1 - 2\end{bmatrix}
= \begin{bmatrix} 3 \\ -3\end{bmatrix} = 3\begin{bmatrix} 1 \\ -1\end{bmatrix}$ ✓

**For $\lambda_2 = 1$:**

$(A - I) = \begin{bmatrix} 1 & -1 \\ -1 & 1\end{bmatrix}$

Row 1: $v_1 - v_2 = 0 \implies v_2 = v_1$. Take $v_1 = 1$:

$$\mathbf{v}_2 = \begin{bmatrix} 1 \\ 1\end{bmatrix}$$

Verify: $A\mathbf{v}_2 = \begin{bmatrix} 2 - 1 \\ -1 + 2\end{bmatrix}
= \begin{bmatrix} 1 \\ 1\end{bmatrix} = 1 \cdot \begin{bmatrix} 1 \\ 1\end{bmatrix}$ ✓

*Note:* $\mathbf{v}_1 \cdot \mathbf{v}_2 = (1)(1) + (-1)(1) = 0$ —
orthogonal, as expected for a symmetric matrix with distinct eigenvalues.

(d) **Mode shape interpretation.**

$\mathbf{v}_2 = \begin{bmatrix} 1 \\ 1\end{bmatrix}$ with $\lambda_2 = 1$
(the smaller eigenvalue): both coordinates move by the same amount in the
**same direction** — they move together, in phase. This is the
**lower-frequency mode**, because moving in unison does less work against
the coupling between them.

$\mathbf{v}_1 = \begin{bmatrix} 1 \\ -1\end{bmatrix}$ with $\lambda_1 = 3$
(the larger eigenvalue): the coordinates move by equal amounts in
**opposite directions** — out of phase. This is the **higher-frequency
mode**, because the coupling is being stretched and compressed as the two
coordinates work against each other.

The general pattern holds broadly: in-phase modes are lower frequency,
out-of-phase modes are higher. Chapter 02-33 develops this fully.

**17. A — $3 \times 2$.** Inner dimensions $4 = 4$ ✓ match, so the product
is defined. Outer dimensions survive: $3 \times 2$. (§14.3)

**18. B — $ad - bc$.** Main diagonal product minus off-diagonal product.
Choice D has the wrong sign; A and C pair the wrong elements. (§14.5)

**19. C — Its determinant is zero.** $\det A = 0$ means singular, no
inverse. Symmetry and triangularity say nothing about invertibility — a
symmetric matrix can be invertible or not, and a triangular matrix is
invertible exactly when no diagonal element is zero. A zero trace also
doesn't imply singularity. (§14.6)

**20. C — Its trace.** $\sum\lambda_i = \text{tr}(A)$. The *product* of the
eigenvalues equals the determinant (choice A confuses the two). (§14.9)

**21. B — $B^{-1}A^{-1}$.** Order reverses, same as with the transpose.
Verify: $(AB)(B^{-1}A^{-1}) = A(BB^{-1})A^{-1} = AIA^{-1} = AA^{-1} = I$ ✓
Choice A fails this test. (§14.6)

**22. B — $3$ and $-2$.** The matrix is upper triangular, so the eigenvalues
are the diagonal elements. Check: sum $= 1 = \text{tr}(A) = 3 + (-2)$ ✓;
product $= -6 = \det A = (3)(-2) - (7)(0)$ ✓. The off-diagonal 7 does not
affect the eigenvalues. (§14.9)

**23. C — $\lambda^2 - \text{tr}(A)\lambda + \det A = 0$.** Derived by
expanding $\det(A - \lambda I) = (a-\lambda)(d-\lambda) - bc$. The trace term
is negative; the determinant term is positive. Choice B has both signs
wrong; D has the determinant sign wrong. (§14.9)

**24. C — $\begin{bmatrix} -2 \\ -6\end{bmatrix}$.** This is
$-2 \times \begin{bmatrix} 1 \\ 3\end{bmatrix}$ — a nonzero scalar multiple,
so it lies along the same direction and is a valid eigenvector for the same
eigenvalue. Choices A and B point in different directions. Choice D is the
zero vector, which is excluded by definition — an eigenvector must be
nonzero. (§14.9)

---

## Quick Reference

**Dimensions** — rows × columns, always in that order

$$(m \times n)(n \times p) = (m \times p) \quad \text{— inner must match}$$

**Matrix multiplication** — *Handbook p. 37*

$$(AB)_{ij} = \sum_k a_{ik}b_{kj} \qquad AB \ne BA$$

**Transpose and inverse — order reverses**

$$(AB)^T = B^TA^T \qquad (AB)^{-1} = B^{-1}A^{-1}$$

**Determinants** — *Handbook p. 37*

$$\begin{vmatrix} a & b \\ c & d\end{vmatrix} = ad - bc$$

3×3 cofactor sign pattern:
$\begin{bmatrix} + & - & + \\ - & + & - \\ + & - & +\end{bmatrix}$

Expand along the row or column with the most zeros.

**Fast determinant facts**

| Situation | $\det$ |
|---|---|
| Triangular or diagonal | product of diagonal |
| Two rows (or columns) proportional | $0$ |
| Any row or column all zeros | $0$ |
| Two rows swapped | sign flips |
| $\det A^T$ | $= \det A$ |
| $\det(AB)$ | $= (\det A)(\det B)$ |
| $\det(A^{-1})$ | $= 1/\det A$ |
| $\det(cA)$, $n\times n$ | $= c^n \det A$ |

**2×2 inverse — memorize**

$$\begin{bmatrix} a & b \\ c & d\end{bmatrix}^{-1} = \frac{1}{ad-bc}\begin{bmatrix} d & -b \\ -c & a\end{bmatrix}$$

Swap the diagonal, negate the off-diagonal, divide by $\det$. Always verify
$AA^{-1} = I$.

**Linear systems** — *Handbook p. 37 (Cramer's rule)*

$$A\mathbf{x} = \mathbf{b} \implies \mathbf{x} = A^{-1}\mathbf{b} \qquad x_i = \frac{\det A_i}{\det A}$$

| Condition | Solution |
|---|---|
| $\det A \ne 0$ | unique |
| $\det A = 0$, $\mathbf{b}\ne\mathbf{0}$ | none or infinitely many |
| $\det A = 0$, $\mathbf{b}=\mathbf{0}$ | infinitely many (nontrivial exist) |
| $\det A \ne 0$, $\mathbf{b}=\mathbf{0}$ | only $\mathbf{x}=\mathbf{0}$ |

**Eigenvalues** — *Handbook p. 38*

$$A\mathbf{v} = \lambda\mathbf{v} \qquad \det(A - \lambda I) = 0$$

2×2 shortcut:

$$\lambda^2 - \text{tr}(A)\lambda + \det A = 0$$

Checks: $\sum\lambda_i = \text{tr}(A)$ and $\prod\lambda_i = \det A$

Triangular or diagonal matrix → eigenvalues are the diagonal elements.

Real symmetric matrix → all eigenvalues real; eigenvectors for distinct
eigenvalues are orthogonal.

**Eigenvector procedure**

1. Form $(A - \lambda I)$ — subtract $\lambda$ from the **diagonal only**
2. Solve $(A - \lambda I)\mathbf{v} = \mathbf{0}$ using **one row**
   (the rows are proportional)
3. Pick any convenient value for one component
4. Verify $A\mathbf{v} = \lambda\mathbf{v}$

Any nonzero multiple is equally valid.

**Not in the Handbook — memorize**

2×2 inverse shortcut · 2×2 characteristic equation shortcut · trace and
determinant eigenvalue checks · dimension-compatibility rule · order
reversal in $(AB)^T$ and $(AB)^{-1}$ · determinant properties as singularity
shortcuts · eigenvalues of a triangular matrix · the
$\det A = 0 \leftrightarrow$ singular $\leftrightarrow$ rank-deficient
$\leftrightarrow$ nontrivial homogeneous solution chain · eigenvector
solution procedure

---

## What's Next

Apprentice, that closes Tier 1B. Look at what you can now do.

You can manipulate algebraic expressions, solve equations and inequalities,
work with exponents and logarithms, analyze functions and their graphs, find
roots of polynomials, solve linear systems three different ways, handle
coordinate geometry and conic sections, compute areas and volumes, do
trigonometry from the unit circle out, work in the complex plane, and
operate on vectors and matrices in three dimensions.

That is the complete algebraic and geometric toolkit. Every one of those
tools gets used in Tier 2 and beyond, and none of them will be re-taught.

**Chapter 01-15 opens Tier 1C: Calculus**, beginning with limits and
continuity. Everything in Tier 1B was static — a fixed triangle, a fixed
matrix, a fixed root. Calculus is about change: how fast something varies,
and how small changes accumulate into large ones. Velocity is the rate of
change of position. Stress is force distributed over an area that may vary
point to point. Heat flux depends on a temperature gradient. Every one of
those is a derivative or an integral.

The limit is the foundation of all of it, and it is the one idea in calculus
that people usually memorize instead of understand. We will do it properly.

Before you turn the page: if any of the Tier 1B chapters felt shaky, this is
the checkpoint to go back. The Tier 1B review exam in the appendices covers
chapters 01-04 through 01-14 in exam conditions. Take it timed. A score
below 70% on any chapter's questions means return to that chapter before
moving on — Tier 1C leans hard on algebra fluency, and shoring it up now
costs far less than debugging it later.

Open the Handbook to page 45. Calculus begins there.

See you there.

— Your Mentor
