import time
import math
import collections
import re

current_time = lambda: int(round(time.time() * 1000))
start = current_time()

players = 452
#last_point = 71250 #pt1
last_point = 71250 * 100 #pt2

circle = collections.deque()
circle.append(0)

elf = 0
max_score = 0

scores = collections.defaultdict(int)
player = 1

for x in range(1, last_point + 1):
    if (x % 23) == 0:
        circle.rotate(-7)
        scores[player] += (x + circle.pop())
        if scores[player] > max_score:
            max_score = scores[player]
            elf = player
    else:
        circle.rotate(2)
        circle.append(x)
    player += 1
    if player > players:
        player = 1

print(elf, max_score)

print ((current_time() - start)/ 1000.0)