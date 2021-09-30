n = list(input())
candidate = []
result = "YES"

print(n)
while n:
    s = n.pop(0)

    if s == ")":
        if len(candidate) == 0:
            result = "NO"
            break
        candidate.pop()
    else:
        candidate.append(s)

if len(candidate) != 0:
    result = "NO"

print(result)
