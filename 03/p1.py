import re

with open('03/input.txt', 'r') as file:
    input = file.read().strip()

# input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

pattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(pattern, input)

total = 0
for match in matches:
    x, y = match
    total += int(x) * int(y)
    print(f"mul({x}, {y})")

print(f"Total: {total}")
