from collections import defaultdict


class Graph:
    def __init__(self, adj_list={}, directed=False):
        self._adj = defaultdict(dict)
        self._directed = directed
        self.add_edges(adj_list=adj_list)

    def __getitem__(self, vertex):
        if vertex not in self._adj:
            raise KeyError
            
        return self._adj[vertex]

    def __delitem__(self, vertex):
        del self._adj[vertex]
        for u, adj in self._adj.items():
            if vertex in self._adj[u]:
                del self._adj[u][vertex]

    def __len__(self):
        return len(self._adj)

    def add_edges(self, adj_list={}):
        for u, adj in adj_list.items():
            for v, attr in adj.items():
                self.add_edge(u, v, attr)

    def add_edge(self, u_of_edge, v_of_edge, attributes={}):
        if u_of_edge in self._adj and v_of_edge in self._adj[u_of_edge]:
            raise Exception

        self._adj[u_of_edge][v_of_edge] = attributes
        self._adj[v_of_edge]
        if not self._directed and u_of_edge != v_of_edge:
            self._adj[v_of_edge][u_of_edge] = attributes
