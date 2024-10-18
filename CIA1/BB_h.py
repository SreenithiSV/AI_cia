import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def branch_and_bound_heur(d_h, start, end, oracle):
    queue = [[0, start]]  
    path = []
    vis = set() 
    gn = [] 

    while queue:
        queue.sort(key=lambda x: x[0])
        current_path = queue.pop(0) 
        current_node = current_path[-1]

        if current_node == end:
            path.append(current_path)
            gn = current_path
            break

        for neighbor, cost in d_h[current_node].items():
            if neighbor in current_path: 
                continue

            if current_path[0] + d_h[current_node][neighbor] <= oracle:
                new_path = current_path[:] 
                new_path[0] += d_h[current_node][neighbor]  
                new_path.append(neighbor)
                queue.append(new_path)  
    print("Final path with heuristic:", gn)
    return gn

def oracle_cost_heur(d, start, end, d_h, factor):
    return sum([min(heuristics.values()) for heuristics in d_h.values() if heuristics.values()]) * factor

def form_graph(d, final_route):
    G = nx.Graph()
    for node, neighbors in d.items():
        for neighbor, cost in neighbors.items():
            G.add_edge(node, neighbor, weight=cost)

    
    path_edges = [(final_route[i], final_route[i + 1]) for i in range(len(final_route) - 1)]

    pos = nx.spring_layout(G) 
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=15, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{d[u][v]}' for u, v in G.edges()})
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2.5)

    return G

def Viz(G):
    plt.show()

d = {
    'S': {'A': 2, 'B': 4},
    'A': {'S': 2, 'B': 3, 'D': 2},
    'B': {'S': 4, 'A': 3, 'C': 2},
    'C': {'B': 2, 'E': 5},
    'E': {'C': 5, 'G': 2}, 
    'D': {'A': 2, 'G': 4},
    'G': {'D': 4, 'E': 2}
}

d_h = { 
    'S': {'A': 3, 'B': 2}, 
    'A': {'S': np.inf, 'B': 1, 'D': 3}, 
    'B': {'S': np.inf, 'A': 2, 'C': 1}, 
    'C': {'B': 1, 'E': 2}, 
    'E': {'C': 2, 'G': 0},  
    'D': {'A': 3, 'G': 1}, 
    'G': {'D': 1, 'E': 0} 
}

oracle_value = oracle_cost_heur(d, 'S', 'G', d_h, 2)
final_route = branch_and_bound_heur(d_h, 'S', 'G', oracle_value)

g = form_graph(d, final_route)
Viz(g)
