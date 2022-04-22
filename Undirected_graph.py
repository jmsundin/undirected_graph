import re
import numpy as np
import networkx as nx


class Undirected_graph():

    def __init__(self) -> None:
        pass

    
    def create_undirected_graph(noun_chunks):
        similarity_matrix = np.triu(similarity_matrix, k=1)
        iterator = np.nditer(similarity_matrix, flags=['multi_index'], order='C')
        node_labels = dict()
        G = nx.Graph()
        pattern = re.compile(r'[\w\s]*[\'\"]?[\w\s]+\-?[\w\s]*[\'\"]?[\w\s]*')
        for edge in iterator:
            key = 0
            value = ''
            if edge > 0.95:
                key = iterator.multi_index[0]
                value = str(noun_chunks[iterator.multi_index[0]])
                if pattern.fullmatch(value) and (value.lower().rstrip() != 'figure'):
                    node_labels[key] = value
                G.add_node(iterator.multi_index[0])
                G.add_edge(iterator.multi_index[0], iterator.multi_index[1], weight=edge)
