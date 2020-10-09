from service.oop import oop_first_class as oop

#학생의 이름, 학년평점을 저장한다면??
# stu_name = '섭섭해'
# stu_grade = 4.5
# stu_name1 = '섭섭이'   ##일일이 나열하고 리스트만들고 넣고 하는 방법이 객체지향에서는 비효율적임.
# stu_grade1 = 4.0

stu = oop.Student('jslim') # instance 생성
print(stu.hardStudy())
