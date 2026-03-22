raw_scores = [
    ("Alice", "Math", 85),
    ("Bob", "Math", 75),
    ("Alice", "Physics", 90),
    ("Charlie", "History", 88),
    ("Bob", "Physics", 82),
    ("Alice", "History", 92)
]
gradebook = {}
for name , subject , score in raw_scores:
    if name in gradebook:
        gradebook[name][subject] = score
    else:
        gradebook[name] = {}
        gradebook[name][subject] = score
print(gradebook)