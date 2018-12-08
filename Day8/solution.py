def solve(child, meta):
    if child == 0:
        return sum(next(data) for _ in range(meta))
    value = 0
    children = {}
    for i in range(1, child+1):
        value += solve(next(data), next(data)) #part 1
        #children[i] = solve(next(data), next(data)) #part 2
    for _ in range(meta):
        value += next(data) # part 1
        #value += children.get(next(data), 0) #part 2
    return value

data = iter(map(int, open ("input.txt").read().split()))

print (solve(next(data), next(data)))