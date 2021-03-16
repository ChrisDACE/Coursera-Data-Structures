#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


def IsBinarySearchTree(idx, minv, maxv):
    # Implement correct algorithm here
    if idx == -1:
        return True
    if tree[idx][0] < minv or tree[idx][0] >= maxv:
        return False
    return IsBinarySearchTree(tree[idx][1], minv, tree[idx][0]) and IsBinarySearchTree(tree[idx][2],
                                                                                       tree[idx][0], maxv)



def main():
    nodes = int(sys.stdin.readline().strip())
    global tree
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))

    if not tree or len(tree) == 1:
        print("CORRECT")
    else:
        if IsBinarySearchTree(0, float('-inf'), float('inf')):
            print("CORRECT")
        else:
            print("INCORRECT")


threading.Thread(target=main).start()
