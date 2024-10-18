import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def bestfirst(d, s, e):
    queue = [[0, s]] 
    res = []
    found = False  

    while queue:
        u = queue.pop(0) 
        print("Current path being explored:", u)

        if u[-1] == e:
            res.append(u)
            found = True
            break
        else:
            cn = u[-1] 
            for i in d[cn].keys():
                if i in u:
                    continue  
                new_path = u + [i]
                new_path[0] += d[cn][i] 
                queue.append(new_path)

                if i == e: 
                    res.append(new_path)
                    found = True
                    break

            queue.sort(key=lambda k: k[0])

            if found:
                break

        res.append(u)  

    print("Final result paths:", res)
    return res

def form_graph(d, final_route):
    G = nx.Graph()

    for node, neighbors in d.items():
        for neighbor, cost in neighbors.items():
            G.add_edge(node, neighbor, weight=cost)

    path_edges = [(final_route[i], final_route[i + 1]) for i in range(1, len(final_route[-1]) - 1)]

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

final_route = bestfirst(d, 'S', 'G')
g = form_graph(d, final_route)
Viz(g)
