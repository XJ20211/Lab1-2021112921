import re
import random
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict, deque

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    # 将非字母字符转换为空格
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    # 合并多个空格为一个空格
    text = re.sub(r'\s+', ' ', text).strip().lower()
    return text

def create_directed_graph(text):
    words = text.split()
    graph = nx.DiGraph()
    for i in range(len(words) - 1):
        if graph.has_edge(words[i], words[i+1]):
            graph[words[i]][words[i+1]]['weight'] += 1
        else:
            graph.add_edge(words[i], words[i+1], weight=1)
    return graph

def show_directed_graph(graph):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='skyblue', edge_color='#909090', node_size=500)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.savefig('graph.png')  # 保存图形为文件
    plt.show()

def query_bridge_words(graph, word1, word2):
    if word1 not in graph or word2 not in graph:
        return f"No {word1} or {word2} in the graph!"
    bridges = [node for node in graph if graph.has_edge(word1, node) and graph.has_edge(node, word2)]
    if not bridges:
        return f"No bridge words from {word1} to {word2}!"
    return f"The bridge words from {word1} to {word2} are: {', '.join(bridges)}."

def generate_new_text(graph, input_text):
    words = input_text.lower().split()
    new_text = []
    for i in range(len(words) - 1):
        new_text.append(words[i])
        bridge_words = [node for node in graph if graph.has_edge(words[i], node) and graph.has_edge(node, words[i+1])]
        if bridge_words:
            new_text.append(random.choice(bridge_words))
    new_text.append(words[-1])
    return ' '.join(new_text)

# def calc_shortest_path(graph, word1, word2):
#     try:
#         path = nx.shortest_path(graph, source=word1, target=word2, weight='weight')
#         path_length = sum(graph[u][v]['weight'] for u, v in zip(path[:-1], path[1:]))
#         show_directed_graph_with_path(graph, path)
#         return f"Shortest path: {' -> '.join(path)} with total weight {path_length}"
#     except nx.NetworkXNoPath:
#         return "No path available."

def calc_shortest_path(graph, word1, word2=None):
    try:
        if word2:
            # 如果给定第二个单词，计算单一最短路径
            path = nx.shortest_path(graph, source=word1, target=word2, weight='weight')
            path_length = sum(graph[u][v]['weight'] for u, v in zip(path[:-1], path[1:]))
            show_directed_graph_with_path(graph, path)
            return f"Shortest path: {' -> '.join(path)} with total weight {path_length}"
        else:
            # 如果没有给定第二个单词，计算到所有其他单词的最短路径
            paths = nx.single_source_dijkstra_path(graph, source=word1, weight='weight')
            paths_lengths = {
                target: sum(graph[u][v]['weight'] for u, v in zip(path[:-1], path[1:]))
                for target, path in paths.items()
            }
            # 输出每一条路径及其长度
            all_paths = []
            for target, path in paths.items():
                all_paths.append(f"Shortest path to {target}: {' -> '.join(path)} with total weight {paths_lengths[target]}")
                show_directed_graph_with_path(graph, path)
            return '\n'.join(all_paths)
    except nx.NetworkXNoPath:
        return "No path available."
    except nx.NodeNotFound:
        return f"{word1} not in the graph!"


def show_directed_graph_with_path(graph, path):
    pos = nx.spring_layout(graph)
    path_edges = list(zip(path[:-1], path[1:]))
    nx.draw_networkx_nodes(graph, pos, node_color='skyblue')
    nx.draw_networkx_edges(graph, pos, edgelist=graph.edges, edge_color='gray')
    nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='red', width=2)
    nx.draw_networkx_labels(graph, pos)
    plt.show()

def random_walk(graph):
    node = random.choice(list(graph.nodes))
    visited_edges = set()
    path = [node]
    while True:
        neighbors = list(graph[node])
        if not neighbors or all((node, neighbor) in visited_edges for neighbor in neighbors):
            break
        next_node = random.choice(neighbors)
        if (node, next_node) in visited_edges:
            break
        visited_edges.add((node, next_node))
        path.append(next_node)
        node = next_node
    return ' -> '.join(path)

def main():
    file_path = input("Enter the path to the text file: ")
    text = read_text_file(file_path)
    graph = create_directed_graph(text)
    show_directed_graph(graph)
    while True:
        print("\nOptions:")
        print("1. Show Directed Graph")
        print("2. Query Bridge Words")
        print("3. Generate New Text")
        print("4. Calculate Shortest Path")
        print("5. Random Walk")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            show_directed_graph(graph)
        elif choice == '2':
            word1 = input("Enter the first word: ")
            word2 = input("Enter the second word: ")
            print(query_bridge_words(graph, word1, word2))
        elif choice == '3':
            input_text = input("Enter a line of text: ")
            print("Generated text:", generate_new_text(graph, input_text))
        elif choice == '4':
            # word1 = input("Enter the first word: ")
            # word2 = input("Enter the second word: ")
            # print(calc_shortest_path(graph, word1, word2))
            input_words = input("Enter one or two words (separated by space): ").split()
            if len(input_words) == 1:
                word1 = input_words[0]
                print(calc_shortest_path(graph, word1))
            elif len(input_words) == 2:
                word1, word2 = input_words
                print(calc_shortest_path(graph, word1, word2))
            else:
                print("Invalid input. Please enter one or two words.")
        elif choice == '5':
            print("Random walk:", random_walk(graph))
        elif choice == '6':
            break

if __name__ == "__main__":
    main()
