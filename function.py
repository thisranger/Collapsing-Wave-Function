import numpy as np
import random

def find(set, tiles):
    mod_tiles = tiles.copy()
    for c, e in enumerate(set):
        t = 1
        while t <= len(mod_tiles):
            if mod_tiles[-t][c] != e and e != "-":
                mod_tiles.remove(mod_tiles[-t])
            else:
                t += 1
    return mod_tiles


def min(map):
    true_map = (map == -1)
    mod_map = np.zeros((len(map), len(map[0])))
    com_map = np.full((len(map), len(map[0])), 5)
    rule = lambda x: x == -1
    for x, o in enumerate(true_map):
        for y, u in enumerate(o):
            if x != 0 and u:
                mod_map[x - 1, y] += 1
            if x != len(true_map) - 1 and u:
                mod_map[x + 1, y] += 1
            if y != 0 and u:
                mod_map[x, y - 1] += 1
            if y != len(true_map) - 1 and u:
                mod_map[x, y + 1] += 1
    com_map[rule(map)] = mod_map[rule(map)]
    z = np.argwhere(com_map == np.min(com_map))
    if len(np.argwhere(map == -1)) == 0:
        return False
    return z[random.randint(0,len(z)-1)][0], z[random.randint(0,len(z)-1)][1]


def collapse(map, tiles):
    while True:
        tile = min(map)
        border = ""
        if tile is False:
            break

        if tile[1] == 0:
            border += "0"
        elif map[tile[0], tile[1] - 1] == -1:
            border += "-"
        else:
            border += tiles[map[tile[0], tile[1]-1]][2]

        if tile[0] == len(map) - 1:
            border += "0"
        elif map[tile[0] + 1, tile[1]] == -1:
            border += "-"
        else:
            border += tiles[map[tile[0] + 1, tile[1]]][3]

        if tile[1] == len(map) - 1:
            border += "0"
        elif map[tile[0], tile[1] + 1] == -1:
            border += "-"
        else:
            border += tiles[map[tile[0], tile[1] + 1]][0]

        if tile[0] == 0:
            border += "0"
        elif map[tile[0] - 1, tile[1]] == -1:
            border += "-"
        else:
            border += tiles[map[tile[0] - 1, tile[1]]][1]

        map[tile] = tiles.index(find(border, tiles)[random.randint(0,len(find(border, tiles))-1)])
    return map.tolist()

def display_map(map, tiles):
    display_map = np.full((len(map)*3, len(map[0])*3),0)
    for x in range(len(display_map)):
        for y in range(len(map)):
            display_map[x, y*3:y*3+3] = tiles[map[x//3][y]][x%3]
    return display_map
