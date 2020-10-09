# 파이썬 date type

# 날짜

from datetime import date, datetime   # datetime디렉토리에 date와 datetime이라는 파일을 가져오겠다
today = date.today()
print('today - ',today, type(today))
print("년도 : {}, 월 : {}, 일 : {}".format(today.year,today.month,today.day))

# 날짜 및 시간
my_datetime = datetime.today()
print(my_datetime)

# 시분초
print("시 : {}, 분 : {}, 초 : {}".format(my_datetime.hour,my_datetime.minute,my_datetime.second))


from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
# week, days, hours, minutes, seconds사용, 대신 years, months 사용할 수 없음
today = date.today()
days = timedelta(days = -1)
print("하루 전 날짜 : {}".format(today+days))

#days = timedelta(years=-2)

days = relativedelta(months=-2)
print("두달 전 날짜 : {}".format(today+days))

# 특정 날짜 객체를 생성
from dateutil.parser import parse
myDay = parse("2020-08-11") #parse함수이용
print('myDay - ', myDay)

myDay = datetime(2020,8,11) #datetime함수이용
print(myDay)

# strftime(날짜를 문자열형태로 포맷지정)
# strptime(문자열을 날짜로 변환)
today = datetime.today()
print("{}".format(today.strftime("%m-%d-%Y")))
str = "2020, 08, 11-13:14:20"
my_str = datetime.strptime(str,'%Y, %m, %d-%H:%M:%S')  #년도만 4자리라 대문자
print(type(my_str))
print(my_str)