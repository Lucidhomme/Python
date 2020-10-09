import function as f  #import는 모듈을 가져옴, 별칭도 줄수있다
from service.bigdata import package_function as pf #from 패키지 import 모듈 혹은 from 패키지.모듈이름 import 함수이름
from service.bigdata.package_function import print_coins, first_func #first_func를 하나 더 추가할 수도 있고
from service.bigdata.package_function import *

# f.print_coin()   #함수의 별칭을 주면서 print(첫번째줄)
# pf.print_coins()  #" (두번째줄)
# print_coins()     # 세번째줄
# first_func('세진')

# thanks = return_func("선림")
# print(thanks)

# print(sum_func(1,2,3))

# result = tuple_func(1,2,3,4,5,6,7,8)
# print(result)

# dic_func(name='jslim', name1 ='park', name2 ='kim')

# (sum, mul) = multi_func(2,1) #언패킹
# print("합 {} 곱 {}".format(sum,mul))

# test() #매개변수 없으니 에러
# result = default_func(10,20)
# result = default_func(10,20, False)
# print(result)

# oddSum,evenSum = optionSum(100,500)
# print("홀수 합 : ",oddSum)
# print("짝수 합 : ",evenSum)

# result = calculator(10,"+",20)
# print(result)

# www.naver.com
# url = make_url('naver')
# print(url)

# 세 개의 숫자를 입력받아 가장 큰 수를 출력할 예정이다
# max = print_max(10,20,30)
# print(max)

# 윤년, 평년
# 4의 배수이고 100의 배수가 아니거나 400의 배수일떄
# year = int(input("년도를 입력하세요 : "))
# leapMsg = leap_year(year)
# print(leapMsg)
#
# # year_list는 리스트를 넘겨받는다
# # 한 줄에 5개의 년도씩만 출력
# year_list = leap_year_loop(1900,2020)
# cnt = 0
# for idx in range(len(year_list)):
#     print(year_list[idx],end = "\t")
#     idx += 1
#     if idx % 5 == 0 :
#         print()

# dic = return_dict(10) # 단순히 리턴받는게 아니라 필요한 값들만 꺼낼 수도 있어야함
# for value in dic.values():
#     print(value)