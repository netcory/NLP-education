#!/usr/bin/env python
# coding: utf-8

# # 책으로 진도 나감

# ## matplotlib

# In[3]:


import matplotlib


# In[4]:


matplotlib.__version__


# In[5]:


import matplotlib.pyplot as plt
# 관례적으로 사용


# In[12]:


import numpy as np
import pandas as pd


# ### pyqt로 보기

# In[9]:


get_ipython().system('pip install pyqt5')


# In[10]:


get_ipython().run_line_magic('matplotlib', 'qt')


# In[13]:


arr1 = np.arange(1, 10)
arr2 = arr1 * 3 + 5
arr1, arr2


# In[14]:


plt.plot(arr1, arr2)
# x(옵션), y(필수), format(옵션)
# 그래프 창이 하나 뜸


# ### inline 으로 보기

# In[15]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[16]:


plt.plot(arr1, arr2)


# In[17]:


plt.plot(arr1, arr2)
plt.show()
# 어떤 시점에서 플롯팅을 전부 보여줘라고 명시적으로 나타낸 것


# In[18]:


data1 = [10, 14, 19, 20, 25]
plt.plot(data1)
# y값만 있어도 x값이 자동으로 생성 (0,10), (1, 14), (2, 19)...


# ### 선그래프

# In[19]:


x = np.arange(-4.5, 5, 0.5)
y = 2 * x ** 2
plt.plot(x, y)


# ### 여러 그래프 하나의 figure에 그리기

# In[22]:


# 방법 1
x = np.arange(-4.5, 5, 0.5)
y1 = 2 * x ** 2
y2 = 5 * x + 30
y3 = 4 * x ** 2 + 10

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.show()


# In[23]:


# 방법2
plt.plot(x, y1, x, y2, x, y3)


# ### plt.figure

# In[24]:


plt.plot(x, y1)
plt.figure() #새로운 도화지
plt.plot(x, y2)


# In[25]:


plt.figure(0)
plt.plot(x, y1)
plt.figure(1)
plt.plot(x, y2)
plt.figure(0)
plt.plot(x, y3)

# 0번 도화지에 y1, y3 그리고 1번 도화지에 y2 그림


# ### clf - 그래프 지우기 (clear figure)

# In[29]:


x = np.arange(-5, 5, .1)
y1 = x ** 2 -2
y2 = 20 * np.cos(x) ** 2

plt.figure(1)
plt.plot(x, y1)

plt.figure(2)
plt.plot(x, y2)

plt.figure(1)
plt.plot(x, y2)

plt.figure(2)
plt.clf()
plt.plot(x, y1)

plt.show()

# 결과적으로 1번 피겨에는 y1, y2 다 그리고
# 2번 피겨에는 y1만 그림


# ### 하나의 그래프 창에서 영역 나누기

# In[30]:


#plt.subplot(m, n, p) mxn 행렬의 p번째 그림 그려짐
plt.subbplot()


# In[34]:


plt.figure(figsize = (15, 15)) #피규 사이즈 크게 만듦

x = np.arange(-5, 5, .1)
y1 = 0.3 * (x-5) ** 2 + 1
y2 = -1.5 * x + 3
y3 = np.sin(x) ** 2
y4 = 10 * np.exp(-x) + 1

# 2 X 2 행렬로 나누고 위치 조정
plt.subplot(2, 2, 1)
plt.plot(x, y1)

plt. subplot(2, 2, 2)
plt.plot(x, y2)

plt. subplot(2, 2, 3)
plt.plot(x, y3)

plt.subplot(2, 2, 4)
plt.plot(x, y4)

plt.show()


# ### 그래프의 출력 범위 지정하기

# In[35]:


# plt.xlim(xmin, xmax)
# plt.ylim(ymin, yamx)


# In[36]:


xmin, xmax = plt.xlim() # 현재 x축 범위
ymin, ymax = plt.ylim() # 현재 y축 범위
#아무 것도 안 주면 0부터 1


# In[37]:


xmin, ymin, xmax, ymax # 확인 가능


# In[44]:


plt.figure(figsize = (15, 5))
x = np.linspace(-4, 4, 100)
y1 = 3 * (x ** 2) + 2
y2 = x ** 3
y3 = 10 * (x**2) - 2

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.xlim(-1, 1)
plt.ylim(-5, 10) # 해당 영역만 확대해서 볼 수 있음
# 교차 지점 확인할 때 유용


# In[46]:


x = np.arange(0, 5)
y1 = x
y2 = x + 1
y3 = x + 2
y4 = x + 3


# In[48]:


plt.figure(figsize = (15, 5))
plt.plot(x, y1, x, y2, x, y3, x, y4)
plt.show()


# In[50]:


plt.plot(x, y1, 'm', x, y2, 'y', x, y3, 'k', x, y4, 'c')
plt.show()
# 색상 지정


# In[51]:


plt.plot(x, y1, 'm-', x, y2, 'y--', x, y3, 'k-.', x, y4, 'c:')
plt.show()
# 점선 등


# In[58]:


plt.figure(figsize  = (15, 15))
plt.plot(x, y1, 'm-o', x, y2, 'y--^', x, y3, 'k-.>', x, y4, 'c:*')
plt.show()
# 마커 지정


# ### title, label, grid, legend, text

# In[76]:


plt.figure(figsize = (10, 5))

x = np.arange(-4.5, 5, 0.5)
y = 2 * (x**3)
y2 = 2 * x + 20

# title: figure 제목
plt.title("Sample Plot")
# label : 축 라벨
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
# grid : 특정 지점 격자 표시
plt.grid()

plt.plot(x, y)
plt.plot(x, y2)

# legend : 범례
plt.legend(['Data1', 'Data2'], loc = 'upper right') # plt.plot 다음에 와야 함!!
#위치 지정은 안해도 됨

plt.show()


# In[77]:


plt.figure(figsize = (10, 5))

x = np.arange(-4.5, 5, 0.5)
y = 2 * (x**3)
y2 = 2 * x + 20

plt.title("plot 제목") # 한글로 바꿔 보면 깨짐
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.grid()

plt.plot(x, y)
plt.plot(x, y2)


plt.legend(['Data1', 'Data2'], loc = 'upper right') # plt.plot 다음에 와야 함!!


plt.show()


# In[78]:


import platform
from matplotlib import font_manager, rc 
import matplotlib
# '-' 부호가 제대로 표시되게 하는 설정 
matplotlib.rcParams['axes.unicode_minus'] = False
# 운영 체제마다 한글이 보이게 하는 설정 # 윈도우
if platform.system() == 'Windows':
    path = "c:\Windows\Fonts\malgun.ttf" # 맑은 고딕
    font_name = font_manager.FontProperties(fname=path).get_name() 
    rc('font', family=font_name)


# In[79]:


plt.figure(figsize = (10, 5))

x = np.arange(-4.5, 5, 0.5)
y = 2 * (x**3)
y2 = 2 * x + 20

plt.title("plot 제목") # 위 코드를 작성 후 다시 해보면 한글도 잘 나옴
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.grid()

plt.plot(x, y)
plt.plot(x, y2)


plt.legend(['Data1', 'Data2'], loc = 'upper right')


plt.show()


# In[80]:


plt.figure(figsize = (10, 5))

x = np.arange(-4.5, 5, 0.5)
y = 2 * (x**3)
y2 = 2 * x + 20

plt.title("plot 제목") 
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.grid()

plt.plot(x, y)
plt.plot(x, y2)


plt.legend(['Data1', 'Data2'], loc = 'upper right')

plt.text(0, 100, 'string1') # (0, 100) 위치에 텍스트 추가
plt.text(-4, 30, 'string2') # (-4, 30) 위치에 텍스트 추가

plt.show()


# ## scatter(산점도)

# In[84]:


plt.figure(figsize = (10, 5))

height = [165, 177, 160, 180, 185, 155, 172]
weight = [62, 67, 55, 74, 90, 43, 64]

plt.scatter(height, weight)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.grid()
lt.show()


# In[93]:


x = np.linspace(10, 100, 1000)
y = x * 3 + np.random.normal(0, 10, 1000)
plt.scatter(x, y)


# In[95]:


plt.figure(figsize = (15, 5))
x = np.linspace(10, 100, 1000)
y = x * 3 + np.random.normal(0, 10, 1000)
plt.scatter(x, y, alpha = 0.1) # 투명도 부여
# 많이 겹치면 진해짐


# In[108]:


x = np.linspace(10, 100, 10)
y = x * 3 + np.random.normal(0, 100, 10)
y2 = -3 * x + np.random.normal(0, 2, 10)

s_size = np.random.randint(10, 300, 10)

plt.scatter(x, y, s = 100) # 사이즈 부여
plt.scatter(x, y2, s = s_size, marker = '+') # 플러스 마커의 사이즈가 랜덤
plt.show()


# In[114]:


plt.figure(figsize = (10, 10))

city = ['서울', '인천', '대전', '대구', '울산', '부산', '광주']

lat = [37.56, 37.45, 36.35, 35.87, 35.53, 35.18, 35.16]
lon = [126.97, 126.7, 127.38, 128.6, 129.31, 129.07, 126.85]

pop_den = [16154, 2751, 2839, 2790, 1099, 4454, 2995]

size = np.array(pop_den) * 0.2
colors = ['r', 'g', 'b', 'k', 'm', 'c', 'y']

plt.scatter(lon, lat, c= colors, s = size, alpha = 0.2)
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.title("population density.")

for x, y, c in zip(lon, lat, city):
    plt.text(x, y, c)
    
plt.show()


# ### 막대 그래프 (bar)

# In[115]:


# 운동 전, 후 근육량 데이터

member_IDs = ['m_01', 'm_02', 'm_03', 'm_04']
before_ex = [27, 35, 40, 33]
after_ex = [30, 38, 42, 37]


# In[117]:


n_data = len(member_IDs)
index = np.arange(n_data)
plt.bar(index, before_ex, tick_label = member_IDs)
plt.show()


# In[118]:


n_data = len(member_IDs)
index = np.arange(n_data)
plt.bar(index, before_ex, tick_label = member_IDs, width = 0.5) # 바 너비 줄임
plt.show()


# In[119]:


n_data = len(member_IDs)
index = np.arange(n_data)
plt.bar(index, before_ex, tick_label = member_IDs, width = 0.5, align = 'edge') # 막대를 가장자리로 보냄

plt.show()


# In[123]:


n_data = len(member_IDs)
index = np.arange(n_data)
plt.bar(index-0.5, before_ex, tick_label = member_IDs, width = 0.4, align = 'edge')
plt.bar(index, after_ex, tick_label = member_IDs, width = 0.4, align = 'edge')
# index 위치를 조절해서 막대가 겹치지 않게
plt.show()


# In[125]:


n_data = len(member_IDs)
index = np.arange(n_data)
plt.bar(index-0.5, before_ex, tick_label = member_IDs, width = 0.4, align = 'edge')
plt.bar(index, after_ex, tick_label = member_IDs, width = 0.4, align = 'edge')
plt.xlabel("member ID")
plt.ylabel("muscle")

# legend 별개로 작성
plt.legend(["before_ex", 'after_ex'])

plt.show()


# In[128]:


n_data = len(member_IDs)
index = np.arange(n_data)
plt.bar(index-0.5, before_ex, tick_label = member_IDs, width = 0.4,
        align = 'edge', label = 'before_ex')
plt.bar(index, after_ex, tick_label = member_IDs, width = 0.4,
        align = 'edge', label = 'after_ex')
# 범례를 bar 호출할 때 불러버림

plt.xlabel("member ID")
plt.ylabel("muscle")

plt.legend() # 범례 호출은 해줘야함

plt.show()


# In[130]:


n_data = len(member_IDs)
index = np.arange(n_data)

# barh : bar horizon (수평 막대 그래프)
# width 가 height로 바뀌어야 함
plt.barh(index-0.5, before_ex, tick_label = member_IDs, height = 0.4, align = 'edge')
plt.barh(index, after_ex, tick_label = member_IDs, height = 0.4, align = 'edge')

plt.xlabel("member ID")
plt.ylabel("muscle")


plt.legend(["before_ex", 'after_ex'])

plt.show()


# ### histogram

# In[131]:


data = np.random.normal(0, 100, 10000)


# In[132]:


plt.hist(data)
plt.show()


# In[137]:


plt.hist(data, bins = 20) # 막대 20개로 볼거야
plt.show()


# ### pie graph

# In[138]:


fruit = ['사과', '바나나', '딸기', '오렌지', '포도']
result = [7, 6, 3, 2, 2]


# In[145]:


plt.pie(result, labels = fruit, autopct = '%.2f')
# 소수점 둘째 자리까지 표현해 줘

plt.show()


# In[147]:


plt.figure(figsize = (10, 10))
plt.pie(result, labels = fruit, autopct = '%.2f%%')
# 뒤에 퍼센트까지 써줘
plt.show()


# In[148]:


plt.figure(figsize = (10, 10))
plt.pie(result, labels = fruit, autopct = '%.2f%%',
       explode = [0, 0, 0, 0, 1])
# 포도만 강조해서 보여줘 

plt.show()


# In[152]:


plt.figure(figsize = (10, 10))
plt.pie(result, labels = fruit, autopct = '%.2f%%',
       explode = [0, 0, 0, 0, 1], startangle = 50)
# 시계 반대 방향으로 50도 회전. 시계 방향하려면 마이너스

plt.show()


# In[153]:


plt.figure(figsize = (10, 10))
plt.pie(result, labels = fruit, autopct = '%.2f%%',
       explode = [0, 0, 0, 0, 1], startangle = 50, shadow = True)
# 입체감 부여

plt.show()


# In[155]:


get_ipython().system('pip install scikit-learn')


# In[164]:


from sklearn.datasets import load_boston


# In[167]:


load_boston()


# In[168]:


load_boston().keys()


# In[169]:


data = load_boston()
boston = pd.DataFrame(data.data, columns = data.feature_names) # data라는 변수의 data라는 속성
boston


# In[171]:


boston['target'] = data.target
boston


# In[172]:


boston.info()


# In[176]:


plt.figure(figsize = (15, 15))
boston.hist() # 히스토그램 호출
plt.show()


# In[177]:


boston.describe()


# In[178]:


# 상관계수 corr
# 상관계수는 절대값이 1에 가까울수록 상관관계가 크다
boston.corr()


# In[181]:


boston.corr()['target']
# target값은 LSTA과 상관관계가 가장 높음을 확인 가능


# In[182]:


boston.plot(x = 'LSTAT', y = 'target', kind = 'scatter')


# In[183]:


boston.plot(x = 'LSTAT', y = 'target', kind = 'scatter', alpha = 0.2)


# In[184]:


boston.corr('spearman')


# In[186]:


boston.corr('pearson')
# default는 피어슨


# ### seaborn & plotly

# In[187]:


get_ipython().system('pip install seaborn')


# In[190]:


import seaborn as sns


# In[200]:


boston.columns


# In[201]:


sns.pairplot(boston[['CRIM', 'LSTAT', 'target', 'AGE', 'TAX']])
# 히스토그램과 산점도가 함께
# 예를 들어 CRIM과 CRIM은 어차피 같은 데이터라 히스토그램이 나옴
# 나머지는 스캐터


# In[202]:


get_ipython().system('pip install plotly==4.14.3')


# In[203]:


import plotly.express as px
df = px.data.tips()
df


# In[208]:


fig = px.histogram(df, x = 'total_bill')
fig.show()


# In[209]:


fig = px.histogram(df, x = 'total_bill', color = 'sex')
fig.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




