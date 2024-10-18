import numpy as np

def oracle_search(d, start, goal, max_no_goalcutoff, heuristic):
    
    queue = [[0, start]]  
    results = []    
    goal_count = 0     
    max_goals = max_no_goalcutoff

    while len(queue) != 0:
        current_path = queue.pop(0)
        current_cost = current_path[0]
        current_node = current_path[-1]
        for neighbor in d[current_node].keys():
            if neighbor in current_path:
                continue

            edge_cost = d[current_node][neighbor] 
            new_cost = current_cost + edge_cost    
            new_path = current_path + [neighbor]
            new_path[0] = new_cost 

            estimated_total_cost = new_cost + heuristic[neighbor][goal] if goal in heuristic[neighbor] else new_cost
            queue.append([estimated_total_cost, neighbor])

            if neighbor == goal:
                goal_count += 1
                results.append(new_path)

            if goal_count == max_goals:
                break
        queue.sort(key=lambda x: x[0])

    return results 

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
results = oracle_search(d, 'S', 'G', max_no_goalcutoff=3, heuristic=d_h)
for result in results:
    print(f"Path: {result[1:]}, Cost: {result[0]}")
