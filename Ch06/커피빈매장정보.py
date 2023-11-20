import requests
from bs4 import BeautifulSoup #html 구문분석라이브러리
locate = ('서울','경기','인천','강원','경남','광주','대전','대구','부산','제주','충남','충북')
#result = {}
result2 = []
for local in locate:
    url = 'https://www.coffeebeankorea.com/store/store_data2.asp?lat=&lng=&chk1=0&chk2=0&chk3=0&chk4=0&chk5=0&chk6=0&chk7=0&chk8=0&chk9=0&chk10=0&chk11=0&chk12=0&chk13=0&keyword=&StoreLocal='+local+'&StoreLocal2=&storeNo='
    html_str = requests.get(url).text
    bs = BeautifulSoup(html_str,"html.parser")
    name_index = []

    for data in bs:
        sp = str(data).split("'")
        isName = False
        isTime = False
        name = ""
        time = ""
        for i in sp:
            if isName:
                name = i
                isName=False
            if isTime:
                time = i
                isTime=False
            if i == ", StoreName : ":
                isName = True
            if i == " , StoreOpendate : ":
                isTime = True
            if name != "" and time != "":
                #result[name] = time
                result2.append(name)
                result2.append(time)
                name = ""
                time = ""
    
# for name, time in result.items():
#     print("{} : {}".format(name,time))
#혹시나 매장명 겹칠까봐 리스트로 바꿈
print("총 매장 수",len(result2)//2)
for i in range(0,len(result2),2):
    print(result2[i],":",result2[i+1])
