#!/usr/bin/env python
# coding: utf-8

# ## REST API

# In[1]:


import requests

base_url = 'https://openapi.naver.com/v1/datalab/search'
headers = {
    'X-Naver-Client-Id': 'zfPYmIE8_VXg55xMGAAx',
    'X-Naver-Client-Secret': 'EjngdgANFR'
}


# startDate	string	Y	조회 기간 시작 날짜(yyyy-mm-dd 형식). 2016년 1월 1일부터 조회할 수 있습니다.
# endDate	string	Y	조회 기간 종료 날짜(yyyy-mm-dd 형식)
# timeUnit	string	Y	구간 단위
# - date: 일간
# - week: 주간
# - month: 월간
# keywordGroups	array(JSON)	Y	주제어와 주제어에 해당하는 검색어 묶음 쌍의 배열. 최대 5개의 쌍을 배열로 설정할 수 있습니다.
# keywordGroups.groupName	string	Y	주제어. 검색어 묶음을 대표하는 이름입니다.
# keywordGroups.keywords	array(string)	Y	주제어에 해당하는 검색어. 최대 20개의 검색어를 배열로 설정할 수 있습니다.

# In[2]:


import json



data = {
    'startDate': '2020-01-01',
    'endDate': '2021-05-20',
    'timeUnit': 'month',
    'keywordGroups': [{
        'groupName': '커피',
        'keywords': ['스타벅스', '커피빈', '바나프레소']
    }, {
        'groupName': '쥬스',
        'keywords': ['생과일쥬스', '쥬스', '쥬씨']
    }]

}

data = json.dumps(data)

resp = requests.post(base_url, data = data, headers = headers)


# In[3]:


resp


# In[6]:


resp.text


# In[4]:


data = resp.json()
data


# In[9]:


import json

def naver_data_lab(gender):

    data = {
        'startDate': '2020-01-01',
        'endDate': '2021-05-20',
        'timeUnit': 'month',
        'keywordGroups': [{
            'groupName': '커피',
            'keywords': ['스타벅스', '커피빈', '바나프레소']
        }, {
            'groupName': '쥬스',
            'keywords': ['생과일쥬스', '쥬스', '쥬씨']
        }],
        'gender': gender
    }

    data = json.dumps(data)

    resp = requests.post(base_url, data = data, headers = headers)
    
    return resp


# In[11]:


m_resp = naver_data_lab('m')
f_resp = naver_data_lab('f')


# In[12]:


m_resp.json()


# In[13]:


f_resp.json()


# ## numpy, pandas (04강 데이터베이스와 SQL과 진도 순서 바꿈)

# In[16]:


import numpy as np


# In[21]:


l1 = [1, 2, 3]
arr1 = np.array(l1)
arr1


# In[32]:


arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr2


# In[33]:


arr3 = np.array([0.1, 5, 4, 12, 5.3])
arr3 #자동으로 형변환 (모두 float로 같아지도록)


# In[28]:


arr4 = np.array([1, 2, 'a', 'b', 1.0, 2.0])
arr4 # 자동으로 형변환 (모두 str타입으로. str타입이 가장 광범위함)


# ### dtype (datatype의 약자)

# In[30]:


arr1.dtype


# In[34]:


arr2.dtype


# In[35]:


arr3.dtype


# In[36]:


arr4.dtype


# ### shape (배열의 형태)

# In[39]:


arr1.shape #데이터 길이가 3인 벡터구나


# In[40]:


arr2.shape #2차원 배열. row 가 2 column이 3. 단 행과 열로 받아들이지 않는 게 좋음


# In[41]:


arr3.shape


# In[42]:


arr4.shape


# In[44]:


arr5 = np.array([[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]])
arr5


# In[46]:


arr5.shape
# 바깥쪽 배열부터임. 1~6과 7~12까지 2개 배열. 1~2, 3~4, 5~6 3개. 1, 2 2개.
# 따라서 (2, 3, 2)


# ## astype

# In[48]:


arr3.astype(int)


# In[49]:


arr3.astype(np.int64)


# In[51]:


arr3.astype(float)


# In[52]:


arr3.astype(np.float64)


# In[53]:


arr3.astype(object)


# In[54]:


arr3.astype(bool)


# ## arange

# In[57]:


np.arange(5)


# In[59]:


np.arange(5, 10)


# In[61]:


np.arange(5, 20, 3)


# ## linspace (linear space)

# In[65]:


np.linspace(-5, 10, 16) #-5에서 10까지 16개로 균등하게


# In[66]:


np.linspace(10, 100, 40)


# ## reshape, shape (reshape은 함수, shape은 속성)

# In[69]:


arr1 = np.arange(27)
arr1


# In[70]:


arr1.shape


# In[73]:


arr2 = arr1.reshape(9, 3)
arr2


# In[75]:


arr3 = arr1.reshape(3, 3, 3)
arr3


# In[78]:


arr3.reshape(-1) #-1은 플랫하게 펴준다.


# In[79]:


arr3.reshape(3, -1) #-1 부분은 컴퓨터 니가 알아서 판단해서 펴줘


# In[80]:


arr3.reshape(-1, 9)


# In[82]:


arr1.reshape(-1, 1)


# In[83]:


arr1.shape = (3, 9)
arr1


# ## random

# In[84]:


np.random.rand()


# In[85]:


np.random.rand(3, 3)


# In[86]:


np.random.randint(-3, 3, (10, 5))


# In[87]:


np.random.randn(10, 5)


# ## indexing, slicing (numpy에서 가장 중요)

# In[88]:


arr1 = np.arange(10)
arr1


# In[89]:


arr1[3]


# In[90]:


arr1[3:]


# In[91]:


arr1[3:5]


# In[92]:


arr2 = arr1.reshape(2, 5)
arr2


# In[95]:


arr2[1][2]


# In[97]:


arr2[1, 2] #numpy에서는 이렇게 꺼내올 수 있다.
#arr2[1][2] 는 두 번 연산이므로 비효율적


# In[98]:


arr2[:, 2]


# In[101]:


arr2[:, [1, 3]] #바깥쪽거는 전부 가져올게요. 각각에서 1번과 3번 인덱스 가져올게요.


# In[102]:


arr3 = np.arange(36).reshape((9, -1))
arr3


# In[113]:


arr3[[0, 3],  [1, 3]]  #순서쌍으로 가져옴. (0,1)과 (3,3)을 가져옴. 잘 안씀


# In[114]:


arr1


# In[115]:


arr1[arr1>5] # arr1 중에 5보다 큰 것만


# In[117]:


arr1 + 10 #전체 요소에 10씩 더한 값


# In[119]:


arr1 * 3


# In[120]:


arr1 > 5


# In[121]:


arr1[[False, False, False, False, False, False,  True,  True,  True,
        True]]


# In[122]:


arr1


# In[126]:


arr1 [arr1 % 4 ==0]


# ## NaN(not a number), inf (쓸 일 별로 없음)

# In[128]:


arr2 = [np.nan, 0., 3.2, -np.inf, np.inf]
arr2


# ## 영행렬, 일행렬, 단위행렬, 역행렬

# In[134]:


np.zeros(9)


# In[136]:


np.zeros((3, 3))


# In[137]:


np.ones((3, 3))


# In[139]:


np.eye(3)


# In[141]:


np.identity(3)


# In[144]:


arr1 = np.arange(1, 5)
arr1 = arr1.reshape(2, 2)
arr1


# In[150]:


np.matmul(arr1, np.eye(2)) #arr1에 np.eye(2) 곱한 것


# ## 배열연산 (요소별 연산)

# In[152]:


arr1


# In[151]:


arr1 - 3


# In[156]:


arr1 - np.array([[3, 4], [5, 6]])


# ## 통계를 위한 연산

# In[159]:


arr1 = np.arange(27).reshape((9,3))
arr1


# In[160]:


arr1.sum()


# In[161]:


arr1.sum(axis = 0)


# In[162]:


arr1.sum(axis = 1)


# In[163]:


arr1.mean(axis = 0)


# In[164]:


arr1.var(axis = 0)


# In[165]:


arr1.std(axis = 0)


# In[166]:


arr1.min(axis = 0)


# In[167]:


arr1.max(axis = 1)


# In[168]:


arr1.cumsum(axis = 0)


# In[169]:


arr1.cumprod(axis = 0)


# ## 행렬곱

# In[172]:


A = np.arange(1, 7).reshape((2, 3)) # 보통 행렬 변수는 대문자로 함
B = np.arange(6, 0 , -1).reshape((3, 2))
A


# In[174]:


B


# In[175]:


A@B


# In[176]:


A.dot(B)


# In[177]:


np.matmul(A, B)


# ## 전치행렬 transpose

# In[178]:


A


# In[179]:


A.transpose()


# In[180]:


np.transpose(A)


# In[181]:


A.T


# ## 역행렬

# In[182]:


A = np.arange(1, 5).reshape((2, 2))
A


# In[183]:


np.linalg.inv(A)


# ## 행렬식

# In[184]:


np.linalg.det(A)


# In[ ]:





# ## 특정 사이트에서 로그인 돼있을 때의 리스폰스를 받아오려면

# In[185]:


import requests
sess = requests.Session()


# In[186]:


resp = sess.get('https://www.data.go.kr')


# In[187]:


resp


# In[188]:


resp.cookies

