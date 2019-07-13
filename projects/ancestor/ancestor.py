class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()

        raise IndexError("Stack empty cannot pop")

    def size(self):
        return len(self.stack)

class Graph():
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        self.vertices[value] = set()

    def isvertex(self, value):
        return value in self.vertices

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            return

        raise IndexError("Vertices not found")
        
def dfs(self, starting_vertex):
        # Create empty set
        vertices = set()
        # Create empty Stack
        stack = Stack()

        # Add vertex path to Stack
        initial_path = [starting_vertex]
        stack.push(initial_path)

        final_paths = []

        while stack.size() > 0:
            path = stack.pop()
            vertex = path[-1]

            if vertex not in vertices:
                vertices.add(vertex)

                # Available path at the end of traversal
                # shall be stored in output.
                if len(self.vertices[vertex]) == 0:
                    final_paths.append(path)

                for next_vertex in self.vertices[vertex]:
                    if next_vertex not in vertices:
                        new_path = path.copy()
                        new_path.append(next_vertex)

                        stack.push(new_path)

        max_path_len = float('-inf')
        parent_vertex = float('inf')

        for path in final_paths:
            if len(path) > max_path_len:
                max_path_len = len(path)
                parent_vertex = path[-1]

            if len(path) == max_path_len:
                parent_vertex = min(parent_vertex, path[-1])

        if parent_vertex == starting_vertex:
            parent_vertex = -1

        return parent_vertex

def earliest_ancestor(ancestors, starting_node):
    pass