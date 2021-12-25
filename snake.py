import os
import random
import time
import keyboard

BOARD_SIZE = 20
LOOPTIME = 0.3


def set_food():
    while True:
        new_pos = (random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1))
        if new_pos not in snake:
            return new_pos


def keyboard_detection():
    return keyboard.is_pressed("a") or keyboard.is_pressed("left arrow"), \
           keyboard.is_pressed("d") or keyboard.is_pressed("right arrow"), \
           keyboard.is_pressed("w") or keyboard.is_pressed("up arrow"), \
           keyboard.is_pressed("s") or keyboard.is_pressed("down arrow")


snake = [(5, 10), (6, 10)]
snake_direction = (1, 0)
current_snake_direction = (1, 0)
food = set_food()

snake_index = 0

os.system("mode con: cols=" + str(int(BOARD_SIZE * 3.2)) + "lines=" + str(int(BOARD_SIZE * 1.15)))

time.sleep(0.5)

old_time = time.time()
loop_timer = 0
while True:
    delta_time = time.time() - old_time
    loop_timer += delta_time
    old_time = time.time()

    left, right, up, down = keyboard_detection()
    if snake_direction[0] != 0:
        if up:
            current_snake_direction = (0, -1)
        elif down:
            current_snake_direction = (0, 1)
    else:
        if left:
            current_snake_direction = (-1, 0)
        elif right:
            current_snake_direction = (1, 0)

    if loop_timer >= LOOPTIME:
        snake_direction = current_snake_direction
        loop_timer = 0
        last_part = snake[0]
        new_part = (snake[-1][0] + snake_direction[0], snake[-1][1] + snake_direction[1])
        if not food == new_part:
            snake.remove(last_part)
        else:
            food = set_food()
        snake.append(new_part)
        if len(snake) != len(set(snake)) or \
                new_part[0] < 0 or new_part[0] > BOARD_SIZE - 1 or new_part[1] < 0 or new_part[1] > BOARD_SIZE - 1:
            break
        board = ["  ." * BOARD_SIZE] * BOARD_SIZE
        for coords in snake:
            board[coords[1]] = board[coords[1]][:coords[0] * 3] + "ORM" + board[coords[1]][coords[0] * 3 + 3:]
        board[food[1]] = board[food[1]][:food[0] * 3] + "MAT" + board[food[1]][food[0] * 3 + 3:]
        board = " " + "___" * BOARD_SIZE + "__\n |" + "|\n |".join(board) + "|\n ¯¯" + "¯¯¯" * BOARD_SIZE
        print(board)

print(" YOU DIED\n" * BOARD_SIZE)
