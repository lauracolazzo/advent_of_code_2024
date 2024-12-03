import re
input = open('input_3.txt', 'r').read()

# -- Part 1 --
mul_pattern = r"mul\([1-9]\d*,[1-9]\d*\)"
matches = re.findall(mul_pattern,input)

def mul_result_from_command(mul_command):
    num1, num2 = mul_command.split(',')
    num1 = num1.replace('mul(','')
    num2 = num2.replace(')','')
    return int(num1)*int(num2)

result = 0
for match in matches:
    result+= mul_result_from_command(match)

print(result) # 189527826

# -- Part 2 --
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"
pattern2 = rf"{do_pattern}|{dont_pattern}|{mul_pattern}"
matches2 = re.findall(pattern2, input)

do = True
result = 0
for el in matches2:
    if re.match(dont_pattern, el):
        if do:
            do = False
    elif re.match(do_pattern, el): 
        if not do:
            do = True
    else:
        if do:
            result += mul_result_from_command(el)

print(result) # 63013756