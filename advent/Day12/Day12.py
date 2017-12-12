import re
from collections import deque

input = open("input.txt", "r", encoding="utf-8").read()

# Constructing undirected graph: nodes and edges:
number = re.compile("\d+")
rows = [number.findall(row) for row in input.splitlines()]
nodes = set([row[0] for row in rows])
adj = dict.fromkeys(nodes)
for row in rows:
    adj[row[0]] = row[1:]


# Part 1 can be solved using BFS:
def transitiveClosure(start, V, adj):
    black = dict.fromkeys(V, False)
    black[start] = True
    Q = deque()
    Q.appendleft(start)
    while len(Q) != 0:
        u = Q.pop()
        for v in adj[u]:
            if not black[v]:
                black[v] = True
                Q.appendleft(v)

    closure = set([key for (key, bool) in black.items() if bool])
    return closure


# Part 1
print(len(transitiveClosure("0",nodes,adj)))

# Part 2
def stronglyConnectedComponents(V, adj):
    groups = []
    while len(V) != 0:
        v = V.pop()
        group = transitiveClosure(v, V, adj)
        groups.append(group)
        V.difference_update(group)

    return groups

print(len(stronglyConnectedComponents(nodes,adj)))