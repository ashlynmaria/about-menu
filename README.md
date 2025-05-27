# 🌳 Recursive Artistry Program

An interactive Python application showcasing the power of **functions** and **recursion**.  
Explore factorials, Fibonacci numbers, and draw a stunning **gradient** fractal tree with Turtle graphics.

---

## 📋 Contents

- [Overview](#-overview)  
- [Prerequisites](#-prerequisites)  
- [Installation](#-installation)  
- [Usage](#-usage)  
- [Features](#-features)  
- [Code Walkthrough](#-code-walkthrough)  
- [Example Runs](#example-runs)  
- [Fractal Tree Image](#fractal-tree-image)  

---

## 🔍 Overview

The **Recursive Artistry Program** offers a menu-driven interface to:
1. Calculate the factorial of a non-negative integer.  
2. Compute the nth Fibonacci number.  
3. Draw a depth-based **gradient** fractal tree using Turtle graphics.  
4. Exit the program.

---

## ⚙️ Prerequisites

- **Python 3.x**  
- **tkinter** library (for Turtle graphics)  
- **colorsys** (built into Python)  
- A terminal or command prompt

---

## 🛠 Installation

1. Clone or download the repository.  
2. Ensure `tkinter` is installed:
   ```bash
   # Debian/Ubuntu
   sudo apt update && sudo apt install python3-tk

   # Fedora/RHEL
   sudo dnf install python3-tkinter
   ```

---

## 🚀 Usage

1. Navigate to the project directory.  
2. Run the script:
   ```bash
   python recursive_artistry.py
   ```
3. Select an option from the menu by entering **1**, **2**, **3**, or **4**.

---

## ⭐ Features

- **Factorial**: Recursive calculation with input validation.  
- **Fibonacci**: Recursive sequence generator.  
- **Gradient Fractal Tree**: Uses Turtle + `colorsys` to draw a multicolored fractal tree.  
- **User-Friendly**: Clear prompts, error handling, and looped menu.

---

## 📝 Code Walkthrough

**Depth-based gradient in `draw_fractal`:**  
```python
import colorsys

def draw_fractal(branch_len, t, depth=0):
    if branch_len < 10:
        return
    # Map depth to hue (0.33 green → 0.0 red)
    hue = 0.33 * max(0, 1 - depth / 10)
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    t.pencolor(r, g, b)
    # ... continue recursion ...
```
And remember to set:
```python
screen.colormode(1.0)
```
to enable floating-point RGB values.

---

## 📂 Example Runs

```text
Welcome to the Recursive Artistry Program!

Please choose an option:
  1. Calculate Factorial
  2. Find Fibonacci Number
  3. Draw a Recursive Fractal (requires turtle)
  4. Exit

Enter your choice (1-4): 1
Enter a non-negative integer for factorial: 5
The factorial of 5 is 120.

Enter your choice (1-4): 2
Enter a non-negative integer for Fibonacci: 7
The 7th Fibonacci number is 13.

Enter your choice (1-4): 3
Launching fractal tree drawing… close the window when done.
```

---

## Fractal Tree Image

![Fractal Tree](images/fractal_drawing.png)

---

