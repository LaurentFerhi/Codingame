import sys
import numpy as np
from random import randint, sample
from collections import deque

def bfs(grid, start, end):
    queue = deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x,y) == end:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != '1' and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

def make_move(start,end):
    xs, ys = start[0], start[1]
    xe, ye = end[0], end[1]
    if xe-xs == 1 and ye==ys:
        return 'RIGHT'
    elif xe-xs == -1 and ye==ys:
        return 'LEFT'
    elif xe==xs and ye-ys == 1:
        return 'DOWN'
    elif xe==xs and ye-ys == -1:
        return 'UP'
    else:
        return 'ERROR'

def choose_move(direction,r,c):
    if direction == 'LEFT':
        return r, c-1
    elif direction == 'RIGHT':
        return r, c+1
    elif direction == 'UP':
        return r-1, c
    elif direction == 'DOWN':
        return r+1, c
    else:
        print('ERROR',file=sys.stderr)
        return 'ERROR','ERROR'

# lightpath
dico_players = {0:[],1:[],2:[],3:[]}

# Define grid
width, height = 30, 20
grid = [width*['.'] for _ in range(height)]

# game loop
while True:
    # n: total number of players (2 to 4).
    # p: your player number (0 to 3).
    n, p = [int(i) for i in input().split()]
    for i in range(n):
        x0, y0, x1, y1 = [int(j) for j in input().split()]
        dico_players[i].append((x1,y1))
        if i == p:
            x_now = x1
            y_now = y1
    start_point = (x_now, y_now)

    # Update grid
    for player in dico_players:
        for point in dico_players[player]:
            grid[point[1]][point[0]] = '1'

    # Make a destination (random) -> to be optimized
    valid = False
    while not valid:
        dest = (randint(0,width-1),randint(0,height-1))
        if grid[dest[1]][dest[0]] != '1' and dest != start_point:
            valid = True

    # Find shortest path to destination
    path = bfs(grid, start_point, dest)
    print(path,file=sys.stderr)

    # Case no path is found
    if path is None:
        directions = ['LEFT','RIGHT','UP','DOWN']
        valid_point = False
        while not valid_point:
            try_dir = sample(directions,1)[0]
            row_try, col_try = choose_move(try_dir, start_point[1], start_point[0])
            if grid[row_try][col_try] != '1': # to be optimized (case out of grid)
                valid_point = True
        print(try_dir)

    # Case path is found
    else:
        next_point = path[1]
        print(dest,start_point,next_point,file=sys.stderr)
        print(make_move(start_point,next_point))
