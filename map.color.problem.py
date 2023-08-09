class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacency_list = {vertex: [] for vertex in vertices}
        self.colors = {}

    def add_edge(self, vertex1, vertex2):
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def solve_map_coloring(self):
        color_names = ['red', 'green', 'blue', 'yellow', 'violet', 'gray', 'orange']
        available_colors = set(color_names)

        for vertex in self.vertices:
            if not vertex:
                continue

            used_colors = set(self.colors[neighbour] for neighbour in self.adjacency_list[vertex] if neighbour in self.colors)
            available_colors -= used_colors

            if not available_colors:
                print("Not possible to color the graph with the given colors.")
                return

            color = available_colors.pop()
            self.colors[vertex] = color

        print("Vertex colors:")
        for vertex in self.vertices:
            if vertex != ' ':
                vertex_colors = self.colors.get(vertex)
                print(f"{vertex}: {vertex_colors}")


def main():
    with open("graph.txt") as file:
        total_no_vertices = int(file.readline().strip())

        if total_no_vertices > 7:
            print("Not possible with 7 or more colors.")
            print("Please review your input file and try again.")
            return

        lines = [file.readline().strip() for _ in range(total_no_vertices)]
        vertices = list(set(''.join(lines)))
        graph = Graph(vertices)

        for i in range(total_no_vertices):
            line = lines[i].split()
            vertex = graph.vertices[i]
            adjacent_vertices = list(set(line[1:]))  # Remove duplicates

            # Clear existing adjacent vertices before adding the new ones
            graph.adjacency_list[vertex] = []

            for adjacent_vertex in adjacent_vertices:
                graph.add_edge(vertex, adjacent_vertex)

        # Remove duplicates in the adjacency list
        for vertex, neighbours in graph.adjacency_list.items():
            graph.adjacency_list[vertex] = list(set(neighbours))

        print()
        graph.solve_map_coloring()


if __name__ == '__main__':
    main()
