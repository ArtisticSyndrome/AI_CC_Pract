import heapq

def a_star(graph, start, end, heuristic):
    g_cost = {start:0}
    parent = {start: None}
     
    open_list = []
    heapq.heappush(open_list,(0,start))

    while open_list:
        curr = heapq.heappop(open_list)[1]

        if curr == end:
            path = []

            while curr is not None:
                path.append(curr)
                curr = parent[curr]

            path.reverse()
            return path, g_cost[end]

        for neighbour, cost in graph[curr]:
            new_cost = g_cost[curr] + cost

            if neighbour not in g_cost or new_cost < g_cost[neighbour]:
                cost_f = new_cost + heuristic[neighbour]

                g_cost[neighbour] = new_cost
                parent[neighbour] = curr

                heapq.heappush(open_list, (cost_f, neighbour))


#graph and heuristi
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 4)],
    'C': [('F', 2)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 5)],
    'G': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 3,
    'G': 0
}

start = 'A'
end = 'G'

path, cost = a_star(graph, start, end, heuristic)

if path:
    print("Shortest Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("No path found")