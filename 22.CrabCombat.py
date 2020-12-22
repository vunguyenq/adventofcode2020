import datetime 

input_raw = '''Player 1:
4
14
5
49
3
48
41
39
18
15
46
23
32
16
19
27
47
17
29
26
33
6
10
38
45

Player 2:
1
24
7
44
20
40
42
50
37
21
43
9
12
8
34
13
28
36
25
35
22
2
11
30
31'''

input = input_raw.split("\n\n")

input_test_raw = '''Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10'''

input_test = input_test_raw.split("\n\n")

# Uncomment this row to use test input
# input = input_test

# Parse input:
p1_deck = list(map(int,input[0].split('\n')[1:]))
p2_deck = list(map(int,input[1].split('\n')[1:]))

# PART 1
# Time tracking
p1_start_time = datetime.datetime.now() 

round = 0
prev_decks = []
while(True):
    # From PART2 : Keep track of player decks in previous rounds to prevent infinite loop
    # To save space, store hash values of the decks instead of full cards in each round
    hash_p1 = hash(tuple(p1_deck))
    hash_p2 = hash(tuple(p2_deck))
    if((hash_p1, hash_p2) in prev_decks):
        winner_deck = p1_deck
        break
    else:
        prev_decks.append((hash_p1, hash_p2))

    if(len(p1_deck) == 0):
        winner_deck = p2_deck
        break
    if(len(p2_deck) == 0):
        winner_deck = p1_deck
        break
    round += 1
    p1_card = p1_deck.pop(0)
    p2_card = p2_deck.pop(0)
    if(p1_card > p2_card):
        p1_deck += [p1_card, p2_card]
    else:
        p2_deck += [p2_card, p1_card]

card_count = len(winner_deck)
score = 0
for i, val in enumerate(winner_deck):
    score += (card_count - i) * val

print('-'*10 + 'PART 1' + '-'*10)
print('Part 1 answer: {}'.format(score))
p1_end_time = datetime.datetime.now() 
print('Part 1 time: {}'.format(p1_end_time - p1_start_time))

# PART 2
# Time tracking
p2_start_time = datetime.datetime.now() 

# Re-parse initial decks
p1_init_deck = list(map(int,input[0].split('\n')[1:]))
p2_init_deck = list(map(int,input[1].split('\n')[1:]))

# Initialize global variables
depth = 0
recursion_count = 0

def recursive_combat(deck1, deck2):
    global depth, recursion_count
    p1_deck, p2_deck = deck1.copy(), deck2.copy()

    # recursion tracking
    depth +=1
    recursion_count += 1
    if(recursion_count % 1000 == 0):
        print('Recursion depth: {}. Recursion count: {}'.format(depth, recursion_count))

    prev_decks = []
    winner_deck = []
    winner = 1
    round = 0
    while(True):
        # Check win conditions
        # Win condition 1: If deck state appears before, stop recursion and return p1 wins
        hash_p1 = hash(tuple(p1_deck))
        hash_p2 = hash(tuple(p2_deck))
        if((hash_p1, hash_p2) in prev_decks):
            winner_deck = p1_deck
            winner = 1
            break
        else:
            prev_decks.append((hash_p1, hash_p2))

        # Win condition 2: a player has no card left
        if(len(p1_deck) == 0):
            winner_deck = p2_deck
            winner = 2
            break
        if(len(p2_deck) == 0):
            winner_deck = p1_deck
            winner = 1
            break
        round += 1

        # No player wins yet, play next round
        p1_card = p1_deck.pop(0)
        p2_card = p2_deck.pop(0)

        # check if the round must be decided by a recursive sub-game
        if(len(p1_deck) >= p1_card and len(p2_deck) >= p2_card):
            sub_winner, _ = recursive_combat(p1_deck[:p1_card], p2_deck[:p2_card])
            if(sub_winner == 1):
                p1_deck += [p1_card, p2_card]
            else:
                p2_deck += [p2_card, p1_card]
        else: # regular round, no recursive
            if(p1_card > p2_card):
                p1_deck += [p1_card, p2_card]
            else:
                p2_deck += [p2_card, p1_card]
    depth -=1
    return(winner, winner_deck)

# Main part 2
print('-'*10 + 'PART 2' + '-'*10)
winner_no, win_deck = recursive_combat(p1_init_deck, p2_init_deck)

card_count = len(win_deck)
score = 0
for i, val in enumerate(win_deck):
    score += (card_count - i) * val

print('Part 2 answer: {}'.format(score))

p2_end_time = datetime.datetime.now() 
print('Part 2 time: {}'.format(p2_end_time - p2_start_time))