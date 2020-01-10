import random
import time

def homework(students):
    count = 0  # 과제 낸 횟수
    while True:
        common_fatigue = 0
        print('(1) 개인과제    (2) 팀플과제')
        x = int(input('입력: '))
        if x == 1:
            common_fatigue = 20 + count*5
            self_homework(students, common_fatigue)
        elif x == 2:
            common_fatigue = 30 + count*5
            team_homework(students, common_fatigue)
        print('(1) 과제 이제 그만    (2) 과제 한번 더 가즈아')
        y = int(input('입력: '))
        if y == 1:
            break
        elif y == 2:  # 과제를 더 낼 때마다 피로도 +5
            count += 1
            print('!!!!학생들 피로도가 5 상승했다!!!!')

def self_homework(students, fatigue):
    n = random.sample(range(len(students)), random.randint(1, len(students)))  # 누구 학생으로 할지
    print('\n\n회장님: 여러분 여기 봐주세요ヾ(＾∇＾)/\n\t   오늘 엄청 간단한 개인과제가 주어질 예정입니다!')
    time.sleep(1)
    print('학생들: ㅠㅠ')
    time.sleep(1)
    print('\n<개인과제하는 사람>')
    for i in n:
        print(students[i].st_name)
        students[i].st_coding += 20  # coding 20 rise
        students[i].st_fatigue += fatigue  # fatigue 20 rise
        students[i].st_passion -= 10  # passion 10 down
        students[i].st_humanity -= 10  # humanity 10 down
    print('''\n
     ( - __ -) ┌-----┐
    ___\_____\_|_____|         
    ''')
    time.sleep(2)
    print('''\n개인과제로 인해 해당 학생들의 피로도가 %d 상승, 열정이 10 하락, 인류애가 10 하락하였다...
    하지만 코딩능력은 20 상승하였다(얏호)\n''' % fatigue)

def team_homework(students, fatigue):
    n = random.sample(range(len(students)), random.randint(1, len(students)))
    print('\n\n회장님: 여러분! 저기요??( ﾟ▽ﾟ)/\n\t   오늘 드디어 기다리던 팀플 과제가 있는 날입니다!')
    time.sleep(1)
    print('학생들: （○Ａ○）;;')
    time.sleep(1)
    print('\n<팀플과제하는 사람>')
    for i in n:
        print(students[i].st_name)
        students[i].st_coding += 40  # coding 40 rise
        students[i].st_fatigue += fatigue  # fatigue 30 rise
        students[i].st_passion -= 15  # passion 15 down
        students[i].st_humanity -= 20  # humanity 20 down

    print('''\n
       ( 팀플 중...)
    \●  \●/ ●   ●/ ●
     |\  | /|\ /| /|\\
    ---------------------
    ''')
    time.sleep(2)

    print('''\n팀플과제로 인해 해당 학생들의 피로도가 %d 상승, 열정이 15 하락, 인류애가 20 하락하였다...
    하지만 코딩능력은 40 상승하였다(얏호)\n''' % fatigue)