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
        
def earliest_ancestor(ancestors, starting_node):
    pass