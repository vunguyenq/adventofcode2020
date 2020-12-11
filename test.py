import copy 
input_test_raw = '''#.LL.LL.L#
#LLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLL#
#.LLLLLL.L
#.LLLLL.L#'''

def check_occupied_seats_in_sight(seat_layout, position):
    directions = [(-1,-1), (1,1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0)]
    occupied_count = 0
    for direction in directions:
        (row, col) = position
        while (True):
            row += direction[0]
            col += direction[1]
            if(row < 0 or col < 0 or row >= len(seat_layout) or col >= len(seat_layout[0])): # out of bound
                break
            if seat_layout[row][col] == 1: # break on the first OCCUPIED seat found on each direction, increase count
                occupied_count += 1
                break
            if seat_layout[row][col] == -1: # break on the first EMPTY seat found on each direction, NO increase count
                break
    return occupied_count

def apply_rule_part2(seat_layout):
    current_seat_layout = copy.deepcopy(seat_layout)
    for i, row in enumerate(current_seat_layout):
        for j, seat in enumerate(row):
            occupied_adjacent_count = check_occupied_seats_in_sight(current_seat_layout, (i,j)) 
            if (seat == -1 and occupied_adjacent_count == 0) or (seat == 1 and occupied_adjacent_count >= 5):
                seat_layout[i][j] *= -1
    return seat_layout

input_test = input_test_raw.split("\n")
input = input_test
seats = []
for i, row in enumerate(input):
    seats.append([])
    for seat in row:
        if(seat == 'L'):
            seats[i].append(-1)
        elif(seat == '#'):
            seats[i].append(1)
        else: # floor
            seats[i].append(0)

print(seats[0][3])
print(check_occupied_seats_in_sight(seats,(0,3)))

for row in seats:
    print(row)

print('-------------------------------------------')

s2 = apply_rule_part2(seats)
for row in s2:
    print(row) 