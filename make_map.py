import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
#img=mpimg.imread('mario.png')

SIZE = 200
TILE = 5

START_T = mpimg.imread('Tiles/Start.png')
END_T = mpimg.imread('Tiles/End.png')
LR_T = mpimg.imread('Tiles/LR.png')
TB_T = mpimg.imread('Tiles/TB.png')
EMPTY_T = mpimpg.imread('TILES/Empty.png')

tiles = [['empty']*SIZE]*SIZE 
img = np.zeros((TILE*SIZE,TILE*SIZE,3))

class Path():
    def __init__(self):    
        self.cur_end = (SIZE/2,SIZE/2)
        self.cur_in = 's'
        self.cur_out = 'n'
        self.terminated = False

    def terminate(self):
        self.terminated = True
        tiles[self.cur_end[0]][self.cur_end[1]] = END_T

def draw_tile(loc, tile, img):
    for x in xrange(TILE):
        for y in xrange(TILE):
            img[loc[0]*TILE + x][loc[1]*TILE + y] = tile[x][y]
    return img

def put_tile(cur_in, cur_out):
    if cur_in in ['n','s'] and cur_out in ['n','s']:
        return TB_T
    else: return EMPTY_T 
    
def draw_shell(img):
    # for each path, add a new tile, or delete the paths
    for path in paths:
        if not path.terminated:
            if 0 in path.cur_end or SIZE in path.cur_end:
                path.terminate()    
    return img

def make_random_map():
    
    start = (int(random.random()*SIZE), int(random.random()*SIZE))
    while start[0] < 0.1*SIZE or start[0] > 0.9*SIZE or start[1] < 0.1*SIZE or start[1] > 0.9*SIZE:
        start = (int(random.random()*SIZE), int(random.random()*SIZE))
        
    tiles[start[0]][start[1]] = START_T 
   
    paths = [Path()]*4
    paths[0].cur_out, paths[0].cur_in, paths[0].cur_end = 'n','s', (start[0], start[1]+1)
    paths[1].cur_out, paths[1].cur_in, paths[1].cur_end = 'e','w', (start[0]+1, start[1])
    paths[2].cur_out, paths[2].cur_in, paths[2].cur_end = 's','n', (start[0], start[1]-1)
    paths[3].cur_out, paths[3].cur_in, paths[3].cur_end = 'w','e', (start[0]-1, start[1])

    for path in paths:
        tiles[path.cur_end[0]][path.cur_end[1]] = put_tile(path.cur_in, path.cur_out)

    halt = False
    while not halt:
        img = draw_shell(img)
        Halt = check_finished()

    for row in xrange(SIZE):
        for col in xrange(SIZE):
            img = draw_tile((row,col), tiles[row][col], img)
    return img



if __name__ == '__main__':
    img = make_random_map() 
    imgplot = plt.imshow(img)
    mpimg.imsave("map.png", img)
    plt.show()
