# Name: Ferran
# Student ID: 1113542
# Date of Submission: 2024/12/12

from collections import deque

def bfs_traversal(adj):
    """
    Perform Breadth First Search (BFS) on a graph represented as an adjacency list.

    Parameters:
        adj (list of list of int): The adjacency list of the graph.

    Returns:
        list of int: The BFS traversal order.
    """
    visited = [False] * len(adj)  # To keep track of visited nodes
    queue = deque([0])           # BFS queue, starting from node 0
    visited[0] = True
    bfs_result = []              # To store the BFS traversal order

    while queue:
        # Dequeue a vertex and add it to the BFS result
        current = queue.popleft()
        bfs_result.append(current)

        # Enqueue all unvisited neighbors of the current vertex
        for neighbor in adj[current]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

    return bfs_result

if __name__ == "__main__":
    # Take user input for the adjacency list
    n = int(input("Enter the number of vertices: "))
    adj = []
    print("Enter the adjacency list for each vertex:")
    for i in range(n):
        neighbors = list(map(int, input(f"Neighbors of vertex {i}: ").split()))
        adj.append(neighbors)

    # Perform BFS and print the result
    print("BFS Traversal of the graph:", bfs_traversal(adj))
