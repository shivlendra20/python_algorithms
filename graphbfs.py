
from collections import defaultdict as ddict

class Graph:
    def __init__(self):
        self.graph = ddict(list)
        
    def addEdge(self, u, v):
        self.graph[u].append(v)
        
    def BFS(self, s):
        
        visited = [False] * (max(self.graph) + 1)
        
        queue = []
        
        queue.append(s)
        visited[s] = True
        
        while queue:
            
            s = queue.pop(0)
            print(s, end = " ")
            
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
            
            
if __name__ == '__main__':
    grf = Graph()
    
    grf.addEdge(0, 1)
    grf.addEdge(1, 2)
    grf.addEdge(2, 3)
    grf.addEdge(3, 1)
    grf.addEdge(2, 0)
    
    grf.BFS(1)