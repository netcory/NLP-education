#!/usr/bin/env python
# coding: utf-8

# # numpy 연습문제

# ## 1. 10개의 0 벡터를 만들고 4번째와 5번째 Index의 값을 1로 한 후 (5,2) 행렬로 만들어라

# In[4]:


import numpy as np


# In[13]:


arr1 = np.zeros(10)
arr1


# In[15]:


arr1[4:6] = 1
arr1


# In[16]:


arr1 = arr1.reshape((5,2))
arr1


# ## 2. 10에서 30까지 2씩 증가하는 vector를 만들고 다음 list와 요소별 사칙연산(+, -, *, /)을 하여라
# ##### a = [1. , 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]

# In[20]:


a = [1. , 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
arr2 = np.arange(10, 30, 2)
arr2


# In[21]:


arr2 + a


# ## 3.  <1에서 100>까지 10개를 균등하게 분할하여 배열을 만들고,  각각의 합, 평균, 표준편차, 분산, 최소값, 최대값, 누적합, 누적곱을 구하여라

# In[22]:


arr3 = np.linspace(1, 100, 10)
arr3


# In[29]:


print('합 = ',arr3.sum(), '곱 = ', arr3.mean(), '분산 = ', arr3.var(),
      '표준편차 = ', arr3.std(), '최소값 = ', arr3.min(), '최대값 = ', arr3.max(), '누적합 = ', arr3.cumsum(), '누적곱 = ', arr3.cumprod())


# ## 4.  0에서 10까지 random한 값을 지닌 3x3 실수 행렬을 만들어라

# In[31]:


arr4 = np.random.uniform(0, 10, (3, 3))
arr4


# ## 5.  0에서 10까지 random한 값을 지닌 3x3 정수 행렬을 만들어라

# In[32]:


arr5 = np.random.randint(0, 10, (3, 3))
arr5


# ## 6. 5x2 행렬을 만들고 Standardization(표준화 하여라)
# - standardization: (x - mean(x))/std(x)
# - mean과 std는 Row단위로 연산을 해야함.(return shape이 (2,))
# - 전체 결과는 5x2 행렬

# In[33]:


arr6 = np.random.randint(0, 50, (5, 2))
arr6


# In[37]:


mean = arr6.mean(axis = 0)
std = arr6.std(axis = 0)

mean, std


# In[42]:


stan = (arr6 - mean)/std
stan


# # 7. 5x2 행렬을 만들고 Min-Max정규화(Nomalization) 하여라
# - (x - min(x)) / (max(x) - min(x))
# - Row단위로 연산. (return shape)
# - mean과 std는 Row단위로 연산을 해야함.(return shape이 (2,))
# - 전체 결과는 5x2 행렬

# In[43]:


arr7 = np.random.randint(0, 100, (5, 2))
arr7


# In[45]:


max_ = arr7.max(axis = 0)
min_ = arr7.min(axis = 0)
max_, min_


# In[47]:


norm = (arr7 - min_) / (max_ - min_)
norm


# In[ ]:




