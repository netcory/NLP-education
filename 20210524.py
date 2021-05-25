#!/usr/bin/env python
# coding: utf-8

# # 책으로 진도 나감

# ## Pandas

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


s = pd.Series([1, 3, 5, np.nan, 6, 8])
s


# In[4]:


s = pd.Series([1, 3, 5, np.nan, 6, 8])
s
# 인덱스도 자동으로 출력
# np.nan이 실수형이므로 나머지 정수들도 더 큰 범위인 실수로 캐스팅됨


# In[5]:


s[0], s[1], s[1:]


# In[7]:


s.index


# In[8]:


s.values


# In[9]:


type(s.values)


# In[10]:


type(s.index)


# In[11]:


s2 = pd.Series(['a', 'b', 'c', 1, 2, 3])
s2


# In[12]:


s3 = pd.Series([np.nan, 10, 30])
s3


# In[20]:


index_date = ['2018-10-07', '2018-10-08', '2018-10-09', '2018-10-10']
s4 = pd.Series([200, 195, np.nan, 205], index = index_date)
s4


# In[23]:


s4.index = [1, 2, 3, 4]
s4


# In[24]:


s4.index


# In[25]:


pd.date_range(start = '2019-01-01', end = '2019-01-07')


# In[26]:


pd.date_range(start= '2019/01/01', end = '2019.01.07')


# In[27]:


pd.date_range(start = '01-01-2019', end = '01/07/2019')


# In[29]:


pd.date_range(start = '2019-01-01', periods = 7)


# In[30]:


pd.date_range(start = '2019-01-01', periods = 4, freq = '2D')


# In[31]:


pd.date_range(start = '2019-01-01', periods = 4, freq = 'W')


# In[32]:


df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df


# In[33]:


data_list = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
pd.DataFrame(data_list)


# In[34]:


data_list


# In[46]:


data= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
index_date = pd.date_range('2019-09-01', periods = 4)
columns_list = ['A', 'B', 'C']
pd.DataFrame = (data, index = index_date, columns = columns_list)


# In[42]:


table_data = {'연도': [2015, 2016, 2016, 2017, 2017],
             '지사': ['한국', '한국', '미국', '한국', '미국'],
             '고객 수': [200, 250, 450, 300, 500]}
table_data


# In[48]:


pd.DataFrame(table_data)


# In[50]:


df = pd.DataFrame(table_data)


# In[51]:


df['연도']


# In[52]:


df['지사']


# In[54]:


a = np.array([1, 2, 3, 4, 5, 6])
a>3


# In[55]:


a[a>3] # 인덱스를 조건으로 줌


# In[57]:


df


# In[58]:


df['연도'] >= 2017


# In[59]:


df[[False, False, True, True, True]]


# In[60]:


df[df['연도'] >= 2017]


# In[61]:


df['연도']


# In[63]:


df[['연도', '지사']]


# In[64]:


df[['연도']] #인덱스를 리스트로 주면 2차원 결과 받을 수 있음


# ## DataFrame 다양한 방법으로 조회하기

# ### Quiz 1
# ### 연도는 2017년 이후(2017년 포함)이고 고객수는 350 이상인 Row만 조회하기
# 
# ### 참고: pandas에서는 and는 &, or는 | 로 사용

# In[71]:


df


# In[85]:


df[(df['연도'] >= 2017) & (df['고객 수'] >= 350)]

#() 괄호 안 해주면 2017 & df['고객 수'] 를 먼저 해야되는 건지 헷갈림


# ### Quiz 2
# ### 지사가 한국이거나 고객수가 300 이상인 row 조회

# In[88]:


df[(df['지사'] == '한국') | (df['고객 수'] >= 300)]


# In[91]:


df['고객 수']


# ## Pandas 연산

# In[95]:


s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([10, 20, 30, 40, 50])
s1 + s2


# In[96]:


s2 - s1


# In[99]:


s1 * s2


# In[98]:


s2 / s1


# In[100]:


s3 = pd.Series([1, 2, 3, 4])
s4 = pd.Series([10, 20, 30, 40, 50])
# numpy와 달리 pandas는 데이터끼리 크기가 달라도 연산 가능
# 연산할 수 없는 부분은 NaN으로 표시


# In[101]:


s3 + s4


# In[102]:


s4 - s3


# In[103]:


s3 * s4


# In[104]:


s4 / s3


# In[105]:


table_data1 = {'A' : [1, 2, 3, 4, 5],
              'B': [10 , 20 , 30, 40, 50],
              'C': [100, 200, 300, 400, 500]}
df1 = pd.DataFrame(table_data1)
df1


# In[106]:


table_data2 = {'A': [6, 7, 8],
              'B': [60, 70, 80],
              'C': [600, 700, 800]}
df2 = pd.DataFrame(table_data2)
df2


# In[107]:


df1 + df2


# In[199]:


table_data3 = {'봄': [256.5, 264.3, 215.9, 223.2, 312.8],
              '여름': [770.6, 567.5, 599.8, 387.1, 446.2],
              '가을': [363.5, 231.2, 293.1, 247.7, 381.6],
              '겨울': [139.3, 59.9, 76.9, 109.1, 108.1]}
index_list = ['2012', '2013', '2014', '2015', '2016']

df3 = pd.DataFrame(table_data3, index = index_list)
df3


# In[118]:


df3.mean()


# In[119]:


df3.sum()


# In[120]:


df3.cumsum()


# In[121]:


df3.cumprod()


# In[122]:


df3.std()


# In[124]:


df3.mean(axis = 1)
#axis = 1이므로 index 기준


# In[125]:


df3.info()


# In[126]:


df3.describe()


# In[127]:


df3['우박여부'] = ['내림', '안내림', '내림', '내림', '안내림']
df3


# In[129]:


df3.describe()
# 수치 데이터가 아닌 우박여부(카테고리컬 데이터, 범주형 데이터)는 빼고 나옴


# In[130]:


df3.describe(include="all")
#unique는 값의 종류 (내림, 안내림 두 종류가 있어서 2)
#top은 가장 많이 나온 것(내림)
#freq


# In[132]:


df3['우박여부'].unique()


# In[133]:


df3['우박여부'].value_counts()


# In[134]:


import pandas as pd
import numpy as np

KTX_data = {'경부선 KTX': [39060, 39896, 42005, 43621, 41702, 41266, 32427],
            '호남선 KTX': [7313, 6967, 6873, 6626, 8675, 10622, 9228],
            '경전선 KTX': [3627, 4168, 4088, 4424, 4606, 4984, 5570],
            '전라선 KTX': [309, 1771, 1954, 2244, 3146, 3945, 5766],
            '동해선 KTX': [np.nan,np.nan, np.nan, np.nan, 2395, 3786, 6667]}
col_list = ['경부선 KTX','호남선 KTX','경전선 KTX','전라선 KTX','동해선 KTX']
index_list = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']

df_KTX = pd.DataFrame(KTX_data, columns = col_list, index = index_list)
df_KTX


# In[135]:


df_KTX.head()
#앞에 5개만 열어봄


# In[136]:


df_KTX.head(3)
#앞에 3개만 열어봄


# In[137]:


df_KTX.tail()
#뒤에 5개


# In[138]:


df_KTX.tail(3)


# In[142]:


df_KTX[1:2]


# In[143]:


df_KTX[2:5]


# ### .loc: index명과 column이름으로 조회

# In[144]:


df_KTX


# In[145]:


df_KTX.loc['2012']


# In[147]:


df_KTX.loc['2013':]


# In[148]:


df_KTX.loc['2013':, :]
#인덱스는 2013, 칼럼은 전부 가져와


# In[150]:


df_KTX.loc['2013':'2016', ['경부선 KTX', '호남선 KTX']]
#인덱스는 2013~2016, 칼럼은 경부선, 호남선 가져와


# ### df.iloc
# ### 숫자로접근

# In[153]:


df_KTX


# In[154]:


df_KTX.iloc[:3, :2]
#인덱스는 0,1,2 칼럼은 0,1 불러와


# In[155]:


df_KTX


# In[156]:


df_KTX.loc[df_KTX['경전선 KTX'] >= 4200, ['경부선 KTX', '동해선 KTX']]


# In[158]:


df_KTX.T
#전치


# In[ ]:





# In[ ]:





# In[159]:


import numpy as np
import pandas as pd

df1 = pd.DataFrame({'Class1': [95, 92, 98, 100],
                   'Class2': [91, 93, 97, 99]})

df1


# In[160]:


df2 = pd.DataFrame({'Class1': [87, 89],
                   'Class2': [85, 90]})
df2


# In[162]:


df3 = df1.append(df2)
df3
# row 추가
# index가 중복돼서 이상함


# In[163]:


# 첫 번째 방법
df3 = df3.reset_index(drop=True)
# 기존 인덱스 다 지우고 0부터 채울거야
df3


# In[165]:


# 두 번째 방법
df4 = df1.append(df2, ignore_index=True)
#인덱스까지 추가하진 않을거야
df4


# In[167]:


df4.append(pd.DataFrame({'Class1': [87],
                        'Class2': [90]}), ignore_index=True)


# In[170]:


df4 = pd.DataFrame({'Class3': [93, 91, 95, 98]})
df4


# In[172]:


df1.join(df4)
# 인덱스 기준으로 합침


# In[173]:


df5 = pd.DataFrame({'Class3': [93, 91]})
df5


# In[174]:


df1


# In[177]:


df1.join(df5)


# In[180]:


df5.join(df1)
# df1이 잘려서 들어감. 즉 앞에놈 기준


# ### join의 how 키워드 인자

# In[183]:


df1.loc[0, 'Class1'] = np.NaN
#df1 조작
df1


# In[185]:


df1.index = [1, 2, 3, 4]
df1


# In[187]:


df5


# In[189]:


df1.join(df5)
# df1에 0번 인덱스가 없으므로 df5의 0번 인덱스도 잘림


# In[190]:


df1.join(df5, how = 'left')
#df1을 기준으로 해라


# In[193]:


df1.join(df5, how = 'right')
#df5를 기준으로 해라


# In[195]:


df1.join(df5, how = 'inner')
#인덱스 중복된 것만 가져와라


# In[196]:


df1.join(df5, how = 'outer')
#다 합치고 없으면 NaN


# ### merge

# In[197]:


df_A_B = pd.DataFrame({'판매월': ['1월', '2월', '3월', '4월'],
                      '제품A': [100, 150, 200, 130],
                      '제품B': [90, 110, 140, 170]})

df_A_B


# In[198]:


df_C_D = pd.DataFrame({'판매월': ['1월', '2월', '3월', '4월'],
                      '제품C': [112, 141, 203, 134],
                      '제품D': [90, 110, 140, 170]})
df_C_D


# In[201]:


df_A_B.merge(df_C_D)
#자동으로 같은 칼럼 이름을 찾아서 합침


# In[203]:


df_C_D['판매월'] = ['3월', '4월', '5월', '6월']
df_C_D
#df_C_D를 조작


# In[204]:


df_A_B['담당자'] = ['A', 'B', 'C', 'D']
df_C_D['담당자'] = ['D', 'C', 'B', 'A']
# 담당자 이름 추가


# In[205]:


df_A_B


# In[206]:


df_C_D


# In[207]:


df_A_B.merge(df_C_D, on = '판매월')
# 판매월 기준으로 통합해라


# In[209]:


df_A_B.merge(df_C_D, on = '판매월', how = 'left')
#결국 merge와 join은 완전히 같은 기능
#여러 언어에서 쓰는 명령어를 다 합쳐 놔서 그럼


# In[210]:


df_A_B.merge(df_C_D, on = '판매월', how = 'outer')


# In[211]:


df_A_B


# In[212]:


df_C_D


# In[213]:


df_A_B.merge(df_C_D, on = '담당자')
#담당자를 기준으로 합침. 그에 따라 df_C_D의 판매월은 뒤집힘


# In[215]:


df


# ## 결측치 처리

# In[239]:


import pandas as pd
import numpy as np

KTX_data = {'경부선 KTX': [39060, np.nan, 42005, 43621, 41702, 41266, 32427],
            '호남선 KTX': [7313, 6967, 6873, 6626, np.nan, np.nan, 9228],
            '경전선 KTX': [3627, 4168, np.nan, 4424, 4606, 4984, 5570],
            '전라선 KTX': [309, 1771, 1954, 2244, 3146, 3945, 5766],
            '동해선 KTX': [np.nan,np.nan, np.nan, np.nan, 2395, 3786, 6667]}

index_list = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']

df_KTX = pd.DataFrame(KTX_data, index = index_list)
df_KTX


# In[220]:


df_KTX.isna()
#nan 값만 True로, 나머지는 False


# In[221]:


df_KTX.isnull()
#.isna와 같음


# In[225]:


df_KTX.dropna(axis = 0)
#nan 값 있으면 다 삭제
#axis = 0 이면 행 기준, axis = 1 이면 열 기준


# In[226]:


df_KTX.dropna(axis = 1)


# In[232]:


df_KTX.fillna(df_KTX.mean())
# nan 값을 평균값으로 채워줌


# In[235]:


df_KTX.fillna(df_KTX.median())
# nan 값을 중간값으로 채워줌


# In[240]:


df_KTX


# In[236]:


df_KTX.interpolate()
#보간법. 양 끝 값을 통해 중간에 빈 값을 추정


# In[238]:


df_KTX.dropna(inplace = True)
# df_KTX 자기 자신이 바뀌어버림

