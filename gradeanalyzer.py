import numpy as np

n = int(input("How many students you want to enter?"))
names_list = []
marks_list = []
for i in range(n):
    names = input("Enter name:")
    names_list.append(names)
    mks = int(input("Enter marks:"))
    marks_list.append(mks)

array = np.array(marks_list)
names_array = np.array(names_list)

def grade(mks):
    if mks >= 90:
        return 'A'
    elif mks >= 75:
        return 'B'
    elif mks >= 60:
        return 'C'
    elif mks >= 40:
        return 'D'
    else:
        return 'F'

## finding who scored highest and lowest
highest = np.argmax(array)
lowest = np.argmin(array)

print(f"Highest Marks: {names_array[highest]} = {array[highest]}")
print(f"Lowest Marks: {names_array[lowest]} = {array[lowest]}")

## Failed students
result = array < 40
print(f"Failed Students :\n {names_array[result]} = {array[result]}")

print("\n---Class Report---")
print("Average:",np.mean(array))
print("Highest:",np.max(array))
print("Lowest:",np.min(array))

sorted_idx = np.argsort(array)[::-1]

print("\n--Final Report--")
for idx in sorted_idx:
    print(f"{names_array[idx]}:{array[idx]} Grade: {grade(array[idx])}")