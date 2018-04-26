import networkx as nx


__author__ = "Junliang Yu"
__email__ = "yu.jl@cqu.edu.cn"

class Graph(nx.Graph):
    'Basic Graph: Homogeneous Graph'
    def __init__(self):
        pass

class AGraph(Graph):
    'Attributed Graph'
    def __init__(self):
        super(AGraph, self).__init__()

class HGraph(object):
    'Heterogeneous Graph'
    def __init__(self):
        pass