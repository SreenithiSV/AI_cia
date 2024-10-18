import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def BMS(graph, start, goal, max_no_goalcutoff):
    queue = [[start]] 
    res = [] 
    f = 0 
    n_g = max_no_goalcutoff 

    while len(queue) != 0:
        tmp = []  
        curr = queue.pop(0)  
        currnode = curr[-1] 

        for neighbor in graph[currnode].keys():
            if neighbor in curr:  # Avoid cycles
                continue

            tmp1 = curr + [neighbor]
            tmp.append(tmp1)
            queue.append(tmp1) 

            queue.sort(key=lambda k1: ord(k1[-1]))

            if goal == neighbor:
                f += 1

        for i in tmp:
            res.append(i)

        if f == n_g:
            break

    print("All Paths Explored:", res)

    goal_node = [i for i in res if goal in i]
    print('BMS Paths containing the goal:', goal_node)

    return res, goal_node
graph_example = {
    'S': {'A': 2, 'B': 4}, 
    'A': {'S': 2, 'B': 3, 'D': 2}, 
    'B': {'S': 4, 'A': 3, 'C': 2}, 
    'C': {'B': 2, 'E': 5},  
    'E': {'C': 5}, 
    'D': {'A': 2, 'G': 4}, 
    'G': {'D': 4} 
}


def visualize_graph(graph, explored_paths):
    G = nx.Graph()

    for node in graph:
        for neighbor, weight in graph[node].items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', edge_color='gray')

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    for path in explored_paths:
        edges_in_path = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color='red', width=2.5)

    plt.show()
explored_paths, goal_paths = BMS(graph_example, 'S', 'G', 2)
visualize_graph(graph_example, explored_paths)
