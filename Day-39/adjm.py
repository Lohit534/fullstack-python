n = 4
edges = [(1,2,2) , (2,3,1) , (4,3,1) , (1,4,1)]

adj = {}
for i in range(1,n+1):
    adj[i] = []

print(adj)

for i in edges:
    u ,v,w = i
    print(u , v , w ,adj)
    adj[u].append((v,w))
    #undirected graph
    adj[v].append((u,w))

print("\n",adj)
# n = 4
# edges = [(1,2,2) , (2,3,3) , (3,4,4)]

# adjMatrix = [ [0] * (n+1) for i in range(n+1)]

# for i in edges:
#     u , v , w = i
#     adjMatrix[u][v] = w
#     #undirected graph
#     # adjMatrix[v][u] = w

# for row in adjMatrix:
#     print(row)


# edges = [(1,2,2) , (2,3,1) , (4,3,1) , (1,4,1)]