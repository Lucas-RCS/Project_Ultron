class Node(object):
    def __init__(self, father=None, coord=None, level=None, previous=None, 
                       next=None):
        self.father       = father
        self.coord    = coord
        self.level     = level
        self.valor2     = 0
        self.previous  = previous
        self.next   = next