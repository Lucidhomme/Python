# 파이썬 boolean
# True | False

a = 5
b = 0

print('&',a & b) #이진수 0101 & 0000의 비트연산 => 0이나옴
print('bool',bool(a & b)) # 0을 False로 바꿔주고있음
print('bool',bool(1)) # 비어있는거 전부 False, 채워져있으면 True

print('bool(1,2,3)',bool((1,2,3)))
temp = {} # temp = {"key" :"value"}로 출력해도 bool {} True 나옴 
print('bool {}', bool(temp))

print('bool not', bool(not 0))

trueFlag = True
falseFlag = False
print(int(trueFlag))
print(int(falseFlag))

print("&", trueFlag & falseFlag)
print("|", trueFlag|falseFlag)

print("and", trueFlag and falseFlag)
print("or", trueFlag or falseFlag)

print(not trueFlag)