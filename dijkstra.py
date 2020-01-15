from graph import Graph
import time
sx = 10
sy = 10
dx = 20
dy = 20
g = Graph(sx, sy, dx, dy)


def setup():
    size(501, 501)
    g.createGraph()
    g.helperBFS()
    # creating graph nodes at every position of the array


def draw():
    background(255)
    # displaying the grid
    g.displayGraph()
    path = g.dijkstra()
    g.show()
    fill(255, 0, 0)
    rect(sx*10, sy*10, 10, 10)
    fill(255, 0, 0)
    rect(dx*10, dy*10, 10, 10)
    if path:
        for k in range(1, len(path)-1):
            path[k].findColour(131, 20, 242)
