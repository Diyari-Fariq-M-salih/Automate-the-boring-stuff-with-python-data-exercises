# Automate the Boring Stuff with Python – Data Exercises & Notes

This repository contains **practice exercises inspired by _Automate the Boring Stuff with Python_**.  
It is designed as both:
- A **hands-on coding practice space**
- A set of **learning notes** for core Python concepts

The scripts focus on **logic, loops, functions, and problem-solving**, rather than complex libraries.

---

## Repository Structure

```text
Automate-the-boring-stuff-with-python-data-exercises-main/
├── Collatz_Sequence.py
├── heart_grid.py
└── .gitattributes
```

Each file is a **self-contained exercise** demonstrating a specific programming idea.

---

## 1. Collatz Sequence

### What This Script Does
This script implements the **Collatz Conjecture**, a famous mathematical sequence defined as:

For a number \( n \):

```
n = n / 2        if n is even
n = 3n + 1       if n is odd
```

The process is repeated until the number reaches **1**.

### Example
Starting with `6`:

```
6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
```

### Why This Is Interesting
- The sequence always reaches **1** (as far as tested), but **no formal proof exists**
- It’s a great way to practice:
  - `while` loops
  - Conditional logic
  - Input validation

### Analogy
Think of it like a **maze with strange rules**:
- Sometimes you halve your steps
- Sometimes you triple them and add one
- Somehow, you always find the exit

### What You Learn
- Control flow
- Integer arithmetic
- Defensive programming (handling bad input)

---

## 2. Heart Grid

### What This Script Does
This script prints a **heart shape** using characters arranged in a grid.

The shape emerges from:
- Nested lists
- Nested loops
- Careful spacing

### Core Concept: 2D Data Representation

A grid is stored as:

```
grid[row][column]
```

By looping through **columns first**, then rows, the output is rotated into a recognizable shape.

### Analogy
Imagine placing **pixels on graph paper**:
- Each character is a pixel
- Printing them in the right order draws an image

### What You Learn
- Nested lists
- Loop ordering
- Visual reasoning with data

---

## Using This Repository as Study Notes

### Recommended Approach
1. Run each script
2. Predict the output before running
3. Modify values and observe changes
4. Rewrite the logic in your own words

### Good Practice Ideas
- Add comments explaining each step
- Rewrite the Collatz script using functions
- Change the grid to draw new shapes

---

## Requirements

- Python 3.x
- No external libraries required

---

## Learning Outcomes

By completing these exercises, you strengthen:
- Logical thinking
- Loop control
- Problem decomposition
- Confidence reading and writing Python code

---

## Final Note

This repository is best treated as a **Python thinking notebook** —  
small programs that train you to reason clearly before scaling up to larger projects.
