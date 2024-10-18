import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def oracle_cost_heur(d, start, end, d_heuristic, max_no_goalcutoff): 
    queue = [[0, start]]  
    res = []
    f = 0  
    g = end 
    n_g = max_no_goalcutoff 

    while len(queue) != 0: 
        tmp = [] 
        curr = queue.pop(0) 
        currnode = curr[-1]  
        for i in d[currnode].keys(): 
            if i in curr: 
                continue  
            tmp1 = curr + [i] 
            tmp1[0] = curr[0] + d[currnode][i] + d_heuristic[currnode][i]  # Update cumulative cost
            tmp.append(tmp1) 
            queue.append(tmp1) 

        queue.sort(key=lambda k1: k1[0])  
        for i in tmp: 
            if g == i[-1]: 
                f += 1 
                res.append(i)  
            
            if f == n_g: 
                break 

    goal_node = [] 
    for i in res: 
        if end in i: 
            goal_node.append(i)

    print('Oracle Paths:', goal_node) 
    return res 

def form_graph(d, paths):
    G = nx.DiGraph()

    for node, neighbors in d.items():
        for neighbor, cost in neighbors.items():
            G.add_edge(node, neighbor, weight=cost)

    for path in paths:
        for i in range(len(path) - 1):
            G[path[i]][path[i + 1]]['color'] = 'red'  

    return G

def Viz(G):
    pos = nx.spring_layout(G)  
    edges = G.edges()
    colors = [G[u][v].get('color', 'black') for u, v in edges]
    nx.draw(G, pos, edges=edges, edge_color=colors, with_labels=True, node_size=2000, node_color='lightblue')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Graph Visualization")
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

FR = oracle_cost_heur(d, 'S', 'G', d_h, 2)
g = form_graph(d, FR) 
Viz(g)
