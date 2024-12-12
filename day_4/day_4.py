mat = []

with open("input_4.txt","r") as file:
    for line in file:
        line = line.strip()
        mat.append(line)

# -- Part 1 --
matches = 0
max_rows = len(mat)
max_cols = len(mat[0])

for r in range (0,max_rows):
    for c in range (0,max_cols):
        if mat[r][c] == 'X':    
            # vertical bottom-up match
            if r >= 3: 
                matches += 1 if mat[r-3][c] == 'S' and mat[r-2][c] == 'A' and mat[r-1][c] == 'M' and mat[r][c] == 'X' else 0
            # vertical top-down match
            if r + 3 < max_rows:
                matches += 1 if mat[r][c] == 'X' and mat[r+1][c] == 'M' and mat[r+2][c] == 'A' and mat[r+3][c] == 'S' else 0
            # horizobtal right-left match
            if c >= 3: 
                matches += 1 if mat[r][c] == 'X' and mat[r][c-1] == 'M' and mat[r][c-2] == 'A' and mat[r][c-3] == 'S' else 0
            # horizobtal left-right match
            if c + 3 < max_cols: 
                matches += 1 if mat[r][c+3] == 'S' and mat[r][c+2] == 'A' and mat[r][c+1] == 'M' and mat[r][c] == 'X' else 0
            # diagonal right-left bottom-up match
            if r >= 3 and c >= 3:
                matches +=1 if mat[r][c] == 'X' and mat[r-1][c-1] == 'M' and mat[r-2][c-2] == 'A' and mat[r-3][c-3] == 'S' else 0
            # diagonal left-right top-down match
            if r + 3 < max_rows and c + 3 < max_cols:
                matches +=1 if mat[r][c] == 'X' and mat[r+1][c+1] == 'M' and mat[r+2][c+2] == 'A' and mat[r+3][c+3] == 'S' else 0
            # diagonal left-right bottom-up match
            if c + 3 < max_cols and r >= 3:
                matches +=1 if mat[r][c] == 'X' and mat[r-1][c+1] == 'M' and mat[r-2][c+2] == 'A' and mat[r-3][c+3] == 'S' else 0
            # diagonal right-left top-down match
            if r + 3 < max_rows and c >= 3:
                matches +=1 if mat[r][c] == 'X' and mat[r+1][c-1] == 'M' and mat[r+2][c-2] == 'A' and mat[r+3][c-3] == 'S' else 0

print(matches) # 2458

# -- Part 2 --
matches = 0

for r in range (0,max_rows):
    for c in range (0,max_cols):
        if mat[r][c] == 'A':
            if r > 0 and c > 0 and r + 1 < max_rows and c + 1 < max_cols:
                # 'MAS' on top-left to bottom-right diagonal AND on top-right to bottom-left diagonal  
                matches += 1 if (mat[r-1][c-1] == 'S' and mat[r+1][c+1] == 'M' or mat[r-1][c-1] == 'M' and mat[r+1][c+1] == 'S')\and (mat[r-1][c+1] == 'S' and mat[r+1][c-1] == 'M' or mat[r-1][c+1] == 'M' and mat[r+1][c-1] == 'S') else 0

print(matches) # 1945
