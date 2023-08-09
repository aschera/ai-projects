from collections import deque

# A* algorithm 
def a_star(graph, startingNode, goal, heuristic):
    queue = []
    queue.append((startingNode, 0, [startingNode]))  # (node, total_cost, path)
    visitedNodes = set()
    visitedNodes.add(startingNode)

    while queue:
        print(queue)
        node, cost, path = queue.pop(0)

        if node == goal:
            return path, cost

        for neighbor in graph[node]:
            if neighbor not in visitedNodes:
                total_cost = cost + heuristic(neighbor)  # A* heuristic function
                queue.append((neighbor, total_cost, path + [neighbor]))
                visitedNodes.add(neighbor)

        queue.sort(key=lambda x: x[1])  # Sort the queue based on total cost

    return None, None


# Define your graph
graph = {
    'S': ['A', 'C'],
    'A': ['B'],
    'C': ['A', 'D'],
    'B': ['E', 'F'],
    'D': ['F'],
    'E': ['G'],
    'F': ['G'],
    'G': []
}


# Define a heuristic function for A*
def heuristic(node):
    return 0


# Using A*
path, cost = a_star(graph, 'S', 'G', heuristic)

if path is not None:
    print("Best path:", path)
    print("Cost:", cost)
else:
    print("Goal node (G) is not reachable using A*.")
