

INF = 10000 # 'infinity' is something larger than expected value 

class Vertex:
    def __init__(self):
        self._name = '.'
        self._neighbors = []
        self._dist = INF
        self._seen = False

def nodeLvl(n):
    if n == 'S':
        return ord('a')
    if n == 'E':
        return ord('z')
    return ord(n)

def make_vertices(g):
    width  = len(g[0])
    height = len(g)
    verts = []
    targets = []
    source = None
    for x in range(width * height): verts.append(Vertex())
    for i, r in enumerate(g):
        for j, c in enumerate(r):
            lvl = nodeLvl(c)
            v = verts[(width * i) + j]
            v._name = c
            if (c == 'S' or c == 'a'): targets.append(v)
            elif (c == 'E'): source = v
            if (i < (height - 1)) and lvl <= (nodeLvl(g[i+1][j]) + 1):
                v._neighbors.append((width * (i + 1)) + j)
            if (j < (width - 1)) and lvl <= (nodeLvl(g[i][j+1]) + 1):
                v._neighbors.append((width * (i)) + j + 1)        
            if i > 0 and lvl <= (nodeLvl(g[i-1][j]) + 1):
                v._neighbors.append((width * (i - 1)) + j)
            if j > 0 and lvl <= (nodeLvl(g[i][j-1]) + 1):
                v._neighbors.append((width * (i)) + j - 1)
    return verts, source, targets

def pop_min_dist(q):
    m = INF
    bestIdx = 0
    for idx, v in enumerate(q):
        if v._dist < m:
            m = v._dist
            bestIdx = idx
    return q.pop(bestIdx)

def dijkstra(verts, source):
    q = []
    for v in verts: q.append(v)
    source._dist = 0
    
    while len(q) > 0:
        u = pop_min_dist(q)
        u._seen = True
        for vi in u._neighbors:
            v = verts[vi]
            if not v._seen:
                alt = u._dist + 1 # Graph distance is always 1
                if alt < v._dist:
                    v._dist = alt
                    v._prev = u
# script
grid  = []
#with open('test_ignored.txt') as f:
with open('day_12_input.txt') as f:
    for line in f:
        r = line.strip('\n')
        grid.append([i for i in r])

v, s, t = make_vertices(grid)
dijkstra(v, s)
part1 = t[0]
part2 = t[0]
for v in t: 
    if v._dist < part2._dist: part2 = v
    if v._name == "S": part1 = v
print( f"Result part1 {part1._dist}.")
print( f"Result part2 {part2._dist}.")
