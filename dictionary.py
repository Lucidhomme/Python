# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용되는 타입
# key와 value의 대용관계 type
# 순서 X, key 중복 X, 수정 O, 삭제 O
# {}
# class란 실세계(오브젝트)의 명사,동사적인 특징들을 추상화시키는 것, 즉 프로그램 내 인스턴트(객체)를 추출하는 템플릿이다
# class는 틀이고 인스턴스는 틀에의해 만들어지는 결과물.하여 instance.class()로 표현

#temp = {}
#print(type(temp))

dic01 = {'name' : 'seop',
         'age' : 48,
         'address' : 'seoul',
         'birth' : '730919',
         'gender' : True}
#print('dic - ',dic01,type(dic01))
#print(dir(dic01))  #iter가 있으므로 순환반복가능

# key 유무를 판단하기 위해서
#print('name' in dic01)

# 요소를 추가하는 방법
#dic01['marriage'] = False
#print(dic01)

#dic01['marriage'] = True
#print(dic01)

# 데이터 확인
#print("데이터 확인 - ",dic01['birth'])

#개발자성향에 따라 데이터를 리스트하여 관리하기도함, 각각의 값들은 튜플 이용
dic02 = dict( [('name' , 'seop'),
               ('age' , 48),
               ('address' , 'seoul'),
               ('birth','730919'),
               ('gender' , True)]  )
#print("tuple을 이용한 dict 생성 -",dic02)

#변수에다 값을 할당하는 방법
dic03 = dict( name = 'seop',
              age = 48,
              address = 'seoul',
              birth = '730919',
              gender = True)


#출력
#print('dic03 -',dic03['Name']) #키값을 이용, 대소문자 Name때문에 오류남
#print('dic03 -',dic03.get('Name')) #함수를 이용, 해당하는 밸류를 가져오는 것이라 Name에 담긴 값들이 없어서 None을 출력

#print('len - ', len(dic03))

# dict_keys(키), dict_values(값), dict_items(키와값)
#print('dict_keys -',list(dic03.keys()))  #각각의 키들은 리스트, 루프를 돌려서 값들을 꺼내올 수도 있다, 리스트화 시킬수도 있음
#print('dict_values -', list(dic03.values())) #밸류도 키와 마찬가지로 각각의 값 리스트
#print('dict_items -',list(dic03.items()))

# for key in dic03.keys() :
    # print("{0},{1}".format(key,dic03[key]))
    # print("key : {0}, value : {1}".format(key,dic03.get(key)))
# for value in dic03.values() :
#     print(value)

# 튜플 패킹 & 언패킹
#t = ('foo','bar','baz','qux') ##괄호형 쳐주고 선언하는 것,패킹
#print(type(t))
#(x1,x2,x3,x4) = t  ##다른변수에 담을때 언패킹해서 담아준다(괄호형은 보기편하게묶은것), 언패킹할때 튜플에 있는 값들의 개수가 담을 변수의 개수에 맞게 선언이 되어있어야함
#(x1,x2,x3,x4) = ('foo','bar','baz','qux')
#print(x1,x2,x3,x4)

a, *b, c = (0,1,2,3,4,5)  #언패킹할때 개수가 안맞을때 *를 사용하여 처리할 수도 있음, 보통 *이 하나만 나오는 경우가 많음
#print(a)
#print(b)
#print(c)

#for (key , value) in dic03.items() :
#    print("key : {0}, value : {1}".format(key,value))


# 삭제 pop(), del
#del dic03['gender']
#print(dic03)

#print('pop -', dic03.pop('birth'))
#print('dic03 - ',dic03)

#dic03.clear()
#print('dic03 - ', dic03)