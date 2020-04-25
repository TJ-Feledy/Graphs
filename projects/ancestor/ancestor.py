class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


def earliest_ancestor(ancestors, starting_node):
    # create a empty queue, and enqueue a PATH to the starting node
    queue = Queue()
    queue.enqueue([starting_node])
    # create a set for visited_vertices
    visited = set()
    prev_parents = []

    # while the queue is not empty
    while queue.size() > 0:
        # dequeue the first PATH
        curr_path = queue.dequeue()
        # grab the last node in the path
        curr_node = curr_path[-1]

        # if it hasn't been visited
        if curr_node  not in visited:
            # mark it as visited
            visited.add(curr_node)
            # make new versions of the current path, with each neighbor added to them
            parents = []

            for relation in ancestors:
                if relation[1] == curr_node:
                    parents.append(relation[0])
            print('parents', parents)

            if len(parents) > 0:
                prev_parents = parents
                for parent in parents:
                    # dubplicate the path
                    new_path = list(curr_path)
                    # add the neighbor
                    new_path.append(parent)
                    # add the new path to the queue
                    queue.enqueue(new_path)

    print('prev_parent', prev_parents)

    if len(visited) > 1 and len(prev_parents) > 1:
        eldest = prev_parents[0]
        for parent in prev_parents:
            if parent < eldest:
                eldest = parent
        return eldest
    elif len(visited) > 1 and len(parents) == 0:
        return curr_node

    return -1