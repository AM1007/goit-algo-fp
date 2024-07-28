import uuid  # Importing the uuid module to generate unique IDs for nodes
import networkx as nx  # Importing NetworkX for creating and manipulating graphs
import matplotlib.pyplot as plt  # Importing Matplotlib for plotting graphs
import matplotlib.colors as mcolors  # Importing Matplotlib colors for color manipulations

# Define a Node class to represent each node in the binary tree
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None  # Left child node
        self.right = None  # Right child node
        self.val = key  # Value of the node
        self.color = color  # Color of the node
        self.id = str(uuid.uuid4())  # Unique ID for the node

# Function to add edges to the graph representation of the tree
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Add node to the graph
        if node.left:
            graph.add_edge(node.id, node.left.id)  # Add edge to the left child
            l = x - 1 / 2 ** layer  # Calculate position for the left child
            pos[node.left.id] = (l, y - 1)  # Set position for the left child
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)  # Recursively add edges for the left child
        if node.right:
            graph.add_edge(node.id, node.right.id)  # Add edge to the right child
            r = x + 1 / 2 ** layer  # Calculate position for the right child
            pos[node.right.id] = (r, y - 1)  # Set position for the right child
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)  # Recursively add edges for the right child
    return graph  # Return the updated graph

# Function to draw the binary tree using Matplotlib and NetworkX
def draw_tree(tree_root):
    tree = nx.DiGraph()  # Create a directed graph
    pos = {tree_root.id: (0, 0)}  # Initialize position of the root node
    tree = add_edges(tree, tree_root, pos)  # Add edges to the graph

    colors = [node[1]['color'] for node in tree.nodes(data=True)]  # Get colors of all nodes
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Get labels of all nodes

    plt.figure(figsize=(8, 5))  # Set figure size
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)  # Draw the tree
    plt.show()  # Show the plot

# Function to convert a list to a binary heap represented as a tree
def list_to_binary_heap(lst):
    def create_node(index):
        if index >= len(lst):
            return None  # Return None if index is out of bounds
        node = Node(lst[index])  # Create a new node with the list element
        node.left = create_node(2 * index + 1)  # Recursively create the left child
        node.right = create_node(2 * index + 2)  # Recursively create the right child
        return node  # Return the created node

    return create_node(0)  # Create the root node

# Function to generate a list of colors
def generate_colors(n):
    cmap = plt.get_cmap('viridis')  # Get the 'viridis' colormap
    return [mcolors.rgb2hex(cmap(i/n)) for i in range(n)]  # Return n colors from the colormap

# Function to visualize depth-first search traversal

def visualize_dfs(root):
    stack = [(root, 0)]  # Initialize stack with the root node and its depth
    visited = set()  # Set to keep track of visited nodes
    colors = generate_colors(len(heap_list))  # Generate colors for visualization
    
    step = 0  # Step counter for color assignment
    while stack:
        node, depth = stack.pop()  # Pop node and its depth from the stack
        if node and node.id not in visited:  # If node is not visited
            visited.add(node.id)  # Mark node as visited
            node.color = colors[step]  # Assign color to the node
            draw_tree(heap_root)  # Draw the tree
            step += 1  # Increment step counter
            stack.append((node.right, depth + 1))  # Push right child to stack
            stack.append((node.left, depth + 1))  # Push left child to stack

# Function to visualize breadth-first search traversal
def visualize_bfs(root):
    queue = [(root, 0)] # Initialize a queue with the root node and its depth
    visited = set() # Keep track of visited nodes
    colors = generate_colors(len(heap_list)) # Generate colors for each node based on the length of the heap list
    step = 0 # Initialize the step counter
    
    # Start the BFS traversal
    while queue:
        node, depth = queue.pop(0) # Pop the next node from the queue       
        # Check if the node has not been visited
        if node and node.id not in visited:
            visited.add(node.id) # Mark the node as visited
            node.color = colors[step] # Assign a color to the node based on the step counter
            draw_tree(heap_root) # Draw the tree with the updated colors           
            # Increment the step counter
            step += 1
            # Add the left and right child nodes to the queue
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))

# Example list representing a binary heap
heap_list = [1, 3, 5, 7, 9, 2, 6, 8, 4]

# Creating the binary heap from the list
heap_root = list_to_binary_heap(heap_list)

# Visualizing DFS traversal
visualize_dfs(heap_root)

# Reset colors for BFS visualization
heap_root = list_to_binary_heap(heap_list)

# Visualizing BFS traversal
visualize_bfs(heap_root)
