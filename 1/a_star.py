import heapq

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position  # (x, y)
        self.parent = parent
        self.g = g  # Cost from start to current
        self.h = h  # Heuristic cost to goal
        self.f = g + h  # Total cost

    def __lt__(self, other):
        return self.f < other.f  # For priority queue

def heuristic(a, b):
    # Manhattan distance (use Euclidean if diagonal moves allowed)
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    open_list = []
    closed_set = set()
    
    start_node = Node(start, None, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current = heapq.heappop(open_list)

        if current.position == goal:
            # Reconstruct path
            path = []
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        closed_set.add(current.position)

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            neighbor_pos = (current.position[0] + dx, current.position[1] + dy)

            # Check boundaries and obstacles
            if (0 <= neighbor_pos[0] < len(grid) and
                0 <= neighbor_pos[1] < len(grid[0]) and
                grid[neighbor_pos[0]][neighbor_pos[1]] == 0 and
                neighbor_pos not in closed_set):

                g = current.g + 1
                h = heuristic(neighbor_pos, goal)
                neighbor = Node(neighbor_pos, current, g, h)

                heapq.heappush(open_list, neighbor)

    return None  


grid = [
    [0, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
]

start = (0, 0)
goal = (4, 4)

path = astar(grid, start, goal)

if path:
    print("Path found:")
    print(path)
else:
    print("No path found.")
