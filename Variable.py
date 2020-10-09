# 변수
'''
Python Built-in Types
-Numeric
-Sequence
-Text Sequence
-Set
-Mapping(dict,tuple)
-Bool

변수 지정 방법
- Camel Case : numberOfCollege -> method, function
- Pascal Case : NumberOfCollege -> class
- Snake Case : number_of_college -> method, function
'''
##새로운 파일에서는 Run해서 새로운 스크립트로 지정해줘야함
import keyword  ##R에서 file함수랑 같은기능으로 만들어놓은 모듈가지고 옴
print(keyword.kwlist)  ##파이썬은 대소문자를 구분하는 언어라는 것도 알 수 있음

'''
변수는 숫자로 시작할 수 없고
특수문자_, $
예약어는 변수명으로 사용이 불가하다
'''
year = 2019 # R에서 <-로 변수지정한거와 같음
month = 8
day = 10
print('{}년 {}월 {}일'.format(year,month,day)) ##변수입력
print(type(year), type(month), type(day))  ##타입확인

intValue = 123
floatValue = 3.14159
boolValue = True
strValue = 'jslim'
print(type(intValue), type(floatValue), type(boolValue), type(strValue))

# 형변환 type casting
num_str = "720"
num_num = 100
#print(num_str + num_num)  #문자형+숫자형 연산불가해서 바꿔줘야함
print(int(num_str) + num_num)
print(num_str + str(num_num))

year = "2020"  ##조금전 year변수는 2019라는 숫자형이었는데 바로 str형으로 지정못하고 형변환해야함
# print(year-1)
print(int(year)-1)

# 데이터 타입
str01 = "python"
bool = True
str02 = 'Anaconda'
float = 10.0
#int = 20

list = [str01,str02]  # R에서 리스트랑 비슷
dic = {
    "name" : "Machine Learning",   # 키: 값 으로 직접 설정
    "version" : 2.0
}
tuple = (3,5,7)   # R에서 벡터값입력하는거랑 비슷
set = {3,5,7} # tuple이랑 다름.집합타입변수

print(type(list))
print(type(dic))
print(type(tuple))
print(type(set))

# 키보드 입력
# input()   기본적으로 문자열타입 리턴하기때문에 결과가 숫자가 나와도 숫자형이 아님
# inputNumber = input("숫자를 입력하세요: ")
# print(inputNumber)

# #inputNumber = input("숫자를 입력하세요: ")
# #sum = 100 + inputNumber
# #print(type(set))

# inputNumber = int(input("숫자를 입력하세요: "))
# sum = 100 + inputNumber
# print(sum)

# 파이썬의 문자형(중요)
str01 = "I am Python"
str02 = 'Python'
str03 = """this is a multiline sample test"""
str04 = '''this is a multiline sample test'''
print(str01,str02,str03,str04)


query = '''    # 동적 바인딩
select *
from emp
where deptno = {no}
order by eno desc
'''
print(query)


seqText = "Talk is cheap. Show me the code"
print(seqText)

# dir()
print(dir(seqText))  ##내장함수

# slicing()
print(seqText[3]) #K만 출력
print(seqText[-1]) # R과 다르게 맨뒤에서부터 1자리
print(seqText[0:4]) # [0:3]으로 출력하면 하면 talk가 아니라 tal로 나옴 왜냐면 0:3으로 하면 012까지만 나오게 문법이 만들어짐

str_slicing = "Nice Python"
print(str_slicing[0:4])
print(str_slicing[-6:]) # print(str_slicing[5:])도 가능
print(str_slicing[0:7:2])
print(str_slicing[0:len(str_slicing):2])  ##length는 1부터 셈.하여 11
print()
print(str_slicing[:]) # 전체를 가져옴
print(str_slicing[::2])
print(str_slicing[::-1]) #뒤에서부터 하나씩 가져오겠습니다

#아래 문자열에서 '홀'만 출력하세요
string = "홀짝홀짝홀짝홀짝"
print(string[0:len(string):2])
#아래 문자열을 거꾸로 뒤집어서 출력하세요
string = "PYTHON"
print(string[::-1])
#첫문자를 대문자 만들고 싶다면?
string = "python"
print("Capitalize :",string.capitalize())
# - 문자를 공백으로 치환하고 싶다면?
phone_number = "010-4603-2283"
replace_phone_number = phone_number.replace("-","")
print(replace_phone_number)
# 아래 문자열에서 소문자 a를 대문자로 변경한다면?
string = 'abcdefe2a345a345a'
replace_string = string.replace("a","A")
print(replace_string)
# 아래 문자열에서 도메인만 출력한다면? #split()이용
url = "http://naver.com"
url_split = url.split('.')
print(url_split[-1])

# 좌우공백을 제거할떄  #strip(), rstrip(), lstrip()이용
data = "    삼성전자    "
print(data.strip())
print(data.rstrip())
print(data.lstrip())

#대문자로 바꾸고, 다시 소문자로 변환
ticker = "btc_krw"
upper_ticker = ticker.upper()
print(upper_ticker)
lower_ticker = upper_ticker.lower()
print(lower_ticker)

# endswith() 마지막에 이러한 문자열을 포함하는지 확인하는 함수 -> true / false
file_name = "report.xls"
isExits = file_name.endswith(("xls","xlsx"))
print(isExits)


# split()
string = "삼성전자/LG전자/Naver/Google"
interest = string.split("/")
print(interest)

# in, not in -> True | False
myStr = "This is a sample Text"
print("sample" in myStr)
print("text" not in myStr) # Text는 False지만 대소문자를 구분하기에 True 출력
print("this" in myStr.lower())  #myStr을 소문자로 만들어주고 비교하는거랑 True를 출력

brand_name = "cocacola"
result = len(brand_name) ###브랜드네임 렝스호출
print(result)
result = brand_name.count('c') ###브랜드네임 안에 c가 몇번노출됬는지 카운트
print(result)
result = brand_name.find('o') ###o의 인덱스 리턴, 문자를 못찾으면 음수를 리턴
print(result)
result = brand_name.index('a') ###find같이 인덱스를 찾는건데 문자가 없으면 에러호출
print(result)

#아스키 코드 출력
a = 'A'
print(ord(a))
print(chr(65))

