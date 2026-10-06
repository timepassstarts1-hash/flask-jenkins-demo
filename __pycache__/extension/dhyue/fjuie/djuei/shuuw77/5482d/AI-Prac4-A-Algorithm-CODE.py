graph={
    'A':[('B',1),('D',2),('E',3),4],
    'B':[('C',2),('D',1),3],
    'C':[('F',3),2],
    'D':[('F',2),3],
    'E':[('D',3),('F',4),2],
    'F':[(),0]
    }

def get_min(q):
    mn = (0, (0, float("INF")))
    for i in q:
        if sum(q[i]) < sum(mn[1]):
            mn = (i, q[i])
            #print (mn)
    return mn[0]

def a_star(graph, prev, dst, path, pcost, q):
    # n: (h(n), g(n)) OF CURRENT VERTEX
    print("Connected nodes of current node", prev, "with h(n) values: ")
    
    # FIX 1: Iterate over all tuples (excluding the last element which is the heuristic)
    for item in graph[prev][:-1]:    
        if not item: # FIX 2: Handle the empty tuple in 'F':[(), 0]
            continue
        
        n, weight = item # Unpack the neighbor and its edge weight
        
        if n not in path:
            # FIX 3: Fixed 'perv' typo and invalid dictionary indexing.
            # q[n] stores (heuristic, cumulative cost to reach node)
            q[n] = (graph[n][-1], pcost + weight)
            print(n, "->", q[n])
            
            add1 = sum(q[n])
            path_cost = add1    # A* value is just the sum of the tuple h(n) + g(n)
            print("A* value for ",n, "is: ",path_cost)
            
    while q:
        mn = get_min(q)
        print("Selecting Minimum Vertex: ", mn)
        print("_________________________________________________")
        if dst == mn:
            return path + [dst]
            
        # FIX 4: pc is simply the cumulative cost we already calculated and stored in q
        pc = q[mn][1]
        print("Previous path cost: ", pc)
        
        # FIX 5: MUST uncomment this to remove the node from the queue and prevent an infinite loop
        del q[mn]
        
        new_path = a_star(graph, mn, dst, path + [mn], pc, q)
        if new_path:
            return new_path
    return []

source=input("Enter Source vertex: ")
dest=input("Enter Destination vertex: ")
heuristic=int(input("Enter given heuristic value for source: "))

path = a_star(graph, source, dest, [], 0, {source: (heuristic, 0)})
if path:
    print(path)
else:
    print("Path Not Found!!")
