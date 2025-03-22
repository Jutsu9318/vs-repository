def bipartite(graph):
    n = len(graph.keys())
    colors = [-1] * n

    for start in range(n):
        if colors[start] == -1:
            queue = [start]
            colors[start] = 0

            while queue:
                u = queue.pop(0)
                for v in graph[u]:
                    if colors[v] == -1:
                        colors[v] = 1 - colors[u]
                        queue.append(v)
                    elif colors[v] == colors[u]:
                        return False, []

    set1 = [i for i in range(n) if colors[i] == 0]
    set2 = [i for i in range(n) if colors[i] == 1]
    return True, (set1, set2)


def kuhn(graph):
    n = len(graph.keys())
    match = [-1] * n
    _, parts = bipartite(graph)
    L = parts[0]

    def dfs(v, visited):
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                if match[u] == -1 or dfs(match[u], visited):
                    match[u] = v
                    return True
        return False

    max_matching = 0
    for v in L:
        visited = [False] * n
        if dfs(v, visited):
            max_matching += 1
    return match, max_matching


def minpocr(graph):
    a, parts = bipartite(graph)
    if not a:
        return 'pym pym'
    queue = []
    match, _ = kuhn(graph)
    L, R = parts
    v_L = [False] * len(graph)
    v_R = [False] * len(graph)
    for v in L:
        notm = True
        for u in graph[v]:
            if match[u] == v:
                notm = False
                break
        if notm:
            queue.append(v)
            v_L[v] = True
    while queue:
        v = queue.pop(0)
        for u in graph[v]:
            if match[u] != v and not v_R[u]:
                v_R[u] = True
                if match[u] is not None and not v_L[match[u]]:
                    v_L[match[u]] = True
                    queue.append(match[u])
    b = []
    for v in L:
        if not v_L[v]:
            b.append(v)
    c = []
    for v in R:
        if v_R[v]:
            c.append(v)

    return b + c
G = {
    0: [1, 3],
    1: [0, 2, 6],
    2: [1],
    3: [4],
    4: [3, 5, 7],
    5: [0, 4],
    6: [1],
    7: [4]
}
print(minpocr(G))
