import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "Common"))
from vertex import Vertex
from edge import Edge
from graph import Graph
from collections import deque

def to_visit_vertexes(curr_v,visited,edges):
        return [ e.destination for e in edges if e.origin == curr_v and e.destination not in visited ]

def recursive_dfs(curr_vertex,deep,father,visited,edges):
    vertex_stack = to_visit_vertexes(curr_vertex, visited,edges)
    result = str(curr_vertex) + " " + str(father) +" " + str(deep) + "\n"
    while( len(vertex_stack) != 0):
        adj_vertex = vertex_stack.pop()
        visited.append(adj_vertex)
        result += recursive_dfs(adj_vertex,deep + 1,curr_vertex,visited,edges)
    return result

def dfs(graph,start_vertex=None):
    vertexes = graph.V
    edges = graph.E
    if start_vertex == None:
        start_vertex = vertexes[0]
    visited = [start_vertex]
    deep = 0
    return recursive_dfs(start_vertex,deep,"--",visited,edges)


def main(args):
    V = [Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D"), Vertex("E"), Vertex("F"), Vertex("G")]
    E = [Edge(9,V[0],V[1]),Edge(10,V[0],V[5]) ,Edge(5,V[0],V[2]), Edge(10,V[1],V[2]), Edge(1,V[2],V[3]), Edge(11,V[2],V[4]), Edge(5,V[3],V[6])]
    G = Graph(V, E) 
    result = dfs(G)
    print "Node | Father | Deep"
    print result

if __name__ == "__main__":
    main(sys.argv[1:])
