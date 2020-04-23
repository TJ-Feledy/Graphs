"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex does not exist!')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a plan to visit queue and add starting_vertex to it
        plan_to_visit = Queue()
        plan_to_visit.enqueue(starting_vertex)
        # create a Set for visited_vertices
        visited_vertices = set()

        # while the plan_to_visit queue is not Empty:
        while plan_to_visit.size() > 0:
            # dequeue the first vertex on the queue
            current_vertex = plan_to_visit.dequeue()
            # if its not been visited
            if current_vertex not in visited_vertices:
                # print the vertex
                print(current_vertex)
                # mark it as visited, (add it to visited_vertices)
                visited_vertices.add(current_vertex)
                # add all neighbors to the queue
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.enqueue(neighbor)



    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a plan to visit stack and add starting_vertex to it
        plan_to_visit = Stack()
        plan_to_visit.push(starting_vertex)
        # create a Set for visited_vertices
        visited_vertices = set()

        # while the plan_to_visit stack is not Empty:
        while plan_to_visit.size() > 0:
            # pop the first vertex on the stack
            current_vertex = plan_to_visit.pop()
            # if its not been visited
            if current_vertex not in visited_vertices:
                # print the vertex
                print(current_vertex)
                # mark it as visited, (add it to visited_vertices)
                visited_vertices.add(current_vertex)
                # add all neighbors to the stack
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # add starting vertex to visited
        visited.add(starting_vertex)
        print(starting_vertex)
        # get the neighbors of the starting vertex
        neighbors = self.get_neighbors(starting_vertex)

        # if no neighbors, return
        # else for each neighbor
            # if it is not in visited, run recursion with neighbor as starting vertex
            # else return
        if len(neighbors) == 0:
            return
        else:
            for neighbor in neighbors:
                if neighbor not in visited:
                    self.dft_recursive(neighbor, visited)
                else:
                    return

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a empty queue, and enqueue a PATH to the starting vertex
        queue = Queue()
        queue.enqueue([starting_vertex])
        # create a set for visited_vertices
        visited = set()

        # while the queue is not empty
        while queue.size() > 0:
            # dequeue the first PATH
            curr_path = queue.dequeue()
            # grab the last vertex in the path
            end_vertex = curr_path[-1]

            # if it hasn't been visited
            if end_vertex  not in visited:
                # check if its the target
                if end_vertex == destination_vertex:
                    # Return the path
                    return curr_path

                # mark it as visited
                visited.add(end_vertex)
                # make new versions of the current path, with each neighbor added to them
                neighbors = self.get_neighbors(end_vertex)

                for neighbor in neighbors:
                    # dubplicate the path
                    new_path = list(curr_path)
                    # add the neighbor
                    new_path.append(neighbor)
                    # add the new path to the queue
                    queue.enqueue(new_path)
        

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create a empty stack, and push a PATH to the starting vertex
        stack = Stack()
        stack.push([starting_vertex])
        # create a set for visited_vertices
        visited = set()

        # while the stack is not empty
        while stack.size() > 0:
            # pop the first PATH
            curr_path = stack.pop()
            # grab the last vertex in the path
            end_vertex = curr_path[-1]

            # if it hasn't been visited
            if end_vertex  not in visited:
                # check if its the target
                if end_vertex == destination_vertex:
                    # Return the path
                    return curr_path

                # mark it as visited
                visited.add(end_vertex)
                # make new versions of the current path, with each neighbor added to them
                neighbors = self.get_neighbors(end_vertex)

                for neighbor in neighbors:
                    # dubplicate the path
                    new_path = list(curr_path)
                    # add the neighbor
                    new_path.append(neighbor)
                    # add the new path to the stack
                    stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # add starting vertex to visited
        visited.add(starting_vertex)
        # add starting vertex to path
        path = path + [starting_vertex]

        # if starting vertex is equal to destination vertex, return the path
        if starting_vertex == destination_vertex:
            return path
        
        # get starting vetex's neighbors
        neighbors = self.get_neighbors(starting_vertex)

        # for each neighbor
        for neighbor in neighbors:
            # if the neighbor is not in visited, return the dfs_recursive(neighbor, destination, visited, path)
            if neighbor not in visited:
                next_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                
                if next_path is not None:
                    return next_path





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
    print('bft')
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('dft')
    graph.dft(1)
    print('dft_recursive')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('bfs')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('dfs')
    print(graph.dfs(1, 6))
    print('dfs_recursive')
    print(graph.dfs_recursive(1, 6))
