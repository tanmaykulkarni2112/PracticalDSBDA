jobs = [
    {'id': 'A', 'deadline': 2, 'profit': 100},
    {'id': 'B', 'deadline': 1, 'profit': 19},
    {'id': 'C', 'deadline': 2, 'profit': 27},
    {'id': 'D', 'deadline': 1, 'profit': 25},
    {'id': 'E', 'deadline': 3, 'profit': 15}
]

jobs.sort(key = lambda x: x["profit"], reverse = True)
n = max(job["deadline"] for job in jobs)
slots = [False] * n
result = [None] * n

for job in jobs:
    for i in range(min(n, job["deadline"])-1, -1, -1):
        if not slots[i]:
            slots[i] = True
            result[i] = job["id"]
            break

print(result)