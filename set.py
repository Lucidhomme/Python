# 집합(Set)
# 순서 X, 중복 X
# set()
# {value, value, ~~~}

#temp = set()
#print( type(temp))
#temp = {'jslim', 'teacher'}
#print( type(temp))

#b = set([1,2,3,4,5,5,5,5,5])  #집합에서 리스트형식으로 담아야 셋으로 정의가됨
#print(type(b),b)
#c = set([1, 3.14, 'Pen', False])
#print(c)
#t = tuple(c)
#print('casting - ',t, t[1:3])


s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

# 교집합 : &,intersection()
#print('& - ',s1&s2)
#print('& - ', s1.intersection(s2))

# 합집합 : |, union()
#print('OR - ',s1|s2)
#print('OR - ', s1.union(s2))

# 차집합 : -, difference()
#print('MINUS - ',s1 - s2)
#print('MINUS - ',s1.difference(s2))


s1.add(7)
print(s1)
s1.remove(7)   ##없는 데이터를 삭제하려고 하면 오류를 뱉어냄.discard함수를 쓰는게 오류가 나지않음
print(s1)
s1.discard(9)
print(s1)


#중복제거(핵심)
#gender = ['남','여','남','여','남','여']
#print(gender)
#sgender = set(gender)
#print(sgender)
#lgender = list(sgender)
#print(lgender)
#print(lgender[0])
#print(lgender[1])

#print(dir(s1)) #iter확인, set도 루핑은 가능하다
#for idx in s1 :
#    print(idx, end="")