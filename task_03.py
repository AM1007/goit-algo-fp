import heapq  # Import the heapq module to use a binary heap
import networkx as nx  # Import the networkx module to create and handle graphs
import matplotlib.pyplot as plt  # Import matplotlib for visualization

def dijkstra(graph, start):
    # Initialize distances from the start node to all other nodes as infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # The distance from the start node to itself is 0
    priority_queue = [(0, start)]  # Initialize the priority queue with the start node

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)  # Get the node with the smallest distance

        # If the current distance is greater than the recorded shortest distance, skip processing
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight  # Calculate the new distance

            # If the new distance is shorter, update the shortest distance and push it to the priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def create_graph():
    # Create a graph using an adjacency list representation
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    return graph

def visualize_graph(graph, shortest_paths, start):
    G = nx.Graph()  # Create an empty graph

    # Add edges to the graph
    for node in graph:
        for neighbor, weight in graph[node].items():
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G)  # Define the layout for the nodes

    # Draw the graph
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Highlight the shortest paths
    for node, distance in shortest_paths.items():
        if node != start:
            path = nx.shortest_path(G, source=start, target=node, weight='weight')
            edges = list(zip(path, path[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='r', width=2)

    plt.title("Graph with Shortest Paths from Node '{}'".format(start))
    plt.show()

if __name__ == "__main__":
    graph = create_graph()  # Create the graph
    start_node = 'A'  # Define the start node
    shortest_paths = dijkstra(graph, start_node)  # Run Dijkstra's algorithm

    # Print the shortest paths
    for node, distance in shortest_paths.items():
        print("Shortest distance from node '{}' to node '{}' is {}".format(start_node, node, distance))

    visualize_graph(graph, shortest_paths, start_node)  # Visualize the graph
