# python3
multiplier = 256
prime = 500007


def read_input():
    return input().rstrip(), input().rstrip()


def print_occurrences(output):
    print(' '.join(map(str, output)))


def hash_func(s):
    ans = 0
    for c in reversed(s):
        ans = (ans * multiplier + ord(c)) % prime
    # ans = ((ans * multiplier + ord(c)) % prime + prime) % prime
    return ans


def compute_hashes(text, pattern):
    t = len(text)
    p = len(pattern)

    H = [-1] * (t - p + 1)
    S = text[t - p:]
    H[-1] = hash_func(S)
    y = 1
    for i in range(p):
        y = (y * multiplier) % prime
    for i in range(t - p - 1, -1, -1):
        H[i] = (multiplier * H[i + 1] + ord(text[i]) - y * ord(text[i + p])) % prime

    return H


def get_occurrences(pattern, text):
    ans = []
    pHash = hash_func(pattern)
    H = compute_hashes(text, pattern)
    for i in range(len(text) - len(pattern)+1):
        if H[i] != pHash:
            continue
        if pattern == text[i: i + len(pattern)]:
            ans.append(i)
    return ans


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
