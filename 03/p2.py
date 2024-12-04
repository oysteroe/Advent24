import re

with open('03/input.txt', 'r') as file:
    input = file.read()

# input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

# Remove text between "don't()" and "do()"
input = re.sub(r"don\'t\(\).*?do\(\)", "", input)

# Remove text between "don't()" and "newline"
input = re.sub(r"don\'t\(\).*?\n", "", input)

# Find all "mul(x,y)" and extract x and y
pattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(pattern, input)

total = 0
for match in matches:
    x, y = match
    total += int(x) * int(y)
    print(f"mul({x}, {y})")

print(f"Total: {total}")
