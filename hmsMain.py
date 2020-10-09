from service.oop.hms.student import *

# 객체생성
# stu01 = Student()
# # print(stu01) #주소번지자체는 의미없고 주소번지를 참조하고 있는 변수는 stu01이라는게 중요함
# stu01.stuInfo() #자식(인스턴스)것도 자식거 부모(클래스)것도 자식거.하여 인스턴스가 클래스의 함수 이용가능

# stuList = []
#
# stu02 = Student('섭섭님',48,'Instructor','male')
# # stu02.stuInfo()  # stu01은 인자가 없어서 클래스의 이니셜라이즈가 가능한데 stu02는 인자가 정해진데 이니셜라이즈 메소드(함수에 매개변수)를 정의안하면 오류남
# stuList.append(stu02) #리스트에 담을 수 있음.루핑에 활용
#
# stu03 = Student('김한준',30, 'Student','male')
# # stu03.stuInfo()
# stuList.append(stu03)
#
# for stu in stuList:
#     stu.stuInfo()

tea = Teacher('임정섭','많이','best')
print(tea.name)
print(tea.salary)
print(tea.survey)
tea.salaryInfo()
tea.working()

print(Teacher.class_variable)
Teacher.classFunction() #클래스 소유의 함수 호출
Teacher.printClassVariable() ###클래스라는 Teacher가 아니라 tea라는 인스턴스 소유의 함수로 지정해주면 호출됨
