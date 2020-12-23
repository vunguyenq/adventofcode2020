import datetime
input_raw = '''653427918'''

input = list(map(int,list(input_raw)))

input_test_raw = '''389125467'''

input_test = list(map(int,list(input_test_raw)))

# Uncomment this row to use test input
#input = input_test

# PART 1

# Function to return n next elements from a given element
# Input: non-duplicated list
# Param remove: whether to remove next n elements from list
def next_elements(lst, el_val, n, remove = False):
    if el_val not in lst:
        print('Element not in list!')
        return None
    if n > len(lst) - 1:
        print('Too many next elements')
        return None
    start = (lst.index(el_val) + 1) % len(lst)
    end = (start + n) % len(lst)
    if end > start:
        next_n = lst[start:end]
        if(remove):
            if (end < len(lst)):
                lst = lst[:start] + lst[end:]
            else:
                lst = lst[:start]
    else:
        next_n = lst[start:] + lst[:end]
        if(remove):
            lst = lst[end:start]
    if(remove):
        return next_n, lst
    return next_n

def move(cups, current_cup):
    picks, cups = next_elements(cups, current_cup, 3, remove = True)
    if current_cup == min(cups):
        destination_cup = max(cups)
    else:
        destination_cup = max([i for i in cups if i < current_cup])
    destination_index = cups.index(destination_cup)
    if destination_index == len(cups):
        cups = cups + picks
    else:
        cups = cups[:destination_index+1] + picks + cups[destination_index+1:]
    current_index = cups.index(current_cup)
    next_index = (current_index + 1) % len(cups)
    next_cup = cups[next_index]
    return cups, next_cup

# print all cups starting from 1
def print_cups(cups):
    i = cups.index(1)
    return ''.join(list(map(str,cups[i:] + cups[:i]))).replace('1','')

print('-'*10 + 'PART 1' + '-'*10)
# Time tracking
p1_start_time = datetime.datetime.now() 
all_cups = input
current_cup = all_cups[0]
for i in range(100):
    all_cups, current_cup = move(all_cups, current_cup)

print('Part 1 answer: {}'.format(print_cups(all_cups)))
p1_end_time = datetime.datetime.now() 
print('Part 1 time: {}'.format(p1_end_time - p1_start_time))

# PART 2
# Implementing a circular list by slicing & concatenating lists is way too slow for part 2 volume (1M cups x 10M steps)
# Idea: use a linked list instead. Each cup is a node that points to the next cup (next node)
# Linked list is best for this situation because there is minor changes to cup sequences after each step
# Code uses a dictionary to implement linked list. Key = cup label, value = next cup label

# Build a dictionary to store linked list from input
def build_linked_list(lst):
    linked_lst = {}
    for i in range(len(lst) - 1):
        linked_lst[lst[i]] = lst[i+1]
    linked_lst[lst[-1]] = lst[0]
    return linked_lst

# Function to move one step
def move_p2(cups, current_cup):
    # Take next 3 cups from current cup
    next1 = cups[current_cup]
    next2 = cups[next1]
    next3 = cups[next2]
    # Find destination cup
    dest_cup = current_cup
    while(True):
        dest_cup -= 1
        if(dest_cup < 1):
            dest_cup = max(set(cups.keys()) - set([next1, next2, next3]))
        if(dest_cup not in (next1, next2, next3)):
            break
    # Link the 3 pick-up cups after destination
    cups[current_cup] = cups[next3]
    t = cups[dest_cup]
    cups[dest_cup] = next1
    cups[next3] = t
    next_cup = cups[current_cup]
    return cups, next_cup

# Main Part 2
print('-'*10 + 'PART 2' + '-'*10)
# Time tracking
p2_start_time = datetime.datetime.now()

input = input + list(range(max(input)+1, 1000001))
all_cups = build_linked_list(input)
current_cup = input[0]
n_steps = 10000000
for i in range(n_steps):
    all_cups, current_cup = move_p2(all_cups, current_cup)

    # progress tracking
    if i%200000  == 0:
        print('Processed {:,} steps ({:.2%})'.format(i, i/n_steps))

next1 = all_cups[1]
next2 = all_cups[next1]
print('2 cups next to cup 1: {}, {}'.format(next1, next2))
print('Part 2 answer: {}'.format(next1*next2))
p2_end_time = datetime.datetime.now() 
print('Part 2 time: {}'.format(p2_end_time - p2_start_time))