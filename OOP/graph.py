from typing import Dict, List


class Graph:
    def __init__(self, directed=False) -> None:
        self._adj_mat : Dict[str, List] = {}
        self.directed = directed

    def add_node(self, node_name):
        if node_name in self._adj_mat:
            return
        else:
            self._adj_mat[node_name] = []

    def add_edge(self, node_a, node_b):
        """
        if graph is directed then we have an edge from frist argument to second argument
        """
        if node_a not in self._adj_mat:
            self.add_node(node_a)
        if node_b not in self._adj_mat:
            self.add_node(node_b)

        if not self.directed:
            self._adj_mat[node_a].append(node_b)
            self._adj_mat[node_b].append(node_a)
        else:
            self._adj_mat[node_a].append(node_b)
    
    def degree(self, node_a):
        
        assert node_a in self._adj_mat, f"{node_a} dar graph nist"
        
        if self.directed:
            print("felan elm riazimun nemikeshe. bayad berim bekhunim. bad az chan sanie shaghayegh search kard va fahmidim che khabare va tamrin shod.")
            return
        else:
            return len(self._adj_mat.get(node_a))
            
    def __str__(self) -> str:
        return str(self._adj_mat)

    def is_connected(self) -> bool:
        pass

    def short_path(self, node_a, node_b):
        pass


g_1 = Graph()
g_1.add_node("a")
g_1.add_node("b")
g_1.add_node("c")
g_1.add_node("d")
g_1.add_node("e")

g_1.add_edge("a", "b")
g_1.add_edge("a", "c")
g_1.add_edge("d", "c")
g_1.add_edge("d", "b")
g_1.add_edge("c", "b")
print(g_1)
print(g_1.degree("e"))
