names = ["Alice", "Bob", "Charlie", "David", "Eve", "Joe"]
gpas = [3.9, 3.2, 3.6, 3.7, 3.5, 3.9]
hours = [10, 100, 60, 20, 40, 20]
eligebles = []
for name, gpa, hour in zip(names, gpas, hours):
    if gpa>3.8 or (gpa>3.5 and hour>50):
        eligebles.append((name, gpa, hour))
eligebles.sort(key = lambda t: (-t[1], -t[2]))
print(eligebles)