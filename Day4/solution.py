import re
from collections import Counter

with open("input.txt", "r") as f:
    guards = {}
    start, stop, current_guard = 0, 0, 0
    lines = [x.strip() for x in f.readlines()]
    lines.sort()

    for line in lines:
        values = re.findall("\d+", line)
        if "Guard" in line:
            current_guard = int(values[-1])
        elif "falls asleep" in line:
            start = int(values[-1])
        elif "wakes up" in line:
            stop = int(values[-1])
            for i in range(start, stop):
                guards.setdefault(current_guard, []).append(i)

    # Pt1
    id1 = max(guards, key=lambda x: len(guards[x]))
    c = Counter(guards[id1])
    minute = c.most_common()[0][0]
    print(id1 * minute)

    #pt2
    id2 = max(guards, key=lambda x: Counter(guards[x]).most_common()[0][1])
    print(id2 * Counter(guards[id2]).most_common()[0][0])
