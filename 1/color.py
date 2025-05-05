graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

colors = ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple']

node_color = {}

for node in graph:
    for color in colors:
        if all(node_color.get(neighbour) != color for neighbour in graph[node]):
            node_color[node] = color
            break

print(node_color) 