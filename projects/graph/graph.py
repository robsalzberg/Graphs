"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph
        """
        if v1 not in self.vertices:
            self.add_vertex(v1)

        if v2 not in self.vertices:
            self.add_vertex(v2)

        self.vertices[v1].add(v2)

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex
        """
        # make a queue
        queue = Queue()
        # make a visited set
        visited = set()
        # put starting index in the queue
        queue.enqueue(starting_vertex)
        # while q isn't empty
        while queue.size():
            # dequeue the item, it is our current item
            node = queue.dequeue()
            print(node)
        # mark current as visited
            visited.add(node)
        # for each of the dequeued item's edges
            for edge in self.vertices[node]:
                # if not visited
                if edge not in visited:
                    # put them in the queue
                    queue.enqueue(edge)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        stack = Stack()
        # make a visited set
        visited = set()
        # put starting vertex in our stack
        stack.push(starting_vertex)
        # while the stack isn't empty
        while stack.size():
            # pop off the top of the stack, it is our current item
            node = stack.pop()
            # if not visited
            if node not in visited:
                print(node)  # print for fun
                # mark it as visited
                visited.add(node)
                # for each of our current item's edges
                for edge in self.vertices[node]:
                    # put them on the stack
                    stack.push(edge)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        def dft_recurs(self, starting_vertex, visited=None):
            if visited is None:
                visited = set()
            
            visited.add(starting_vertex)
            print(starting_vertex)
            for child in self.vertices[starting_vertex]:
                if child not in visited:
                    dft_recurs(self, child, visited)

        dft_recurs(self, starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # make a queue
        q = Queue()
        # make a visited set
        visited = set()
        # enqueue the PATH to that node
        q.enqueue([starting_vertex])
        # while the queue isn't empty:
        while q.size() > 0:
        ## dequeue the PATH
            path = q.dequeue()
        ## the last thing in the path is our current item
            node = path[-1]
        ## if it's not visited:
            if node not in visited:
        ## CHECK if it's the target
                if node == destination_vertex:
        #### if so, return the path
                    return path
                ### for each of the node's neighbor's
                for neighbor in self.vertices[node]:
                    #### copy the path
                    copy_path = path[:]
                    #### add the neighbor to the path
                    copy_path.append(neighbor)
                    #### enqueue the PATH_COPY
                    q.enqueue(copy_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # make a stack
        stack = Stack()
        # make a visited set
        visited = set()
        # push on the stack the PATH to that node
        stack.push([starting_vertex])
        # while the stack isn't empty:
        while stack.size() > 0:
        ## pop the PATH
            path = stack.pop()
        ## the last thing in the path is our current item
            node = path[-1]
        ## if it's not visited:
            if node not in visited:
        ## CHECK if it's the target
                if node == destination_vertex:
        #### if so, return the path
                    return path
                ### for each of the node's neighbor's
                for neighbor in self.vertices[node]:
                    #### copy the path
                    copy_path = path[:]
                    #### add the neighbor to the path
                    copy_path.append(neighbor)
                    #### enqueue the PATH_COPY
                    stack.push(copy_path)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
