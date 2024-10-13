import turtle
from pixart import initialization, draw_shape_from_string, draw_grid, draw_shape_from_file

def main():
    # asking the user for the type of drawing they want to do
    choice = input("Enter '1' for drawing with color code strings, '2' for grid with 2 colors, '3' for drawing from file: ")
    
    # setting up the turtle window
    turtle.bgcolor("#87CEEB") # sky blue background
    turta = turtle.Turtle()
    initialization(turta)

    if choice == '1':
        draw_shape_from_string(turta)
    elif choice == '2':
        draw_grid(turta)
    elif choice == '3':
        draw_shape_from_file(turta)
    else:
        print("Invalid choice.")

    turtle.done()

if __name__ == "__main__":
    main()
