#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. 실습파일 불러오기
import pandas as pd
import pandas_profiling
data = pd.read_csv(r'C:\Users\user\!jupyter\spam.csv', encoding='latin1')


# In[2]:


data[:5]


# In[3]:


# 2. 리포트 생성하기
pr = data.profile_report()


# In[4]:


pr.to_file('.pr_report.html')


# In[5]:


# 3. 리포트 살펴보기
pr


# In[6]:


# https://kanoki.org/2019/01/15/pandas-exploratory-data-analysis-data-profiling/

