from service.oop.hms.employee import *

# emp01 = Employee('임정섭',1000) #객체생성
# emp01.appy_raise()
# print(emp01.getEmp())
# 
# emp02 = Employee('섭섭해',2000)
# emp02.appy_raise()
# print(emp02.getEmp())
# 
# # print(dir(emp01))  #init에서는 자동으로 호출하지만 사용자가 init안에 인자값을 추가하게 되면 동일하게 받을때도 인자값을 추가해주어야함
# 
# # print(id(emp01)) #id는 instance가 같은지 다른지 식별하는 함수, emp01과 emp02가 주소값이 다름을 확인가능
# # print(id(emp02))
# 
# print()
# Employee.change_raise_rate(1.5) # 만약 저 함수를 호출하고 싶으면 인스턴스의 이름이 아닌 클래스의 이름으로 접근해야함, 만약 인스턴스이름으로 접근하려면 함수위에 @staticmethod 지정해주고 접근해야함
# emp01.appy_raise()
# print(emp01.getEmp())
# emp02.appy_raise()
# print(emp02.getEmp())
# 
# print("car 객체 생성 후 작업진행")
# # Car.name = 'Jeep'
# # Car.door = 4
# # Car.cc = 2000
# # print("{}, {}, {}".format(Car.name, Car.door, Car.cc))
# 
# car01 = Car('레인지로버',5,4000)
# car01.info()
# 
# car02 = Car('포르쉐 카레라 911', 2, 3500)
# car02.info()



# Question
# 1. 전원을 on 시킨다
# 2. 채널 18번으로 변경
# 3. 볼륨을 9로 변경
# 4. TV상태를 출력

# print(TV.power)
# print(TV.channel)
# print(TV.volume)
# tv = TV()
# print(tv.power)
# print(tv.channel)
# print(tv.volume)

tv = TV()
tv.display()
#1.
tv.changePower()
tv.display() # employee모듈의 not(TV.power)를 not(self.power)로 바꿔줌

#2.
for i in range(8):
    tv.channelUp()
tv.display()

#3.
for i in range(4):
    tv.volumeUp()
tv.display()

