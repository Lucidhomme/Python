# 클래스의 구성요소
# 멤버 변수 - 자료를 저장
# 생성(Constructor) - 객체생성 시 호출되는 일급함수(__init__)
# def function() - 자료처리를 위한 함수

class Student(object) : # 명시적인방법으로 스튜던트클래스는 오브젝트를 상속받겠다.묵시적으로 안써도 의미는 동일 (일반적으로 클래스이름은 첫글자만 대문자씀)
    msg = '나는 전역변수이지만 인스턴스 소유가 아닌 클래스 소유야'
    def __init__(self, name) : #인스턴스를 생성하는순간 init자동호출
        self.name = name

    def hardStudy(self):
        return "오늘도 열공했다~~~"
