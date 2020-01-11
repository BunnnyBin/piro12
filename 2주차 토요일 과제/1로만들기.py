def makeone(n):
    count = 0
    line = [n]
    line2 = []
    while True:
        if 1 in line:
            break
        for i in range(len(line)):
            if line[i] % 3 == 0:
                line2.append(line[i]//3)
            if line[i] % 2 == 0:
                line2.append(line[i]//2)
            line2.append(line[i]-1)
        line = line2.copy()
        line2.clear()
        count += 1
    return count

n = int(input())
print(makeone(n))