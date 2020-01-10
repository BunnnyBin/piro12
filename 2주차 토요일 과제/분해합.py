def find_init(n):
    for i in range(1,int(n)):  # 1 ~ 입력값까지 생성자 찾기
        s = str(i)
        sum = 0
        for x in range(len(s)): # 해당 값(i)의 분해합 구하기
            sum += int(s[x])
        sum += int(s)
        if sum == int(n):
            return i
    return 0

n = input()
print(find_init(n))