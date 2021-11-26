from collections import defaultdict


class Graph(object):
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, v1, v2):
        self.graph[v1].append(v2)

    def DFS(self, start_node):
        """Initialize stack, push initial node, loop thru the stack"""
        stack = []
        visited = set()
        stack.append(start_node)
        
        while len(stack):
            current = stack[-1]
            stack.pop()

            if current not in visited:
                print(current, end="->")
                visited.add(current)

            for vertex in self.graph[current]:
                if vertex not in visited:
                    stack.append(vertex)


g = Graph()

g.insertEdge(2, 1)
g.insertEdge(2, 5)
g.insertEdge(5, 6)
g.insertEdge(5, 8)
g.insertEdge(6, 9)

g.DFS(2)
