Wheat and the Chessboard Problem

## Overview

This project explores the famous Wheat and the Chessboard Problem, which demonstrates exponential growth by placing grains of wheat on a chessboard, doubling the count with each subsequent square. The project utilizes NumPy for calculations and Matplotlib for visualization.

## Objectives

- Gain familiarity with NumPy for numerical computations.
- Understand and visualize exponential growth.
- Explore different methods to compute values efficiently.
- Use Matplotlib to create bar graphs and heat maps.
- Compare the computational efficiency of different implementations.

## Problem Description

The problem states:

> "If a chessboard were to have wheat placed upon each square such that one grain were placed on the first square, two on the second, four on the third, and so on (doubling the number of grains on each subsequent square), how many grains of wheat would be on the chessboard at the finish?"

We extend the problem by implementing:

1. A 2x2 chessboard calculation.
2. A function for an **n × m** chessboard.
3. Total sum and column-wise average calculations.
4. Data visualization using bar graphs and heatmaps.
5. Analysis of exponential growth in the **second half of the chessboard**.
6. Alternative implementations using different NumPy techniques.
7. A comparison of computational time using **%%timeit** in Jupyter Notebook.

---

## Installation

- Python 3.7+
- Jupyter Notebook:

\
**TASK**:

### 1. Compute Wheat Distribution

### 2. Compute Total Wheat

### 3. Visualize Data

- Bar GrapH
- Heatmap

---

## Results:

- The number of grains grows **exponentially**, leading to massive values.
- **The second half of the chessboard** contains exponentially more grains than the first half.
- Different NumPy approaches (loops, `np.append()`, broadcasting) affect performance.
- Visualizations provide an intuitive understanding of exponential growth.

---

## References

- [Wheat and Chessboard Problem - Wikipedia](https://en.wikipedia.org/wiki/Wheat_and_chessboard_problem)
- [NumPy Documentation](https://numpy.org/doc/stable/)
- [Matplotlib Documentation](https://matplotlib.org/)

---

##

