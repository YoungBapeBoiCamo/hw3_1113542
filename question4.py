# Your Name: Ferran
# Student ID: 1113542
# Date of Submission: 2024/12/12


# Function to find the root of a node
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

# Function to do the union of two sets
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

# Function to calculate MST
def kruskal(V, edges):
    # Sort edges by their weight
    edges = sorted(edges, key=lambda x: x[2])
    
    parent = [i for i in range(V)]
    rank = [0] * V

    mst_weight = 0
    mst_edges = []

    # Process each edge in sorted order
    for u, v, weight in edges:
        # Find the roots of the two vertices
        root_u = find(parent, u)
        root_v = find(parent, v)

        # If the roots are different, then include this edge in MST
        if root_u != root_v:
            mst_weight += weight
            mst_edges.append((u, v, weight))
            union(parent, rank, root_u, root_v)

    return mst_weight


V = int(input("V: "))
E = int(input("E: "))
edges = []

print("Enter the edges in the format 'u v weight':")
for _ in range(E):
    u, v, weight = map(int, input().split())
    edges.append((u, v, weight))

# Find the weight of the MST
mst_weight = kruskal(V, edges)
print(f"The weight of the Minimum Spanning Tree is: {mst_weight}")
