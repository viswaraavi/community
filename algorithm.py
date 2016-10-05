
"""
should take input files and should return graph in form
dict{v1:set(adjacency_list),......}
"""
from igraph import EdgeSeq
from igraph import Graph
import sys

graph= {}
mapping={}
f = open("amazon.graph.small")
edges_list = text = f.readlines()
for element in edges_list[1:]:
    edge = element.strip()
    edge = edge.split(" ")
    edge[0] = edge[0]
    edge[1] = edge[1]
    if (graph.has_key(edge[0])):
        graph[edge[0]].add(edge[1])
    else:
        graph[edge[0]] = {edge[1]}

    if (graph.has_key(edge[1])):
        graph[edge[1]].add(edge[0])
    else:
        graph[edge[1]] = {edge[0]}


mapping["0"]=0
for i in range(1,len(graph)):
    mapping[str(i)]=i
g= Graph(edges= [(mapping[v], mapping[a]) for v in graph.keys() for a in graph[v]])
membership = range(0, g.vcount() )




"""
Returns the degree of vertices as dictionary
"""


def degree(graph):
    degree1 = {}
    for element in graph:
        degree1[element] = len(graph[element])

    degree_list = sorted(degree1.items(), key=lambda x: x[1])
    return degree_list


"""
Partition the vertices into p
"""


def partition(graph):
    p=set()
    list1=degree(graph)
    for element in list1:
        if(element[1]==1):
            p.add(element[0])

    return p



"""
takes input as graph
select min degree vertex
"""


def select_vertex_min_degree(graph):
    list1 = degree(graph)
    return list1[0][0]






def calculate_delta_qv(u, v):
    temp = membership
    temp[int(v)] = temp[int(u)]
    return g.modularity(temp)



"""
compute v
v = arg max v 0 4Q uv 0 ;
"""


def compute_v(u):
    maximum=-(sys.maxint)
    v=0
    
    for vertex in graph[u]:
        temp=calculate_delta_qv(u,vertex)
        if(temp>maximum):
            v=vertex
        return v


"""
main function that would be called
"""

list1=[]

def algorithm():
    # T is set of vertices
    T = set(graph.keys())
    while (T):
        # partition function calculates all the nodes in graph with degree less than 0 or equal to 1
        p=partition(graph)
        for element in p:
            T = T - {element}
            if(graph[element]):
                new_vertex=list(graph[element])[0]
                if(new_vertex in graph):
                    graph[new_vertex] = graph[new_vertex] - {element}
            membership[int(element)] = membership[int(new_vertex)]
            g.contract_vertices(membership)
            del graph[element]

           
        u = str(select_vertex_min_degree(graph))
        list1.append(u)
        v = compute_v(u)
        if (calculate_delta_qv(u, v) > 0):
            membership[int(v)]=membership[int(u)]
            g.contract_vertices(membership)
            T = T - {u, v}
            for element in graph[u]:
                if (element in graph):
                    graph[element]=graph[element]-{u}
            if(v in graph):
                graph[v]=graph[v] | graph[u]-{v}
            del graph[u]


        else:
            T = T - {u}
            del graph[u]

        

algorithm()
index=0
for element in set(membership):
    print "community"+str(index)
    indices = [i for i, x in enumerate(membership) if x == element]
    print indices
    index=index+1


