import heapq

def a_star(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0
    
    parent = {}
    
    while open_list:
        current_f, current_node = heapq.heappop(open_list)
        
        if current_node == goal:
            path = []
            while current_node in parent:
                path.append(current_node)
                current_node = parent[current_node]
            path.append(start)
            path.reverse()
            return path, g_cost[goal]
        
        for neighbor, cost in graph[current_node].items():
            tentative_g = g_cost[current_node] + cost
            
            if tentative_g < g_cost[neighbor]:
                parent[neighbor] = current_node
                g_cost[neighbor] = tentative_g
                f_cost = tentative_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))
    
    return None, float('inf')

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1, 'E': 4},
    'C': {'F': 2},
    'D': {'G': 2},
    'E': {'G': 1},
    'F': {'G': 5},
    'G': {}
}

heuristic = {
    'A': 6, 'B': 4, 'C': 4, 'D': 2, 'E': 1, 'F': 3, 'G': 0
}

start = 'A'
goal = 'G'

path, cost = a_star(graph, start, goal, heuristic)

if path:
    print("Path:", " -> ".join(path))
    print("Cost:", cost)
else:
    print("No path found")