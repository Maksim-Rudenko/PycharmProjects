# python3

from collections import deque

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
        # store all strings in one list
        self.hash_table = list(deque() for _ in range(self.bucket_count))


    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count


    def process_query(self, query):
        if query.type == 'check':
            if self.hash_table[query.ind]:
                print(' '.join(self.hash_table[query.ind]))
            else:
                print()
        else:
            hash_value = self._hash_func(query.s)
            if query.type == "add":
                if query.s not in self.hash_table[hash_value]:
                    self.hash_table[hash_value].appendleft(query.s)
            elif query.type == "del":
                if query.s in self.hash_table[hash_value]:
                    self.hash_table[hash_value].remove(query.s)
            elif query.type == "find":
                if query.s in self.hash_table[hash_value]:
                    print('yes')
                else:
                    print('no')



if __name__ == '__main__':
    n_buckets = int(input())
    hash_table = QueryProcessor(n_buckets)
    n_queries = int(input())
    for _ in range(n_queries):
        command = Query(input().split())
        hash_table.process_query(command)
