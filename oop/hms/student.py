# 네임스페이스 : 패키지이름, 같은 클래스라도 네임스페이스가 다르면 다른 것으로 본다
# 클래스소유의 변수는 누구나 변경이 안됨(상수처리하는 것이 보통)
class Student(object) :
    def __init__(self, name, age, job, gender):   #self는 신경쓰지말고 넘겨주는 매개변수와 받는 매개변수 수가 같아야함
        self.name = name
        self.age = age
        self.job = job
        self.gender = gender

    def stuInfo(self): #클래스의 정의된 변수나 메소드는 클래스가 아닌 인스턴스의 소유이다 하여 함수를 정의하면 자동으로 셀프들어감.인스턴스 소유의 함수구나 식별가능
        print("이름 : {}, 나이 : {}, 직업 : {}, 성별 : {}".format(self.name, self.age, self.job, self.gender))


class Stu(object):
    scholarship_rate = 3.5  ##클래스 소유의 변수

    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    
    def stuInfo(self):
        return "이름 : {}, 학점 : {}".format(self.name, self.grade) #name, grade 인스턴스 소유라 self적어줘야함

    def isScholarship(self):
        if self.grade >= Stu.scholarship_rate :
            return True
        else :
            return False


class Teacher(object) :    
    
    class_variable = "클래스 변수입니다"  ##클래스 소유의 변수
    
    def __init__(self, name, salary,survey):
        self.name = name
        self.salary = salary
        self.survey = survey

    def working(self):
        print("지금 열심히 객체지향 프로그램을 강의하고 있습니다")

    def salaryInfo(self):
        print("{}님의 급여는 {}입니다.".format(self.name,self.salary))

    def surveyInfo(self):
        print("참 잘했어요")

    def printClassVariable(self):
        print(Teacher.class_variable) #클래스이름.변수

    @staticmethod
    def classFunction(): #클래스 소유의 함수는 self가 안들어가고 @staticmethod를 넣어줘야함
        print(Teacher.class_variable)

