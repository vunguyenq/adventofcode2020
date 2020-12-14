input_raw = '''1000390
13,x,x,41,x,x,x,x,x,x,x,x,x,997,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,619,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,17'''

input = input_raw.split("\n")

input_test_raw = '''939
1789,37,47,1889'''

input_test = input_test_raw.split("\n")

# Uncomment this row to use test input
#input = input_test

# PART 1
depart_time = int(input[0])
schedule = [int(x) for x in input[1].split(',') if x.isnumeric()]
min_wait = depart_time
latest_bus = 0
for bus_freq in schedule:
    wait_time = bus_freq * (depart_time//bus_freq + 1) - depart_time
    if (wait_time < min_wait):
        min_wait = wait_time
        latest_bus = bus_freq

print('PART 1')
print('Part 1 answer: min wait {} minutes, bus {}, answer = {}.'.format(min_wait, latest_bus, min_wait * latest_bus))

# PART 2
import math
def check_timestamp(timestamp, bus_offset_dict):
    for bus in bus_offset_dict.keys():
        offset = bus_offset_dict[bus]
        if ((timestamp + offset) % bus > 0):
            return False
    return True

bus_offset = {}
bus_remainder = {}
for i, bus in enumerate(input[1].split(',')):
    if(bus.isnumeric()):
        bus_offset[int(bus)] = i
        bus_remainder[int(bus)] = int(bus) - i

old_code = '''
max_bus = max(bus_offset.keys())
max_bus_offset = bus_offset[max_bus]

# min_search_range = max_bus
min_search_range = 100000000000000
timestamp_max_bus = (min_search_range // max_bus) * max_bus

print(timestamp_max_bus)

i = 0
while True:
    timestamp_max_bus += max_bus
    timestamp = timestamp_max_bus - max_bus_offset
    #print(timestamp_max_bus, timestamp)
    if(check_timestamp(timestamp,bus_offset)):
        break

    #progress tracking
    i+=1
    if (i % 1000000 == 0):
        print('Tested {:,} trials. Current timestamp {:,} (temstamp length: {:,})'.format(i, timestamp, len(str(timestamp))))
print('Answer: {}'.format(timestamp))
#print(check_timestamp(1202161486,bus_offset))
'''

# AS USUAL, brute force by multiplying max(bus_frequency) failed :-()
# Actually this is the Chinese Remainder Theorem (CRT). See https://drx.home.blog/2018/07/25/dinh-ly-so-du-trung-hoa/ https://en.wikipedia.org/wiki/Chinese_remainder_theorem
# Observation: CRT can be applied because all bus ids are PRIME numbers
# Supposed the bus schedule is presented as a list of {bus_id:offset}, then the problem becomes "Find minimized X that
# X = r1 (mod bus_id1)
# X = r2 (mod bus_id2)
# X = r3 (mod bus_id3)
# ...
# with r1, r2, r3 = bus_id1 - offset1, bus_id2 - offset2, bus_id3 - offset3"

# Return min result following Chinese Remainder Theorem
def multiplyList(myList) :
    result = 1
    for x in myList:
         result = result * x 
    return result 

def CRT(crt_input):
    m_s = list(crt_input.keys())
    a_s = []
    for m in m_s:
        a_s.append(crt_input[m])
    M = multiplyList(m_s)
    M_s = [int(M/x) for x in m_s]
    y_s = []
    for i in range(len(M_s)):
        y_s.append(modinv(M_s[i], m_s[i]))
    
    result = 0
    #print(a_s, M_s, y_s)
    for i in range(len(M_s)):
        result += a_s[i] * M_s[i] * y_s[i]
    return result % M

# Compute modular inverse - https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

print('')
print('PART 2')
print('Bus IDs & time offset: {}'.format(bus_offset))
print('Chinese Remainder Theorem input (moduli:remainder): {}'.format(bus_remainder))

#sample_CRT = {17: 17, 13: 11, 19: 16}
#print(CRT(sample_CRT))
print('Part 2 answer: {}'.format(CRT(bus_remainder)))