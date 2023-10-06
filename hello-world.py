# License MIT
# by: Mohamed Aziz Khayati, 2023

# Visit nodes in a graph using BFS
# Breadth First Search

# Graph
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["peggy"] = []
graph["anuj"] = []
graph["thom"] = []
graph["jonny"] = []

# Queue
from collections import deque
search_queue = deque()
search_queue += graph["you"]

# Search
def person_is_seller(name):
    return name[-1] == 'm'

while search_queue:
    person = search_queue.popleft()
    if person_is_seller(person):
        print(person + " is a mango seller!")
        break
    else:
        search_queue += graph[person]

# Output
# thom is a mango seller!

# Time complexity
# O(V+E)

# Space complexity
# O(V)
