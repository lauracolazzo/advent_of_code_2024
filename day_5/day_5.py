# -- Part 1--
import math
rules = {}
mid_sum = 0
updates = []
with open("input_5.txt","r") as file:
    rules_ended = False
    for line in file:
        if line == '\n':
            rules_ended = True
        else:
            x,y = '',''
            if rules_ended == False:
                x,y = line.replace('\n','').split('|')
                rules.setdefault(x,[])
                rules[x].append(y)
            else:
                update = line.replace('\n','').split(',')
                updates.append(update)
                valid = True
                if len(update)==1:
                    mid_sum += int(update[0])
                else:
                    i = 0
                    while i < len(update)-1:
                        if update[i] in rules[update[i+1]]:
                            valid = False
                            break
                        i += 1
                    if valid:
                        mid_sum += int(update[math.floor(len(update)/2)])

print(mid_sum) # 4689

# -- Part 1--
mid_sum = 0
for update in updates:
    valid = True
    reordered = False
    if len(update)>1:
        i = 0
        while i < len(update)-1:
            if update[i] in rules[update[i+1]]:
                valid = False
                temp = update[i+1]
                update[i+1] = update[i]
                update[i] = temp
                reordered = True
                if not update[i] in rules[update[i+1]]:
                    valid = True
                if reordered and i > 0: 
                    i -= 1
            else:
                i += 1
        if valid and reordered:
            mid_sum += int(update[math.floor(len(update)/2)])

print(mid_sum) # 6336