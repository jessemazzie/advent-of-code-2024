list_one = []
list_two = []
similarity_score = 0

with open("input.txt", "r") as f:
    for line in f:
        x, y = line.split()

        list_one.append(int(x))
        list_two.append(int(y))

for x in list_one:
    count = list_two.count(x)
    similarity_score = similarity_score + x * count

print(similarity_score)