from collections import deque

def is_visited(state):
    return state in visited

def water_jug_bfs():
    max_a, max_b= 5,4
    visited= set()
    queue= deque()

    queue.append((0,0))
    while queue:
        a,b= queue.popleft()
        if(a,b) in visited:
            continue
        visited.add((a,b))
        print(f"Jug A:{a}L, Jug B: {b}L")

        if a== 2 or b==2:
            print("Found a solution:")
            return
        possible_states= [
            (max_a,b),
            (a,max_b),
            (0,b),
            (a,0),
            (min(a+b, max_a), b- (min(a+b, max_a)- a)),
            (a- (min(a+b, max_b)-b), min(a+b, max_b))
        ]
        for state in possible_states:
            if state not in visited:
                queue.append(state)
    print("No solution found")

water_jug_bfs()
