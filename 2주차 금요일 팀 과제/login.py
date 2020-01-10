from boss import *
from student import *


def login():
    students = []
    f = open("st_name.txt", 'r', encoding='UTF8')
    make_boss = boss(input('회장님 이름: '))
    for i in range(28):
        st_read = f.readline()
        students.append(student(st_read.rstrip('\n')))
    return make_boss, students


def make_avgdict(students):
    sum_coding = sum_fatigue = sum_humanity = sum_passion = 0
    for student in students:
        sum_coding += student.st_coding
        sum_fatigue += student.st_fatigue
        sum_humanity += student.st_humanity
        sum_passion += student.st_passion
    avgdict = {
        'avg_coding': sum_coding // len(students),
        'avg_fatigue' : sum_fatigue // len(students),
        'avg_humanity' : sum_humanity // len(students),
        'avg_passion' : sum_passion // len(students)
    }
    return avgdict