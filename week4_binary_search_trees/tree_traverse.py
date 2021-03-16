# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def __init__(self):
        self.n = int(sys.stdin.readline())
        self.right = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.key = [0 for i in range(self.n)]

    def read(self):
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inTraverse(self, idx, result):
        if self.left[idx] == -1 and self.right[idx] == -1:
            result.append(self.key[idx])
            return
        if self.left[idx]!= -1:
            self.inTraverse(self.left[idx], result)
        result.append(self.key[idx])
        if self.right[idx]!=-1:
            self.inTraverse(self.right[idx], result)

        return

    def preTraverse(self, idx, result):
        if self.left[idx] == -1 and self.right[idx] == -1:
            result.append(self.key[idx])
            return

        result.append(self.key[idx])
        if self.left[idx] != -1:
            self.preTraverse(self.left[idx], result)
        if self.right[idx] != -1:
            self.preTraverse(self.right[idx], result)

        return

    def postTraverse(self, idx, result):
        if self.left[idx] == -1 and self.right[idx] == -1:
            result.append(self.key[idx])
            return

        if self.left[idx] != -1:
            self.postTraverse(self.left[idx], result)
        if self.right[idx] != -1:
            self.postTraverse(self.right[idx], result)
        result.append(self.key[idx])

        return

    def inOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.inTraverse(0, self.result)
        return self.result

    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.preTraverse(0, self.result)

        return self.result

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.postTraverse(0, self.result)

        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
