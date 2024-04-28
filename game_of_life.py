import random, time, copy

WIDTH = 20
HEIGHT = 10


# Create a list of list for cells
next_cells = []
for _ in range(WIDTH):
    column = []
    for _ in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('■') # live cells
        else:
            column.append('□') # dead cells
            
            
    next_cells.append(column)
    
    
    
while True:
    print("") # space between each step
    
    current_cells = copy.deepcopy(next_cells)
    
    # print current cells
    
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[x][y], end='') # print the cell
        print()
        
    # calculate for next step
    
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighboring coordinate
            # % WIDTH ensures leftcoord is  alway between 0 and width - 1
            left_coord  = (x - 1) % WIDTH
            right_coord = (x + 1) % WIDTH
            above_coord = (y - 1) % HEIGHT
            below_coord = (y + 1) % HEIGHT
            
            # count the neighbors of living:
            num_neighbors = 0
            
            if current_cells[left_coord][above_coord] == '■':
                num_neighbors += 1 # Top-left neighbor is alive.
                
            if current_cells[x][above_coord] == '■':
                num_neighbors += 1 # Top neighbor is alive.
                
            if current_cells[right_coord][above_coord] == '■':
                num_neighbors += 1 # Top-right neighbor is alive.
                
            if current_cells[left_coord][y] == '■':
                num_neighbors += 1 # Left neighbor is alive.
                
            if current_cells[right_coord][y] == '■':
                num_neighbors += 1 # Right neighbor is alive.
                
            if current_cells[left_coord][below_coord] == '■':
                num_neighbors += 1 # Bottom-left neighbor is alive.
                
            if current_cells[x][below_coord] == '■':
                num_neighbors += 1 # Bottom neighbor is alive.
                
            if current_cells[right_coord][below_coord] == '■':
                num_neighbors += 1 # Bottom-right neighbor is alive.
                
            
            # set the cell based on the rule
            if current_cells[x][y] == '■' and ( num_neighbors == 2 or num_neighbors == 3) :
                # Living cells with 2 or 3 neighbors stay alive:
                next_cells[x][y] = '■'
                
            elif current_cells[x][y] == '□' and num_neighbors == e:
                # Dead cells with 3 neighbors become alive:
                next_cells[x][y] = '■'
            
            else:
                next_cells[x][y] == '□'
            
    time.sleep(1) # Add a 1-second pause to reduce flickering.
                
            
