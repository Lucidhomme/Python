from service.oop.hms.exception import *

# animal = Liger() #객체생성
# animal.cry()
# animal.jump()
# animal.bite()
# animal.play()

# base = Base() # 추상클래스는 인스턴스를 만들 수 없음, 상속에서 내려줘야함
# base = BaseSub()
# base.study()  # 자식이 추상클래스라는 부모로부터 상속받을 경우, 반드시 자식클래스에서 모든 함수들을 오버라이딩 해주어야함!! = 강제성의 개념
# base.gotoAcademy()

#문법오류
# print('error)
# print('success')

# a = 10
# b = 20
# print(c)

# print(100/0)
# print('end')

# list = [50, 70, 90]
# print(list[4])
# print('end')

# dic = {'name' : 'jslim', 'age' : 48, 'address' : 'seoul'}
# print(dic['Name'])  #대문자로 바꿀때 에러발생
# print(dic.get('Name'))  #대문자여도 get을 쓰면 키로 데이터 가져올때 대문자여도 에러발생은 안됨 그냥 못가져올뿐

# file = open("C:/test.text")

# x = [1,2]
# y = (1,2)
# z = 'test'
# print(x+list(y))

# userInput()
# print('after userInput()')

# list01 = [1,2,3,-100]
# exceptionFunc(list01)
# print('end')

list = [10,20,25,'num',40,50]
listExcepFunc(list)