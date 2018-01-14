from priodict import priorityDictionary
def Dijkstra(G,s,e=None):
    D = {}  # dictionary of final distances
    P = {}  # dictionary of predecessors
    Q = priorityDictionary()  # estimated distances of non-final vertices
    Q[s] = 0

    for v in Q:
        D[v] = Q[v]
        if v == e: break
        for w in G[v]:
            vwLength = D[v] + G[v][w]
            if w in D:
                if vwLength < D[w]:
                    raise ValueError, "Dijkstra: found better path to already-final vertex"
            elif w not in Q or vwLength < Q[w]:
                Q[w] = vwLength
                P[w] = v

    return (D, P)


def shortestPath(G,s,e):
    F_D, P_D = Dijkstra(G, s, e)
    Path = []
    while 1:
        Path.append(e)
        if e == s: break
        e = P_D[e]
    Path.reverse()
    return Path

G = G = {'A': {'B':10,'C':3},
	'B': {'D':2,'C':1},
	'C': {'B':4,'E':2,'D':8},
	'D':{'E':7},
	'E':{'D':9}}

print Dijkstra(G,'A')
print shortestPath(G,'A','D')