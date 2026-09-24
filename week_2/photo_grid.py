import math as m

grid_size = 17

grid_side = m.ceil(m.sqrt(grid_size))

empty_spaces = grid_side ** 2 - grid_size



print(f"Griddet er {grid_size} * {grid_size} med {empty_spaces} tomme pladser for {grid_size}")