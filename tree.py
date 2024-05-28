import turtle

# Screen settings
WIDTH, HEIGHT = 1600, 900
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor('#000')

# Turtle settings
leo = turtle.Turtle()
leo.speed(0)

def draw_branch(t, branch_length, angle, factor, thickness):
    if branch_length > 5:
        # Set the color gradient for the trunk and branches
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

# Initial position
leo.penup()
leo.goto(0, -HEIGHT // 2 + 50)
leo.pendown()
leo.left(90)

# Parameters for tree
initial_branch_length = 150
angle = 22
length_factor = 15
initial_thickness = 20  # Increased initial thickness

# Draw the tree
draw_branch(leo, initial_branch_length, angle, length_factor, initial_thickness)

# Hide the turtle and display the result
leo.hideturtle()
screen.exitonclick()
