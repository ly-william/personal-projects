import turtle

turtle = turtle.Turtle()
screen = turtle.getscreen()
screen.title("Tic-tac-toe")

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


def letterX(t, length):

    half_length = length / 2
    hypotenuse = (2 * half_length ** 2) ** 0.5

    t.pendown()
    t.right(45)
    t.forward(half_length)
    t.left(135)

    t.penup()
    t.forward(hypotenuse)
    t.pendown()

    t.left(135)
    t.forward(length)
    t.right(135)

    t.penup()
    t.forward(hypotenuse)
    t.pendown()

    t.right(135)
    t.forward(half_length)
    t.left(45)
    t.penup()


def draw_X():
    letterX(turtle, 100)


def draw_O():
    turtle.up()
    turtle.back(50)
    turtle.down()
    turtle.right(90)
    turtle.circle(45)


def draw_play_again():
    turtle.up()


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
    global is_drawing

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

    is_won, points = check_win()

    if is_won:
        draw_win_line(points)
        draw_play_again()
        screen.onclick(handle_reset_game_click)

    if check_tie():
        draw_play_again()
        screen.onclick(handle_reset_game_click)

    is_drawing = False


def check_tie():
    for row in range(3):
        for column in range(3):
            if array_2d[row][column] == "-":
                return False
    return True


def handle_reset_game_click(foo, bar):
    # Clear screen
    turtle.reset()
    # Starts game again
    start_game()


def draw_win_line(points):
    # print(f"{points[0]} {points[1]}")
    direction = points[1]
    padding = 20

    # Vertical wins
    if direction == "vertical":
        first_column = TOP_LEFT_X + points[0][1] * BOX_WIDTH + BOX_WIDTH // 2
        first_row = TOP_LEFT_Y - padding
        second_column = first_column
        second_row = -first_row

    # Horizontal wins
    if direction == "horizontal":
        first_column = TOP_LEFT_X + padding
        first_row = TOP_LEFT_Y - (points[0][0] * BOX_HEIGHT + BOX_HEIGHT // 2)
        second_column = -first_column
        second_row = first_row

    # Top-left to bottom-right wins
    if direction == "top-bottom":
        first_column = TOP_LEFT_X + padding
        first_row = TOP_LEFT_Y - padding
        second_column = -first_column
        second_row = -first_row

    # Bottom-left to top-right wins
    if direction == "bottom-top":
        first_column = TOP_LEFT_X + padding
        first_row = -TOP_LEFT_Y + padding
        second_column = -TOP_LEFT_X - padding
        second_row = TOP_LEFT_Y - padding

    turtle.up()
    turtle.goto(first_column, first_row)
    turtle.down()
    turtle.color("red")
    turtle.goto(second_column, second_row)
    turtle.hideturtle()


def check_win():
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
                points = [(row, 0), "horizontal"]
                return True, points

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
                points = [(0, column), "vertical"]
                return True, points

    # Check diagonal (top-left to bottom-right)
    for i in range(3):
        first_char = array_2d[0][0]
        if first_char == "-":
            break
        compare = array_2d[i][i]
        if first_char != compare:
            break
        if i == 2:
            return True, [(0, 0), "top-bottom"]

    # Check diagonal (bottom-left to top-right)
    for i in range(3):
        first_char = array_2d[2][0]
        if first_char == "-":
            break
        compare = array_2d[2 - i][i]
        if first_char != compare:
            break
        if i == 2:
            return True, [(2, 0), "bottom-top"]

    return False, []


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


def start_game():
    global x_turn
    x_turn = True
    turtle.pencolor("black")
    turtle.pensize(12)
    turtle.speed(15)
    global array_2d
    array_2d = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"],
    ]
    draw_column_lines()
    draw_row_lines()
    draw_borders()
    turtle.pensize(10)
    turtle.speed(10)
    screen.onclick(handle_click)


start_game()

# Keeps the window open
screen.mainloop()
