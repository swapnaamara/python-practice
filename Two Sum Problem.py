n = int(input("Enter size: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter value {i+1}: ")))

target = int(input("Enter target: "))

found = False
for i in range(n):
    for j in range(i+1, n):
        if arr[i] + arr[j] == target:
            print(i, j)
            found = True
            break
    if found:
        break

if not found:
    print("No Pair Found")