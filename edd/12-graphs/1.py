class Graph:
    def __init__(self, directed=False):
        """
        Initializes a graph.
        :param directed: If True, the graph is directed. Default is False (undirected).
        """
        self.graph = {}
        self.directed = directed

    def add_node(self, node):
        """
        Adds a node to the graph.
        :param node: The node to be added.
        """
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2, weight=1):
        """
        Adds an edge to the graph.
        :param node1: The starting node.
        :param node2: The ending node.
        :param weight: The weight of the edge. Default is 1.
        """
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)
        
        self.graph[node1].append((node2, weight))
        
        if not self.directed:
            self.graph[node2].append((node1, weight))

    def remove_node(self, node):
        """
        Removes a node and its edges from the graph.
        :param node: The node to be removed.
        """
        if node in self.graph:
            del self.graph[node]
            
            for n in self.graph:
                self.graph[n] = [(dest, w) for dest, w in self.graph[n] if dest != node]

    def remove_edge(self, node1, node2):
        """
        Removes an edge from the graph.
        :param node1: The starting node.
        :param node2: The ending node.
        """
        if node1 in self.graph:
            self.graph[node1] = [(dest, w) for dest, w in self.graph[node1] if dest != node2]
        
        if not self.directed and node2 in self.graph:
            self.graph[node2] = [(dest, w) for dest, w in self.graph[node2] if dest != node1]

    def get_neighbors(self, node):
        """
        Returns the neighbors of a node.
        :param node: The node to get neighbors for.
        :return: A list of tuples (neighbor, weight)
        """
        return self.graph.get(node, [])

    def display(self):
        """
        Displays the graph.
        """
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")
            
    def dfs(self, start):
        """
        Depth-First Search (DFS) traversal.
        :param start: The starting node.
        :return: A list of nodes in the order they are visited.
        """
        visited = set()
        result = []

        def _dfs(node):
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor, _ in self.graph.get(node, []):
                    _dfs(neighbor)

        _dfs(start)
        return result

    def bfs(self, start):
        """
        Breadth-First Search (BFS) traversal.
        :param start: The starting node.
        :return: A list of nodes in the order they are visited.
        """
        visited = set()
        queue = [(start, 0)]
        result = []
        layer = 1
        while queue:
            node, layer = queue.pop(0)
            if node not in visited:
                visited.add(node)
                result.append((node, layer))
                for neighbor, _ in self.graph.get(node, []):
                    queue.append((neighbor, layer + 1))

        return result

    def __str__(self):
        return str(self.graph)


for idx in range(1, int(input()) + 1):
    i, b = map(int, input().split(', '))
    party = Graph()
    for _ in range(b):
        p1, p2 = map(int, input().split())
        party.add_edge(p1, p2)
    print(f'fiesta {idx}:')
    layers = dict(party.bfs(0))
    for node in sorted(party.graph.keys())[1:]:
        print(f'{node} {layers.get(node, "INF")}')
    print()
        