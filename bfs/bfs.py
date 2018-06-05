import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "Common"))
from vertex import Vertex
from edge import Edge
from graph import Graph
from collections import deque

def to_visit_vertexes(curr_v,visited,edges):
    return [ e.destination for e in edges if e.origin == curr_v and e.destination not in visited ]

def register_path(to_visit_list, father,depth):
    return map(lambda k: str(k) + " | " + str(depth) + " | " + str(father), to_visit_list )

def bfs(graph, start_vertex=None):
    result = ["Node | Depth | Father"]
    vertexes = graph.V
    edges = graph.E
    if start_vertex == None:
        start_vertex = vertexes[0]
    vertex_queue = deque([ start_vertex ])
    visited = [start_vertex]
    result += [str(start_vertex) + " | " + "0" + " | " + " -- "]
    depth_level = 1
    while len(vertex_queue) != 0:
        curr_vertex = vertex_queue.popleft()
        visited.append(curr_vertex)
        to_visit_list = to_visit_vertexes(curr_vertex,visited,edges)
        map(lambda x: vertex_queue.append(x), to_visit_list)
        visited.extend(to_visit_list)
        result += register_path(to_visit_list,curr_vertex,depth_level)
        if len(to_visit_list) != 0:
            depth_level += 1
    return "\n".join(result)
        

def main(args):
    V = [Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D"), Vertex("E")]
    E = [Edge(9,V[0],V[1]), Edge(5,V[0],V[2]), Edge(10,V[1],V[2]), Edge(1,V[2],V[3]), Edge(11,V[2],V[4])]
    G = Graph(V, E) 
    result = bfs(G)
    print result

if __name__ == "__main__":
    main(sys.argv[1:])
