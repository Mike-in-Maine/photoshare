import os
from functools import reduce


def generate_directory_tree(path):
    directory_tree = {}
    for root, dirs, files in os.walk(path):
        tree_path = root.split(os.sep)
        subtree = {d: {} for d in dirs}
        subtree.update({f: None for f in files})

        # Ensure the parent path exists
        parent = directory_tree
        for node in tree_path[:-1]:
            parent = parent.setdefault(node, {})

        parent[tree_path[-1]] = subtree
    return directory_tree
