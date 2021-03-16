# python3

class MakeHeap:
    def __init__(self):
        self.n = int(input())
        self.data = list(map(int, input().split()))
        assert len(self.data) == self.n
        self.swap = []

    def sift_down(self, q, i):
        m = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < len(q) and q[m] > q[l]:
            m = l
        if r < len(q) and q[m] > q[r]:
            m = r

        if i != m:
            q[i], q[m] = q[m], q[i]
            self.swap.append((i, m))
            self.sift_down(q, m)

    def build(self):
        for i in range(self.n//2, -1, -1):
            self.sift_down(self.data, i)

    def solver(self):
        self.build()
        for i,j in self.swap:
            print(i, j)


    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # # TODO: replace by a more efficient implementation
    # swaps = []
    # for i in range(len(data)):
    #     for j in range(i + 1, len(data)):
    #         if data[i] > data[j]:
    #             swaps.append((i, j))
    #             data[i], data[j] = data[j], data[i]
    # return swaps


def main():
    builder=MakeHeap()
    builder.solver()


if __name__ == "__main__":
    main()
