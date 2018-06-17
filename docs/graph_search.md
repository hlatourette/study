# Graph Search

* [Depth-First Search](#dfs)
* [Breadth-First Search](#bfs)

There are two primary means to traverse/search a graph: depth-first and breadth-first. Although both will visit every other vertex that can be reached from a given vertex, they're optimal for different categories of problems.

## <a name="dfs"></a> Depth-First Search

A simple algorithm, DFS is preferred when we simply want to visit every vertex in a graph. In DFS, we wisit a vertex (_u_), then iterate through all of it's neighbors. When visiting one of these neighbors (_v_), we visit all of it's neighbors before continuing with the rest of _u_'s neighbors.

```python
def dfs(graph, vertex, func, neighbor_sort_key=lambda val: val):
    visited = set()
    _dfs(graph, vertex, visited, func, neighbor_sort_key)

def _dfs(graph, vertex, visited, func, sort_key):
    func(vertex)
    visited.add(vertex)
    for neighbor in sorted(graph[vertex], key=sort_key):
        if neighbor not in visited:
            _dfs(graph, neighbor, visited, func, sort_key)
```

### Complexity

* O(_v_)

## <a name="bfs"></a> Breadth-First Search

BFS is usually more useful if we want to find a path between two vertices in a graph. When visiting a vertex _u_, we iterate through all of it's neighbors and visit them before moving on to their own respective neighbors. The key to BFS is the use of a queue to track the neighboring vertices that still need to be visited.

```python
def bfs(graph, vertex, func, neighbor_sort_key=lambda val: val):
    queue = Queue()
    visited = set()
    visited.add(vertex)
    queue.enqueue(vertex)
    while not queue.is_empty():
        v = queue.dequeue()
        func(v)
        for neighbor in sorted(graph[v]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
```

### Complexity

* O(_v_)