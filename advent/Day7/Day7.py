import re

input = open("input.txt", "r", encoding="utf-8").read()

rows = input.splitlines()

rs = [row.split("->") for row in rows]

leaves = [elem for elem in rs if len(elem) == 1]

nodes = [elem for elem in rs if len(elem) == 2]

name = re.compile("[a-z]+")

non_roots = [name.findall(node[1]) for node in nodes]
non_roots_flat = [elem for list in non_roots for elem in list]

candidates = [name.search(node[0]).group() for node in nodes]

roots = [elem for elem in candidates if not elem in non_roots_flat]

# part 1
print(roots)
root = roots[0]

# part 2:
# Can be modelled as a graph problem where we fill a field tw (tower weight) for each node and determine wheter
# a given node is balanced base on the tw-values of its children. V is the set of nodes, and adj is the adjacency list of our graph

V = [row.split()[0] for row in rows]
leaves = [name.search(leaf[0]).group() for leaf in leaves]

number = re.compile("\d+")

adj = dict.fromkeys(V)
w = dict.fromkeys(V)
tw = dict.fromkeys(V)

# Filling out weights and adjacency list
for row in rows:
    names = name.findall(row)
    v = names[0]
    w[v] = int(number.search(row).group())
    children = [elem for elem in names if elem != names[0]]
    adj[v] = children

#Bottom up filling of tw
def balanced(v):
    if v in leaves:
        tw[v] = w[v]
        return True

    tw_ = w[v]
    child_tws = set()
    count = {}

    for u in adj[v]:
        balanced(u)

        child_tws.add(tw[u])

        if tw[u] in count:
            count[tw[u]] = count[tw[u]] + 1
        else:
            count[tw[u]] = 1
        tw_ += tw[u]

    tw[v] = tw_

    if len(child_tws) != 1:
        # We found a node where children dont have same tower-weight. We print what the weight of the "odd-child-out" should be.
        print(v + " was not balanced")
        bad_node = [u for u in adj[v] if count[tw[u]] == min(count.values()) ][0]
        matchweight = [x for x in child_tws if count[x]==max(count.values())][0]
        correct = w[bad_node] + (matchweight-tw[bad_node])
        print(bad_node + " should have weight " + str(correct) +" but has weight " + str(w[bad_node]))
        return False

    return True

balanced(root)

