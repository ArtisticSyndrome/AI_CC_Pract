colors = ["Red", "Blue", "Green"]
states = ["A", "B", "C", "D"]
graph = {
    "A": ["B", "C", "D"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["A", "B", "C"]
}
assignment = {}


def is_safe(state, color):
    for neighbor in graph[state]:
        if assignment.get(neighbor) == color:
            return False
    return True


def color_graph(idx):
    if idx == len(states):
        return True
    
    state = states[idx]
    for color in colors:
        if is_safe(state, color):
            assignment[state] = color
            if color_graph(idx + 1):
                return True
            del assignment[state]
    
    return False


print("Graph:")
for state in graph:
    print(state, graph[state])

if color_graph(0):
    print("\nColors:")
    for state in assignment:
        print(state, assignment[state])
else:
    print("No solution")