import queue
import time

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

def print_maze(maze, path=[]):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if (i, j) in path:
                print('X', end=' ')
            else:
                print(cell, end=' ')
        print()

def find_start(maze):
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 'O':
                return i, j
    return None

def find_path(maze):
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
            time.sleep(0.02) 
            print_maze(maze, path + [neighbour])
            print()

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

path = find_path(maze)
print_maze(maze, path)

