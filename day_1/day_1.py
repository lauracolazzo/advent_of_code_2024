# --- Part 1 -------------------------------------------------------------------------------- 
left_list = []
right_list = []
total_distance = 0

# Read input file and build the left and right lists
with open('input_1.txt', 'r') as file:
    for line in file:
        left_el, right_el = line.split('   ')
        left_list.append(int(left_el))
        right_list.append(int(right_el))

# Sort left and rigth lists in ascending order
left_list.sort()
right_list.sort()

# Compute total distance
i = 0
for i in range (0,len(left_list)):
    total_distance += abs(left_list[i] - right_list[i])

# Print total distance
print(total_distance) # 2285373
# --- End Part 1 ----------------------------------------------------------------------------- 


# --- Part 2 -------------------------------------------------------------------------------- 
similarity_score = 0
i = 0
ll_id_frequency = {}
rl_id_frequency = {}

# Compute id's frequencies in left and right lists
for i in range (0,len(left_list)):
    ll_id_frequency.setdefault(left_list[i], 0)
    ll_id_frequency[left_list[i]] += 1
    rl_id_frequency.setdefault(right_list[i], 0)
    rl_id_frequency[right_list[i]] += 1

# Compute similarity score
for el in left_list:
    weight = 0
    if el in rl_id_frequency:
        weight = rl_id_frequency[el]
    similarity_score += el * weight

# Print similarity score
print(similarity_score) # 21142653
# --- End Part 2 ----------------------------------------------------------------------------- 
