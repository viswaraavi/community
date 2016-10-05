

"""
should take input files and should return graph in form
dict{v1:set(adjacency_list),......}
"""
from igraph import Graph

graph={}


f=open("amazon.graph.small")
edges_list=text = f.readlines()
for element in edges_list[1:]:
    edge=element.strip()
    edge=edge.split(" ")
    edge[0]=tuple([int(edge[0])])
    edge[1] = tuple([int(edge[1])])
    if(edge[0] in graph):
        graph[edge[0]].add(edge[1])
    else:
        graph[edge[0]]={edge[1]}

    if (edge[1] in graph):
        graph[edge[1]].add(edge[0])
    else:
        graph[edge[1]] = {edge[0]}


g = Graph.TupleList([(k, v) for k, vs in graph.iteritems() for v in vs])
membership=range(1,g.vcount()+1)
print(g.modularity(membership))
#print graph.keys





"""
Returns the degree of vertices as dictionary
"""

def degree():
    pass

"""
Partition the vertices into p
"""

def partition():
    pass

"""
takes input as graph
select min degree vertex
"""

def select_vertex_min_degree():
    pass


def calculate_delta_qv(u,v):
    temp=membership
    temp[v]=temp[u]
    


"""
compute v
v = arg max v 0 4Q uv 0 ;
"""

def compute_v():
    pass


"""
main function that would be called
"""




def algorithm():
    #T is set of vertices
    T=graph.keys()
    while(T):
        #partition function calculates all the nodes in graph with degree less than 0 or equal to 1
        p=partition()
        for element in p:
            new_vertex=graph[element][0]
            edge_list=graph[new_vertex]
            edge_list.remove(element)
            T=T-{element}
            graph[element+new_vertex]=edge_list
            del graph[element]
            del graph[new_vertex]

        u=select_vertex_min_degree()
        v=compute_v(u)
        if(calculate_delta_qv(u,v)>0):
            graph[u+v]=graph[u].remove(v)+graph[v].remove(u)
            del graph[u]
            del graph[v]
            T=T-{u,v}
            T=T+{u+v}
        else:
            T=T-{u}































