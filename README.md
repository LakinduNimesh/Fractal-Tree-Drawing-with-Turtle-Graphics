# Fractal Tree Drawing with Turtle Graphics

This project demonstrates how to use the Python `turtle` module to draw a fractal tree. The tree is drawn recursively, with each branch splitting into two smaller branches. The colors and thickness of the branches change depending on their length, creating a natural-looking fractal tree.

## Features

- **Fractal Tree Drawing**: Uses recursion to draw a tree with branches that split and reduce in size.
- **Color Gradient**: Applies different colors to branches based on their length to simulate a natural look.
- **Adjustable Parameters**: Change the initial branch length, angle, length factor, and initial thickness to customize the tree's appearance.

## Prerequisites

- Python 3.x
- `turtle` module (included with Python standard library)

## How to Run

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/LakinduNimesh/Fractal-Tree-Drawing-with-Turtle-Graphics.git
   cd Fractal-Tree-Drawing-with-Turtle-Graphics
   ```

2. **Run the Script**:
   ```sh
   python tree.py
   ```

The tree drawing will open in a new window. Click on the window to close it after the drawing is complete.

## Code Explanation

### Screen Settings
```python
WIDTH, HEIGHT = 1600, 900
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor('#000')
```
Sets up the screen dimensions and background color.

### Turtle Settings
```python
leo = turtle.Turtle()
leo.speed(0)
```
Initializes the turtle and sets its drawing speed to the maximum.

### Draw Branch Function
```python
def draw_branch(t, branch_length, angle, factor, thickness):
    if branch_length > 5:
        if branch_length > 60:
            t.color('#8B4513')  # Light brown for thicker branches
        elif branch_length > 20:
            t.color('#FFD700')  # Yellow for medium branches
        else:
            t.color('green')  # Green for the tips

        t.pensize(thickness)
        t.forward(branch_length)
        t.right(angle)
        
        draw_branch(t, branch_length - factor, angle, factor, thickness * 0.8)
        
        t.left(2 * angle)
        
        draw_branch(t, branch_length - factor, angle, factor, thickness * 0.8)
        
        t.right(angle)
        t.backward(branch_length)
```
This recursive function draws the branches of the tree. The branch length and thickness decrease with each recursive call, and the turtle changes direction to create the branching effect.

### Initial Position and Parameters
```python
leo.penup()
leo.goto(0, -HEIGHT // 2 + 50)
leo.pendown()
leo.left(90)

initial_branch_length = 150
angle = 22
length_factor = 15
initial_thickness = 20
```
Sets the initial position and orientation of the turtle, and defines the parameters for the tree.

### Draw the Tree
```python
draw_branch(leo, initial_branch_length, angle, length_factor, initial_thickness)
leo.hideturtle()
screen.exitonclick()
```
Calls the `draw_branch` function to start drawing the tree, hides the turtle, and waits for a click to close the window.

## Customization

You can modify the following parameters to change the appearance of the tree:
- `initial_branch_length`: Length of the initial branch.
- `angle`: Angle between branches.
- `length_factor`: Amount by which each subsequent branch is shorter than the previous one.
- `initial_thickness`: Thickness of the initial branch.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

Inspired by fractal trees and the capabilities of the `turtle` module in Python.

