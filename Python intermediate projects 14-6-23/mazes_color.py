import time
import curses
import queue

maze = [
    ["#", "#", "#", "#", "#", "O", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(stdscr, maze, path=[]):
    stdscr.clear()
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j * 3, 'X', curses.color_pair(1))
            else:
                stdscr.addstr(i, j * 3, cell, curses.color_pair(2))
    stdscr.refresh()

def find_start(maze):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 'O':
                return i, j
    return None

def find_path(stdscr, maze):
    start = find_start(maze)
    end = (len(maze) - 1, len(maze[0]) - 2)

    q = queue.Queue()
    q.put((start, [start]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        if current_pos == end:
            return path

        neighbours = find_neighbours(maze, row, col)
        for neighbour in neighbours:
            if neighbour in visited:
                continue
            row, col = neighbour

            if maze[row][col] == '#':
                continue

            new_path = path + [neighbour]
            q.put((neighbour, new_path))
            visited.add(neighbour)
            time.sleep(0.2)  # Delay of 0.2 seconds
            print_maze(stdscr, maze, path + [neighbour])

def find_neighbours(maze, row, col):
    neighbours = []
    if row > 0:  # UP
        neighbours.append((row - 1, col))
    if row + 1 < len(maze):  # DOWN
        neighbours.append((row + 1, col))
    if col > 0:  # LEFT
        neighbours.append((row, col - 1))
    if col + 1 < len(maze[0]):  # RIGHT
        neighbours.append((row, col + 1))
    return neighbours

def main(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    find_path(stdscr, maze)
    stdscr.getch()

curses.wrapper(main)
