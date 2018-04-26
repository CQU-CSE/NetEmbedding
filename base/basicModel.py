
__author__ = "Junliang Yu"
__email__ = "yu.jl@cqu.edu.cn"

class BasicModel(object):
    def __init__(self,conf,graph):
        self.isLoad = False
        self.isSave = False

    def readConfiguration(self):
        pass

    def initialize(self):
        pass

    def train(self):
        pass

    def save(self):
        pass

    def load(self):
        pass

    def evaluate(self):
        pass

    def run(self):
        self.readConfiguration()

        if self.isLoad:
            self.load()
        else:
            self.initialize()
            self.train()

        if self.isSave:
            self.save()

        self.evaluate()

