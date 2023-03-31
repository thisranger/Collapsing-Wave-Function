tiles = ["0000","0001","0011","0101","0111","1111"]

def create_tiles(tiles):
    b = []
    for i in tiles:
        for v in range(len(i)):
            b.append(i[v:]+i[:v])
    return list(dict.fromkeys(b))

def create_tilesmap(tiles):
    map = []
    for b in tiles:
        map.append([[0,0,0],[0,3,0],[0,0,0]])
        if b[0] != "0":
            map[-1][1][0] = 2
        if b[1] != "0":
            map[-1][2][1] = 2
        if b[2] != "0":
            map[-1][1][2] = 2
        if b[3] != "0":
            map[-1][0][1] = 2
    return map

print(create_tiles(tiles))
print(create_tilesmap(create_tiles(tiles)))
