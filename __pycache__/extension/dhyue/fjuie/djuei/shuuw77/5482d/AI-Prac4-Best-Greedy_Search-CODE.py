graph={
    "A": ({"D":1},3),
    "S": ({"A":2, "E":3, "D":1},6),
    "D": ({"B":3, "G":2},4),
    "B": ({"C":2},2),
    "C": ({"G":3},2),
    "E": ({"G":2},2),
    "G": ({},0),
}

def greedy_search_rec(graph, prev, dst, path, q):
    # n:(h(n))
    print("Connected nodes of current node", prev,"with h(n) values")
    for n in graph[prev][0]:
        if n not in path:
            q[n] = graph[n][1]
            print(n, "->", q[n])
            
    while q:
        mn = min(q, key=q.get)
        print("Taking minimum h(n) vertex:", mn)
        
        if dst == mn:
            return path + [dst]
            
        # FIX 1: You must delete the node from the queue to prevent an infinite loop
        del q[mn] 
        
        new_path = greedy_search_rec(graph, mn, dst, path + [mn], q)
        if new_path:
            return new_path
            
    # FIX 2: This return must be outside the while loop, otherwise it quits on the first dead end
    return []

source = input("Enter source vertex: ")
dest = input("Enter destination vertex: ")
path = greedy_search_rec(graph, source, dest, [source], {})

if path:
    print(path)
else:
    print("Path not found!")
