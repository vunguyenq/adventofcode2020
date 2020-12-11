input_raw = '''151
94
14
118
25
143
33
23
80
95
87
44
150
39
148
51
138
121
70
69
90
155
144
40
77
8
97
45
152
58
65
63
128
101
31
112
140
86
30
55
104
135
115
16
26
60
96
85
84
48
4
131
54
52
139
76
91
46
15
17
37
156
134
98
83
111
72
34
7
108
149
116
32
110
47
157
75
13
10
145
1
127
41
53
2
3
117
71
109
105
64
27
38
59
24
20
124
9
66'''

input = list(map(int,input_raw.split("\n")))

input_test_raw = '''16
10
15
5
1
11
7
19
6
12
4'''

input_test_raw = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''

input_test = list(map(int,input_test_raw.split("\n")))

# Uncomment this row to use test input
#input = input_test

# PART 1
######
# WRONG approach here
# Treating adapters as graph and finding all paths from 0 to max(input) + 3 is not an option due to performance
# Supposed each node is connected to avg. 2 possible next nodes
# 99 nodes => 2^99 = 6.3 * 10^29 possibilities

old_code = '''
# https://www.python.org/doc/essays/graphs/
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        print(path)
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

input.append(0)
input.append(max(input) + 3)
adapter_graph = {}
end_node = max(input)

for node in input:
    possible_next_nodes = [x for x in input if 0< x - node <=3]
    adapter_graph[node] = possible_next_nodes

paths = find_all_paths(adapter_graph, 0, end_node)
for path in paths:
    if set(path) == set(input):
        break

diffs = {}    
for i in range(1, len(path)):
    node, prev_node = path[i], path[i-1]
    key = node - prev_node
    if key not in diffs:
        diffs[key] = 1
    else:
        diffs[key] += 1
print(diffs)
print(diffs[1] * diffs[3])
'''
# New approach: because all nodes must be connected, next node must be the smallest possible
input.append(0)
input.append(max(input) + 3)
diffs = {}

for node in input:
    possible_next_nodes = [x for x in input if 0< x - node <=3]
    if len(possible_next_nodes) == 0:
        break
    next_node = min(possible_next_nodes)
    key = next_node - node
    if key not in diffs:
        diffs[key] = 1
    else:
        diffs[key] += 1

print(diffs)
print(diffs[1] * diffs[3])

# PART 2
# Idea: if there are 2 nodes with gap 3, then both nodes MUST exist in every possible paths
# For exp: [0,1,2,3,6,7,8,11,13,14] => 0,3,6,8,11,14 must exist in every possible paths. 1,2,7,13 are optional
# => Instead of backtracking the whole input, backtrack on sub-sequences instead
# => Algorithm:
# 1. Sort input ascending
# 2. Break input into sub-sequences separated by gap 3
# 3. For each sub-sequence, recursively backtracking to count possible paths in the sub-sequence
# 4. Multiply subsequence counts
# Examples:
## Input - 2nd test case in description
# [0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 17, 18, 19, 20, 23, 24, 25, 28, 31, 32, 33, 34, 35, 38, 39, 42, 45, 46, 47, 48, 49, 52]
## Subsequences + path counts:
# [0, 1, 2, 3, 4] 7
# [7, 8, 9, 10, 11] 7
# [17, 18, 19, 20] 4
# [23, 24, 25] 2
# [31, 32, 33, 34, 35] 7
# [38, 39] 1
# [45, 46, 47, 48, 49] 7
## Final count:
# 19208
# https://www.python.org/doc/essays/graphs/
def count_all_paths(graph, start, end):
    if start == end:
        return 1
    if not start in graph:
        return 0
    path_count = 0
    for node in graph[start]:
        path_count += count_all_paths(graph, node, end)
    return path_count

input.sort()
#print(input)
end_node = max(input)

sequences = []
current_seq = [0]
for i in range(1,len(input)):
    prev_node, node = input[i-1:i+1]
    if (node-prev_node == 3): #new sequence
        sequences.append(current_seq)
        current_seq = [node]
    else:
        current_seq.append(node)

all_path_count=1
for seq in sequences:
    if(len(seq) > 1):
        seq_graph = {}
        start_node,end_node = min(seq),max(seq)
        for node in seq:
            possible_next_nodes = [x for x in seq if 0 < x - node <=3]
            seq_graph[node] = possible_next_nodes
        path_count = count_all_paths(seq_graph, start_node, end_node)
        all_path_count *= path_count
        print(seq, path_count)
print(all_path_count)
