import heapq
import numpy as np

def heuristic(node, end, d_h):
    return d_h[node][end] 

def branch_and_bound(graph, start, end, oracle, d_h):
    queue = []
    heapq.heappush(queue, (0, [start])) 
    optimal_path = []
    
    while queue:
        current_cost, current_path = heapq.heappop(queue)
        current_node = current_path[-1]
        if current_node == end:
            optimal_path = current_path
            break
        
        for next_node, cost in graph[current_node].items():
            if next_node in current_path: 
                continue
            
            new_cost = current_cost + cost
            if new_cost <= oracle: 
                new_path = current_path + [next_node]
                estimated_cost = new_cost + heuristic(next_node, end, d_h)
                heapq.heappush(queue, (estimated_cost, new_path))
    
    print("Optimal Path:", optimal_path) 
    return optimal_path


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

start_node = 'S'
end_node = 'G'
oracle_value = 10 

optimal_path = branch_and_bound(d, start_node, end_node, oracle_value, d_h)
