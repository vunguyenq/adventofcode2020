import datetime
input_raw = '''14082811
5249543'''

input = input_raw.split("\n")

input_test_raw = '''5764801
17807724'''

input_test = input_test_raw.split("\n")

BASE_SUBJECT_NO = 7

# Uncomment this row to use test input
#input = input_test

# Parse input
card_pub, door_pub = list(map(int,input))

def transform(subject_no, loop_size):
    val = 1
    for i in range(loop_size):
        val *= subject_no
        val = val % 20201227
    return val

# Find number of loop from pub_key
def reverse_transform(pub_key):
    val = 1
    i = 0
    while True:
        i+=1
        val *= BASE_SUBJECT_NO
        val = val % 20201227
        if val == pub_key:
            return i
    return None

# PART 1
# Time tracking
p1_start_time = datetime.datetime.now() 
door_loop = reverse_transform(door_pub)
card_loop = reverse_transform(card_pub)
door_encrypt = transform(card_pub, door_loop)
card_encrypt = transform(door_pub, card_loop)

print('-'*10 + 'PART 1' + '-'*10)
print('Door loop size {:,}; Door encrypt: {}; Card loop size: {:,}; Card encrypt: {}'.format(door_loop, door_encrypt, card_loop, card_encrypt))
print('Part 1 answer: {}'.format(door_encrypt))
p1_end_time = datetime.datetime.now() 
print('Part 1 time: {}'.format(p1_end_time - p1_start_time))

# PART 2
# Time tracking
p2_start_time = datetime.datetime.now()


print('-'*10 + 'PART 2' + '-'*10)
print('Part 2 answer: {}'.format(0))
p2_end_time = datetime.datetime.now() 
print('Part 2 time: {}'.format(p2_end_time - p2_start_time))