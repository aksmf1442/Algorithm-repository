n = input()

if len(n) == 4:
    print(20)

if len(n) == 3 and n[1] == "0":
    print(int(n[0:2]) + int(n[2]))

if len(n) == 3 and n[2] == "0":
    print(int(n[0]) + int(n[1:3]))

if len(n) == 2:
    print(int(n[0]) + int(n[1]))
