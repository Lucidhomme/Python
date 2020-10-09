'''
텍스트 파일 입출력
open(file = "파일경로/파일명 , mode = "") ex)절대경로 또는 상대경로 c:\\, c:\, ..\(디렉토리수에 따라 다름)"
mode = r / w / a / wb
'''

def filewrite(fileName, mode):    #한줄로밖에 안됨
    file = None
    try :
        if mode == 'w' :
            file = open(fileName,mode)
            file.write('Heloo~, Seop')
        elif mode == 'r':
            file = open(fileName, mode)
            line = file.read() #한꺼번에 읽음
            print('result read - ', line)
        else :
            file = open(fileName, mode)
            file.write('\n Seop append')

    except ValueError as verr :
        print(str(verr))
    finally :
        if file != None :
            file.close()
    print('close function')

#자동으로 클로즈시키는 구문
def withFile(fileName, mode) :
    with open(fileName, mode) as file :
        line = file.read()
        print(line)

#여러줄 생성
def withMultiwriteFile(fileName, mode) :
    with open(fileName, mode, encoding = 'utf-8') as file:
        for text in range(3) :
            inputMsg = input("문자열을 입력하세요 : ")
            file.write('{}\n'.format(inputMsg))

def WithListFile(fileName, mode, list):
    with open(fileName, mode, encoding = 'utf-8') as file :
        # file.writelines(list) 여러줄 생성하는 함수
        for text in list :
            file.write(text)

def withListReadFile(fileName, mode) :
    with open(fileName, mode, encoding = 'utf-8') as file:
        line = None
        while line != '':
            line = file.readline() # 한줄씩 리딩
            print(line.strip('\n')) #내가 개행시킨거 이외에 자동으로 개행된 부분이 있어 띄어쓰기 되서 출력되는 부분을 제거함
        for line in file :
            print(line.strip('\n'))

#단어가 줄 단위로 저장된 cnt_words.txt 파일로부터 10자 이하인 단어의 개수를 카운팅 해본다면?
def cntFunction() :
    with open('../../etc. word/cnt_words.txt', 'r') as file : #경로는 파이썬 베이스기준
        cnt = 0
        for text in file :
            if len(text.strip('\n')) <= 10 :
                cnt += 1
    print("10자 이하의 단어의 수 {}".format(cnt))


#문자열이 저장된 special_words.txt 파일에서 문자 'c'가 포함된 단어를 각 줄에 출력하는 프로그램을 만들어보자
#단어를 출력할때는 등장한 순서대로 출력하며, .은 출력하지 않는다

def cwords() :
    with open('../../etc. word/special_words.txt', 'r') as file :
        words = file.read().split()
        for word in words :
            if 'c' in word :
                print(word.strip(',.'))

# zipcode.txt 파일을 이용하는 문제이다. input함수를 이용해 동 이름을 입력 받아 ex)개포 해당하는 동 주소를 출력하는 함수를 정의한다면?
# hint 한줄씩 읽어서 tab키로 분리하고, startwith()함수를 이용하여 처리
try :
    dong = input("동을 입력하세요 : ")
    f = open(file ="../../etc. word/zipcode.txt", mode ='r', encoding ='utf-8')
    line = f.readline()
    while line :
        addr = line.split(sep='\t')
        if addr[3].startswith(dong) :
            print('['+addr[0]+']',addr[1],addr[2],addr[3],addr[4])
        line = f.readline()
except Exception as e :
    print('예외 발생 : ', e)
finally :
    f.close






