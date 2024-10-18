import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def oracle_cost_heur(d, start, end, d_heur, scaling_factor):
    return min([d[start][neighbor] + d_heur[start][neighbor] for neighbor in d[start].keys()]) * scaling_factor

def A_star_search(d, start, end, d_heur, oracle_cost_heur):
    queue = [[0, start]]
    path = []
    vis = []  
    gn = []
    
    while queue:
        sl = []
        cp = queue.pop(0)
        current_cost = cp[0] 
        current_node = cp[-1]  
        
        if current_node == end:
            gn = cp
            break
        
        for neighbor in d[current_node].keys():
            if neighbor in cp:
                continue
            elif current_cost + d[current_node][neighbor] + d_heur[current_node][neighbor] <= oracle_cost_heur and neighbor not in vis:
                vis.append(neighbor)
                new_path = cp + [neighbor]
                new_cost = current_cost + d[current_node][neighbor] + d_heur[current_node][neighbor]
                new_path[0] = new_cost
                sl.append(new_path)
                
        sl.sort(key=lambda x: x[0]) 
        queue.extend(sl) 

        for step in sl:
            path.append(step)
        
    print("Final Path:", gn)
    return gn

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

def form_graph(d, final_route):
    G = nx.Graph()
    for node in d.keys():
        for neighbor, weight in d[node].items():
            G.add_edge(node, neighbor, weight=weight)

    return G

def Viz(G, final_route):
    pos = nx.spring_layout(G) 
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15, font_weight='bold', edge_color='gray')
    path_edges = [(final_route[i], final_route[i + 1]) for i in range(len(final_route) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("A* Search Path Visualization")
    plt.show()

oracle_cost = oracle_cost_heur(d, 'S', 'G', d_h, 2)
final_route = A_star_search(d, 'S', 'G', d_h, oracle_cost)

g = form_graph(d, final_route)
Viz(g, final_route)
