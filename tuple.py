# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서 o, 중복 o, 수정 X, 삭제 X)
# 불변(immutable)
# 읽기 전용
# ()

my_tuple = ()
movie_rank = ("반도","강철비2","아이언맨")

test_tuple = (1,) #요소가 하나일때는 반드시 컴마찍어야 됨.안찍으면 인트형으로 인식할수도 있기때문
print("tuple type - ",type(test_tuple))

# 사용자 편의를 위해서 괄호없이 만들 수 있다
test_tuple = 1,2,3,4,5
print(test_tuple,type(test_tuple))

multi_tuple = (100,1000,'Ace','Base','Captine')
print('tuple print -',multi_tuple)

# 인덱싱
print(">>>>>>>>>>>>>>>>>>>>>튜플 인덱싱")
print("index 1 - ",multi_tuple[1])
print("index 1 - ",multi_tuple[0]+multi_tuple[1])
print("slicing - ",multi_tuple[2:5])

print(type(multi_tuple[2:5] ) )
list = list(multi_tuple[2:5]) ##수정,추가,삭제가 안되니까 리스트로 형변환하는게 편함
casting_tuple = tuple(list) ##리스트를 다시 튜플로 바꾸는건 튜플만 씌워주면됨
print(casting_tuple)

# 1 ~ 99까지의 정수 중 짝수만 저장된 튜플을 생성한다면?
even = tuple(range(2,100,2))
print(even)

# 보통 튜플보다는 리스트랑 딕셔너리 많이사용
