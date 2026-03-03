names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 92]

for name, score in zip(names, scores):
    print(name, score)

print()

for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(i, name, score)

#
values = ["10", "20", "abc", "30"]

converted = []

for v in values:
    if v.isdigit():     
        converted.append(int(v))
    else:
        converted.append(v)

print("Converted:", converted)