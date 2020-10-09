def print_coins() :
    for i in range(100):
        print("bitcoin")

def first_func(name) :
    print("Welcome To ~ ", name)

def return_func(name) :
    return "커피 사줘요~" +str(name)   # return은 변수에 담을 수 있고, 프린트는 담을 수 없음

def sum_func(x,y,z) :     # 변수여러개 리턴
    return x+y+z

def tuple_func(*args) :    # *은 튜플, **은 딕셔너리의 가변인자를 넣어야함
    result = 0
    for idx in range(len(args)) :
        result += args[idx]
    return result

def dic_func(**args) :                       #변수 두개 딕셔너리
    for key , value in args.items() :
        print("{} = {}".format(key, value))

def multi_func(x, y) :      # 변수 두개를 튜플
    sum = x + y
    mul = x * y
    return(sum, mul)


def test(x) :
    print("test")

def default_func(x, y, flag = True) :     # 매개변수가 들어오지않으면 디폴트값으로 True 인식.원래 매개변수 3개넣어야하는데 2개만 넣어도 됨
    sum = x + y
    if sum > 10 and flag :
        return sum
    else :
        return 0

def optionSum(x,y):
    odd = 0
    even = 0
    for i in range(x,y+1) :
        if i % 2 == 0 :
            even += i
        elif i % 2 == 1 :
            odd += i
    return odd, even

#operator 따라서 +,-,*,/ 연산을 수행하고 결과를 리턴하는 함수를 정의
def calculator(op1, operator, op2) :
    if operator == "+" :
        return op1 + op2
    elif operator == "-" :
        return op1 - op2
    elif operator == "*" :
        return op1 * op2
    elif operator == "/" :
        return op1 / op2

def make_url(x) :
    return "www."+x+".com"

def print_max(a,b,c) :
    #list = [a, b, c]
    #list = sorted(list, reverse = True)
    #return list[0]
    max_value = 0
    if a > max_value :
        max_value = a
    if b > max_value :
        max_value = b
    if c > max_value :
        max_value = c
    return max_value

def leap_year(year) :
    if((year % 4 == 0) and (year % 100 !=0)) or (year% 400 == 0):
        return "윤년"
    return "평년"

def leap_year_loop(start, end) :
    yearList = []
    for year in range(start, end +1):
        if((year % 4 ==0) and (year % 100 != 0)) or (year % 400 == 0):
            yearList.append(year)
    return yearList


def return_dict(x) :
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'val01' : y1, 'val02' : y2, 'val03' : y3}




# 변수의 스코프
# 콜바이 밸류는 지지고볶아도 원본에 영향을 미치지않음, 반면 콜바이레퍼런스는 원본에 영향을 미침
# x = 50       #x는 전역변수
# def local_func(x) :
#     x += 50       #x는 지역변수 함수가 끝나면 효력을 잃어버림
#     print("inner func",x)
#
# local_func(x)
# print('x = ',x) #여기서 x는 전역변수를 뜻하기때문에 50을 호출
#
# # 변수의 스코프 응용
# x = 50
# def local_func(y) :
#     # x = 60  #전역변수와 지역변수의 변수명이 동일할때는 함수안에서는 지역변수가 우선권을 가짐
#     global x # global로 변수를 주게되면 x는 더이상 지역변수가 아니라 함수밖에 설정된 전역변수를 의미함
#     x += y
#     print("inner func",x)
#
# local_func(x)
# print('x = ',x)


# 전역변수
# data = [1,3,5,7,9]
# tot = 0
#
# for value in data :
#     tot += value
# print(tot)        # 함수가 아님 전역변수
#
# def tot_calc(data) :
#     tot1 = 0
#     for value in data :
#         global tot      # print(tot) 전역변수에서 값을 내려받음
#         tot += value
#         tot1 += value
#     return tot, tot1
#
# (tot0,tot1) = tot_calc(data)
#
# print(tot0, tot1)