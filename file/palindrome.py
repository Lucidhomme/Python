# 서비스패키지 밑 파일 패키지 밑 palindrome모듈생성, 파이썬 베이스밑에 palindrome caller모듈 생성
# 회문(palindrome)
# 단어를 거꾸로 읽어도 제대로 읽는 것과 같은 단어 또는 문장
# level, sos, rotator, 'nurses run'
# 기준점이 필요하다. 첫 글자와 마지막 글자를 비교
# 반복문
# //

# str = 'jslim9413'
# idx = len(str) // 2
# print(str[idx])

# 특정단어가 들어 왔을 때 이 단어가 회문인지 아닌지 검사하는 함수
def isPalindrome():
    word = input("단어를 입력하세요 : ")
    isFlag = True
    for i in range(len(word) // 2 ) : #// 실수자리 두자리
        if word[i] != word[-1 -i] :
            isFlag = False
            break
    return isFlag

def reversePalindrome() :
    word = input("단어를 입력하세요 : ")
    # print(word == word[::-1])
    # print( type(reversed(word)) )
    # print(list(reversed(word)))
    if list(word) == list(reversed(word)) :
        print(True)
    else :
        print(False)

#단어가 줄단위로 저장된 파일에서 회문인 단어를 각 줄에 출력하라. 단) 파일에서 읽은 단어는 \n이 붙어 있으므로 \n을 제외한 뒤 회문인지를 판단하여야 함. 단어사이 줄 바꿈이 두번일어나면 안됨

def reverse_check() :
    with open('./etc. word/palindrome_words.txt', 'r') as file :
        for i in file :
            i = i.strip('\n')
            if list(i) == list(reversed(i)) :
                print(i)

##강사님답
def palindromeExc():
    with open('./etc. word/palindrome_words.txt', 'r') as file :
        for line in file :
            line = line.strip('\n')
            if line == line[::-1] :
                print(line)

# N-gram
# hello 문자단위로 추출한다면?
# he / el / li / lo
# 0 1 2 3 4
# h e l l o
# text = 'hello'
# for i in range(len(text)-1) :
#     print(text[i], text[i+1], sep = "")

# 공백을 기준으로 문자열을 분리한다면 타입은??
# 리스트 - 정답입니다
# 리스트 2-gram 현재문자와 다음 문자를 출력하고 싶다면?

# text = 'this is python script'
# words = text.split()
# for i in range(len(words) -1) :
#     print(words[i], words[i+1])

#zip()
number = [1,2,3,4]
name = ['a','b','c','d']
# number_name = dict(zip(number, name))
# print(number_name)

# dic = {}
# for number, name in zip(number, name):
#     dic[number] = name
# print(dic)

# a = 'lim'
# b = [1,2,3]
# c = ('one','two','three')
# print(list(zip(a,b,c)))
# print(dict(zip(a,b)))
# print(set(zip(a,b,c)))



# input 함수를 이용해서 문자열이 입력되고
# 예시) Python is a programming language that lets you work quickly
# gram 할 숫자도 input 함수를 이용하여 입력받아
# 예시) 3
# 입력된 숫자에 해당하는 단어 n-gram을 튜플로 출력하라
# 단) 입력된 문자열의 단어개수가 입력된 정수미만이라면 예외를 발생시키고 처리한다
def zipNgram():
    n = int(input("gram : "))
    text = input("sentences : ")
    words = text.split()
    try :
        if (len(words) < n ) :
            raise Exception('문장의 길이가 더 길어야 합니다')
        else :
            for i in range(len(words) - n + 1) :
                print(words[i:i+n])
    except Exception as e:
        print(e)

