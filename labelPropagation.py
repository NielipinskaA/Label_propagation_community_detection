import networkx as nx
import pandas as pd
import numpy as np
import random

def labelPropagationDetection(G: nx.Graph, iterations = None):

    nodes = list(G.nodes())
    nodes_labels = {}

    for node in nodes:
        nodes_labels[node] = node

    t = False
    i = 0
    while t == False:
        t = True
        X = nodes
        random.shuffle(X)

        for x in X:
            neighbors = G.neighbors(x)
            labels_counter = {}

            for node in neighbors:
                if nodes_labels[node] in labels_counter:
                    labels_counter[nodes_labels[node]] += 1
                else:
                    labels_counter[nodes_labels[node]] = 1

            max_occurrence = max(list(labels_counter.values()))
            max_labels = [key for key in labels_counter.keys() if labels_counter[key] == max_occurrence]

            if len(max_labels) > 1:
                new_label = random.choice(max_labels)
            else: 
                new_label = max_labels[0]

            if new_label != nodes_labels[x]:
                nodes_labels[x] = new_label
                t = False
        i += 1
        if iterations != None and i == iterations:
            break

            
    unique_labels = list(np.unique(list(nodes_labels.values())))
    cluster_number = len(unique_labels)
    for key in nodes_labels:
        label = nodes_labels[key]
        nodes_labels[key] = unique_labels.index(label)

    return cluster_number, nodes_labels