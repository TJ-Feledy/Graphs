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
    # create a place holder for previous parents
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
            # create a parents list
            parents = []

            # for each relationship, add the parent to the parents list
            for relation in ancestors:
                if relation[1] == curr_node:
                    parents.append(relation[0])
            # if there are parents, update prev_parents
            if len(parents) > 0:
                prev_parents = parents
                # for each parent
                for parent in parents:
                    # dubplicate the path
                    new_path = list(curr_path)
                    # add the parent to the path
                    new_path.append(parent)
                    # add the new path to the queue
                    queue.enqueue(new_path)

    # if more than one node has been visited and there is more than one previous parents
    if len(visited) > 1 and len(prev_parents) > 1:
        # set an eldest parent and compare it to the other parents to find the eldest parent.
        eldest = prev_parents[0]
        for parent in prev_parents:
            if parent < eldest:
                eldest = parent
        return eldest
    # else if more than one node has been visited and there are no parents, return the current node.
    elif len(visited) > 1 and len(parents) == 0:
        return curr_node
    # else return -1
    return -1