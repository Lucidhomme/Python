import pandas as pd
data = pd.read_csv("./etc. word/mpg.txt",encoding = 'UTF-8')
# print(data)
# print(data.info())
# print(data.head())

##강사님 답
import mpg as m
from statistics import mean
# exam
# manufacturer,model,displ,year,cyl,trans,drv,cty,hwy,fl,cls
#
mpgList = []
with open('./etc. word/mpg.txt' , 'r') as file :
    file.readline()
    line = file.readline()
    while line != '' :
        data = line.strip('\n').split(',')
        obj = m.Mpg(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10])
        mpgList.append(obj)
        line = file.readline()


# 1. displ(배기량)이 4 이하인 자동차와 5 이상인 자동차 중 
# 어떤 자동차의 hwy(고속도로 연비)가 평균적으로 더 높은지 확인하세요.

# a = data.displ <= 4
# aa = data[a]
# print("배기량 4이하 자동차의 고속도로 연비 평균은 : ",sum(aa.hwy)/len(aa))
#
# b = data.displ >= 5
# bb = data[b]
# print("배기량 5이상 자동차의 고속도로 연비 평균은 : ",sum(bb.hwy)/len(bb))

##강사님 답
def question01():
    displ04 = []
    displ05 = []
    for instance in mpgList :
        if float(instance.getDispl()) <= 4 :
            displ04.append(int(instance.getHwy()))
        if float(instance.getDispl()) >= 5 :
            displ05.append(int(instance.getHwy()))
    print('4 - ' , mean(displ04))
    print('5 - ' , mean(displ05))
    disp4_mean = mean(displ04)
    disp5_mean = mean(displ05)

    if disp4_mean > disp5_mean :
        print('배기량 4의 연비가 더 좋습니다.')
    else :
        print('배기량 5의 연비가 더 좋습니다.')

# question01()

# 2. 자동차 제조 회사에 따라 도시 연비가 다른지 알아보려고 한다. 
# "audi"와 "toyota" 중 어느 manufacturer(제조회사)의 cty(도시 연비)가 
# 평균적으로 더 높은지 확인하세요.

# a = data.manufacturer == 'audi'
# t = data.manufacturer == 'toyota'
# au = data[a]
# to = data[t]
#
# print("audi의 도시 연비 평균은 : ",sum(au.cty)/len(au))
# print("toyota의 도시 연비 평균은 : ",sum(to.cty)/len(to))

##강사님 답
def question02():
    audiCty_list = []
    toyotaCty_list = []
    for instance in mpgList:
        if instance.getManufacturer() == 'audi' :
            audiCty_list.append(int(instance.getCty()))
        if instance.getManufacturer() == 'toyota':
            toyotaCty_list.append(int(instance.getCty()))

    print('audi - ', mean(audiCty_list))
    print('toyota - ', mean(toyotaCty_list))

# question02()

# 3. "chevrolet", "ford", "honda" 자동차의 고속도로 연비 평균을 알아보려고 한다. 
# 이 회사들의 데이터를 추출한 후 hwy(고속도로 연비) 평균을 구하세요.

# c = data.manufacturer == 'chevrolet'
# f = data.manufacturer == 'ford'
# h = data.manufacturer == 'honda'
# ch = data[c]
# fo = data[f]
# ho = data[h]
#
# print("쉐보레의 고속도로 연비 평균은 : ",sum(ch.hwy)/len(ch))
# print("포드의 고속도로 연비 평균은 : ",sum(fo.hwy)/len(fo))
# print("혼다의 고속도로 연비 평균은 : ",sum(ho.hwy)/len(ho))

##강사님 답
def question03():
    chevroletHwy_list = []
    fordHwy_list = []
    hondaHwy_list = []

    for instance in mpgList:
        if instance.getManufacturer() == 'chevrolet':
            chevroletHwy_list.append(int(instance.getHwy()))
        if instance.getManufacturer() == 'ford':
            fordHwy_list.append(int(instance.getHwy()))
        if instance.getManufacturer() == 'honda':
            hondaHwy_list.append(int(instance.getHwy()))
    print('chevrolet - ', mean(chevroletHwy_list))
    print('ford - ', mean(fordHwy_list))
    print('honda - ', mean(hondaHwy_list))

# question03()

# 4. "audi"에서 생산한 자동차 중에 어떤 자동차 모델의 hwy(고속도로 연비)가 
# 높은지 알아보려고 한다. "audi"에서 생산한 자동차 중 hwy가 1~5위에 해당하는 
# 자동차의 데이터를 출력하세요.

# au = data.manufacturer == 'audi'
# audi = data[au]
# print(audi.sort_values(ascending = False,by = 'hwy').head())

##강사님 답

def question04():
    audi_list = []
    fordHwy_list = []
    hondaHwy_list = []

    for instance in mpgList:
        if instance.getManufacturer() == 'audi' :
            audi_list.append(instance)
    # audi_list.sort()
    audi_list.sort(key= lambda object : object.getHwy() , reverse=True)
    cnt = 0
    for i in range(len(audi_list)):
        cnt += 1
        print("model {} , hwy {} ".format(audi_list[i].getModel(),audi_list[i].getHwy()))
        if cnt == 5 :
            break
# question04()


# 5. mpg 데이터는 연비를 나타내는 변수가 2개입니다. 
# 두 변수를 각각 활용하는 대신 하나의 통합 연비 변수를 만들어 사용하려 합니다. 
# 평균 연비 변수는 두 연비(고속도로와 도시)의 평균을 이용합니다. 
# 회사별로 "suv" 자동차의 평균 연비를 구한후 내림차순으로 정렬한 후 1~5위까지 데이터를 출력하세요.

# new = (data.cty + data.hwy)/2
# data['new'] = new
# sv = data['class'] == 'suv'
# su = data[sv]
# ssu = su.groupby(['manufacturer'],as_index = False).mean()
# print(ssu.sort_values(ascending = False, by = 'new').head())

##강사님 답
def question05():
    suv_list = []
    for instance in mpgList :
        instance.Overall = (float(instance.getCty()) + float(instance.getHwy()) ) / 2
        if instance.getCls() == 'suv':
            suv_list.append(instance)
    sorted(suv_list,key= lambda object : object.Overall , reverse=True)
    cnt = 0
    for i in range(len(suv_list)):
        cnt += 1
        print("manufacturer {} , overall {} ".format(suv_list[i].getManufacturer(),suv_list[i].getOverall() ))
        if cnt == 5 :
            break
question05()

# 6. mpg 데이터의 class는 "suv", "compact" 등 자동차의 특징에 따라 
# 일곱 종류로 분류한 변수입니다. 어떤 차종의 도시 연비가 높은지 비교하려 합니다. 
# class별 cty 평균을 구하고 cty 평균이 높은 순으로 정렬해 출력하세요.

# cl = data.groupby(['class'],as_index = False).mean()
# print(cl.sort_values(ascending = False, by = 'cty').head())

# 7. 어떤 회사 자동차의 hwy(고속도로 연비)가 가장 높은지 알아보려 합니다. 
# hwy(고속도로 연비) 평균이 가장 높은 회사 세 곳을 출력하세요.

# hw = data.groupby(['manufacturer'],as_index = False).mean()
# print(hw.sort_values(ascending = False, by = 'hwy').head(3))

# 8. 어떤 회사에서 "compact" 차종을 가장 많이 생산하는지 알아보려고 합니다. 
# 각 회사별 "compact" 차종 수를 내림차순으로 정렬해 출력하세요.

# com = data['class'] == 'compact'
# comp = data[com]
# cnt = comp.groupby(['manufacturer'],as_index = False).count()
# print(cnt.sort_values(ascending = False, by = 'class'))


#시험문제
'''
type()
abc+3
[1,2,3,[4]]
%
bestteacher(teacher)
__init__
list(중복허용타입)
tuple(immutable타입)
bool(0)
def multi(*p) 가변인자 튜플인거
['b','c','e','h'
딕셔너리에 특정한 키 데이터 삭제는? del
크롤링할때 알필요없는거? 프레임워크
rvest? r셀레늄?(웹크롤링할때 필요한 패키지)
#tbody(id='tbody')로 찾는거
.contents(class = contents)로찾는거
json
웹스크래핑시 HTML태그를 읽어올때 필요한 기술 아닌거
+++실습 5번까지
'''