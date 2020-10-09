# 주석문
'''
멀티라인 주석가능
'''
## shift + f10은 모듈전체를 실행, alt+shoft+f10은 블럭씌운것만 실행
#print : 자동개행
print('Python Start')
print("Python Start")

#"""""" : 코드작성한 방식대로 출력문장 개행
print("""우리는 UI시각화 기법 및 데이터 분석을 배우는 과정입니다.
글서 파이썬을 공부하고 있습니다.""")

#"", '' 모두 문자열 데이터를 담을 수 있음
print("Seop's Python")
print('Speak Out. ~ "Student" ')
print('오늘은','월요일','이고 파이썬 첫날입니다')
print()

# print option
# end옵션 , Separate 옵션
print('P','Y','T','H','O','N', sep='')
print('010','4603','2283',sep='-')
print('jslim9413','naver.com',sep='@')

print('Welcome To ', end = ' ')
print('BigData News', end=' ')
print('Web Site')

print()
# format 사용(d,s,f)
# %, {}
print('%s %s'%('one','100'))  ##문자열 2개를 쓰겠고 하나는 원, 하나는 투
print('{} {}'.format('one','two'))
print('{1} {0}'.format('one','two')) ## 파이썬은 첨자번 0부터 시작하므로 첫번째 자리는 투가 나오고 두번째 자리는 원이나옴

print()
#자리수 지정
print('%10s'%'seop') # 자리는 10자리 확보하고 seop4자리만 확보
print('%-10s'%'seop')
print('%5s'%'pythonGood') ##파이썬은 5자리만 확보했어도 무시하고 출력함

# %d
print()
print('%4d' % 100)
print('%f'% 3.14159)
print('%1.2f' % 3.14159) #1.2f : 정수 1, 실수 2자리