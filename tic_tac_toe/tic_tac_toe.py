import turtle

turtle = turtle.Turtle()
screen = turtle.getscreen()
screen.title("Tic-tac-toe")
turtle.pensize(12)

SCREEN_WIDTH = screen.window_width()
SCREEN_HEIGHT = screen.window_height()

screen.setup(width=SCREEN_WIDTH * 1.1, height=SCREEN_WIDTH * 1.1)

screen.screensize(1000, 1000)

BOX_WIDTH = SCREEN_WIDTH // 3
BOX_HEIGHT = SCREEN_HEIGHT // 3
TOP_LEFT_POSITION = (-SCREEN_WIDTH // 2 + 2, SCREEN_HEIGHT // 2 - 2)
TOP_LEFT_X = TOP_LEFT_POSITION[0]
TOP_LEFT_Y = TOP_LEFT_POSITION[1]

array_2d = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],
]

x_turn = True
win = False
is_drawing = False


def draw_X():
    for angle in range(-135, 136, 90):
        mock = turtle.clone()
        mock.left(angle)
        mock.forward(100 / 2)
        mock.hideturtle()


def draw_O():
    turtle.up()
    turtle.back(50)
    turtle.down()
    turtle.right(90)
    turtle.circle(45)


# This function draws the column lines
def draw_column_lines():
    turtle.up()
    turtle.goto(TOP_LEFT_POSITION)
    for i in range(2):
        turtle.forward(BOX_WIDTH)
        turtle.down()
        turtle.right(90)
        turtle.forward(SCREEN_HEIGHT)
        turtle.backward(SCREEN_HEIGHT)
        turtle.left(90)
        turtle.up()


# This function draws the row lines
def draw_row_lines():
    turtle.up()
    turtle.goto(TOP_LEFT_POSITION)
    turtle.right(90)
    for i in range(2):
        turtle.forward(BOX_HEIGHT)
        turtle.down()
        turtle.left(90)
        turtle.forward(SCREEN_WIDTH)
        turtle.backward(SCREEN_WIDTH)
        turtle.right(90)
        turtle.up()


def prepare_draw(row, column, character):
    # Move to the center
    turtle.up()
    desired_x_pos = TOP_LEFT_X + (column * BOX_WIDTH + BOX_WIDTH // 2)
    desired_y_pos = TOP_LEFT_Y - (row * BOX_HEIGHT + BOX_HEIGHT // 2)
    turtle.goto(desired_x_pos, desired_y_pos)
    turtle.down()

    if character == "X":
        draw_X()
    if character == "O":
        draw_O()

    turtle.up()


def handle_click(x, y):
    global win
    global is_drawing
    if win:
        return

    if is_drawing:
        return

    is_drawing = True

    global x_turn
    # Checks horizontal borders
    if x < TOP_LEFT_X or x > -TOP_LEFT_X:
        return

    # Checks vertical borders
    if y > TOP_LEFT_Y or y < -TOP_LEFT_Y:
        return

    row, column = get_array_index(x, y)
    character = array_2d[row][column]
    # print(f"Row: {row} Column: {column}")
    # print(character)

    # If there is a X or O there, do nothing
    if character == "X" or character == "O":
        return

    if x_turn:
        array_2d[row][column] = "X"
        prepare_draw(row, column, "X")
        x_turn = False
    else:
        array_2d[row][column] = "O"
        prepare_draw(row, column, "O")
        x_turn = True

    if checkWin():
        win = True

    is_drawing = False


def checkWin():
    # Check horizontal wins
    for row in range(3):
        first_char = array_2d[row][0]
        if first_char == "-":
            continue
        for column in range(3):
            compare = array_2d[row][column]
            if first_char != compare:
                break

            if column == 2:
                return True

    # Check vertical wins
    for column in range(3):
        first_char = array_2d[0][column]
        if first_char == "-":
            continue
        for row in range(3):
            compare = array_2d[row][column]
            if first_char != compare:
                break

            if row == 2:
                return True

    # Check diagonal (top-left to bottom-right)
    for i in range(3):
        first_char = array_2d[0][0]
        if first_char == "-":
            break
        compare = array_2d[i][i]
        if first_char != compare:
            break
        if i == 2:
            return True

    # Check diagonal (bottom-left to top-right)
    for i in range(3):
        first_char = array_2d[2][0]
        if first_char == "-":
            break
        compare = array_2d[2 - i][i]
        if first_char != compare:
            break
        if i == 2:
            return True

    return False


def get_array_index(x, y):
    for i in range(4):
        if i == 0:
            continue

        if y > TOP_LEFT_Y - (i * BOX_HEIGHT):
            row = i - 1
            break

    for i in range(4):
        if i == 0:
            continue

        if x < TOP_LEFT_X + (i * BOX_WIDTH):
            column = i - 1
            break

    return row, column


def draw_borders():
    turtle.up()
    turtle.goto(TOP_LEFT_POSITION)
    turtle.down()
    for i in range(4):
        if i % 2 == 0:
            turtle.forward(SCREEN_HEIGHT)
        else:
            turtle.forward(SCREEN_WIDTH)
        turtle.left(90)


draw_column_lines()
draw_row_lines()
draw_borders()
turtle.pensize(10)
screen.onclick(handle_click)

# Keeps the window open
screen.mainloop()
