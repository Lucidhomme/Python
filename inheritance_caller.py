from service.oop.hms.inheritance import *

# date = MyDate(2020, 8, 17)
# print(date.year)   #은닉화때문에 프린트 안됨
# print(date.month)
# print(date.day)
# date.__getInfo()

# date.setYear(-2020)
# print(date.setYear(2020)) #return 없어서 안넘어옴
# date.getYear()
# print(date.getYear())

# sub = Sub('상속관계아들 생성자 호출')
# sub.getState()  #자식에는 변수가 없지만 부모로부터 가져와서 호출

# stu01 = StudentVO('임정섭',48,'서울','1992')
# tea01 = TeacherVO('임섭순',48,'광주','파이썬')
# stu01.perInfo()
# print(stu01.perInfo())
# tea01.perInfo()
# print(tea01.perInfo())

# perList = []
# perList.append(stu01)
# perList.append(tea01)
# 
# for obj in perList :
#     if isinstance(obj, StudentVO) :
#         print(obj.stuInfo())
#     else :
#         print(obj.teaInfo())

# scCar = SportsCar(300, '터보기능')
# print("speed - ",scCar.getSpeed())
# print("desc - ",scCar.carDesc())


#[실습]
# account = Account('44-2919-1234',500000,0.073,'S')
# account.accountInfo()
# account.withDraw(600000)
# account.deposit(200000)
# account.accountInfo()
# print("현재 잔액의 이자를 포함한 금액")
# account.printInterestRate()

saving = SavingAccount('44-2919-1234',500000,0.073,'S')
saving.printInterestRate()

fund = FundAccount('44-2919-1234',500000,0.073,'F')
fund.printInterestRate()


