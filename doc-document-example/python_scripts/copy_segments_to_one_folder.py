import os
import shutil

import shutil
import os


def copy_directory_contents(src, dest):
    # Ensure destination directory exists
    if not os.path.exists(dest):
        os.makedirs(dest)

    for item in os.listdir(src):
        if item.endswith(".png"):
            src_item = os.path.join(src, item)
            dest_item = os.path.join(dest, item)

            if os.path.isdir(src_item):
                shutil.copytree(src_item, dest_item, dirs_exist_ok=True)
            else:
                shutil.copy2(src_item, dest_item)

def copy_segments_to_one_folder(output_path):

    pairs = []


    result_files_path = os.path.join(output_path, "result")
    res = []
    for file_path in os.listdir(result_files_path):
        parts = file_path[:-4].split("_")
        part_1 = parts[0] + "_" + parts[1]
        part_2 = parts[2] + "_" + parts[3]
        pairs.append((part_1, part_2))

    components = find_connected_components(pairs)
    count = 0
    for component in components:
        count += len(component)
        print(component)




    combined_path = os.path.join(output_path, "combined")
    os.makedirs(combined_path, exist_ok=True)

    index = 0
    for component in components:
        for part in component:
            src = os.path.join(output_path, "person", part)
            dest = os.path.join(combined_path, str(index))
#            copy_directory_contents(src, dest)
            print(part)

        index += 1

    a = 0

    pass


from collections import defaultdict


def build_graph(pairs):
    graph = defaultdict(list)
    for a, b in pairs:
        graph[a].append(b)
        graph[b].append(a)
    return graph


def dfs(node, graph, visited, component):
    stack = [node]
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            component.append(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append(neighbor)


def find_connected_components(pairs):
    graph = build_graph(pairs)
    visited = set()
    components = []

    for node in graph:
        if node not in visited:
            component = []
            dfs(node, graph, visited, component)
            components.append(component)

    return components


