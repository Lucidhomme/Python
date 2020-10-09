#hms패키지밑에 inheritance 모듈생성, 파이썬베이스 밑에 inheritance_caller 모듈생성

# encapsulation(은닉화)
# information - hiding(정보은닉)

class MyDate(object):

    def __init__(self, year, month, day):
        self.__year = year  #인스턴스에 __를 붙이게되면 잠금형태가 되면서 외부의 접근을 허용하지않음
        self.__month = month
        self.__day = day

    def __getInfo(self):
        return "해당 메서드는 private 형식의 함수이므로 접근 불가"

    def setYear(self, year):
        if(year < 0) :
            self.__year = 2020
        else :
            self.__year = year

    def getYear(self):
        return self.__year


# inheritance
class Sup(object):
    def __init__(self,name):
        self.name = name

    def getState(self):
        print('Super - ',self.name)

class Sub(Sup):
    def getState(self):
        print('Sub - ', self.name)  ##부모에 정의된것을 자식에서 재정의 하는 예(오버라이딩)



class Person(object):
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def perInfo(self):
        return self.name + str(self.age) + self.address

class StudentVO(Person):
    def __init__(self, name, age, address, stuId):
        super().__init__(name,age,address)
        self.stuId = stuId

    def stuInfo(self):
        return super().perInfo() + "," + self.stuId

class TeacherVO(Person):
    def __init__(self,name, age, address, subject):
        super().__init__(name,age,address)
        self.subject = subject

    def teaInfo(self):
        return super().perInfo() +","+self.subject



class Car(object):
    def __init__(self, speed):
        self.speed = speed

    def getSpeed(self):
        return self.speed

    def carDesc(self):
        return "차량 : {}".format(self.speed)

class SportsCar(Car):
    def __init__(self, speed, turbo):
        super().__init__(speed)
        self.turbo = turbo
    def getTurbo(self):
        return self.turbo
    def carDesc(self):
        return super().carDesc() + "\t터보 여부 = " + self.turbo


class Truck(Car):
    def __init__(self,speed,capacity):
        super().__init__(speed)
        self.capacity = capacity
    def getCapacity(self):
        return self.capacity
    def carDesc(self):
        return super().carDesc() + "\t 적재 공간 = " + str(self.capacity)



# [실습]
# 1. Account class 작성 - account, balance, interestRate
# class Account(object):
#     def __init__(self,account,balance,interestRate):
#         self.account = account
#         self.balance = balance
#         self.interestRate = interestRate
#
# # 2. accountInfo() - 계좌의 정보를 출력한다(account, balance, interestRate)
#     def accountInfo(self):
#         print("{}계좌의 잔액은 {}이며 이자율은 {}입니다".format(self.account,self.balance,self.interestRate))
#
# # 3. deposit(amount) - 계좌 잔액에 매개변수로 들어온 amount를 누적한다.
#     def deposit(self,amount):
#         self.balance += amount
#
# # 4. printInterestRate() - 현재 잔액의 이자율을 계산하여 소수점 자리 2자리까지 출력한다.
#     def printInterestRate(self):
#         interest = self.balance * self.interestRate
#         print("%.2f"% (interest))
#
# # 5. withDraw(amount) - 매개변수로 들어온 금액만큼을 출금하여 잔액을 변경한다. 단 잔고가 부족할 경우 '잔액이 부족하여 출금할 수 없습니다' 라는 메시지를 출력한다
#     def withDraw(self,amount):
#         if(self.balance < amount) :
#             print("잔액이 부족하여 출금할 수 없습니다")
#         else :
#             self.balance -= amount

# caller쪽에서 객체생성 후
# account = Account('44-2919-1234',500000,0.073)
# account.accountInfo()
# account.withDraw(600000)
# account.deposit(200000)
# account.accountInfo()
# print("현재 잔액의 이자를 포함한 금액")
# account.printInterestRate()


#[실습] 상속개념
#1. Account class 작성, account, balance, interestRate, type(계좌 종류 S\F)
class Account(object):
    def __init__(self,account,balance,interestRate,type):
        self.account = account
        self.balance = balance
        self.interestRate = interestRate
        self.type = type

    def accountInfo(self):
        print("{}계좌의 잔액은 {}이며 이자율은 {}입니다".format(self.account, self.balance, self.interestRate))

    def deposit(self,amount):
        self.balance += amount

    def printInterestRate(self):
        interest = self.balance * self.interestRate
        print("%.2f" % (interest))

    def withDraw(self,amount):
         if (self.balance < amount):
             print("잔액이 부족하여 출금할 수 없습니다")
         else :
             self.balance -= amount

#1.1. SavingAccount, FundAccount 자식 클래스 추가
class SavingAccount(Account):
    def __init__(self,account,balance,interestRate,type):
        super().__init__(account,balance,interestRate,type)

    def printInterestRate(self):
        self.balance = 1.1 * self.balance + (self.balance * self.interestRate)
        print("{}입니다".format(self.balance))

class FundAccount(Account):
    def __init__(self,account,balance,interestRate,type):
        super().__init__(account,balance,interestRate,type)

    def printInterestRate(self):
         if self.balance >= 100000 :
             self.balance = self.balance * 1.1
         if self.balance >= 500000 :
             self.balance = self.balance * 1.15
         if self.balance >= 1000000 :
             self.balance = self.balance *1.2
         print("{}입니다".format(self.balance))

#1.2. -- def printInterestRate() -- printInterestRate()오버라이딩


#1.3. SavingAccount - printInterestRate()
#     기본 이자율에 만기시 이자율을(0.1) 복리로 계산


#1.4. FundAccount - printInterestRate()
#     기본 이자율에 잔액 10만원 이상이면 10%
#     기본 이자율에 잔액 50만원 이상이면 15%
#     기본 이자율에 잔액 100만원 이상이면 20%
