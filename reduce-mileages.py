# Copyright © 2014 Bart Massey
# Given a mileage list, reduce it to a minimal set of edges
# that imply the same mileages.

# Strategy: Fill the whole list of edges into the
# result, then loop over all triples deleting implied edges.

from sys import stdin, stderr

def read_graph(f):
    vs = set()
    es = {}
    for line in f:
        (v1, v2, w) = line.split()
        w = int(w)
        vs |= {v1}
        vs |= {v2}
        e = tuple({v1, v2})
        if e in es and es[e] != w:
            print("warning: edge {%s, %s} mismatch %d / %d" % \
                  (v1, v2, es[e], w), file=stderr)
            continue
        es[e] = w
    return (vs, es)

def reduced(g):
    (vs, es) = g
    res = es.copy()
    for e in es:
        for v in vs:
            if e not in res:
                continue
            (v1, v2) = e
            if v1 == v or v2 == v:
                continue
            e1 = tuple({v1, v})
            e2 = tuple({v, v2})
            if e1 not in es or e2 not in es:
                continue
            if es[e1] + es[e2] != es[e]:
                print("triangle error: %s %s %s" % (v1, v, v2), file=stderr)
                continue
            print("removing redundant %s %s" % (v1, v2), file=stderr)
            del res[e]
    return (vs, res)

def write_graph(g):
    (_, es) = g
    for e in es:
        (v1, v2) = e
        w = es[e]
        print(v1, v2, w)

g = read_graph(stdin)
rg = reduced(g)
write_graph(rg)
