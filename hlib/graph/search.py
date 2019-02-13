from collections import deque

def dfs(graph, vertex, func, neighbor_sort_key=lambda val: val):
    visited = set()
    _dfs(graph, vertex, visited, func, neighbor_sort_key)

def _dfs(graph, vertex, visited, func, sort_key):
    func(vertex)
    visited.add(vertex)
    for neighbor in sorted(graph[vertex], key=sort_key):
        if neighbor not in visited:
            _dfs(graph, neighbor, visited, func, sort_key)


def bfs(graph, vertex, func, neighbor_sort_key=lambda val: val):
    queue = deque()
    queue.append(vertex)
    visited = set()
    visited.add(vertex)
    while len(queue) > 0:
        v = queue.popleft()
        func(v)
        for neighbor in sorted(graph[v], key=neighbor_sort_key):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
