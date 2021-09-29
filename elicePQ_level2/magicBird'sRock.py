s = input()
t = input()

minLength = min(len(s), len(t))
maxLength = max(len(s), len(t))
result = 0

length1 = (maxLength * minLength) // minLength
length2 = (maxLength * minLength) // maxLength

if len(s) > len(t) and s * length2 == t * length1:
    result = 1

if len(t) > len(s) and t * length2 == s * length1:
    result = 1

if len(t) == len(s) and t == s:
    result = 1
        

print(result)
