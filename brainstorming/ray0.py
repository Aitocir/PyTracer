#  Assumptions: 
#    screen origin is in the lower left

import math
import sys
import time

fov_w = 90
fov_h = 90

screen_w = 1920
screen_h = 1080

def bound_to_360(x):
    return x % 360

def veclen(vec):
    return math.sqrt(sum([x**2 for x in vec]))

def normalize(vec):
    if not sum(vec):
        return vec
    new_vec = []
    vl = veclen(vec)
    for v in vec:
        new_vec.append(v / vl)
    return new_vec

def ray0(screen_x, screen_y):
    screen_li = screen_x / (screen_w-1)
    screen_bi = screen_y / (screen_h-1)
    
    fov_x = -(fov_w/2) + (fov_w * screen_li)
    fov_y = -(fov_h/2) + (fov_h * screen_bi)
    
    world_x1 = math.cos(math.radians(fov_x - 90))
    world_z1 = -math.cos(math.radians(fov_x))
    
    world_w1 = veclen((world_x1, world_z1))
    world_y1 = world_w1 * math.tan(math.radians(fov_y))
    
    return normalize((world_x1, world_y1, world_z1))

def main():
    start = time.time()
    vectors = []
    for x in range(screen_w):
        vectors.append([])
        for y in range(screen_h):
            vectors[-1].append(ray0(x, y))
    print(time.time() - start)
    print(sum([sys.getsizeof(x) for x in vectors]))
    """
    while True:
        coord_x = int(input('Enter a coordinate x: '))
        coord_y = int(input('Enter a coordinate y: '))
        print(ray0(coord_x, coord_y))
        print()
    """

if __name__ == "__main__":
    main()