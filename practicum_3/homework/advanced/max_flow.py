import networkx as nx
from typing import Any

# поиск пути от вершины s до вершины t с учетом весов ребер
def dfs(G: nx.Graph, s: Any, t: Any, parent):
    visited = {node: False for node in G.nodes}
    stack = [s]
    visited[s] = True

    while stack:
        current_node = stack.pop()
        for neighbor in G.neighbors(current_node):
            if not visited[neighbor] and G[current_node][neighbor]['weight']:
                stack.append(neighbor)
                visited[neighbor] = True
                parent[neighbor] = current_node
                if neighbor == t:
                    return True
    return False

# поиск максимального потока при помощи алгоритма Форда-Фалкерсона
def max_flow(G: nx.Graph, s: Any, t: Any) -> int:
    value: int = 0
    parent = {node: 0 for node in G.nodes}
    while dfs(G, s, t, parent):
        current_flow = float("inf")
        current_node = t
        
        while current_node != s:
            current_flow = min(current_flow, G[parent[current_node]][current_node]['weight'])
            current_node = parent[current_node]
        
        value += current_flow
        backward_node = t
        
        while backward_node != s:
            forward_node = parent[backward_node]
            G[forward_node][backward_node]['weight'] -= current_flow
            backward_node = forward_node
    return value

if __name__ == "__main__":
    G = nx.read_edgelist("practicum_3/homework/advanced/graph_1.edgelist", create_using=nx.DiGraph)
    
    val = max_flow(G, s='0', t='5')
    print(f"Maximum flow is {val}. Should be 23")
