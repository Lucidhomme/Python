# 파이썬 리스트(자료구조에서 중요)
# 파이썬에는 배열 존재하지 않음
# 1차원 자료구조로써 R의 Vector 개념
# 순서, 중복, 수정, 삭제 가능
# Index 사용 : 0 ~
# []이용하여 변수를 선언할 수 있다.

# 선언
a = list()
a = []
a = [1,2,3]
a = [1,2,"hello",3,4,True]
a = [1,2,["show","me","the","money"],3.14]
print(a, type(a))

# 슬라이싱 가능
print(a[0])
print(a[-1])
inner_list = a[2]
print(inner_list[1]) # = print(a[2][1])과 같은 결과
print(a[2][2:])
print(a[2][-1])

# list 연산가능 (길이 같지않아도됨)
a = [1,2,3]
b = [4,5,6]
print(a + b)  #(결합형태)
c = a + b
print(c, type(c))

print("*"*50) # 아스테리스크 50번
a = [1,2,3,]
print(a*3)

a = [1,2,3]
a[0] = 5  # 기존숫자없어짐
print(a)

a.append(4) #기존숫자는 살리고 새로운 값에 맞추어 순서만 밀리게 하고싶을때.근데 어펜드는 마지막 인덱스에만 추가할 수 있음
print("append 4 : ", a)
a.insert(0,6) #0번째에 6을 넣겠다.인서트는 내가원하는 인덱스 위치에 넣을 수 있음
print("insert 6 : ",a)

a.sort() #오름차순
print(a)
a.reverse() #내림차순
print(a)

# pop() : 기존 리스트에서 원소를 가져오고 삭제시킨다.
print("a - pop() : ", a.pop())  #가장 마지막에 들어오는거부터 꺼내고
print("a - print : ", a)  #꺼낸거는 사라짐

ex = [4,3]
a.extend(ex) # 추가하는 함수로 중복가능하다
print("a - print : ", a)


# ------------실습1
movie_rank = ["강철비2","반도","다만 악에서 구하소서","인셉션"]
# 1. 해당리스트에 배트맨을 추가하세요
movie_rank.append("배트맨")
print(movie_rank)

# 2. "강철비2"와 "반도" 사이에 "슈퍼맨"을 추가
movie_rank.insert(1,"슈퍼맨")
print(movie_rank)

# 3. 리스트에서 "인셉션"을 삭제
# 삭제시에 del 명령어를 이용해서 해당 인덱스를 제거할 수 있다
del movie_rank[4]
print(movie_rank)

# 4. 리스트에서 "다만 악에서 구하소서"와 "배트맨"을 삭제
del movie_rank[3:5]
print(movie_rank)


##인덱스를 찾을떄(데이터많을때는 순서찾기힘듬)
movie_rank = ["강철비2","반도","다만 악에서 구하소서","인셉션"]
idx = movie_rank.index("다만 악에서 구하소서")
print(idx)
del movie_rank[idx]
print(movie_rank)

#pop를 이용해 마지막이 아닌 특정 단어 제거하고 싶을때
movie_rank2 = ["강철비2","반도","다만 악에서 구하소서","인셉션"]
idx2 = movie_rank2.index("다만 악에서 구하소서")
print(idx2)
print(movie_rank2.pop(idx2))
print(movie_rank2)


#-----------실습2
#다음 리스트에서 최댓값과 최솟값 및 총합, 평균을 출력하라(힌트 : min(),max() 함수 사용)
nums = [1,2,3,4,5,6,7]
print(min(nums))
print(max(nums))
print(sum(nums))
print(sum(nums)/len(nums))

#리스트에 저장된 데이터의 개수를 화면에 구하여라
cook = ["피자","김밥","만두","양념치킨","족발","피자","김치만두","쫄면","소세지","라면","팥빙수","김치전"]
print(len(cook))

#price 변수에는 날짜와 종가정보가 저장되어있다.날짜 정보를 제외하고 가격정보만을 출력하라.(힌트 : 슬라이싱)
price = ['20180728',100,130,140,150,160,170]
print(price[1:6])

#슬라이싱을 사용해서 홀수,짝수를 출력하라
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[0::2])
print(nums[1::2])

#슬라이싱을 사용해서 리스트의 숫자를 역방향으로 출력하라
nums = [1,2,3,4,5]
#print(nums[::-1])
#print(nums.reverse())
nums.sort(reverse = True)
print(nums)

#interest 리스트에는 아래의 데이터가 바인딩되어 있다. 삼성전자 네이버만 출력하라
interest = ['삼성전자','LG전자','Naver']
print(interest[0],interest[2])

#join()
interest = ['삼성전자','LG전자','Naver','SK하이닉스','미래에셋']
print(interest, type(interest))
#공백으로 연결된 출력
print(" ".join(interest),type(interest))
print("\n".join(interest))

# python sequence type range()
# range() : 숫자 sequence 주로 for ~ 사용
range_01 = range(10)
print("range - ", range_01)
range_02 = range(1,11,2)
print("range - ", range_02)
print(11 in range_02)
print(10 in range_01)

for idx in range(10) :
    print(idx)
