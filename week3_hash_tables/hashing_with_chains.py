# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self.elems = [[] for i in range(self.bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            #ans = (ans * self._multiplier + ord(c)) % self._prime
            ans = ((ans * self._multiplier + ord(c)) % self._prime + self._prime) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            self.write_chain(reversed(self.elems[query.ind]))
        else:
            ind = self._hash_func(query.s)

            if query.type == 'find':
                was_found = True
                if query.s not in self.elems[ind]:
                    was_found = False
                self.write_search_result(was_found)

            elif query.type == 'add':
                if query.s not in self.elems[ind]:
                    self.elems[ind].append(query.s)

            else:
                if query.s in self.elems[ind]:
                    self.elems[ind].pop(self.elems[ind].index(query.s))

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
