# Your Name: Ferran
# Student ID: 1113542
# Date of Submission: 2024/12/12

# create and return an adjacency list for an undirected graph
def create_adjacency_list(V, edges):
    # Initialize an empty adjacency list with V empty lists
    adjacency_list = [[] for _ in range(V)]

    # Iterate over each edge in the edges list
    for edge in edges:
        u, v = edge  # Extract the two vertices of the edge
        adjacency_list[u].append(v)  # Add v to u's adjacency list
        adjacency_list[v].append(u)  # Add u to v's adjacency list 

    return adjacency_list


if __name__ == "__main__":
    # Prompt user for input
    V = int(input("Enter the number of vertices: "))  
    E = int(input("Enter the number of edges: "))    

    edges = []
    print("Enter each edge as a pair of space-separated integers (u v):")
    for _ in range(E):
        u, v = map(int, input().split())  # Read each edge
        edges.append([u, v])

    # Call function to creatae the adjacency list
    adjacency_list = create_adjacency_list(V, edges)

    # Print the adjacency list
    print("Adjacency List:", adjacency_list)
