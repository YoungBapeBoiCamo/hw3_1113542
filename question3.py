# Name: Ferran
# Student ID: 1113542
# Date of Submission: 2024/12/12

# Depth First Search (DFS) implementation in Python

def dfs_traversal(adj):
  
    visited = set()  # To keep track of visited nodes
    traversal = []  # List to store DFS traversal order

    def dfs(node):
        # Mark the current node as visited and add it to the traversal list
        visited.add(node)
        traversal.append(node)

        # Recur for all neighbors of the current node, in the given order
        for neighbor in adj[node]:
            if neighbor not in visited:
                dfs(neighbor)

    # Start DFS from node 0 (assuming node 0 always exists)
    dfs(0)

    return traversal
adj_list = []
n = int(input("Enter the number of nodes: "))
for i in range(n):
    neighbors = list(map(int, input(f"Enter neighbors of node {i} (separate by space): ").split()))
    adj_list.append(neighbors)

# Perform DFS traversal
result = dfs_traversal(adj_list)
print("DFS Traversal:", result)
