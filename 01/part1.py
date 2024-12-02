list_one = []
list_two = []
distance = 0

with open("input.txt", "r") as f:
    for line in f:
        x, y = line.split()

        list_one.append(int(x))
        list_two.append(int(y))

list_one.sort()
list_two.sort()

for x, y in zip(list_one, list_two):
    distance = distance + abs(int(x) - int(y))

print(distance)
