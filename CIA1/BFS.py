import matplotlib.pyplot as plt
import networkx as nx

def BFS(graph, start, goal):
    queue = [[start]]  
    explored_paths = [] 
    goal_paths = [] 

    while queue:
        curr_path = queue.pop(0) 
        curr_node = curr_path[-1] 
        
        if curr_node in curr_path[:-1]: 
            continue
        if curr_node == goal:
            goal_paths.append(curr_path)

        for neighbor in graph[curr_node].keys():
            if neighbor not in curr_path: 
                new_path = curr_path + [neighbor]
                queue.append(new_path) 

        explored_paths.append(curr_path)

    print("All Paths Explored (including goal nodes):", explored_paths)
    print('BFS Paths containing the goal:', goal_paths)
    return explored_paths, goal_paths

def visualize_graph(graph, explored_paths, goal_paths):
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
    for goal_path in goal_paths:
        edges_in_goal_path = [(goal_path[i], goal_path[i + 1]) for i in range(len(goal_path) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges_in_goal_path, edge_color='green', width=3)

    plt.show()

d = {
    'S': {'A': 2, 'B': 4},
    'A': {'S': 2, 'B': 3, 'D': 2},
    'B': {'S': 4, 'A': 3, 'C': 2},
    'C': {'B': 2, 'E': 5},
    'E': {'C': 5},
    'D': {'A': 2, 'G': 4},
    'G': {'D': 4}
}

explored_paths, goal_paths = BFS(d, 'S', 'G')
visualize_graph(d, explored_paths, goal_paths)
