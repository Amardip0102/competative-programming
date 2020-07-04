from itertools import product

k,M = input().split(" ")

N = (list(map(int, input().split()))[1:] for _ in range(int(k)))
results = map(lambda x: sum(i**2 for i in x)%int(M), product(*N))

print(max(results))