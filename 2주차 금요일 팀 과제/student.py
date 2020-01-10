from random import randrange
import time

class student:
    def __init__(self, st_name):
        self.st_name = st_name
        self.st_coding = 0
        self.st_fatigue = 0
        self.st_humanity = 100
        self.st_passion = 100


def escape(students):
    print('\n\n')
    run_st = []
    for num in range(len(students)):
        rate = ((100-students[num].st_passion) + (100-students[num].st_humanity) + students[num].st_fatigue) / 3
        randnum = randrange(0, 100)
        if randnum < rate:
            run_st.append(num)
    run_st.sort(reverse=True)
    print('탈주 계획중...')
    time.sleep(3)
    if run_st:
        for run in run_st:
            print("'{0}'가 탈주하였습니다. RUN~~~~~~~~~".format(students[run].st_name))
            del students[run]
    else:
        print('다행히도 이번 주는 탈주한 사람이 없다. 휴')
        time.sleep(1)
    print('\n\n')