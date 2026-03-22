ll_students = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
submitted = ["alice", "Bob", "Frank", "George"] # Note: 'alice' is lowercase, 'George' is new
copy1 = [name.lower() for name in ll_students]
copy2 = [name.lower() for name in submitted]
students_set = set(copy1)
submitted_students_set = set(copy2)
not_submitted = list(students_set - submitted_students_set)
not_in_list = list(submitted_students_set - students_set)
print("Not submitted:")
for name in not_submitted:
    print(f" - {name.title()}")
print("Not on class list:")
for name in not_in_list:
    print(f" - {name.title()}")