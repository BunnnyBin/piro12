def bracket(basket): # 괄호 문자 list
    # 괄호 갯수 새기(더 간단!!)
    if basket.count('(') != basket.count(')'):
        return 'NO'
    #스택 개념
    stack = []
    for i in range(len(basket)):
        if basket[i] == '(':
            stack.append('(')
        elif basket[i] == ')':
            if len(stack) != 0:
                stack.pop()
            else:
                return 'NO'
    if len(stack) != 0:
        return 'NO'
    return 'YES'

T = int(input())
line = []
for i in range(T):
    line.append(input())
for i in range(T):
    print(bracket(list(line[i])))