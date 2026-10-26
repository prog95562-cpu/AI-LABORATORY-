# Experiment: Travelling Salesman Problem (TSP) Using Brute Force

from itertools import permutations

def tsp(graph, start):
    cities = list(graph.keys())
    cities.remove(start)

    min_cost = float("inf")
    best_path = []

    for path in permutations(cities):
        current_path = [start] + list(path) + [start]
        cost = 0

        for i in range(len(current_path) - 1):
            cost += graph[current_path[i]][current_path[i + 1]]

        if cost < min_cost:
            min_cost = cost
            best_path = current_path

    print("Shortest Path:", " -> ".join(best_path))
    print("Minimum Cost:", min_cost)


n = int(input("Enter number of cities: "))
cities = []

for i in range(n):
    city = input(f"Enter city {i + 1}: ").upper()
    cities.append(city)

graph = {}

for city in cities:
    graph[city] = {}
    for other_city in cities:
        if city != other_city:
            distance = int(
                input(f"Distance from {city} to {other_city}: ")
            )
            graph[city][other_city] = distance

start = input("Enter starting city: ").upper()

if start in graph:
    tsp(graph, start)
else:
    print("Invalid starting city.")