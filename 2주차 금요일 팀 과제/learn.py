import random
from random import randint
import time

teacher = ['장용석', '늘한', '몰랑이는 귀여워']

def learn(students):
    num = randint(0, 2)
    d_teacher = teacher[num]
    print("\n흠..어떤 걸 시키지??")
    print("1. 인강 듣기 2. {0}의 강의 듣기 3. 성모 따라하기".format(d_teacher))  # teacher 변수 필요

    num = input()  # input 예외처리 필요

    # 어떤걸 시킬지에 따라 학생들의 능력치 변화
    if num == '1':
        online_lec(students)
    elif num == '2':
        offline_lec(students, d_teacher)
    elif num == '3':
        follow_boss(students)


# learn의 datail action
def online_lec(students):
    print("\n우리 오늘 인강 들으면 됩니다~여러분ㅎㅎ여러분ㅎㅎ힘내세요")
    time.sleep(1)
    print('''
       ■■■■■■■■■■■■■■
       ■    코딩     ■
       ■    도장     ■
       ■■■■■■■■■■■■■■
           /    \\
    ''')
    time.sleep(1)
    index = random.sample(list(range(len(students))), randint(1, len(students)))
    print('\n-----------인강 들은 사람 목록-----------')
    for i in index:
        students[i].st_coding += 10
        students[i].st_fatigue += 3
        students[i].st_humanity -= 2
        students[i].st_passion -= 3
        print(students[i].st_name, end=' ')
    print()
    print("----------------------------------------")
    print()
    time.sleep(1)
    print("{}명의 학생들 왈: ".format(len(index)), "휴~~ 보람차네에")
    time.sleep(1)
    print('{}명의 코딩력이 +10, 열정 -3, 인류애가 +2, 피로가 +3 되었습니다\n'.format(len(index)))

def offline_lec(students, d_teacher):# 누구의 강의인지에 따라 학생들의 능력치 변화
    if d_teacher == '장용석':
        print('\n(웅성웅성){} 강사님 잘생겼다~~'.format(d_teacher))
        index = random.sample(list(range(len(students))), randint(1, len(students)))
        time.sleep(1)
        print('\n-----------강의 집중한 사람 목록-----------')
        for i in index:
            students[i].st_coding += 8
            students[i].st_fatigue += 3
            students[i].st_humanity -= 1
            students[i].st_passion += 3
            print(students[i].st_name, end=' ')
        print()
        print("----------------------------------------")
        print()
        time.sleep(1)
        print("{}명의 학생들 왈: ".format(len(index)), "용석 강사님 사랑해요~~")
        time.sleep(1)
        print('{}명의 코딩력이 +8, 열정 +3, 인류애가 -1, 피로가 +3 되었습니다\n'.format(len(index)))
    elif d_teacher == '늘한':
        print('\n질문방 네임드 {} 등장!!'.format(d_teacher))
        index = random.sample(list(range(len(students))), randint(1, len(students)))
        time.sleep(1)
        print('\n-----------강의 집중한 사람 목록-----------')
        for i in index:
            students[i].st_coding += 5
            students[i].st_fatigue += 2
            students[i].st_humanity -= 2
            students[i].st_passion += 4
            print(students[i].st_name, end=' ')
        print()
        print("----------------------------------------")
        print()
        time.sleep(1)
        print("{}명의 학생들 왈: ".format(len(index)), "늘한이 저분이였다니!")
        print('{}명의 코딩력이 +5, 열정 +4, 인류애가 -2, 피로가 +2 되었습니다\n'.format(len(index)))
    elif d_teacher == '몰랑이는 귀여워':
        print('\n앗, 저분은 질문방의 몰랑이...귀여워')
        index = random.sample(list(range(len(students))), randint(1, len(students)))
        time.sleep(1)
        print('\n-----------강의 집중한 사람 목록-----------')
        for i in index:
            students[i].st_coding += 20
            students[i].st_fatigue -= 3
            students[i].st_humanity += 4
            students[i].st_passion += 3
            print(students[i].st_name, end=' ')
        print()
        print("----------------------------------------")
        print()
        time.sleep(1)
        print("{}명의 학생들 왈: ".format(len(index)), "몰랑이....갖고 싶다...")
        time.sleep(1)
        print('{}명의 코딩력이 +20, 열정 +3, 인류애가 +4, 피로가 -3 되었습니다\n'.format(len(index)))

def follow_boss(students):
    print("\n저를 따라해보세요~여기보세요~")
    index = random.sample(list(range(len(students))), randint(1, len(students)))
    time.sleep(1)
    print('\n-----------잘 따라간 사람 목록-----------')
    for i in index:
        students[i].st_coding += 5
        students[i].st_fatigue += 1
        students[i].st_humanity += 3
        students[i].st_passion -= 4
        print(students[i].st_name, end=' ')
    print()
    print("----------------------------------------")
    print()
    time.sleep(1)
    print("{}명의 학생들 왈: ".format(len(index)), "회장님...집 보내줘요...")
    time.sleep(1)
    print('{}명의 코딩력이 +5, 열정 -4, 인류애가 +3, 피로가 +1 되었습니다\n'.format(len(index)))

