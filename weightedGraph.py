class WeightedGraph:
    # constructor
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        # Adding a node to the graph of districts
        self.nodes.add(value)
        # Initialize the list of edges for this node
        self.edges[value] = []

    def add_edge(self, from_node, to_node, distance):
        # Add a weighted edge to the graph
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

    # the method to find shortest path(returns two dictionaries
    # one with shortest distance from initial node and
    # another with shortest path using djikstra algorithm
    def shortest_path(self, initial_node, end_node):
        visited = {initial_node: 0}
        path = {}

        nodes = set(self.nodes)
        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node

            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node]

            for edge in self.edges[min_node]:
                weight = current_weight + self.distances[(min_node, edge)]
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = min_node

        return visited, path
