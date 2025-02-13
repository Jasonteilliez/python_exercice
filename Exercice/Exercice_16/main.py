def get_nbr_of_living_neighbours(coordonnées, cells):
    i,j = coordonnées
    n = 0
    for x in range(-1,2):
        for y in range(-1,2):
            if x+i>=0 and x+i<len(cells) and y+j>=0 and y+j<len(cells[0]) and not (x==0 and y==0):
                n+=cells[i+x][j+y]
    return n

def get_state(coordonnées, cells):
    i,j = coordonnées
    if i>=0 and i<len(cells) and j>=0 and j<len(cells[0]):
        return cells[i][j]
    return 0

def new_state(state,neighbours):
    if state and neighbours == 2 or neighbours == 3:
        return 1
    return 0

def crop_cells(cells):
    # crop top
    crop = True
    while crop:
        if not cells:
            break
        for x in cells[0]:
            if x == 1 :
                crop = False
        if crop :
            cells.pop(0)

    # crop bottom
    crop = True
    while crop:
        if not cells:
            break
        for x in cells[-1]:
            if x == 1 :
                crop = False
        if crop :
            cells.pop(-1)

    # crop left
    crop = True
    while crop:
        if not cells:
            break
        for x in cells:
            if x[0] == 1:
                crop = False
        if crop : 
            for i, x in enumerate(cells):
                cells[i].pop(0)

    # crop right
    crop = True
    while crop:
        if not cells:
            break
        for x in cells:
            if x[-1] == 1:
                crop = False
        if crop : 
            for i, x in enumerate(cells):
                cells[i].pop(-1)
    return cells

def get_generation(cells : list[list[int]], generations : int) -> list[list[int]]:
    tmp = []
    n=0
    state=0
    neighbours=0

    while n < generations: 
        tmp = [[0 for _ in range(len(cells[0])+2)] for _ in range(len(cells)+2)]
        i=-1
        while i < len(cells)+1:
            j=-1
            while j < len(cells[0])+1:
                state = get_state((i,j), cells)
                neighbours = get_nbr_of_living_neighbours((i,j), cells)
                tmp[i+1][j+1]=new_state(state, neighbours)
                j+=1
            i+=1
        cells = crop_cells(tmp)
        n+=1      
    return cells or [[]]


x = get_generation([
            [1,1,1,0,0,0,1,0],
            [1,0,0,0,0,0,0,1],
            [0,1,0,0,0,1,1,1]
     ],16)
for i in x:
    print(i)