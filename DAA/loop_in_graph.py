from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def is_cyclic_util(self, v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True
        for neighbor in self.graph.get(v, []):
            if not visited[neighbor]:
                if self.is_cyclic_util(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                return True
        rec_stack[v] = False
        return False
    
    def is_cyclic(self):
        num_vertices = max((max(self.graph.keys()) if self.graph else 0), 
                           (max([v for values in self.graph.values() for v in values]) if self.graph else 0)) + 1
        visited = [False] * num_vertices
        rec_stack = [False] * num_vertices
        for i in range(num_vertices):
            if not visited[i] and i in self.graph:
                if self.is_cyclic_util(i, visited, rec_stack):
                    return True
        return False


g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 4)
g.add_edge(3, 1)
g.add_edge(3, 4)


if g.is_cyclic():
    print("The graph contains a cycle.")
else:
    print("The graph does not contain a cycle.")
