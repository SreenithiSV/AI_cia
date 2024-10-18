import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def hill_climbing(graph, heuristics, start, goal):
    current_node = start
    explored_path = [current_node]

    while True:
        neighbors = graph[current_node]
        next_node = None
        best_heuristic = float('inf')

        for neighbor in neighbors:
            if neighbor not in explored_path: 
                if heuristics[current_node][neighbor] < best_heuristic:
                    best_heuristic = heuristics[current_node][neighbor]
                    next_node = neighbor

        if next_node is None:
            print("Stuck in local maxima!")
            break
        
        explored_path.append(next_node)
        current_node = next_node
        if current_node == goal:
            print("Goal reached!")
            break
    
    return explored_path

def visualize_graph(graph, explored_paths):
    G = nx.Graph()
    for node in graph:
        for neighbor, weight in graph[node].items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', edge_color='gray')

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    edges_in_path = [(explored_paths[i], explored_paths[i + 1]) for i in range(len(explored_paths) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color='red', width=2.5)

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

path = hill_climbing(d, d_h, 'S', 'G')
print("Explored Path:", path)

visualize_graph(d, path)
