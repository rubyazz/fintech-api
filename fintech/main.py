inp = input().strip()

max_length = 0
cur = 0

for c in inp:
    if c == '(':
        cur += 1
    elif c == ')' and cur > 0:
        cur -= 1
        max_length += 2

print(max_length)
