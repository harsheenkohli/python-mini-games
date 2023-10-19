# Points Distributuion method for Page Ranking
# Whatever you have, share equally with all your out edges
# Sum of points will be same as initial
# But individual values will change
# A has 1 pt and 2 out edges, then give 1/2 each to each neighbour

import networkx as nx
import random
import matplotlib.pyplot as plt


def add_edges():
    nodes = list(G.nodes())
    for source in nodes:
        for target in nodes:
            if (source == target):
                continue
            if (random.random() <= 0.5):
                G.add_edge(source, target)

    return G


def assign_points(G):
    nodes = list(G.nodes())
    # for node in nodes :
    #     points.append(100)
    points = [100 for _ in nodes]
    return points


def distribute_points(points, G):
    nodes = list(G.nodes())
    new_points = [0] * len(nodes)

    for node in nodes:
        out = list(G.out_edges(node))
        if len(out) == 0:
            new_points[node] += points[node]
            # otherwise points will accumulate
        else:
            share = points[node] / len(out)
            for (source, target) in out:
                new_points[target] += share

    return new_points


def keep_distributing(points, G):
    nodes = list(G.nodes())
    while (True):
        new_points = distribute_points(points, G)
        # print(new_points)
        if (points == new_points):
            break
        points = new_points

    return points


def rank_by_points(final_points):
    rank_dict = {node: final_points[node] for node in range (len(final_points))}
    # for node in range(final_points) :
    #     rank_dict[node] = final_points[node]
    return (sorted(rank_dict.items(), key=lambda f:f[1]))


# Create a directed graph
G = nx.DiGraph()
G.add_nodes_from([i for i in range(10)])
G = add_edges()

# Visualize the graph
nx.draw(G, with_labels=True)
plt.show()

# Assign initial points
points = assign_points(G)

# Distribute points
final_points = keep_distributing(points, G)

# Rank by points
final_points = rank_by_points(final_points)

# Compare with default networkx function
result = nx.pagerank(G)
result = sorted(result.items(), key=lambda f:f[1])

print([node for node, points in final_points])
print([node for node, points in result])
