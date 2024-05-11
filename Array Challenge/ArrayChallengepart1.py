import numpy as np
from itertools import combinations

def ArrayChallenge(arr):
    # Extracting the number of desks
    K = arr[0]
    
    # Extracting the occupied desks
    occupied_desks = arr[1:]
    
    # Creating a binary array to represent occupied desks
    occupied_array = np.zeros(K)
    for desk in occupied_desks:
        occupied_array[desk - 1] = 1
    
    # Reshaping the array to represent the classroom layout as a 2D grid
    layout = occupied_array.reshape(-1, 2)
    
    # Counting the number of ways 2 students can be seated next to each other
    ways = 0
    for i in range(len(layout) - 1):
        for j in range(2):
            if layout[i, j] == 0 and layout[i + 1, j] == 0:
                ways += 1
            if j == 0 and layout[i, j + 1] == 0 and layout[i + 1, j + 1] == 0:
                ways += 1
    
    return ways

# define-ocg: ArrayChallenge function with a sample input
print(ArrayChallenge([6, 4]))  # Output: 4
