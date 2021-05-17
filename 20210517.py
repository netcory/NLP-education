#!/usr/bin/env python
# coding: utf-8

# ## request 함수의 사용법

# In[ ]:


import requests


# In[18]:


resp = requests.get("https://naver.com")
resp

#응답이 2XX 라는 건 성공


# In[24]:


resp2 = requests.request("get", "https://naver.com") # 위랑 같은 코드
resp2


# In[25]:


resp3 = requests.get("https://naver.com", params={'query': '무역전쟁'})
#리스폰스3 는 파라미터를 줘서 호출함
resp3


# In[28]:


resp.text

#리스폰스의 Body 호출


# In[32]:


resp3.headers
#리스폰스3의 헤더 호출


# In[34]:


resp.content

#resp.text와 resp.content는 첫글자 빼고 같은 결과
#resp.text는 말 그대로 텍스트로 호출
#resp.content는 b' 가 붙었음. 이건 binary 로 호출한 것
#예를 들어 이미지, 음악 파일 등 받아야할 때는 content로 받을 필요 있음


# In[36]:


resp.encoding

#대체로 UTF-8인데 가끔 한국 사이트에 euc-kr이 있을 수 있음


# In[38]:


resp.status_code


# In[39]:


resp.headers


# In[40]:


resp.url


# In[41]:


resp3.url
#리스폰스3는 호출할 때 파라미터를 넣었었음
#따라서 호출 결과에 query가 있음


# ## parsing
# ## 응답으로 온 자료의 구문 분석

# In[ ]:


#응답 형태가 json 인 경우 resp.json() 입력해야 하고 xml인 경우 BeatuifulSoup 설치 필요
#아나콘다 네비게이터, study 가상환경에 설치
#BeautifulSoup 사용법은 https://www.crummy.com/software/BeautifulSoup/bs4/doc/


# In[43]:


import requests
from bs4 import BeautifulSoup
#BeautifulSoup의 대문자 구성으로 보아 얘는 클래스임을 예상 가능


# In[44]:


soup = BeautifulSoup(resp.text)
#리스폰스 바디를 BeautifulSoup으로


# In[47]:


print(soup.prettify())
#별로 쓸 일은 없음


# In[48]:


#HTML Tags <>꺽쇠로 구성. 속성을 담을 수 있다.
#div. 블럭 단위 구분
#ul / ol. 리스트
#a(href). 중요! 앵커 태그(링크 태그). 하이퍼레퍼런스: 이쪽을 참조해주세요.
#img(src). source의 약자. 중요! 이미지 태그. 


# In[50]:


soup.title
#해당 URL의 제목 호출 (크롬 탭에 뜨는 제목과 일치)


# In[52]:


type(soup.title)
#데이터 타입은 클래스임을 확인 (BeautifulSoup에서 만든 Tag라는 클래스)


# In[53]:


soup.a


# In[55]:


soup.a.attrs
#a 태그의 속성 호출. 결과는 딕셔너리


# In[57]:


soup.a.attrs['href']


# In[58]:


soup.a.get('href')


# ## find

# In[65]:


a_link = soup.find('a') #태그 a를 찾겠습니다. find 사용시 '속성'과 같이 찾을 수 있음
a_link


# In[66]:


gnb = soup.find('div', id = 'gnb')
gnb


# In[67]:


a_list = gnb.find_all('a')
a_list


# In[68]:


type(gnb)


# In[70]:


type(a_list)
#ResultSet은 List와 같다고 봐도 무방


# In[73]:


a_list[3]
#리스트처럼 인덱스로 접근 가능


# In[74]:


a_list.find('a')
#안됨


# In[75]:


a_list[0].find('a')
#이건 됨


# ## find_all with attrs

# In[78]:


gnb.find_all('a', class_ = 'nav')
#태그 a 중 class='nav'인 것만 호출
#class 가 이미 파이썬의 예약어이므로 class_ 라고 언더바 하나 붙여줌


# In[80]:


a_tags = soup.find_all('a')
len(a_tags)
#이 문서안에 a태그 검색


# In[81]:


a_tags2 = soup.find_all('a', recursive=False)
len(a_tags2)


# ## descendatns - 자손들(generator), parent, parents

# In[86]:


gnb.descendants


# In[87]:


for i in gnb.descendants:
    print(i)
    print("-" * 10)


# In[89]:


gnb.parent
#부모 태그 호출


# In[90]:


gnb.parents


# ## 네이버에서 '스타벅스' 검색했을 때 뜨는 결과에서 뉴스 탭,
# ## 제일 처음 뜨는 뉴스 10개의 링크와 제목 가져오기
# ## "title": '~~~',
# ## 'url': '~~~' 와 같이 딕셔너리로 이루어진 리스트의 형태로 가져오기

# In[ ]:


## 네이버에서 '스타벅스' 검색했을 때 뜨는 결과에서 뉴스 탭,
## 제일 처음 뜨는 뉴스 10개의 링크와 제목 가져오기
## "title": '~',
## 'url': '~' 와 같이 딕셔너리로 이루어진 리스트의 형태로 가져오기
## 심화 : 타이틀 밑에 약간의 본문, 이미지까지 가져오고 뉴스 5페이지 범위까지 가져오기
## 심화2 : 최신순, 오래된순 으로
## 이미지를 컴퓨터에 다운로드까지


# In[99]:


import requests

starbucks = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%8A%A4%ED%83%80%EB%B2%85%EC%8A%A4")

from bs4 import BeautifulSoup

soup = BeautifulSoup(starbucks.text)
title_list = soup.find_all('a', class_ = 'news_tit')
dsc = soup.find_all('div', class_ = 'news_dsc')
img = soup.find_all('img', class_ = 'thumb api_get') #api_get 으로만 찾는게 엄밀히 맞음
#html에서 클래스 여러개 엮을 때 띄어쓰기로 엮음
#대신 thumb으로 검색하는 건 나오는 개수 보면 아닌 걸 알 수 있음

a = []

for i in range (10):
    
    title = title_list[i]['title']
    url = title_list[i]['href']
    description = dsc[i].text
    img = soup.find_all('img', class_ = 'thumb api_get')
    img
    
    a.append({'title' : title_list[i]['title'], 'url' : title_list[i]['href'], 'dsc' : dsc[i].text, 'image' : img[i]['src']})
             
print(a)


# In[98]:


## 강사님 버젼

resp = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%8A%A4%ED%83%80%EB%B2%85%EC%8A%A4")

soup = BeautifulSoup(resp.text)
list_news_ul = soup.find('ul', class_ = 'list_news')
#찾는 방법은 다 다를 수 있음

news_list = list_news_ul.find_all('li', class_ = 'bx')

result_list = []
for news_item in news_list:
    a_tag = news_item.find('a', class_ = 'news_tit')
    desc_tag = news_item.find('div', class_ = 'dsc_wrap')
    result_list.append({
        'title' : a_tag.text,
        'url' : a_tag.get('href'),
        'desc': desc_tag.text
    })
    
result_list


# ## 네이버 뉴스 5페이지

# In[ ]:





# In[107]:


import requests

from bs4 import BeautifulSoup

a = []

for page in range(5):

    starbucks = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%8A%A4%ED%83%80%EB%B2%85%EC%8A%A4&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=81&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=" + str(10*page+1))



    soup = BeautifulSoup(starbucks.text)
    title_list = soup.find_all('a', class_ = 'news_tit')
    dsc = soup.find_all('div', class_ = 'news_dsc')
    img = soup.find_all('img', class_ = 'thumb api_get')

    

    for i in range (10):

        title = title_list[i]['title']
        url = title_list[i]['href']
        description = dsc[i].text
        image = img[i]['src']

        a.append({'title' : title, 'url' : url, 'dsc' : description, 'image' : image})

print(a)


# In[4]:


import requests

from bs4 import BeautifulSoup

a = []

for page in range(5):

    starbucks = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%8A%A4%ED%83%80%EB%B2%85%EC%8A%A4&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=81&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=" + str(10*page+1))

    soup = BeautifulSoup(starbucks.text)
    title_list = soup.find_all('a', class_ = 'news_tit')
    dsc = soup.find_all('div', class_ = 'news_dsc')
    img = soup.find_all('img', class_ = 'thumb api_get')

    for i in range (10):

        title = title_list[i]['title']
        url = title_list[i]['href']
        description = dsc[i].text
        image = img[i]['src']
        
        contents = requests.get(url)
        contentssoup = BeautifulSoup(contents.text)
        cs = contentssoup.find('div', class_ = 'article')
        ctext = contentssoup.text

        a.append({'title' : title, 'url' : url, 'dsc' : description, 'image' : image, 'content' : ctext})

print(a)


# In[5]:


get_ipython().system('pip install tqdm')


# In[7]:


import tqdm


# In[ ]:




