import networkx as nx

TEST_GRAPH_FILES = [
    "graph_1_wo_cycles.edgelist",
    "graph_2_wo_cycles.edgelist",
    "graph_3_w_cycles_edgelist",
]

def has_cycles(g: nx.DiGraph):
    def detect_cycle(i, visited, ancestors):
        visited[i] = True
        ancestors.add(i)

        for neighbor in g[i]:
            if not visited[neighbor]:
                if detect_cycle(neighbor, visited, ancestors):
                    return True
            elif neighbor in ancestors:
                return True

        ancestors.remove(i)

    visited = {node: False for node in g} # создаёт словарь visited где ключами являются вершины графа, а каждому ключу соответствует значение False
    
    for i in g.nodes:
        if not visited[i]:
            if detect_cycle(i, visited, set()):
                return True

    return False

if __name__ == "__main__":
    for filename in TEST_GRAPH_FILES:
        # Load the graph
        G = nx.read_edgelist(f"practicum_2/homework/advanced/{filename}", create_using=nx.DiGraph)
        # Output whether it has cycles
        print(f"Graph {filename} has cycles: {has_cycles(G)}")
