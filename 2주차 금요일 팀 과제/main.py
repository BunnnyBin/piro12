from login import *
from learn import *
from event2_Lunch import *
from homework_event import *
from gohome import *
from student import escape
from time import sleep

boss, students = login()
avg_ability = make_avgdict(students)
finish = True
week = 1

print("\n\n------안녕하세요. '{0}'의 피로 키우기에 오신것을 환영합니다.------##\n" .format(boss.b_name))
sleep(1)
print("## {0}님은 28명의 피로그래밍12기를 8주 동안 낙오자없이 데려가야합니다. ## ".format(boss.b_name))
sleep(1)
print("## 학생들이 '{0}님을 잘 따를 수 있도록 리더십을 발휘하세요! ##".format(boss.b_name))
sleep(1)

print('''
\t\t\t\t\t       ___
\t\t\t\t\t    \( ○-○ )/
\t\t\t\t\t     \|   |/
\t\t\t\t\t      |   |
\t\t\t\t\t      /---\\
\t\t\t\t\t
\t\t\t\t\t ●   ●   ●   ●   ●
\t\t\t\t\t/|\ /|\ /|\ /|\ /|\\
\t\t\t\t\t/ \ / \ / \ / \ / \\
''')

while finish:
    select = 0
    repeat = True
    print("                 Week {0} - P'rogramming 12th\n[12기의 평균 능력치] - 열정: {1}%, 피로감: {2}%, 코딩력: {3}%, 인류애: {4}%\n"
          .format(week, avg_ability['avg_passion'], avg_ability['avg_fatigue'], avg_ability['avg_coding'], avg_ability['avg_humanity']))
    while repeat:
        print('(1) 강의하기    (2) 밥먹이기    (3) 과제내기    (4) 집보내기    (0) 엔딩')
        select = input('입력: ')
        if select == '0':
            finish = False
            print("\n'{}'님이 {}주차 도중 도망쳤습니다.ㅠㅠㅠㅠㅠㅠㅠ".format(boss.b_name, week))
            sleep(1)
            print('학생들: {}가 우릴 버렸어...'.format(boss.b_name))
            sleep(1)
            print("\nP'rogramming 12th 종료!")
            break
        elif select == '1':
            learn(students)
        elif select == '2':
            lunch(boss, students)
        elif select == '3':
            homework(students)
        elif select == '4':
            change = gohome(boss, students, avg_ability['avg_passion'])
            avg_ability['avg_passion'] = change
            repeat = False
        else:
            print('ERROR: 잘못된 번호를 선택하였습니다.\n\n')

    if select == '0':
        break
    escape(students)
    week += 1

    if len(students) <= 0:
        print("모든 12기가 탈주했습니다...")
        sleep(1)
        print("회장님: 내가 능력부족이라니!!!!")
        sleep(1)
        break
    avg_ability = make_avgdict(students)
    view_student(students, week)
    if week > 8:
        print("P'rogramming 12th 종료!")
        ending(boss, students)
        break;


