import numpy as np
from sklearn.neighbors import NearestNeighbors

def ArrayChallenge(arr):
    # Define-ocg: This function calculates the number of ways 2 students can be seated next to each other in a classroom
    K = arr[0]
    occupied_desks = arr[1:]

    # Convert the occupied desks to a numpy array
    varOcg = np.array(occupied_desks)

    # Create a grid of all possible desk positions
    all_desks = np.arange(1, K+1)
    grid = np.stack([all_desks//2, all_desks%2], axis=1)

    # Find the nearest neighbors for each unoccupied desk
    neigh = NearestNeighbors(n_neighbors=2, metric='manhattan')
    neigh.fit(grid)
    distances, indices = neigh.kneighbors(grid)

    # Count the number of ways to seat two students next to each other
    ways_to_seat = 0
    for i in range(len(grid)):
        if all_desks[i] not in varOcg:
            neighbors = indices[i]
            for j in neighbors:
                if all_desks[j] not in varOcg:
                    ways_to_seat += 1

    return ways_to_seat
