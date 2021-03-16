# python3
from collections import deque

def max_sliding_window_naive(sequence, m):
    maxs=[]
    monodeq=deque()
    i=j=0
    while j<len(sequence):
        while monodeq and sequence[j]>monodeq[-1]:
            monodeq.pop()

        monodeq.append(sequence[j])

        if j-i+1==m:
            maxs.append(monodeq[0])
            if maxs[-1]==sequence[i]:
                monodeq.popleft()
            i+=1
        j+=1

    return maxs

    # maximums = []
    # for i in range(len(sequence) - m + 1):
    #     maximums.append(max(sequence[i:i + m]))
    #
    # return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

