# python3

import sys
import threading
from collections import defaultdict


def build_tree(parents):
    tree=defaultdict(list)
    for idx, par in enumerate(parents):
        if par==-1:
            root=idx
        tree[par].append(idx)
    return root, tree


def compute_height(n, parents):
    # Replace this code with a faster implementation

    root, tree=build_tree(parents)
    layers=tree[-1]
    height=0
    while layers:
        height+=1
        for i in range(len(layers)):
            curr=layers.pop(0)
            if curr in tree.keys():
                for child in tree[curr]:
                    layers.append(child)
        #print(layers)
    return height

    # max_height = 0
    # for vertex in range(n):
    #     height = 0
    #     current = vertex
    #     while current != -1:
    #         height += 1
    #         current = parents[current]
    #     max_height = max(max_height, height)
    # return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

