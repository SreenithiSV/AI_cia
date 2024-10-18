class Node:
    def __init__(self, name, heuristic, node_type, children=None):
        self.name = name
        self.heuristic = heuristic
        self.node_type = node_type 
        self.children = children if children is not None else []
        self.cost = float('inf')
        self.solved = False
        self.best_child = None

def ao_star(graph, start_node):
    if graph[start_node].solved:
        return graph[start_node].cost

    if graph[start_node].node_type == 'OR':
        min_cost = float('inf')
        for child in graph[start_node].children:
            child_cost = ao_star(graph, child)
            if child_cost + graph[start_node].heuristic < min_cost:
                min_cost = child_cost + graph[start_node].heuristic
                graph[start_node].best_child = child
        graph[start_node].cost = min_cost
        graph[start_node].solved = True
        return min_cost

    elif graph[start_node].node_type == 'AND':
        total_cost = graph[start_node].heuristic
        for child in graph[start_node].children:
            child_cost = ao_star(graph, child)
            total_cost += child_cost
        graph[start_node].cost = total_cost
        graph[start_node].solved = True
        return total_cost

if __name__ == "__main__":
    graph = {
        'A': Node('A', 2, 'OR', ['B', 'C']),
        'B': Node('B', 1, 'AND', ['D', 'E']),
        'C': Node('C', 3, 'OR', ['F']),
        'D': Node('D', 2, 'AND'),
        'E': Node('E', 1, 'AND'),
        'F': Node('F', 4, 'AND')
    }

    graph['D'].cost = 0
    graph['D'].solved = True
    graph['E'].cost = 0
    graph['E'].solved = True
    graph['F'].cost = 0
    graph['F'].solved = True

    cost = ao_star(graph, 'A')
    print("Cost to reach the goal:", cost)
    print("Best child of A:", graph['A'].best_child)
