# 파이썬 반복문
# for, while
# for idx in <collection> :
# for idx in range(start, stop, step)

#for idx in range(2,11,2) :
#    print("idx - ",idx)

# scores = []
# for idx in range(5) :   ##range(5)는 5안에서가 아닌 5개
#     scores.append(int(input("성적을 입력하세요 : ")))
##     print(scores)
#
# for idx in scores :
##     print(idx)
#
# for idx in range(len(scores)) :
##     print(scores[idx], "\t", end=" ")

# 입력받은 성적의 총합과 평균을 구하시오
# sum = 0
# for element in scores :
#     sum +=element
# avg = sum / len(scores)
# print("총합은 : {},평균은 : {} 입니다".format(sum,avg))

# 리스트 자료형에 들어 있는 개수를 세어보자 (for 루프를 이용해서 몇번 노출되었는지)
# cnt_list = [1,2,1,2,3,5,7,8,9,6,6,2,5,6,7,5,"",""]
# freq = {}
# for i in cnt_list :
#     if i in freq :
#         freq[i]+=1
#     else :
#         freq[i]=1
# print(freq)

# word_vec = ["corona",
# #             "corona",
# #             "corona",
# #             "love",
# #             "word",
# #             "big","big","big","data","data",
# #             "love","jslim","jslim","seop"]
# freq2 = {}
# for i in word_vec :
#     if i in freq2 :
#         freq2[i]+=1
#     else :
#         freq2[i]=1
# print(freq2)


# 1 - 1000 합(할당연산)
# range_sum = 0
# for value in range(1,1001) :
#     range_sum += value
# print(range_sum)

# 구구단 3단만 출력한다면?
# 홀수번째만 출력한다면?
# dan = 3
# for idx in range(1, 10) :
#     if idx %2 == 1 :
#         print(dan,"*",idx,"=",3*idx)

# my_sum = 0
# my_list = [(1,2),(3,4),(5,6)] #items로 리스트에 튜플이 담긴형태
# for (key, value) in my_list :
#     my_sum +=key+value
# print(my_sum)
#
# my_sum = 0
# my_list = [("name",2),("age",4),("address",6)] #위와 다르게 보통 문자+숫자로 담겼을땐 썸이 안됨
# for (key, value) in my_list :
#     #my_sum +=key+value
#     print("key : {}, value : {}".format(key, value))
# #print(my_sum)
#
# temp_list = [1,2,3,4,5,6,7,8,9]
# score01 = [idx*3 for idx in temp_list]
# score02 = [idx*3 for idx in temp_list if idx % 2 == 0] # temp_list에서 idx를 하나씩 가져와서 리스트를 새로만드는데 거기다 각각 x3을 한 형태 중 짝수형태만 값을 가져오는 스킬
# print(score01)
# print(score02)

#올림픽은 4년마다 개최된다
#2000 ~ 2050년까지 중 올림픽이 개최되는 년도를 출력
# olympic = [idx for idx in range(2000,2051) if idx % 4 == 0]
# print(olympic)

# #강사님답
# for idx in range(2000,2051,4) :
#     print(idx)


# 아래 리스트에서 20보다 작은 3의 배수를 출력하라
# list = [12,21,12,14,30,38,34,18]
# for idx in list :
#     if idx %3 == 0 and idx < 20 :
#         print(idx)

# 아래 리스트에서 세 글자 이상의 문자를 출력하라
# list = ['I','am','study','python','language','!']
# for idx in list :
#     if len(idx) >= 3 :
#         print(idx)

##강사님답
# for value in list :
#     if(len(value) >= 3) :
#         print(value)

# 아래 리스트에서 대문자만 화면에 출력하라
# isupper(), islower()
# list = ['I','A','study','PYTHON','JSLIM','for','if']
# for idx in list :
#     if idx.isupper() == True :
#         print(idx.upper())

# 아래 리스트에서 첫글자를 대문자로 변경하여 출력하라
# list = ['dog','cat','pig','parrot','horse']
# for idx in list :
#     if idx.islower() == True :
#         print(idx[0].upper())

# ##강사님답
# for value in list :
#     print(value.capitalize())

# 아래 리스트에 파일 이름이 저장되어 있다.
# 확장자를 제거하고 파일 이름만 출력하라
# # hint - split(".")
# list = ['greeting.py','ex01.py', 'intro.hwp','bigdata.doc']
# for value in list :
#     print(value.split(".")[0])


# word = "Handsome"
# for idx in word :
#     print('word - ', idx, end = ',')


# my_dict = {"name" : "jslim",
#            "age" : 48,
#            "city" : "seoul"}
# print()
# cnt = 1 ;
# print(len(my_dict.keys()))
# for key in my_dict.keys() :
#     if(cnt == len(my_dict.keys())) :
#         print(key)
#     else :
#         print(key, end = " , ")
#     cnt += 1

#upper()
#전체 문자를 대문자로 출력하라
# fruit_name = 'FineApplE'
# for name in fruit_name :
#     if name.isupper() :
#         print(name, end = "")
#     else :
#         print(name.upper(), end="")

# break, continue
# numbers = [14, 3, 6, 17, 34, 25]
# for num in numbers :
#     if num == 17 :
#         print(num)
#         break  ##break없으면 not found 계속 출력됨
#     else :
#         print("Not Found")
        
# numbers = [14, 3, 6, 17, 34, 25]
# for num in numbers :    # for else 구문도 사용가능.루프가 마지막까지 돌았지만 찾지못했을때 else를 수행하겠다
#     if num == 17 :
#         print(num)
#         break  ##break없으면 not found 계속 출력됨
# else :
#     print("Not Found")


# numbers = [14, 3, 6, 17, 34, 25]
# for num in numbers :
#     if num == 17 :
#         continue
#         print(num)
#     else :
#         print(num)
# else :
#     print("Not Found")


#구구단
# for i in range(2, 10):
#     for j in range(1, 10):
#         print("i : {}, j : {}".format(i,j),end = "\t")
#     print()
#
# ##5단까지만
# for i in range(2, 10):
#     for j in range(1, 10):
#        if i % 5 != 0 :
#             print("{}x{} = {}".format(i,j,i*j), end = "\t")
#     print()
#     if i == 5 :
#         break


# #문장과 단어를 나누어서 저장하고 싶음
# string = \
# """
# 저는 파이썬 강의중인 임섭순 입니다.
# 주소는 광주광역시입니다.
# 나이는 숫자에 불과하지만 성인병이 있네요
# """
# sentences = []
# words = []
# # append() , insert(index, value)
# for s in string.split("\n") :
#     sentences.append(s) #3
#     for w in s.split() :
#       words.append(w)
# print(sentences, len(sentences))
# print(words, len(words))


# #----[실습] 분류정확도
# answer = [1,0,2,1,0]
# predict = [1,0,2,0,0]
# acc = 0
# fit = ""
# for i in range(len(answer)) :
#     fit = answer[i] == predict[i]
#     # print(int(fit, end = "\t"))
#     acc += int(fit) * 20
#
# print("분류 정확도", acc)


# enumerate(고급스킬)
# 반복문 사용 시 몇번째 반복문인지 확인이 필요하다면
# 인덱스번호와 컬렉션요소를 확인할 수 있다
# list = ['SQL', 'R', 'TEXT-MINING', 'DATA-MINING', 'PYTHON']
# for idx,value in enumerate(list) :
#     print("{}번째 인덱스이고 값은 {}".format(idx,value))

#단어의 빈도수 체크하는 방법
# word_vec = ["corona",
#             "corona",
#             "corona",
#             "love",
#             "word",
#             "big","big","big","data","data",
#             "love","jslim","jslim","seop"]
# #word_vec = tuple(word_vec)
# freq = {}
# for i in word_vec :
#     freq[i] = word_vec.count(i)
# print(freq)


# While <expression> :
#       statement
#       증감식             #값이 증가되거나 감소되는것이 안나오면 무한루프를 돌음

# n=5
# while n > 0 :
#     print(n)
#     n = n-1

# a = ['foo', 'bar', 'baz']
# while a :
#     print(a.pop())


# while루프 이용하여 1 ~ 100까지의 합, 5의 배수의 합, 3의 배수이면서 5의 배수가 아닌 합 출력
# cnt = tot = tot2 = tot3 = 0
# while cnt <= 100 :
#     cnt += 1
#     tot += cnt
#
#     if cnt % 5 == 0 :
#         tot2 += cnt
#
#     if cnt % 3 == 0 and cnt % 5 != 0 :
#         tot3 += cnt
# print("1~100까지 합 = %d" %(tot))
# print("1~100까지 5의 배수의 합 = %d" % (tot2))
# print("1~100까지 3의 배수이면서 5의 배수가 아닌 합 = %d" %(tot3))

#
# cnt = 10
# while cnt > 0 :
#     if cnt == 11 :    #cnt가 5일때는 break
#         break
#     cnt -= 1
# else :
#     print('while ~ else')





# ---실습
## 문제 1.
## 10보다 작은 자연수 중에서 3 또는 5의 배수는
## 3,5,6,9가 존재해요! 이것들의 합은 23입니다.
## 1000보다 작은 자연수 중에서 3 또는 5의 배수들을
## 구해서 모두 합하면 얼마인가요?
## 정답 : 233168

# sum = 0
# for idx in range(1,1000) :
#     if idx % 3 == 0 or idx % 5 == 0 :
#         sum += idx
# print(sum)

## 문제 2.
## 알파벳 대소문자로 된 문자열이 주어지면,
## 이 문자열에서 가장 많이 사용된 알파벳이
## 무엇인지 출력하는 프로그램을 작성하시오.
## 단, 대소문자는 구별하지 않아요. 만약 동률이 존재하는 경우
## 알파벳 순으로 제일 앞에 있는
## 문자를 출력하세요.

## 문자열) "This is a sample Program mississippi river"
## 문자열) "abcdabcdababccddcd"

## 정답 :  "This is a sample Program mississippi river" => I
## 정답 :  "abcdabcdababccddcd" => C

sentence = "This is a sample Program mississippi river".upper().replace(" ","")
#sentence = "abcdabcdababccddcd".upper().replace(" ","")

maxCount = 0
maxChar = []

for i in range(65,100):
    if(sentence.count(chr(i)) >= maxCount):
        maxCount = sentence.count(chr(i))
        maxChar.append((chr(i),maxCount))

result = list()

idx = maxChar.pop()
result.append(idx[0])

tmp = maxChar.pop()
while idx[1] == tmp[1]:
    result.append(tmp[0])
    tmp = maxChar.pop()

result.sort()
print("가장 많이 등장한 문자 : {}".format(result[0]))




## 문제 3.
## 로또 프로그램 작성. 5000원으로 로또복권을 5장 자동으로 구매합니다.
## 이번 주 로또 당첨번호를 생성하여 로또 당첨을 확인하세요!
## 쉬운버전으로 먼저 작성합니다.
## 6개 숫자가 다 맞으면 1등, 5개 맞으면 2등으로 처리합니다.즉, 쉬운버전은 보너스 숫자는 없는 것으로 간주합니다.
## 쉬운버전을 해결했다면 보너스 숫자를 이용하여 로또 당첨을 확인합니다.
## 보너스 숫자를 제외한 모든 숫자가 다 맞으면 1등, 보너스 숫자를 포함하여 6개의 숫자가 맞으면 2등, 보너스를 제외하고 5개의 숫자가 맞으면 3등으로 처리합니다.
## 쉬운버전의 출력은 1등 몇개, 2등 몇개, 3등 몇개, 4등 몇개, 꽝 몇개로 출력
## 어려운버전의 출력은 1등 몇개, 2등 몇개, 3등 몇개, 4등 몇개, 5등 몇개, 꽝 몇개로 출력
## 랜덤값을 도출하기 위해서는 다음의 코드를 이용한다.
import random
i = random.randint(1, 100)  # 1부터 100 사이의 임의의 정수
f = random.random()  # 0부터 1 사이의 임의의 float
i = random.randrange(1, 101, 2)  # 1부터 100 사이의 임의의 짝수
i = random.randrange(10)  # 0부터 9 사이의 임의의 정수

myLotto = list()

for i in range(5):
    mySet = set()
    while len(mySet) < 6:
        mySet.add(random.randint(1, 45))

    myLotto.append(mySet)

print(myLotto)  # 로또 5장을 구입했어요!

# 이번주 로또번호
winningNumber = set()
while len(winningNumber) < 7:
    winningNumber.add(random.randint(1, 45))

# 최종 결과
result = list()

for i in myLotto:
    winRank = ""
    if len(i & winningNumber) == 6:
        winRank = "1등"
    elif len(i & winningNumber) == 5:
        winRank = "2등"
    elif len(i & winningNumber) == 4:
        winRank = "3등"
    elif len(i & winningNumber) == 3:
        winRank = "4등"
    else:
        winRank = "꽝!!"
    result.append(tuple([i, winRank]))

print(winningNumber)  # 이번주 로또번호
# 당첨여부 출력
for k in result:
    print(k)

myLotto = list()

for i in range(5):
    mySet = set()
    while len(mySet) < 6:
        mySet.add(random.randint(1, 45))

    myLotto.append(mySet)

print(myLotto)  # 로또 5장을 구입했어요!

# 이번주 로또번호 + 보너스 번호
winningNumber = set()
while len(winningNumber) < 7:
    winningNumber.add(random.randint(1, 45))
bonusNum = 0
while True:
    bonusNum = random.randint(1, 45)
    if bonusNum not in winningNumber:
        break;
print(winningNumber, bonusNum)

# 최종 결과
result = list()

for i in myLotto:
    winRank = ""
    if len(i & winningNumber) == 6:
        winRank = "1등"
    elif (len(i & winningNumber) == 5) and (bonusNum in i):
        winRank = "2등"
    elif (len(i & winningNumber) == 5) and (bonusNum not in i):
        winRank = "3등"
    elif len(i & winningNumber) == 4:
        winRank = "4등"
    elif len(i & winningNumber) == 3:
        winRank = "5등"
    else:
        winRank = "꽝!!"
    result.append(tuple([i, winRank]))

print(winningNumber)  # 이번주 로또번호
# 당첨여부 출력
for k in result:
    print(k)

##### 추가문제
##### 1등에 당첨될려면 평균적으로 얼마만큼의 돈을 투자해야 할까요?
##### 로또 1게임은 1000원입니다.


## 문제 4.
## 어떤 수를 소수의 곱으로만 나타내는 것을 소인수분해라 하고,
## 이 소수들을 그 수의 소인수라고 합니다.
## 예를 들면 13195의 소인수는 5, 7, 13, 29 입니다.

## 600851475143의 소인수 중에서 가장 큰 수를 구하세요.

## 정답 : 6857


## 문제 5.
## 앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이
## 같은 수를 대칭수(palindrome)라고 부릅니다.

## 두 자리 수를 곱해 만들 수 있는 대칭수 중
## 가장 큰 수는 9009 (= 91 × 99) 입니다.

## 세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수를 구하세요

## 정답 : 906609

def check_palindrome(x):
    str1 = str(x)
    tmp = list(str(x))
    tmp.reverse()
    if(str1 == "".join(tmp)):
        return True
    else:
        return False

def calcul_palindrome(x):
    result = list()
    for i in range(pow(10,x),pow(10,x+1)):
        for j in range(pow(10,x),pow(10,x+1)):
            if(check_palindrome(i*j)):
                result.append(i*j)
    return max(result)

print(calcul_palindrome(1))
print(calcul_palindrome(2))
print(calcul_palindrome(3))
print(calcul_palindrome(4))


## 문제 6.
## 1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.
## 그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까?

## 정답 : 232792560

searchNum = 1

while True:
    nCount = 0
    for i in range(1,21):
        if searchNum % i == 0:
            nCount += 1
    if nCount == 20:
        break;
    else:
        searchNum += 1

print(searchNum)


## 문제 7.
## 1부터 10까지 자연수를 각각 제곱해 더하면 다음과 같습니다 (제곱의 합).
## 1**2 + 2**2 + ... + 10**2 = 385

## 1부터 10을 먼저 더한 다음에 그 결과를 제곱하면 다음과 같습니다 (합의 제곱).
## (1 + 2 + ... + 10)**2 = 552 = 3025

## 따라서 1부터 10까지 자연수에 대해 "합의 제곱"과 "제곱의 합" 의
## 차이는 3025 - 385 = 2640 이 됩니다.

## 그러면 1부터 100까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이는
## 얼마입니까?

## 정답 : 25164150

sum_1 = 0
for i in range(1,101):
    sum_1 += pow(i,2)

sum_2 = sum(range(1,101)) ** 2

print("결과는 : {}".format(sum_2-sum_1))


## 문제 8.
## 소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.

## 이 때 10,001번째의 소수를 구하세요.

## 정답 : 104743

def isPrimeNumber(x):
    nCount = 0
    for i in range(1, round((x + 1) / 2)):
        if x % i == 0:
            nCount += 1
        if nCount > 2:
            break;

    if nCount == 1:
        return True
    else:
        return False


# isPrimeNumber(23)

primeCount = 0
checkNum = 1
# while primeCount != 10001:
while primeCount != 10002:
    if (isPrimeNumber(checkNum)):
        primeCount += 1
    checkNum += 1

print(checkNum - 1)

## 문제 9.
## 양의 정수 n에 대하여, 다음과 같은 계산 과정을 반복하기로 합니다.

## n → n / 2 (n이 짝수일 때)
## n → 3 * n + 1 (n이 홀수일 때)

## 13에 대하여 위의 규칙을 적용해보면 아래처럼 10번의 과정을 통해 1이 됩니다.

## 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

## 아직 증명은 되지 않았지만, 이런 과정을 거치면 어떤 수로 시작해도
## 마지막에는 1로 끝나리라 생각됩니다.
## (이런 수들을 우박수 hailstone sequence라 합니다.)

## 그러면, 백만(1,000,000) 이하의 수로 시작했을 때 1까지 도달하는데
## 가장 긴 과정을 거치는 숫자는 얼마입니까?
## 계산 과정 도중에는 숫자가 백만을 넘어가도 괜찮습니다.

## 정답 :
import numpy as np
arr = dict()

for i in range(2, 1000001):
    result = i
    nCount = 0
    while result != 1:
        if result % 2 == 0:
            if result in arr:
                nCount += arr[str(result)]
                break;
            else:
                result = int(result / 2)
                nCount += 1
        else:
            if result in arr:
                nCount += arr[str(result)]
                break;
            else:
                result = result * 3 + 1
                nCount += 1

    arr[str(i)] = nCount + 1

maxValue = max(arr.values())

for key, data in arr.items():
    if (data == maxValue):
        print(key)


## 문제 10.
## 다음과 같은 특성을 갖는 숫자의 개수를 찾는 기능을 구현합니다.
## 입력으로 두개의 숫자( x, y )를 이용합니다.
## - 두 개의 숫자 x와 y를 이용하여,
##   x초과 y미만의 숫자 중 각 자리의 숫자를 모두 더한 값이 5의 배수가
##   되는 숫자를 찾습니다.
## - 숫자들을 모두 찾은 후 해당 숫자가 총 몇 개인지를 출력합니다.

## 예1) 두 개의 숫자 1과 100이 주어졌을 경우,
##      1초과 100미만의 숫자 중 각 자리의 숫자를 모두 더한 값이 5의 배수가
##      되는 숫자를 찾습니다.
##      - 20의 경우 각 자리 숫자를 모두 더한 값이 2이므로, 적합하지 않다.
##      - 23의 경우 각 자리 숫자를 모두 더한 값이 5이므로, 적합하다.
##      [총 개수] 19

## 예2) 두 개의 숫자 5와 500이 주어졌을 경우,
##      5초과 500미만의 숫자 중 각 자리의 숫자를 모두 더한 값이 5의 배수가
##      되는 숫자를 찾습니다.
##      [총 개수] 98

## 입력으로 주어지는 두 개의 수 : 100 10000

## 정답 : 예제의 결과가 출력되도록 코드 작성



## 문제 11.
## 6자리 이상 9자리 미만의 수를 입력으로 사용합니다.

## 수의 중앙을 기준으로 두 개의 수로 분리한 후 큰 수를 선택한다.
## - 수의 숫자개수가 홀수 개인 경우 수의 중앙 숫자를 기준으로
##   왼쪽과 오른쪽 수로 분리
## - 수의 숫자개수가 짝수 개인 경우 수를 반으로 나누어
##   왼쪽과 오른쪽 수로 분리
## 예1) 1234567 -> (123, 567) -> (567)
## 예2) 34217869 -> (3421, 7869) ->(7869)

## 입력으로 제공된 수를 더 이상 두 개의 수로 분리할 수 없을 때까지
## 과정을 반복하여 남은 최종 숫자를 구해 출력한다.
## 예1) 567 -> (5, 7) -> (7)
## 예2) 7869 -> (78, 69) -> (78) -> (7, 8) -> (8)

## 정답 : 예제의 결과가 출력되도록 코드 작성


## 문제 12.
## 입력으로 제공되는 숫자열에서 짝수와 홀수를 추출하여 새로운 숫자열을 생성한다.
## 1) 입력된 숫자열에서 짝수와 홀수를 순서대로 추출한다.
##    [입력] 78235169
##    [짝수 추출] 826
##    [홀수 추출] 73519
## 2) 추출된 짝수의 뒤에 추출된 홀수를 연결하여 새로운 숫자열을 생성한다.
##    [짝수와 홀수 연결] 82673519

## 결과숫자열을 앞에서부터 순서대로 뺄셈 연산 또는 덧셈 연산 한다.
## 숫자열의 앞에서 부터 순서대로 뺄셈 연산한다.
## 단, 앞선 연산 결과가 0 이하이면 그 차례에는 덧셈 연산한다.
## [결과 숫자열] 82673519
## [각 수의 연산 순서와 방법]
##   8 - 2 = 6
##   6 – 6 = 0
##   0 + 7 = 7 (앞의 연산 결과가 0 이하이므로 덧셈 연산한다.)
##   7 – 3 = 4
##   4 – 5 = -1
##  -1 + 1 = 0 (앞의 연산 결과가 0 이하이므로 덧셈 연산한다.)
##   0 + 9 = 9 (앞의 연산 결과가 0 이하이므로 덧셈 연산한다.)
## [연산 결과] 9

## [입력]: 78235169
## [출력]: 9

## [입력]: 693756874
## [출력]: 7

## 정답 : 예제의 결과가 출력되도록 코드 작성
