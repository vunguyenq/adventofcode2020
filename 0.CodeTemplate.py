import datetime
input_raw = '''
'''

input = input_raw.split("\n")

input_test_raw = '''
'''

input_test = input_test_raw.split("\n")

# Uncomment this row to use test input
input = input_test

# PART 1
# Time tracking
p1_start_time = datetime.datetime.now() 


answer = 0


print('-'*10 + 'PART 1' + '-'*10)
print('Part 1 answer: {}'.format(answer))
p1_end_time = datetime.datetime.now() 
print('Part 1 time: {}'.format(p1_end_time - p1_start_time))

# PART 2
# Time tracking
p2_start_time = datetime.datetime.now()


print('-'*10 + 'PART 2' + '-'*10)
print('Part 2 answer: {}'.format(answer))
p2_end_time = datetime.datetime.now() 
print('Part 2 time: {}'.format(p2_end_time - p2_start_time))