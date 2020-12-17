import numpy as np
from itertools import product
input_raw = '''.......#
....#...
...###.#
#...###.
....##..
##.#..#.
###.#.#.
....#...'''

input = input_raw.split("\n")

input_test_raw = '''.#.
..#
###'''

input_test = input_test_raw.split("\n")

# Uncomment this row to use test input
#input = input_test

# numpy matrix indexes (0,0,0) at bottom-left-most corner of the cube
# function to convert a datapoint index from 3D coordinates to matrix indexes (axes values can be negative)
def coordinates2matrix(x, y, z, offset):
    return ([i + offset for i in (x,y,z)])

# convert matrix index to 3D coordinates
def matrix2coordinates(x, y, z, offset):
    return ([i - offset for i in (x,y,z)])

def count_active_neighbors(space, coordinates):
    count = 0
    neighbors = set(product([-1,0,1],repeat = 3)) # 26 combinations (0,0,1), (-1,1,0) etc
    neighbors.discard((0,0,0))
    (z_max, x_max, y_max) = space.shape
    for n in neighbors:
        neighbor_coor = tuple(sum(t) for t in zip(n,coordinates))
        if ((neighbor_coor[0] in range(0, z_max)) and (neighbor_coor[1] in range(0, x_max)) and (neighbor_coor[2] in range(0, y_max)) and (space[neighbor_coor] == 1)):
            #print(n, neighbor_coor)
            count += 1
    return count

# After each cycle, space is extended +1 to all directions. So initial state 1x3x3 will grow to 13x15x15 after 6 cycles
#		Example			Real data		
#Cycle	x	y	z		x	y	z
#0		1	3	3		1	8	8
#1		3	5	5		3	10	10
#2		5	7	7		5	12	12
#3		7	9	9		7	14	14
#4		9	11	11		9	16	16
#5		11	13	13		11	18	18
#6		13	15	15		13	20	20

# PART 1
# After each cycle, space is extended +1 to all directions. So initial state 1x3x3 will grow to 13x15x15 after 6 cycles
#		Example			Real data		
#Cycle	x	y	z		x	y	z
#0		1	3	3		1	8	8
#1		3	5	5		3	10	10
#2		5	7	7		5	12	12
#3		7	9	9		7	14	14
#4		9	11	11		9	16	16
#5		11	13	13		11	18	18
#6		13	15	15		13	20	20

# Ininialize numpy matrix to store whole space after 6 cycles
init_size_x = len(input) + 6*2
init_size_y = len(input[0]) + 6*2
init_size_z = 1 + 6*2
offset = 6
np_space = np.zeros((init_size_z,init_size_x,init_size_y)).astype(int)
#print(np_space.shape)

# Parse input and store initial active cubes into space matrix
for i,row in enumerate(input):
    for j,char in enumerate(row):
        if (char == '#'):
            x,y,z = coordinates2matrix(i,j,0, offset)
            np_space[z,x,y] = 1

print('Initial active cubes: {}'.format(np.count_nonzero(np_space)))
# for each cycle, loop each cube and count active neighbors
for k in range (6): 
    print('Processing cycle {}...'.format(k+1))
    current_space = np_space.copy()
    for z in range(init_size_z):
        for x in range(init_size_x):
            for y in range(init_size_y):
                active_count = count_active_neighbors(current_space, (z, x, y))
                if (np_space[(z, x, y)] == 1): # if cube is active
                    if(active_count == 2 or active_count == 3):
                        pass # remain active
                    else:
                        np_space[(z, x, y)] = 0
                else: # cube is inactive
                     if(active_count == 3):
                        np_space[(z, x, y)] = 1
print('Part 1 answer: {}'.format(np.count_nonzero(np_space)))

# PART 2
# Similar to part 1, now with additional 4th dimension w
def coordinates2matrix_4d(x, y, z, w, offset):
    return ([i + offset for i in (x,y,z,w)])

def count_active_neighbors_4d(space, coordinates):
    count = 0
    neighbors = set(product([-1,0,1],repeat = 4)) # 80 combinations (0,0,1,1), (-1,1,0,0) etc
    neighbors.discard((0,0,0,0))
    (w_max, z_max, x_max, y_max) = space.shape
    for n in neighbors:
        neighbor_coor = tuple(sum(t) for t in zip(n,coordinates))
        if ((neighbor_coor[0] in range(0, w_max)) and (neighbor_coor[1] in range(0, z_max)) and (neighbor_coor[2] in range(0, x_max)) and (neighbor_coor[3] in range(0, y_max)) and (space[neighbor_coor] == 1)):
            #print(n, neighbor_coor)
            count += 1
    return count

# Ininialize numpy matrix to store whole space after 6 cycles
init_size_x = len(input) + 6*2
init_size_y = len(input[0]) + 6*2
init_size_z = 1 + 6*2
init_size_w = 1 + 6*2
offset = 6
np_space = np.zeros((init_size_w, init_size_z, init_size_x, init_size_y)).astype(int)
#print(np_space.shape)

# Parse input and store initial active cubes into space matrix
for i,row in enumerate(input):
    for j,char in enumerate(row):
        if (char == '#'):
            x,y,z,w = coordinates2matrix_4d(i,j,0,0,offset)
            np_space[w,z,x,y] = 1

print('-'*30 + 'PART 2' + '-'*30)
print('Initial active cubes: {}'.format(np.count_nonzero(np_space)))
# for each cycle, loop each cube and count active neighbors
for k in range (6): 
    print('Processing cycle {}...'.format(k+1))
    current_space = np_space.copy()
    for w in range(init_size_w):
        print('\t w = {}...'.format(w))
        for z in range(init_size_z):
            for x in range(init_size_x):
                for y in range(init_size_y):
                    active_count = count_active_neighbors_4d(current_space, (w, z, x, y))
                    if (np_space[(w, z, x, y)] == 1): # if cube is active
                        if(active_count == 2 or active_count == 3):
                            pass # remain active
                        else:
                            np_space[(w, z, x, y)] = 0
                    else: # cube is inactive
                        if(active_count == 3):
                            np_space[(w, z, x, y)] = 1
print('Part 2 answer: {}'.format(np.count_nonzero(np_space)))