import heapq

def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0
    parent = {}
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == goal:
            path = []
            node = current
            while node in parent:
                path.append(node)
                node = parent[node]
            path.append(start)
            return path[::-1], g_cost[goal]
        
        for neighbor, cost in graph[current].items():
            new_cost = g_cost[current] + cost
            
            if new_cost < g_cost[neighbor]:
                parent[neighbor] = current
                g_cost[neighbor] = new_cost
                f_cost = new_cost + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))
    
    return None, float('inf')


# Build graph
graph = {}
n = int(input("Number of nodes: "))

for i in range(n):
    node = input("Node name: ")
    m = int(input(f"Neighbors for {node}: "))
    neighbors = {}
    
    for j in range(m):
        neighbor = input("Neighbor: ")
        cost = int(input(f"Cost to {neighbor}: "))
        neighbors[neighbor] = cost
    
    graph[node] = neighbors

# Heuristic values
heuristic = {}
for node in graph:
    heuristic[node] = int(input(f"h({node}): "))

start = input("Start node: ")
goal = input("Goal node: ")

# Run A*
path, cost = a_star(graph, start, goal, heuristic)

if path:
    print("Path:", " -> ".join(path))
    print("Cost:", cost)
else:
    print("No path found")
    
   
   
   #--------------------------------------------------------
    """
Sample Input

Enter number of nodes: 3

Enter node name: A
Enter number of neighbors for A: 1
Enter neighbor node: B
Enter cost from A to B: 1

Enter node name: B
Enter number of neighbors for B: 1
Enter neighbor node: C
Enter cost from B to C: 2

Enter node name: C
Enter number of neighbors for C: 0

Enter Heuristic Values:
h(A) = 3
h(B) = 1
h(C) = 0

Enter Start Node: A
Enter Goal Node: C


Expected Output

Shortest Path: A -> B -> C
Total Cost: 3
"""