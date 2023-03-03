
class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries, contacts):
    if queries.type == "add":
        contacts[queries.number] = queries.name
    elif queries.type == "del":
        if contacts.__contains__(queries.number):
            del contacts[queries.number]
    else:
        response = 'not found'
        if contacts.__contains__(queries.number):
            response = contacts[queries.number]
        return response


n_queries = int(input())
contacts = {}
for _ in range(n_queries):
    queries = Query(input().split())
    result = process_queries(queries, contacts)
    if result:
        print(result)
