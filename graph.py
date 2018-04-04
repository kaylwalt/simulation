class Node:
    def __init__(self, pos, neighbors=[], edge=1):
        self.pos = pos
        # dictionary of parent node pos's
        # key = pos of parent
        # value = (edge cost,)
        self.parents = {}
        # dictionary of children node pos's
        # key = pos of child
        # value = (edge cost,)
        self.children = {}

        for n in neighbors:
            self.parents[n] = edge
            self.children[n] = edge
        # g approximation
        self.g = float('inf')
        # rhs value
        self.rhs = float('inf')

    def __str__(self):
        return 'Node: ' + str(self.pos) + ' g: ' + str(self.g) + ' rhs: ' + str(self.rhs)

    def __repr__(self):
        return self.__str__()

    def update_parents(self, parents):
        self.parents = parents


class Graph:
    def __init__(self):
        #hash from pos to node
        self.nodes = {}

    def __str__(self):
        msg = 'Graph:'
        for i in self.nodes:
            msg += '\n  node: ' + str(i) + ' g: ' + \
                str(self.nodes[i].g) + ' rhs: ' + str(self.nodes[i].rhs)
        return msg

    def __repr__(self):
        return self.__str__()

    def addNode(self, node):
        self.nodes[node.pos] = node

    def setStart(self, pos):
        if(self.nodes[pos]):
            self.start = pos
        else:
            raise ValueError('start pos not in graph')

    def setGoal(self, pos):
        if(self.nodes[pos]):
            self.goal = pos
        else:
            raise ValueError('goal pos not in graph')


def addNodeToGraph(graph, pos, neighbors, edge=1):
    node = Node(pos)
    for i in neighbors:
        node.parents[i] = edge
        node.children[i] = edge
    graph[pos] = node
    return graph


def makeGraph():
    graph = {}

    # 8-connected graph (w diagonals)
    # Impossible to find path - 2 obstacles in middle
    # graph = addNodeToGraph(graph, 'x1y1', ['x1y2', 'x2y1', 'x2y2'])
    # graph = addNodeToGraph(
    #     graph, 'x2y1', ['x1y1', 'x1y2', 'x3y1', 'x2y2', 'x3y2'], float('inf'))
    # graph = addNodeToGraph(graph, 'x1y2', ['x1y1', 'x2y1', 'x2y2'])
    # graph = addNodeToGraph(
    #     graph, 'x2y2', ['x1y1', 'x1y2', 'x3y1', 'x2y1', 'x3y2'], float('inf'))
    # graph = addNodeToGraph(graph, 'x3y1', ['x3y2', 'x2y1', 'x2y2'])
    # graph = addNodeToGraph(graph, 'x3y2', ['x3y1', 'x2y1', 'x2y2'])

    # 8-connected graph (w diagonals)
    # Impossible to find path - 2 obstacles in middle
    # graph = addNodeToGraph(graph, 'x1y1', ['x1y2', 'x2y1', 'x2y2'])
    # graph = addNodeToGraph(
    #     graph, 'x2y1', ['x1y1', 'x1y2', 'x3y1', 'x2y2', 'x3y2'], float('inf'))
    # graph = addNodeToGraph(graph, 'x1y2', ['x1y1', 'x2y1', 'x2y2'])
    # graph = addNodeToGraph(
    #     graph, 'x2y2', ['x1y1', 'x1y2', 'x3y1', 'x2y1', 'x3y2'])
    # graph = addNodeToGraph(graph, 'x3y1', ['x3y2', 'x2y1', 'x2y2'])
    # graph = addNodeToGraph(graph, 'x3y2', ['x3y1', 'x2y1', 'x2y2'])

    # 4-connected graph (w/out diagonals)
    graph = addNodeToGraph(graph, 'x1y1', ['x1y2', 'x2y1'])
    graph = addNodeToGraph(graph, 'x2y1', ['x1y1', 'x3y1', 'x2y2'])
    graph = addNodeToGraph(graph, 'x1y2', ['x1y1', 'x2y2'])
    graph = addNodeToGraph(graph, 'x2y2', ['x1y2', 'x2y1', 'x3y2'])
    graph = addNodeToGraph(graph, 'x3y1', ['x3y2', 'x2y1'])
    graph = addNodeToGraph(graph, 'x3y2', ['x3y1', 'x2y2'])

    g = GridWorld(X_DIM, Y_DIM)
    # g.graph = graph
    # print(g)
    return g
