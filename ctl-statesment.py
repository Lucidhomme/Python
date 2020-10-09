# 먼저, 파이썬 사용자 입력함수
# input()
# name = input("Enter Your Name : ")
# grade = input("Enter Your Grade : ")
# company = input("Enter Your Company Name : ")
# print(name, grade, company)

# score = int(input("Enter Your Score : "))
# print(score+100, type(score))

# 파이썬 제어문
# if, if ~ else, if ~ elif ~ else
# bool True : 0이 아닌수, 문자, 데이터가 있는 리스트, 튜플, 딕셔너리
# bool False : 0인 숫자, 문자, 데이터가 없는 리스트, 튜플, 딕셔너리
# if not False :    # if는 조건의 값이 True일때만 실행
#     print("Bad")

# if False :
#     print("Bad")
# else :             #if가 트루가 아니라 else만 실행되었다
#     print("Good")

# 아래의 값이 3의 배수인지 5의 배수인지
# 3의 배수도 5의 배수도 아닌지를 검정하고 싶다면?
# number = 15
# if (number % 3 == 0 & number % 5 == 0) :
#     print("{}은 3과 5의 배수입니다".format(number))
# else :
#     print("{}은 3과 5의 배수가 아닙니다".format(number))

# 윤년의 조건
# 4의 배수이고 100의 배수가 아니거나
# 400의 배수일때를 윤년으로 본다
# if구문을 사용하여 연도와 월을 입력받아서 월의 마지막 일을 출력하라

# year1 = int(input("연도를 입력하세요 : "))
# month1 = int(input("달을 입력하세요 : "))
# year_month1 = [31,28,31,30,31,30,31,31,30,31,30,31]
# leap_year_month1 = [31,29,31,30,31,30,31,31,30,31,30,31]
# if (year % 4 ==0 and year % 100 != 0) :
#     print("{}년 {}월 마지막 일은 {}입니다".format(year1,month1,leap_year_month1[month-1]))
# elif(year % 400 == 0) :
#     print("{}년 {}월 마지막 일은 {}입니다".format(year1, month1,leap_year_month1[month - 1]))
# else :
#     print("{}년 {}월 마지막 일은 {}입니다".format(year1, month1, year_month1[month - 1]))


# 중첩 조건문
# A학점이면서 95이상의 점수면 장학금 100%
# A학점이면서 90이상의 점수면 장학금 90%
# A학점이 아니면 장학금을 50%

# grade = (input("학점 입력 : "))
# total = int(input("점수 입력 : "))
# if grade == 'A' :
#     if total >= 95 :
#         print("장학금 100%")
#     else :
#         print("장학금 90%")
# else :
#     print("장학금 50%")


# area = ["서울","부산","제주"]  #데이터를 찾는 것
# region = "수원"
#
# if region in area :
#     pass
# else :
#     print("{} 지역은 포함되지 않습니다".format(region))
#
#
# myDict = {"서울" : 100, "광주" : 200} # 키를 찾는 것
# region = "부산"
#
# if region in myDict :
#     print("키 값이 dict안에 있습니다.")
# else :
#     print("키 값이 dict안에 없습니다.")



# num = 9
# result = 0
# if num >= 5 :
#     result = num * 2
# else :
#     result = num + 2
# print(result)
#
# # 삼항 연산자
# result = num*2 if(num>=5) else num+2  ##IF else일때만 사용가능한것으로 if에 해당되면 num*2를 아니라면 num+2를 호출하여 result로 출력하는 조건문
# print(result)

# 참, 거짓 판별 종류
# city = " "   #비어있는 데이터는 False로 본다,대신 공백은 데이터가 들어있는 문자열로 본다
# if city :
#     print(city)
# else :
#     print("Please enter your city")
#
#
# money = 0  # 세미불리언 개념
# if money :
#     print("맛점하세요~")
# else :
#     print("더 맛점하세요~")

#-----------실습
# 문제 1
# 사용자로부터 하나의 값을 입력받아(input) 해당값에 20을 뺀 값을 출력하라
# 단) 출력값의 범위는 0~255이다
# 예를 들어 결과값이 0보다 작은 값이 되는 경우 0을 출력하고 255보다 큰 값이 되는 경우 255을 출력해야한다

# v = int(input("값을 입력해주세요 : "))
# v2 = v - 20
# if v2 <= 255 and v2 >= 0 :
#     print("{}".format(v2))
# elif v2 < 0 :
#     print("0")
# else :
#     print("255")

# 문제 2)
# 사용자로부터 입력 받은 시간이 정각인지 판별하라.
# 현재시간 : 02:00
# 현재시간 : 03:10

# a = int(input("시간을 입력하세요(ex)02,10,14 : "))
# b = int(input("분을 입력하세요(ex)00, 59 : "))
# if b == 00 :
#     print("{}:{}은 정각입니다".format(a,b))
# else :
#     print("{}:{}은 정각이 아닙니다".format(a,b))

# 문제 3)
# 사용자로 입력받은 단어가 아래 fruit 리스트에 포함되어 있는지를 확인하라.
# 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.

# fruit_list = ["사과", "포도", "홍시"]
# idx = input("과일을 입력해주세요 : ")
# if idx in fruit_list :
#     print("정답입니다")
# else :
#     print("오답입니다")


# 문제 4)
# 투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후
# 해당 종목이 투자 경고 종목이라면 '투자 경고 종목입니다'를
# 아니면 "투자 경고 종목이 아닙니다."를 출력하는 프로그램을 작성하라.

# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# idx2 = input("투자할 종목을 입력해주세요 : ")
# if idx2 in warn_investment_list :
#     print("투자 경고 종목입니다")
# else :
#     print("투자 경고 종목이 아닙니다")



# 문제 5)
# 아래와 같이 fruit 딕셔너리가 정의되어 있다.
# 사용자가 입력한 값이 딕셔너리 키 (key) 값에 포함되었다면 "정답입니다"를
# 아닐 경우 "오답입니다" 출력하라.

# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# idx3 = input("단어를 입력해주세요 : ")
# if idx3 in fruit :
#     print("정답입니다")
# else :
#     print("오답입니다")



# 문제 6)
# 사용자로부터 문자 한 개를 입력 받고,
# 소문자일 경우 대문자로,
# 대문자 일 경우, 소문자로 변경해서 출력하라.
# hint -  islower() 함수는 문자의 소문자 여부를 판별합니다.

# letter = str(input("문자 한개를 입력해주세요 : "))
# if letter.islower() == True :
#     print(letter.upper())
# else :
#     print(letter.lower())

# 문제 7)
# 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
# 81~100 A
# 61~80	 B
# 41~60	 C
# 21~40	 D
# 0~20	 E
# 사용자로부터 score를 입력받아 학점을 출력하라.

# score = int(input("score를 입력해주세요 : "))
# if score >= 81 and score <= 100 :
#     print('A')
# elif score >= 61 and score <= 80 :
#     print('B')
# elif score >= 41 and score <= 60 :
#     print('C')
# elif score >= 21 and score <= 40 :
#     print('D')
# else :
#     print('E')


# 문제 8)
# 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
# input number1: 10
# input number2: 9
# input number3: 20

# f = input("숫자를 첫번째로 입력해주세요 : ")
# s = input("숫자를 두번째로 입력해주세요 : ")
# t = input("숫자를 세번째로 입력해주세요 : ")
#
# if f > s and f > t :
#     print(f)
# elif s > f and s > t :
#     print(s)
# elif t > f and t > s :
#     print(t)



# 문제 9)
# 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.
# 번호	통신사
# 011	SKT
# 016	KT
# 019	LGU
# 010	알수없음
# 휴대전화 번호 입력: 011-345-1922

# mobil = input("전화 번호를 입력해주세요 ex)011-345-1922 : ")
# if mobil[0:3] == "011" :
#     print("SKT")
# elif mobil[0:3] == "016" :
#     print("KT")
# elif mobil[0:3] == "019" :
#     print("LGU")
# else :
#     print("알수없음")


# 문제 10)
# 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데 1, 3은 남자 2, 4는 여자를 의미한다.
# 사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.
# >> 주민등록번호: 821010-1635210

# ind = input("주민등록번호를 입력해주세요 ex)821010-1635210 : ")
# if ind[7] == "1" or ind[7] == "3" :
#     print("남자")
# elif ind[7] == "2" or ind[7] == "4" :
#     print("여자")
# else :
#     print("성별인식불가")

# 문제 11)
# 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다.
# 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라
# 지역코드	출생지
# 00 ~ 08	서울
# 09 ~ 12	부산

# acode = input("주민등록번호를 입력해주세요 ex)910000-1000000 : ")
# ccode = acode.split("-")[1]
# if ccode[4] == "0" and (ccode[5] <= "8" or ccode[5] >= "0"):
#     print("서울")
# elif ccode[4] == "0" and ccode[5] == "9" :
#     print("부산")
# elif (ccode[4] == "1" and ccode[5] == "0") or (ccode[4] == "1" or ccode[5] == "1") or (ccode[4] == "1" or ccode[5] =="2") :
#     print("부산")
# else :
#     print("기타")

# 문제 12)
# 어떤 대학교를 졸업하려면 적어도 140학점을 이수해야하고 평점이 2.0은 되어야 한 다고 하자.
# 이것을 파이썬 프로그램으로 검사해보자.
# 사용자에게 이수학점수와 평점을 물어보고 졸업 가능 여부를 출력하는 프로그램을 작성해보자.
#credits = float( input("이수한 학점을 입력하세요 : "))
#avg = float( input("평점을 입력하세요 : "))

# credits = float(input("이수학점을 입력하세요 : "))
# avg = float(input("평점을 입력하세요 : "))
# if credits >=  140 and avg >= 2.0 :
#     print("졸업 가능")
# else :
#     print("학점이 부족하거나 평점이 낮습니다.")

# 문제 13)
# 1부터 10사이의 난수를 생성하고 숫자를 맞춰보자 (정답인 조건문만들기)

# from random import randint
# answer = randint(1,10)
# #print(answer)
# tries = 1

#1 ~ 10사이의 숫자를 입력하세요

# while tries <= 5 :
#     guess = int(input("숫자를 입력하세요 : "))
#     if answer == guess :
#         break;
#     elif answer > guess :
#         print("높은 숫자를 입력하세요")
#     else :
#         print("낮은 숫자를 입력하세요")
#     tries += 1
# if guess == answer :
#     print("정답 시도횟수 : ",tries)
# else :
#     print("정답은 : ", answer)



# 문제 14)
# input()함수를 이용하여 입력받은 숫자가 홀수인지 짝수인지를 판단하는 프로그램을 작성하라.
# 홀수면 '홀수'라고 출력하고 짝수면 '짝수'라고 출력하시오
# +, - , / , * , %(나머지 연산자)

# oh = int(input("숫자를 입력하세요 : "))
# if oh % 2 == 0 :
#     print("짝수")
# else :
#     print("홀수")