from itertools import product, accumulate
 
n, w = map(int, input().split())
w1, v1 = map(int, input().split())
packages = [[v1], [], [], []]
for _ in range(n - 1):
    wi, vi = map(int, input().split())
    packages[wi - w1].append(vi)

print(packages)

for ofs, lst in enumerate(packages):
    lst.sort(reverse=True)
    packages[ofs] = list(accumulate([0] + lst))

print(packages)
 
print([range(len(packages[ofs])) for ofs in range(4)])

tmp_max = 0
for a, b, c, d in product(*(range(len(packages[ofs])) for ofs in range(4))):
    if w1 * (a + b + c + d) + b + 2 * c + 3 * d > w:
        continue
    tmp_max = max(tmp_max, sum(packages[ofs][m] for ofs, m in zip(range(4), (a, b, c, d))))
print(tmp_max)
