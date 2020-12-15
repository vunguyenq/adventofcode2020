input_raw = '''16,1,0,18,12,14,19'''

input = list(map(int,input_raw.split(",")))

input_test_raw = '''0,3,6'''

input_test = list(map(int,input_test_raw.split(",")))

# Uncomment this row to use test input
#input = input_test

# PART 1
# Find index of the n_th last occurence of a given element in a list
# Default: offset = 0 (last occurence)
def list_rindex(li, x, offset = 0):
    counter = 0
    for i in reversed(range(len(li))):
        if li[i] == x:
            if counter == offset:
                return i
            counter += 1
    raise ValueError("{} is not in list".format(x))

def turn(spoken_numbers):
    last_no = spoken_numbers[-1]
    previous_nos = spoken_numbers[:-1]
    if last_no in previous_nos:
        new_no = list_rindex(spoken_numbers, last_no) - list_rindex(spoken_numbers, last_no, 1)
    else:
        new_no = 0
    spoken_numbers.append(new_no)
    return spoken_numbers

numbers = input.copy()
for i in range (2020 - len(input)):
    numbers = turn(numbers)
print('Part 1 answer: {}'.format(numbers[-1]))

# PART 2
# Simple loop doens't work because it is very heavy to search in a list of 30M elements
# Experimental: 1M elements takes ~ 2 hours

old_code = '''numbers = input.copy()
max_turns = 30000000
for i in range (max_turns - len(input)):
    numbers = turn(numbers)
    #track progress
    if i%10000  == 0:
        print('Proceesed {:,} loops ({:.2%})'.format(i, i/max_turns))
print(numbers[-1])'''

# new version of turn() function:
# for each number, keep track of the 2 last occurences only
def turn_v2(spoken_numbers, last_no, turn_no):
    (last_index_1, last_index_2) = spoken_numbers[last_no]
    if(last_index_1 == last_index_2): # number never appeared before
        new_no = 0
    else:
        new_no = last_index_1 - last_index_2
    
    if new_no in spoken_numbers:
        (last_index_1, last_index_2) = spoken_numbers[new_no]
        spoken_numbers[new_no] = (turn_no, last_index_1)
    else:
        spoken_numbers[new_no] = (turn_no, turn_no)
    return new_no, spoken_numbers

max_turns = 30000000
#max_turns = 2020
numbers = {}

for i, no in enumerate(input):
    numbers[no] = (i,i)

print(numbers)
for j in range(i+1, max_turns):
    new_no, numbers = turn_v2(numbers, no, j)
    #print('step {}: '.format(j+1), no, new_no, numbers)
    no = new_no

    #track progress
    if j%100000  == 0:
        print('Processed {:,} steps ({:.2%})'.format(j, j/max_turns))
print('Part 2 answer: {}. Dictionary size: {:,}'.format(new_no,len(numbers.keys())))
