class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
class Edge(object):
    def __init__(self, src, dest, weight = 0):
        self.src = src
        self.dest = dest
        self.weight = weight
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def getWeight(self):
        return self.weight
    def __str__(self):
        return str(self.src) + '->' + str(self.dest)
class Digraph(object):
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node.getName() in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d) + '\n'
        return res[:-1]
class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev) 

def shortestPath(graph, start, end, toPrint = False, visited = []):
    if toPrint:
        print start, end
    if not (graph.hasNode(start) and graph.hasNode(end)):
        raise ValueError('Start or end not in graph.')
    path = [str(start)]
    if start == end:
        return path
    shortest = None
    for node in graph.childrenOf(start):
        if (str(node) not in visited):
            visited = visited + [str(node)] #new list
            newPath = shortestPath(graph, node, end, toPrint, visited)
            if newPath == None:
                continue
            if (shortest == None or len(newPath) < len(shortest)):
                shortest = newPath
    if shortest != None:
        path = path + shortest
    else:
        path = None
    return path 

def load_map():
    mygraph = Digraph()
    myfile = open('mit_map.txt')
    for line in myfile:
        temp = [int(item) for item in line.split()]
        src = Node(temp[0])
        dest = Node(temp[1])
        edge = Edge(src, dest)
        if not mygraph.hasNode(src):
            mygraph.addNode(src)
        if not mygraph.hasNode(dest):
            mygraph.addNode(dest)
        mygraph.addEdge(edge)
    myfile.close()
    return mygraph

mygraph = load_map()
