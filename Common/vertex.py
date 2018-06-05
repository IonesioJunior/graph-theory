from enum import Enum

class VertexColor(Enum):
    WHITE = 0
    GREY  = 1
    BLACK = 2

class Vertex():
    def __init__(self, name):
        self.name = name
        self.color = VertexColor.WHITE

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return str(self.name)
