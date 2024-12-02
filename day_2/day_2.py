# --- Part 1 -------------------------------------------------------------------------------- 
def is_delta_valid(delta):
    return delta >= 1 and delta <= 3

def is_ascending_sequence(el1,el2):
    return el1 <= el2

def is_line_safe(line_elements):
    i = 0
    is_line_safe = True
    is_order_ascending = None

    # Iterate over elements in the line
    while i < len(line_elements)-1 and is_line_safe:
        curr_level = int(line_elements[i])
        next_level = int(line_elements[i+1])

        # Determine the ordering of the first 2 elements
        if is_order_ascending == None:
            is_order_ascending = is_ascending_sequence(curr_level,next_level)
        # Check the ordering is consistent across the line 
        elif is_ascending_sequence(curr_level,next_level) != is_order_ascending:
            is_line_safe = False
            break
        # Compute the delta between 2 adjacent elements
        delta = abs(curr_level - next_level)
        # Check the delta validity against the rules
        if is_delta_valid(delta):
            i += 1
        else:
            is_line_safe = False
            break
    return is_line_safe

safe_lines_count = 0
with open('input_2.txt', 'r') as file:
    # Iterate over the rows of the matrix
    for line in file:
        line_elements = line.split(' ')
        # Check if the line is safe according to the rules
        if is_line_safe(line_elements):
            safe_lines_count += 1

print(safe_lines_count) # 279
# --- End Part 1 ----------------------------------------------------------------------------- 

# --- Part 2 -------------------------------------------------------------------------------- 
safe_lines_count = 0

def check_line_validity_without_next_el(line_elements,i):
    line_elements.remove(line_elements[i+1])
    return is_line_safe(line_elements[i:])

def is_line_safe_with_one_error_tolerance(line_elements):
    i = 0
    is_line_valid = True
    is_order_ascending = None

    # Iterate over elements in the line
    while i < len(line_elements)-1 and is_line_valid:
        curr_level = int(line_elements[i])
        next_level = int(line_elements[i+1])

        # Determine the ordering of the first 2 elements
        if is_order_ascending == None:
            is_order_ascending = is_ascending_sequence(curr_level,next_level)
        
        # Check the ordering is consistent across the line 
        elif is_ascending_sequence(curr_level,next_level) != is_order_ascending:
            # Check if the line can still be considered safe by introducing 1 error tolerance
            is_line_valid = check_line_validity_without_next_el(line_elements,i)
            break
        # Compute the delta between 2 adjacent elements
        delta = abs(curr_level - next_level)
        # Check the delta validity against the rules
        if is_delta_valid(delta):
            i += 1
        else:
            # Check if the delta can still be considered safe by introducing 1 error tolerance
            is_line_valid = check_line_validity_without_next_el(line_elements,i)
            break
    return is_line_valid

with open('input_2.txt', 'r') as file:
    # Iterate over the rows of the matrix
    for line in file:
        line_elements = line.split(' ')
        # Check if the line is safe according to the rules
        if is_line_safe_with_one_error_tolerance(line_elements):
            safe_lines_count += 1

print(safe_lines_count) # 343
# --- End Part 2 ----------------------------------------------------------------------------- 
