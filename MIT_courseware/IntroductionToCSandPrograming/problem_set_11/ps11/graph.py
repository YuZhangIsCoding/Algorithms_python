# 6.00 Problem Set 11
#
# graph.py
#
# A set of data structures to represent graphs
#

class Node(object):
   def __init__(self, name):
       self.name = str(name)
   def getName(self):
       return self.name
   def __str__(self):
       return self.name
   def __repr__(self):
      return self.name
   def __eq__(self, other):
      return self.name == other.name
   def __ne__(self, other):
      return not self.__eq__(other)

class Edge(object):
   def __init__(self, src, dest):
       self.src = src
       self.dest = dest
   def getSource(self):
       return self.src
   def getDestination(self):
       return self.dest
   def __str__(self):
       return str(self.src) + '->' + str(self.dest)

class WeightEdge(Edge):
   def addWeight(self, distance, sundistance):
      self.distance = distance
      self.sundistance = sundistance
   def getDistance(self):
      return self.distance
   def getSundistance(self):
      return self.sundistance

class Digraph(object):
   """
   A directed graph
   """
   def __init__(self):
       self.nodes = set([])
       self.edges = {}
       self.edgeweights = {}
   def addNode(self, node):
       if node.getName() in self.nodes:
           raise ValueError('Duplicate node')
       else:
           self.nodes.add(node.getName())
           self.edges[node.getName()] = []
   def addEdge(self, edge):
       src = edge.getSource().getName()
       dest = edge.getDestination().getName()
       distance = edge.getDistance()
       sundistance = edge.getSundistance()
       if not(src in self.nodes and dest in self.nodes):
           raise ValueError('Node not in graph')
       self.edges[src].append(dest)
       self.edgeweights[(src, dest)] = (distance, sundistance)
   def getWeights(self, node1, node2):
      if node2.getName() not in self.childrenOf(node1):
         raise ValueError('Nodes not connected by an edge')
      return self.edgeweights[(node1.getName(), node2.getName())]
   def childrenOf(self, node):
       return self.edges[node.getName()]
   def hasNode(self, node):
       return node.getName() in self.nodes
   def __str__(self):
       res = ''
       for k in self.edges:
           for d in self.edges[k]:
               res = res + str(k) + '->' + str(d) + '\n'
       return res[:-1]

