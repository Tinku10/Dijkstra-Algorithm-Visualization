from node import Node
import heapq

class Graph:
    def __init__(self, sx, sy, dx, dy):
        self.nodes = [[None for i in range(50)] for j in range(50)]
        self.q = []
        self.close = []
        self.path = [[None for i in range(50)] for j in range(50)]
        self.sx = sx
        self.sy = sy
        self.dx = dx
        self.dy = dy
        self.countP = 0

    def insertEdges(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                node = arr[i][j]
                if i-1 >= 0:
                    if arr[i-1][j].wall == False:
                        node.edges[0] = arr[i-1][j]
                if i+1 <= len(arr)-1:
                    if arr[i+1][j].wall == False:
                        node.edges[1] = arr[i+1][j]
                if j-1 >= 0:
                    if arr[i][j-1].wall == False:
                        node.edges[2] = arr[i][j-1]
                if j+1 <= len(arr)-1:
                    if arr[i][j+1].wall == False:
                        node.edges[3] = arr[i][j+1]
                # for diagonal movement
                if j-1 >= 0 and i-1 >= 0:
                    if arr[i-1][j-1].wall == False:
                        node.edges[4] = arr[i-1][j-1]
                if j-1 >= 0 and i+1 <= len(arr)-1:
                    if arr[i+1][j-1].wall == False:
                        node.edges[5] = arr[i+1][j-1]
                if j+1 <= len(arr)-1 and i-1 >= 0:
                    if arr[i-1][j+1].wall == False:
                        node.edges[6] = arr[i-1][j+1]
                if j+1 <= len(arr)-1 and i+1 <= len(arr)-1:
                    if arr[i+1][j+1].wall == False:
                        node.edges[7] = arr[i+1][j+1]

    def createGraph(self):
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                self.nodes[i][j] = Node(i, j)
                if random(1) < 0.2:
                    if i != self.sx and j != self.sy or i != self.dx and j != self.dy:
                        # if i == -j+40 and i > 5 and j > 5:
                        self.nodes[i][j].wall = True
        self.insertEdges(self.nodes)

    def displayGraph(self):
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                if self.nodes[i][j].wall:
                    self.nodes[i][j].findColour(48, 45, 46)
                else:
                    self.nodes[i][j].findColour(255, 255, 255)

    def helperBFS(self):
        if len(self.q) == 0:
            heapq.heappush(self.q, [0, 0, self.nodes[self.sx][self.sy]])
        for i in range(len(self.path)):
            for j in range(len(self.path)):
                self.path[i][j] = [self.nodes[self.sx][self.sy]]
            
            

    def dijkstra(self):
        dest = self.nodes[self.dx][self.dy]
        if len(self.q) > 0:
            rmdic = heapq.heappop(self.q)
            [distance, order, rm] = rmdic
            self.close.append(rm)
            count = order
            for node in rm.edges:
                if node:
                    if node not in self.close:
                        count += 1
                        if node.distance == float("inf") and node.distance != "removed":
                            node.distance = distance + 1     #edge.wt == 1
                            if self.path[rm.i][rm.j]:
                                self.path[node.i][node.j] = [node]
                                self.path[node.i][node.j].extend(
                                    self.path[rm.i][rm.j])
                            heapq.heappush(
                                self.q, [node.distance, count, node])

                        else:
                            for dic in self.q:
                                [a, order, b] = dic
                                if b is node:
                                    if rm.distance + 1 < node.distance:    #edge.wt == 1
                                        # if previous value was larger, label it "removed" and push the new value
                                        # labeled node will not be considered
                                        b.distance = "removed"
                                        node.distance = distance + 1     #edge.wt == 1
                                        heapq.heappush(
                                            self.q, [node.distance, count, node])
                                        if self.path[rm.i][rm.j]:
                                            self.path[node.i][node.j] = [node]
                                            self.path[node.i][node.j].extend(self.path[rm.i][rm.j])
                    if node is dest:
                        # stop searching when all checks for dest is done
                        self.countP += 1
                        print(self.countP)
                        if self.countP == len(dest.edges)-dest.edges.count(None):
                            noLoop()
                            return self.path[self.dx][self.dy]


    def show(self):
        for i in range(len(self.q)):
            self.q[i][2].findColour(113, 216, 80)
        for j in range(len(self.close)):
            self.close[j].findColour(159, 234, 239)
