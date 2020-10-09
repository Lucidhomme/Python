#hms패키지밑에 employee모듈 생성,파이썬베이스 밑에 emp_caller 모듈생성
class Employee(object) :

    raise_rate = 1.1 #class variable

    def __init__(self, name, pay):
        self.name = name  #instance variable
        self.pay = pay    #instance variable

    def appy_raise(self):
        self.pay = int(self.pay * Employee.raise_rate) ##self.pay는 __init__에서 한번 지정해주었으니 그대로 받아서 씀

    def getEmp(self):
        return "{}님의 급여는 {}입니다".format(self.name,self.pay)  ##{}대신 %d %s가 들어가면 뒤에도 format대신 %를 써야함

    #@staticmethod
    @classmethod #스태틱메소드처럼 클래스 메소드를 쓸 수도 있는데 붙이면 함수의 매개변수에 cls가 붙어야함
    def change_raise_rate(cls, rate):  #self를 가지고있지않으니 instance소유가 아니고 외부에서 호출 불가능
        # print("change_raise_rate ~~")
        cls.raise_rate = rate
        print("인상률 %f 가 적용 되었습니다" % (cls.raise_rate))

class Car(object) :
    # class variable
    name = None # None은 Null과 같은의미
    door = cc = 0

    # constructor
    def __init__(self, name, door, cc):
        self.name = name
        self.door = door
        self.cc = cc

    # function, method
    def info(self):
        if self.cc >= 3000 :
            self.type = '대형'
        elif self.cc >= 2000 :
            self.type = '중형'
        else :
            self.type : '소형'

        self.display()

    def display(self):
        print("%s는 %d cc이고(%s), 문짝은 %d개 입니다" %(self.name, self.cc, self.type, self.door))   ##시험에 나오는문제


class TV(object) :
    # 1. class variable
    channel = 10
    volume = 5
    power = False #(True : on, False : off)
    # init 꼭 필요하지는 않음
    # 2. 전원관리를 위한 함수
    def changePower(self):
        self.power = not(self.power)  ##tv라는 클래스의 power는 트루이다라고 인스턴스소유의 파워를 지정

    # 3. 채널변경을 위한 함수
    def channelUp(self):
        self.channel += 1

    def channelDown(self):
        self.channel -= 1
    
    def volumeUp(self):
        self.volume += 1

    def display(self):
        print("전원상태 : {}, 채널번호 : {}, 볼륨 : {}".format(self.power, self.channel, self.volume))
    
#상속개념에서는 자식의 개념이 부모보다 크다 
#객체를 생성하지않아도 자식은 부모의 값을 가져다 쓸 수 있다
#자식은 부모의 것을 가져다가 수정하여 정의할수도 있음.즉 구문형식은 동일하지만 바디부분의 내용이 +@될 수 있음(오버라이딩의 개념)
#그런데 자식이 부모보다 개념상 큰 범위에 속하기때문에 부모에서의 객체생성은 의미없음. 하여 공통의 요소는 부모에 넣고 자식들은 물려받음형태가 이상적
#캡슐화 : 부모가 자식에게 물려주지않는 것을 남겨두는 개념