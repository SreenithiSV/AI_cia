import numpy as np

MAX = np.inf
MIN = -np.inf


class Node:
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

def minimax(node, ismaxnode):
    if not node.children:
        return node.val

    if ismaxnode:
        best = MIN
        for child in node.children:
            val = minimax(child, False)
            best = max(best, val)
        return best
    else:
        best = MAX
        for child in node.children:
            val = minimax(child, True)
            best = min(best, val)
        return best

def BuildTree():
    x = Node(0.88, [])
    y = Node(-0.98, [])
    p1 = Node(np.inf, [x, y])

    x1 = Node(-8, [])
    x2 = Node(-9, [])
    p2 = Node(np.inf, [x1, p1, x2])

    x3 = Node(0, [])
    x4 = Node(9, [])
    p3 = Node(np.inf, [x3, p2, x4])

    p4 = Node(np.inf, [p3])

    y1 = Node(-9, [])
    y2 = Node(-8.9, [])
    t1 = Node(np.inf, [y1, y2])

    y3 = Node(7, [])
    t2 = Node(np.inf, [y3])

    y4 = Node(-0.009, [])
    t3 = Node(np.inf, [t1, t2, y4])

    y5 = Node(78, [])
    y6 = Node(-7.8, [])
    t4 = Node(np.inf, [y5, y6])

    t5 = Node(np.inf, [t4])

    y7 = Node(4, [])
    t6 = Node(np.inf, [y7, t3, t5])

    y8 = Node(6, [])
    y9 = Node(-7, [])
    y10 = Node(0.8, [])
    t6 = Node(np.inf, [y8, y9, y10])

    y11 = Node(-0.66, [])
    t7 = Node(np.inf, [t6])
    t8 = Node(np.inf, [y11])
    t9 = Node(np.inf, [t7, t8])

    t10 = Node(np.inf, [t6, t9])

    z1 = Node(67, [])
    z2 = Node(-6.7, [])
    z3 = Node(0.067, [])
    s1 = Node(np.inf, [z1, z2, z3])

    z4 = Node(0.66, [])
    s2 = Node(np.inf, [z4, s1])

    z5 = Node(99, [])
    z6 = Node(9.9, [])
    s3 = Node(np.inf, [z5, z6])

    z7 = Node(-0.09, [])
    s4 = Node(np.inf, [s3, z7])

    z8 = Node(87, [])
    z9 = Node(8.7, [])
    s4 = Node(np.inf, [z8, z9])

    s5 = Node(np.inf, [s4])

    z10 = Node(-99, [])
    s6 = Node(np.inf, [s2, s4, s5, z10])

    root = Node(np.inf, [p4, t10, s6])
    return root

root = BuildTree()
result = minimax(root, True)
print("The result of the Minimax algorithm is:", result)
