n = int(input())
data = list(map(int, input().split()))
counter = [0]*1000001
for i in data:
    counter[i] += 1

print(max(counter))