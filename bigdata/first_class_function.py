# first_class_function(일급함수)
# 람다식(lamda)

def add(x,y) :
    return x+y

print("caller ~ {}".format(add(10,20)))
print(add)
print(add(1,2))

# 함수를 다른 함수에 담아보려고 함
other_func = add
print(other_func) #other_func 안에 ()없으면 주소값반환
print("other_func - ",other_func(1,2)) # other_func 안에 ()있으면 연산


def operation(func, arg_list) :
    result = []
    for (tmp1, tmp2) in arg_list :
        result.append(func(tmp1,tmp2))
    return result

def mul(x,y) :
    return x*y

# data = [(1,2),(3,4),(5,6)]
# result = operation(add, data)
# print(result)

# 익명의 함수 (메모리상의 효율성을 위해서)
# def mul_func(x,y):
#     return x * y
# result = mul_func(1,2)

# 위 3줄 1줄로 만드는법 : 람다식(익명의 함수)이용
# lambda x, y : x * y
lambda_func = lambda x, y : x * y
print(lambda_func(1,2))

# 함수(ex def) < 클래스 < 모듈(ex package_function) < 패키지(ex service)
# Class는 변수와 함수를 꾸러미로 담을 수 있음, 커플링은 약하고 응집력이 높아야함
# OOP의 개념 : 캡슐화,상속,다형성,추상화
