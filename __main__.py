import math


def find_all_path(start, end, graph, path=None):
    if not path:
        path = []

    path = path + [start]
    if start == end:
        # todo: path
        distant = 0
        for i in range(1, len(path)):
            distant += graph[path[i - 1]][path[i]]

        return [distant]

    if start not in graph:
        # todo: empty
        return [math.inf]

    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_path(node, end, graph, path)
            for newpath in newpaths:
                paths.append(newpath)

    return paths

if __name__ == '__main__':
    with open('data') as f:
        line = f.readline()
        n, m = line.split()
        m = int(m)

        line = f.readline()
        vertices = line.split()

        edges = []
        for _ in range(m):
            line = f.readline()
            edges.append(line.split())

        queries = []
        l = int(f.readline())
        for _ in range(l):
            line = f.readline()
            queries.append(line.split())

        d = {}
        for vertex in vertices:
            d[vertex] = {}

        for edge in edges:
            d[edge[0]][edge[1]] = int(edge[2])
            d[edge[1]][edge[0]] = int(edge[2])

        for q in queries:
            try:
                print(min(find_all_path(q[0], q[1], d)))
            except ValueError:
                print(math.inf)
