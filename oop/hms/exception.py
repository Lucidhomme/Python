# hms패키지 밑에 exception 모듈만들고  python base밑에 exception_caller모듈만듬
# serivce패키지 밑에 file패키지만들고 그 밑에 text_file_inout만듬
# 다중상속, 추상화
# 타이거와 라이온의 속성들을 상속받아 라이거라는 새로운 클래스를 만든다(부모의 것도 자식거라는 개념을 활용)
class Animal(object) :
    def cry(self):
        pass

class Tiger(Animal) :
    def jump(self):
        print('호랑이가 점프를 한다')
    def cry(self):
        print('어흥')


class Lion(Animal) :
    def bite(self):
        print('한 입에 꿀꺽한다')

    def cry(self):
        print('그르렁')

class Liger(Tiger, Lion) :     ##Tiger,Lion 둘다 cry를 가지고 있지만 왼쪽부터 호출을 하기때문에 Tiger의 cry만 caller에 호출
    def play(self):
        print('라이거가 사육사를 잡아 먹었습니다')


# 추상클래스
# 메서드의 목록만 가진 클래스
# 상속받는 클래스에서 메서드 구현을 강제하기 위해서 사용하는 문법
# 객체생성이 불가함
from abc import *

class Base(metaclass=ABCMeta):
    @abstractmethod  #구현부가 없는 추상메서드
    def study(self):
        pass

    @abstractmethod
    def gotoAcademy(self):
        pass

class BaseSub(Base):
    def study(self):
        print('공부하자')

    def gotoAcademy(self):
        print('멀티캠퍼스 가야지~~')


"""
예외 처리 구문
try : 에러가 발생 할 가능성이 있는 코드
except : 발생된 에러를 잡기위한 객체 정의
except : #다중가능, 귀찮으면 에러클래스로 만들어도 됨
else : 에러가 발생되지 않을 때 실행되는 블럭, 단독 사용 불가능
finally : 무조건 실행
"""
##예외는 에러가 발생하면 그때 잡으면 됨



def userInput():
    try :
        age = int(input("본인의 나이를 입력하세요 : "))
        print('Result - ', age)
    except ValueError :
        userInput()
        # print("숫자값을 입력해주세요~~ 제발")
    else :
        print('Result - ', age)
    finally :
        print('넌 항상 실행되서 재미가 없어~~')


def exceptionFunc(list_data):
    sum = 0
    try :
        sum = list_data[0] * list_data[1] * list_data[2] * list_data[3]
        if sum < 0 :
            raise Exception("User Define Exception") #다른 에러 발생시키기 때문에 프로그램 정상적으로 종료가 안됨
    except IndexError as err :
        print(str(err))
    except Exception as e :   #try에 여러개가 정의되어 있으면 except도 여러개로 예외처리 가능
        print(str(e))      
    else :
        print(sum)



# 매개변수로 넘겨 받은 각 첨자번지의 값에 제곱(**)한 결과를 출력하려고 한다.
# 예외 발생을 확인하고 예외처리 구문을 추가하여 정상적인 흐름의 함수 호출이 되도록 만들어본다면?
def listExcepFunc(list) :
    for i in list :
        try :
            print("raw - ", i)
            squared = i**2
            print("squared - ", squared)
        except TypeError as tr :
            print("숫자가 아닌 값이 들어 있습니다..확인요망")
    print("end function")

# try안에 for구문을 집어넣으면 숫자값 아닐때 루프를 빠져나감
# def listExcepFunc(list) :
#     try :
#         for i in list :
#             print("raw - ", i)
#             squared = i**2
#             print("squared - ", squared)
#     except TypeError as tr :
#         print("숫자가 아닌 값이 들어 있습니다..확인요망")
#     print("end function")
