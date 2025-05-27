import sys
import turtle
import colorsys

def factorial(n):
    """Recursively compute n! (factorial)."""
    if n < 0:
        raise ValueError("Negative numbers do not have a factorial.")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Recursively compute the nth Fibonacci number."""
    if n < 0:
        raise ValueError("Negative index is not allowed.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def draw_fractal(branch_len, t, depth=0):
    """
    Draw a fractal tree with a depth-based color gradient.
    branch_len: length of the current branch
    t: the turtle instance
    depth: recursion depth, used to compute hue
    """
    if branch_len < 10:
        return

    # Map depth to a hue between green (0.33) and red (0.0)
    hue = 0.33 * max(0, 1 - depth / 10)
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    t.pencolor(r, g, b)

    t.forward(branch_len)
    t.left(30)
    draw_fractal(branch_len * 0.7, t, depth + 1)
    t.right(60)
    draw_fractal(branch_len * 0.7, t, depth + 1)
    t.left(30)
    t.backward(branch_len)


def prompt_positive_integer(prompt):
    """
    Prompt the user until they enter a valid non-negative integer.
    Returns the integer.
    """
    while True:
        entry = input(prompt).strip()
        if not entry.isdigit():
            print("Invalid input. Please enter a non-negative integer.")
            continue
        value = int(entry)
        return value

def main():
    print("Welcome to the Recursive Artistry Program!")
    while True:
        print("""
Please choose an option:
  1. Calculate Factorial
  2. Find Fibonacci Number
  3. Draw a Recursive Fractal (requires turtle)
  4. Exit
""")
        choice = input("Enter your choice (1–4): ").strip()
        if choice == '1':
            n = prompt_positive_integer("Enter a non-negative integer for factorial: ")
            print(f"The factorial of {n} is {factorial(n)}.\n")
        elif choice == '2':
            n = prompt_positive_integer("Enter a non-negative integer for Fibonacci: ")
            print(f"The {n}th Fibonacci number is {fibonacci(n)}.\n")
        elif choice == '3':
            print("Launching fractal tree drawing… close the window when done.")
            try:
                screen = turtle.Screen()
                screen.setup(width=800, height=600)
                screen.title("Recursive Fractal Tree")
                t = turtle.Turtle()
                t.speed("fastest")
                t.left(90)
                t.penup()
                t.backward(100)
                t.pendown()
                t.color("green")
                draw_fractal(100, t, depth=0)
                screen.exitonclick()
                turtle.bye()
            except turtle.Terminator:
                pass  
            print()
        elif choice == '4':
            print("Goodbye! Thanks for exploring recursion.")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    main()