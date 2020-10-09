# service-file패키지 밑에 csv_excel모듈생성, 파이썬베이스에 csv_excel_caller모듈생성
# word패키지밑에 service_bmi압축해제

# CSV, Excel input / output
import pandas as pd
# data = pd.read_csv("../../etc. word/service_bmi.csv",encoding = 'UTF-8')
# print(data.info())
# print(data.head())
# print(data.tail())


def load_csv(filePath):
    data = pd.read_csv(filePath, encoding = 'UTF-8') ##파일패키지안에서 호출할때는 ("../../etc. word ~이고 , 콜러에서 호출할때는 "./로시작)
    service_bmi(data)

def service_bmi(data) :
    # displayInfo(data)
    # 컬럼의 정보를 확인하고 싶다면
    # height = data.height
    # height = data['height']
    # print(height)
    # print('type - ', type(height))
    # 키와 몸무게의 평균
    # print('height mean - ',sum(data.height)/ len(data.height))
    # label 컬럼을 활용하여 빈도수를 출력하는 로직을 만들어본다면?
    # 출력예시) {thin : 100개, normal : 50개, fat : 200개}
    labelFreq = {}
    for key in data.label :
        labelFreq[key] = labelFreq.get(key,0) + 1 #키의 값이 없으면 0이고 키값을 찾았으면 +1씩
    print(labelFreq)


def displayInfo(data) :
    print("head")
    print(data.head())

from statistics import mean
def load_xls():
    kospi = pd.ExcelFile('./etc. word/sam_kospi.xlsx')
    kospi = kospi.parse("sam_kospi")
    # print(kospi.info())
    # print(kospi.head())
    print('High - ', mean(kospi.High))
    print('Low - ', mean(kospi.Low))


'''
네트워크 상에서 표준으로 사용되는 파일 형식
{key : value, key : value}
{key : value, key : value}
...
json -> python(dict, list) : decoding
json <- python(dict, list) : encoding
import json
'''

import json
def load_json() :
    dic = {'id' : 'jslim', 'pwd' : 'jslim'}
    print(type(dic))
    # dic -> json(인코딩)
    jsonDic = json.dumps(dic)
    print(type(jsonDic))
    print(jsonDic) #딕셔너리로 나오지만 타입은 딕셔너리가 아님.str으로 변환됨
    # print(jsonDic.id)
    pyobj = json.loads(jsonDic)
    print(type(pyobj))
    print(pyobj['id'],pyobj['pwd'])

def json_load_file() :
    with open('./etc. word/usagov_bitly.txt','r',encoding='utf-8') as file :
        lines = file.readlines()
        # print(type(line))
        # print(len(line))
        # print(type(line[0]))

        rows = [json.loads(line) for line in lines]  #개발자방식
        print(type(rows))
        print(rows[0]['a'])

        # list = []
        # for dic in line :
        #     pyobj = json.loads(dic)
        #     list.append(pyobj) #list형식으로 담는다
        # print(list[0]['a'])

        jsonDF = pd.DataFrame(rows)
        print(jsonDF.head())