with open('02/input.txt', 'r') as file:
    lines = file.readlines()

numbers = [line.strip().split() for line in lines]

safeCount = 0

for i in range(len(numbers)):
    report = numbers[i]
    # print(report)
    safe = True
    direction = (int(report[1]) - int(report[0])) > 0
    for j in range(len(report)-1):
        distance = int(report[j+1]) - int(report[j])
        if abs(distance) > 3:
            safe = False
            break
        elif distance == 0:
            safe = False
            break
        elif direction and (distance < 0):
            safe = False
            break
        elif not direction and (distance > 0):
            safe = False
            break
        direction = distance > 0

    # print(safe)
    if safe:
        safeCount += 1

print(safeCount)
