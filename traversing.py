g = {1 : [2,3], 2:[4,5], 3:[6], 4:None, 5:[7,8], 6:None, 7:None, 8:None}

def BFS(s,t,g):
    print "Source:",s,"Target:",t
    queue = [s]
    v = []

    while len(queue) > 0:
        q =queue.pop(0)

        if q==t:
            v.append(q)
            return v
        elif q not in v:
            v = v+[q]

        if g[q] is not None:
            queue = queue + g[q]

    return v

def DFS(s,t,g):
    print "Source:",s,"Target:",t
    stack = [s]
    v = []

    while len(stack)>0:
        x=stack.pop(0)

        if x==t:
            v.append(x)
            return v
        elif x not in v:
            v = v+[x]
        if g[x] is not None:
            stack = g[x] + stack
    return v



print "BFS PATH", BFS(1,7,g)
print "DFS PATH", DFS(1,3,g)
print "=" * 80
print "BFS Path",BFS(1,3,g)
print "DFS Path",DFS(1,3,g)