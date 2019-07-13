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

def earliest_ancestor(ancestors, starting_node):
    pass