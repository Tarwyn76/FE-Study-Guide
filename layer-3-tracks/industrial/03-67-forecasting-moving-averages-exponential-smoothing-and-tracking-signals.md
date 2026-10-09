---
chapter: "03-67"
title: "Forecasting — Moving Averages, Exponential Smoothing, and Tracking Signals"
layer: 3
tier: null
track: industrial_and_systems
template: technical
ledger_ids: [IND-3-067-01, IND-3-067-02, IND-3-067-03, IND-3-067-04, IND-3-067-05, IND-3-067-06, IND-3-067-07]
routes: [industrial_and_systems]
status: drafted
---

# Chapter 03-67: Forecasting — Moving Averages, Exponential Smoothing, and Tracking Signals

> *"Industrial and systems engineering makes flow, variability, constraints, people, and decisions explicit."*

---

## Before You Start

**Prerequisites:** MATH-1D-033-07

**Route:** FE Industrial & Systems. This is a Layer 3 discipline-track chapter.

**Skip if:** You can formulate the model, identify its assumptions, apply the correct Handbook relation or learned workflow, and interpret the result operationally.

**Time:** About 90–120 min reading and worked examples · 40–50 min review questions · 65–85 min practice problems.

---

## On the Board Today

This chapter develops **Forecasting — Moving Averages, Exponential Smoothing, and Tracking Signals** for the FE Industrial & Systems route. Shared mathematics, economics, software, safety, and engineering-science concepts are reused through prerequisites rather than re-owned.

---

## Learning Objectives

By the end of this chapter, you will be able to:
* **67.1** Explain and apply **Time-Series Components and Forecast Horizon**.
* **67.2** Explain and apply **Moving-Average Forecast**.
* **67.3** Explain and apply **Exponential Smoothing**.
* **67.4** Explain and apply **Forecast Error Metrics**.
* **67.5** Explain and apply **Tracking Signals and Bias**.
* **67.6** Explain and apply **Trend and Seasonal Adjustment**.
* **67.7** Explain and apply **Forecast Integration with Planning**.

---

## Notation Used Here

Define the objective, decision variables, system boundary, time basis, units, stochastic assumptions, and performance denominator before calculation. Distinguish local metrics from total-system outcomes.

---

## 67.1 Time-Series Components and Forecast Horizon

Forecast method selection depends on data pattern and decision horizon.

\\[D_t=\\text{level}+\\text{trend}+\\text{seasonality}+\\text{noise}\\]

![FIG-03-67-001: Textbook-quality industrial engineering diagram illustrating time-series components and forecast horizon with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-67-001-time-series-components-and-forecast-horizon.png)

### Worked Example 1

**Problem.** A stable series without trend may support a simple smoothing method.

**Solution.** A level-only smoothing model is plausible when the series fluctuates around a relatively stable mean without persistent trend or seasonality. Plot the history first; if systematic trend or seasonal structure is present, a level-only method will lag or bias the forecast.

---

## 67.2 Moving-Average Forecast

Moving averages smooth noise but lag changes; larger windows smooth more.

\\[\\hat d_t=\\frac1n\\sum_{i=1}^n d_{t-i}\\]

![FIG-03-67-002: Textbook-quality industrial engineering diagram illustrating moving-average forecast with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-67-002-moving-average-forecast.png)

### Worked Example 2

**Problem.** 90, 100, and 110 average to 100.

**Solution.** The 3-period moving average is \((90+100+110)/3=300/3=\mathbf{100}\). Every included observation receives equal weight \(1/3\), and the oldest value drops out when the window advances.

---

## 67.3 Exponential Smoothing

The smoothing constant controls responsiveness to recent observations.

\\[\\hat d_t=\\alpha d_{t-1}+(1-\\alpha)\\hat d_{t-1}\\]

![FIG-03-67-003: Textbook-quality industrial engineering diagram illustrating exponential smoothing with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-67-003-exponential-smoothing.png)

### Worked Example 3

**Problem.** α=0.2, previous forecast 100, latest actual 110 gives 102.

**Solution.** Simple exponential smoothing gives \(\hat d_t=0.2(110)+0.8(100)=22+80=\mathbf{102}\). The new forecast moves only 20% of the latest 10-unit error because \(\alpha=0.2\).

---

## 67.4 Forecast Error Metrics

Accuracy metrics weight forecast errors differently; choose a metric consistent with the decision.

\\[MAD=\\frac1n\\sum|e_t|,\\quad MSE=\\frac1n\\sum e_t^2\\]

![FIG-03-67-004: Textbook-quality industrial engineering diagram illustrating forecast error metrics with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-67-004-forecast-error-metrics.png)

### Worked Example 4

**Problem.** Errors -10, 0, +10 have MAD 6.67.

**Solution.** For errors \(-10,0,+10\), \(MAD=(10+0+10)/3=20/3=\mathbf{6.67}\). Squaring instead would produce MSE, which penalizes large errors more heavily.

---

## 67.5 Tracking Signals and Bias

A tracking signal compares cumulative signed error with typical absolute error to reveal bias.

\\[TS=\\frac{RSFE}{MAD}\\]

![FIG-03-67-005: Textbook-quality industrial engineering diagram illustrating tracking signals and bias with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-67-005-tracking-signals-and-bias.png)

### Worked Example 5

**Problem.** Repeated underforecasting produces cumulative positive error when e=actual-forecast.

**Solution.** With \(e_t=actual-forecast\), repeated underforecasting gives mostly positive errors, so RSFE becomes positive. The tracking signal \(TS=RSFE/MAD\) therefore becomes positive and can reveal persistent forecast bias.

---

## 67.6 Trend and Seasonal Adjustment

Trend and seasonality require more than a level-only smoothing model.

\\[\\hat D=(\\text{level}+h\\,\\text{trend})\\times\\text{seasonal factor}\\]

![FIG-03-67-006: Textbook-quality industrial engineering diagram illustrating trend and seasonal adjustment with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-67-006-trend-and-seasonal-adjustment.png)

### Worked Example 6

**Problem.** A seasonal factor greater than one raises a baseline forecast.

**Solution.** A multiplicative seasonal factor above 1 scales the baseline upward for a high-season period. For example, a baseline 100 with seasonal factor 1.20 gives **120 units** before any additional adjustments.

---

## 67.7 Forecast Integration with Planning

Forecasts are inputs to inventory, capacity, workforce, and financial plans, not guaranteed outcomes.

\\[\\text{forecast}\\neq\\text{commitment}\\]

![FIG-03-67-007: Textbook-quality industrial engineering diagram illustrating forecast integration with planning with labeled variables, flow, decision points, and relevant performance measures.](../figures/FIG-03-67-007-forecast-integration-with-planning.png)

### Worked Example 7

**Problem.** A plan may exceed the point forecast to meet a service target under uncertainty.

**Solution.** A statistical point forecast is not a production commitment. Planning can add safety capacity, service-stock targets, scenario ranges, or contractual requirements to account for forecast uncertainty and asymmetric shortage/overage consequences.

---

## Integrated Worked Examples

### Worked Example 8

**Problem.** A numerical optimum violates an operating rule omitted from the model. Is it implementable?

**Solution.** In **Forecasting — Moving Averages, Exponential Smoothing, and Tracking Signals**, do not accept a local optimum or locally improved metric until it is checked against the chapter's system boundary and feasibility conditions. Industrial-and-systems problems commonly fail when a local improvement shifts delay, cost, risk, inventory, workload, defects, or constraints elsewhere in the system.

### Worked Example 9

**Problem.** A remembered formula differs from the FE Reference Handbook expression. Which should govern?

**Solution.** For this chapter, the FE Reference Handbook relation and variable definitions control whenever the Handbook supplies them. Use the external source set **HYNDMAN** only for specification-required learned material not fully developed in the Handbook.

---

## As the Handbook States It

Primary source basis: **FE Industrial & Systems specification Area(s) 8; FE Reference Handbook 10.6 Industrial and Systems Engineering, printed pp. 422–435.**

**Source boundary:** **FE-Handbook-supported** material is the portion directly supported by the FE Reference Handbook locations recorded in the ledger. **Externally supported** material is specification-required industrial/systems engineering knowledge not fully developed in the Handbook. **Guide synthesis** connects those sources into exam-oriented explanations, worked examples, and decision checks; it is not presented as Handbook text.

**Recommended external references for this chapter:**
- Hyndman, R. J., & Athanasopoulos, G. (2021, continuously updated online). *Forecasting: Principles and Practice* (3rd ed.). OTexts. Supporting scope: Time-series exploration, moving averages, exponential smoothing, trend/seasonality, forecast accuracy, and forecast validation.

External references support the learned/application portion of the Industrial and Systems specification. They do not replace the FE Reference Handbook as the exam reference.

---

## Where This Goes Wrong

**Using industrial time-series decomposition without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using moving average forecast without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using exponential smoothing without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using forecast error metric without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using forecast tracking signal without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using trend-seasonal forecast without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Using forecast-to-plan interface without its assumptions.** Confirm data basis, units, horizon, stochastic assumptions, constraints, and denominator.

**Optimizing a local metric instead of the system.** Throughput, quality, inventory, safety, staffing, cost, and service can trade off.

**Confusing statistical evidence with operational value.** Detectable differences may still be too small, too costly, or noncausal.

---

## Key Terms

| Term | Working definition |
|---|---|
| industrial time-series decomposition | Industrial/systems concept developed in §67.1; apply with the stated model assumptions and decision basis. |
| moving average forecast | Industrial/systems concept developed in §67.2; apply with the stated model assumptions and decision basis. |
| exponential smoothing | Industrial/systems concept developed in §67.3; apply with the stated model assumptions and decision basis. |
| forecast error metric | Industrial/systems concept developed in §67.4; apply with the stated model assumptions and decision basis. |
| forecast tracking signal | Industrial/systems concept developed in §67.5; apply with the stated model assumptions and decision basis. |
| trend-seasonal forecast | Industrial/systems concept developed in §67.6; apply with the stated model assumptions and decision basis. |
| forecast-to-plan interface | Industrial/systems concept developed in §67.7; apply with the stated model assumptions and decision basis. |

---

## Review Questions

### Conceptual and Applied

1. Define **industrial time-series decomposition** and identify the principal objective, state variable, metric, or decision it organizes.

2. Define **moving average forecast** and identify the principal objective, state variable, metric, or decision it organizes.

3. Define **exponential smoothing** and identify the principal objective, state variable, metric, or decision it organizes.

4. Define **forecast error metric** and identify the principal objective, state variable, metric, or decision it organizes.

5. Define **forecast tracking signal** and identify the principal objective, state variable, metric, or decision it organizes.

6. Define **trend-seasonal forecast** and identify the principal objective, state variable, metric, or decision it organizes.

7. Define **forecast-to-plan interface** and identify the principal objective, state variable, metric, or decision it organizes.

8. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **industrial time-series decomposition**?

9. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **moving average forecast**?

10. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **exponential smoothing**?

11. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **forecast error metric**?

12. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **forecast tracking signal**?

13. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **trend-seasonal forecast**?

14. What assumption, unit basis, stochastic condition, or model limitation must be checked before using **forecast-to-plan interface**?

15. Why should the system boundary and objective be defined before selecting a method?

16. Why is a mathematically optimal or statistically significant result not automatically an operationally good decision?

17. Why should the exact Handbook relation govern over a remembered variant?

18. What system-level reasonableness check should be performed after calculation?

### Multiple Choice

19. Which statement is most accurate for **industrial time-series decomposition**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

20. Which statement is most accurate for **moving average forecast**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

21. Which statement is most accurate for **exponential smoothing**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

22. Which statement is most accurate for **forecast error metric**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

23. Which statement is most accurate for **forecast tracking signal**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

24. Which statement is most accurate for **trend-seasonal forecast**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

25. Which statement is most accurate for **forecast-to-plan interface**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

26. Which statement is most accurate for **industrial time-series decomposition**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative

27. Which statement is most accurate for **moving average forecast**?
A) Its assumptions, units, and system basis must be checked
B) It is independent of decision context
C) It replaces model validation
D) It is always only qualitative


---

## Answer Key with Explanations

1. **industrial time-series decomposition** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

2. **moving average forecast** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

3. **exponential smoothing** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

4. **forecast error metric** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

5. **forecast tracking signal** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

6. **trend-seasonal forecast** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

7. **forecast-to-plan interface** is developed in its numbered section. Apply its displayed relation or workflow with the stated assumptions.

8. For **industrial time-series decomposition**, verify data basis, units, capacity/probability conditions, and operational feasibility.

9. For **moving average forecast**, verify data basis, units, capacity/probability conditions, and operational feasibility.

10. For **exponential smoothing**, verify data basis, units, capacity/probability conditions, and operational feasibility.

11. For **forecast error metric**, verify data basis, units, capacity/probability conditions, and operational feasibility.

12. For **forecast tracking signal**, verify data basis, units, capacity/probability conditions, and operational feasibility.

13. For **trend-seasonal forecast**, verify data basis, units, capacity/probability conditions, and operational feasibility.

14. For **forecast-to-plan interface**, verify data basis, units, capacity/probability conditions, and operational feasibility.

15. In **Forecasting — Moving Averages, Exponential Smoothing, and Tracking Signals**, the model boundary determines what is included in the decision. A valid solution must plot the time series, preserve the error sign convention, compare holdout accuracy, check for trend/seasonality, and distinguish forecast from planning commitment.

16. Units and operational definitions are part of the model, not formatting details. For **Forecasting — Moving Averages, Exponential Smoothing, and Tracking Signals**, convert quantities to a common basis before combining them and state the denominator/capacity/time basis explicitly.

17. The FE Reference Handbook is the exam reference when it supplies the relation for **Forecasting — Moving Averages, Exponential Smoothing, and Tracking Signals**. The external sources HYNDMAN support learned specification content not fully developed in the Handbook.

18. A quick limiting check for **Forecasting — Moving Averages, Exponential Smoothing, and Tracking Signals** is to set \(lpha=1\) and confirm simple exponential smoothing uses the latest actual as the next forecast; set all errors to zero and confirm MAD/MSE/RSFE are zero. Failure to reduce correctly indicates a model, sign, boundary, or arithmetic problem.

19. **A.** Section §67.1, **Time-Series Components and Forecast Horizon**, is based on \(D_t=\\text{level}+\\text{trend}+\\text{seasonality}+\\text{noise}\\). Interpret the result within the specific assumptions and system boundary of §67.1; do not transfer it automatically to a different operating regime.

20. **A.** Section §67.2, **Moving-Average Forecast**, is based on \(\\hat d_t=\\frac1n\\sum_{i=1}^n d_{t-i}\\). Interpret the result within the specific assumptions and system boundary of §67.2; do not transfer it automatically to a different operating regime.

21. **A.** Section §67.3, **Exponential Smoothing**, is based on \(\\hat d_t=\\alpha d_{t-1}+(1-\\alpha)\\hat d_{t-1}\\). Interpret the result within the specific assumptions and system boundary of §67.3; do not transfer it automatically to a different operating regime.

22. **A.** Section §67.4, **Forecast Error Metrics**, is based on \(MAD=\\frac1n\\sum|e_t|,\\quad MSE=\\frac1n\\sum e_t^2\\). Interpret the result within the specific assumptions and system boundary of §67.4; do not transfer it automatically to a different operating regime.

23. **A.** Section §67.5, **Tracking Signals and Bias**, is based on \(TS=\\frac{RSFE}{MAD}\\). Interpret the result within the specific assumptions and system boundary of §67.5; do not transfer it automatically to a different operating regime.

24. **A.** Section §67.6, **Trend and Seasonal Adjustment**, is based on \(\\hat D=(\\text{level}+h\\,\\text{trend})\\times\\text{seasonal factor}\\). Interpret the result within the specific assumptions and system boundary of §67.6; do not transfer it automatically to a different operating regime.

25. **A.** Section §67.7, **Forecast Integration with Planning**, is based on \(\\text{forecast}\\neq\\text{commitment}\\). Interpret the result within the specific assumptions and system boundary of §67.7; do not transfer it automatically to a different operating regime.

26. **A.** An integrated Forecasting — Moving Averages, Exponential Smoothing, and Tracking Signals decision must remain mathematically feasible and operationally implementable after resource, integer, timing, uncertainty, quality, safety, and system-boundary constraints are considered.

27. **A.** This chapter separates FE-Handbook-supported material from externally supported material and guide synthesis. The source-boundary section lists the external references used for Forecasting — Moving Averages, Exponential Smoothing, and Tracking Signals.


---

## Practice Problems

1. A stable series without trend may support a simple smoothing method.

2. 90, 100, and 110 average to 100.

3. α=0.2, previous forecast 100, latest actual 110 gives 102.

4. Errors -10, 0, +10 have MAD 6.67.

5. Repeated underforecasting produces cumulative positive error when e=actual-forecast.

6. A seasonal factor greater than one raises a baseline forecast.

7. A plan may exceed the point forecast to meet a service target under uncertainty.

8. Identify one feasibility, unit, probability, or denominator check that should be performed before accepting the result.

9. Identify the FE Industrial & Systems specification area and Handbook section most relevant to this chapter.

10. Give one system-level check that could reveal a locally optimal but globally poor decision.


---

## Practice Problem Solutions

1. **Independent solution for §67.1 — Time-Series Components and Forecast Horizon.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: A level-only smoothing model is plausible when the series fluctuates around a relatively stable mean without persistent trend or seasonality. Plot the history first; if systematic trend or seasonal structure is present, a level-only method will lag or bias the forecast.

2. **Independent solution for §67.2 — Moving-Average Forecast.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: The 3-period moving average is \((90+100+110)/3=300/3=\mathbf{100}\). Every included observation receives equal weight \(1/3\), and the oldest value drops out when the window advances.

3. **Independent solution for §67.3 — Exponential Smoothing.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: Simple exponential smoothing gives \(\hat d_t=0.2(110)+0.8(100)=22+80=\mathbf{102}\). The new forecast moves only 20% of the latest 10-unit error because \(\alpha=0.2\).

4. **Independent solution for §67.4 — Forecast Error Metrics.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: For errors \(-10,0,+10\), \(MAD=(10+0+10)/3=20/3=\mathbf{6.67}\). Squaring instead would produce MSE, which penalizes large errors more heavily.

5. **Independent solution for §67.5 — Tracking Signals and Bias.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: With \(e_t=actual-forecast\), repeated underforecasting gives mostly positive errors, so RSFE becomes positive. The tracking signal \(TS=RSFE/MAD\) therefore becomes positive and can reveal persistent forecast bias.

6. **Independent solution for §67.6 — Trend and Seasonal Adjustment.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: A multiplicative seasonal factor above 1 scales the baseline upward for a high-season period. For example, a baseline 100 with seasonal factor 1.20 gives **120 units** before any additional adjustments.

7. **Independent solution for §67.7 — Forecast Integration with Planning.** Recompute from the practice givens using the section model, then compare the result with the physical/operational interpretation. The corresponding chapter example demonstrates the key reasoning: A statistical point forecast is not a production commitment. Planning can add safety capacity, service-stock targets, scenario ranges, or contractual requirements to account for forecast uncertainty and asymmetric shortage/overage consequences.

8. For an integrated **Forecasting — Moving Averages, Exponential Smoothing, and Tracking Signals** problem, reject any result that violates this chapter-specific screen: plot the time series, preserve the error sign convention, compare holdout accuracy, check for trend/seasonality, and distinguish forecast from planning commitment.

9. For **Forecasting — Moving Averages, Exponential Smoothing, and Tracking Signals**, start with the FE Industrial and Systems specification area and Handbook location recorded in the ledger. For `split_required` material, use **HYNDMAN** for the learned portion rather than inventing a Handbook page.

10. Use this independent limiting case: set \(lpha=1\) and confirm simple exponential smoothing uses the latest actual as the next forecast; set all errors to zero and confirm MAD/MSE/RSFE are zero. The reduced case should behave as stated before the full model is trusted.

---

## Quick Reference

**Source anchor:** FE Industrial & Systems specification Area(s) 8.

- **industrial time-series decomposition:** Time-Series Components and Forecast Horizon
- **moving average forecast:** Moving-Average Forecast
- **exponential smoothing:** Exponential Smoothing
- **forecast error metric:** Forecast Error Metrics
- **forecast tracking signal:** Tracking Signals and Bias
- **trend-seasonal forecast:** Trend and Seasonal Adjustment
- **forecast-to-plan interface:** Forecast Integration with Planning

---

## What's Next

**Chapter 03-68: Inventory, Aggregate Planning, MRP, Sequencing, and Theory of Constraints**

Carry forward the same FE workflow: define the system and objective, establish variables/units/assumptions, choose the Handbook relation or learned method, solve, then verify feasibility and total-system consequences.

— Your Mentor
