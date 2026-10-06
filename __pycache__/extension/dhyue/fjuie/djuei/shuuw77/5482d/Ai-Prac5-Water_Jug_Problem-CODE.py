from itertools import permutations
dist=[
    [0, 10, 15, 20],
    [10, 0,35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
    ]
n=len(dist)
cities=range(1,n)
min_distance = float('inf')
best_path = None
for path in permutations(cities):
    current_path = (0 ,)+path + (0 ,) + path + (0 ,)
    distance = 0
    for i in range(len(current_path) -1):
        distance  += dist[current_path[i] ] [current_path[i + 1 ] ]
        if distance < min_distance:
            min_distance = distance
            best_path = current_path
print("Shortest distance:", min_distance)
print("Best path:", best_path)
