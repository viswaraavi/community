

"""
should take input files and should return graph in form
dict{v1:set(adjacency_list),......}
"""

graph={}

def load_graph():
    pass

"""
Returns a set of vertices
"""

def set_vertices():
    pass

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


def calculate_delta_qv():
    pass



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
    T=set_vertices()
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































