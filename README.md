# hw3_1113542
#Ferran

Question: 1
Given an undirected graph with V nodes and E edges, create and return an adjacency list of the graph. 0-based indexing is followed everywhere.
Examples: (Should not use the examples to submit your code. These examples are for your understanding)
Input:   vertices: 4
         edges: 5
Enter each edge as a pair of space-separated integers (u v):
0 1
0 2
1 2
1 3
2 3
output : [[1, 2], [0, 2, 3], [0, 1, 3], [1, 2]]

Question 2:
Given a connected undirected graph represented by an adjacency list adj, which is a vector of vectors where each adj[i] represents the list of vertices connected to vertex i. Perform a Breadth First Traversal (BFS) starting from vertex 0, visiting vertices from left to right according to the adjacency list, and return a list containing the BFS traversal of the graph.
Note: Do traverse in the same order as they are in the adjacency list.

Input: Enter the number of vertices in the graph: 6
Enter the adjacency list for each vertex:
Neighbors of vertex 0: 1 2
Neighbors of vertex 1: 0 3 4
Neighbors of vertex 2: 0 5
Neighbors of vertex 3: 1
Neighbors of vertex 4: 1
Neighbors of vertex 5: 2

 Output: BFS Traversal of the graph: [0, 1, 2, 3, 4, 5] 
 Explanation:
Vertex 0 is connected to vertices 1 and 2.
Vertex 1 is connected to vertices 0, 3, and 4.
Vertex 2 is connected to vertices 0 and 5.
Vertex 3 is connected to vertex 1.
Vertex 4 is connected to vertex 1.
Vertex 5 is connected to vertex 2.


Question 3:
Given a connected undirected graph represented by an adjacency list adj, which is a vector of vectors where each adj[i] represents the list of vertices connected to vertex i. Perform a Depth First Traversal (DFS) starting from vertex 0, visiting vertices from left to right as per the adjacency list, and return a list containing the DFS traversal of the graph.
Note: Do traverse in the same order as they are in the adjacency list.

input : Enter the number of nodes: 5
Enter neighbors of node 0 : 1 2
Enter neighbors of node 1 : 0 3
Enter neighbors of node 2 : 0 4
Enter neighbors of node 3 : 1
Enter neighbors of node 4 : 2

 Output : DFS Traversal: [0, 1, 3, 2, 4]

Question 4:
Given a weighted, undirected, and connected graph with V vertices and E edges, your task is to find the sum of the weights of the edges in the Minimum Spanning Tree (MST) of the graph. The graph is represented by an adjacency list, where each element adj[i] is a vector containing vector of integers. Each vector represents an edge, with the first integer denoting the endpoint of the edge and the second integer denoting the weight of the edge.
 input 
V: 4
E: 5

 output
0 1 10
0 2 6
0 3 5
1 3 15
2 3 4



