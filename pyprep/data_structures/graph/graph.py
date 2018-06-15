from collections import defaultdict


class Graph:
    def __init__(self, adj_list={}, directed=False, multigraph=False):
        self._adj = defaultdict(list)
        self._directed = directed
        self._multigraph = multigraph
        self.add_edges(adj_list=adj_list)

    def __getitem__(self, vertex):
        if vertex not in self._adj:
            raise KeyError
            
        return self._adj[vertex]

    def __delitem__(self, vertex):
        del self._adj[vertex]
        for u, adj in self._adj.items():
            self._adj[u] = [val for val in adj if val != vertex]

    def __len__(self):
        return len(self._adj)

    def add_edges(self, adj_list={}, edge_list=[]):
        for u, adj in adj_list.items():
            for v in adj:
                self.add_edge(u, v)

        for edge in edge_list:
            self.add_edge(edge[0], edge[1])

    def add_edge(self, u_of_edge, v_of_edge):
        if u_of_edge in self._adj and v_of_edge in self._adj[u_of_edge] and not self._multigraph:
            raise Exception

        self._adj[u_of_edge].append(v_of_edge)
        self._adj[v_of_edge]
        if not self._directed and u_of_edge != v_of_edge:
            self._adj[v_of_edge].append(u_of_edge)