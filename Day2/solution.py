from itertools import combinations, compress

ids = open("input.txt", 'r')

'''two = 0
three = 0

for i in ids:
    if any(i.count(l)==2 for l in set(i)):
        two +=1
    if any(i.count(l)==3 for l in set(i)):
        three +=1

print(two*three)
 '''

for a, b in combinations(ids, 2):    
    diff = [e1 == e2 for e1,e2 in zip(a,b)]    
    if sum(diff) == (len(a) - 1):
        res2 = ''.join(list(compress(a,diff)))
        break
print(res2)
