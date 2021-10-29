#!/usr/bin/env python
# coding: utf-8

# 이번 챕터에서는 영어 문장에서 NLTK가 정의한 영어 불용어를 제거하는 실습을 하고, 한국어 문장에서 직접 정의한 불용어를 제거해보겠습니다.

# In[1]:


import nltk
nltk.download('stopwords')
nltk.download('punkt')


# In[2]:


# 1. NLTK에서 불용어 확인하기
from nltk.corpus import stopwords  
stopwords.words('english')[:10] 


# In[3]:


# 2. NLTK를 통해서 불용어 제거하기
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

example = "Family is not an important thing. It's everything."
stop_words = set(stopwords.words('english')) 

word_tokens = word_tokenize(example)

result = []
for w in word_tokens: 
    if w not in stop_words: 
        result.append(w) 

print(word_tokens) 
print(result) 


# In[4]:


# 3. 한국어에서 불용어 제거하기
from nltk.tokenize import word_tokenize 

# 아래의 불용어는 저자가 임의로 선정한 것으로 실제 의미있는 선정 기준이 아님
example = "고기를 아무렇게나 구우려고 하면 안 돼. 고기라고 다 같은 게 아니거든. 예컨대 삼겹살을 구울 때는 중요한 게 있지."
stop_words = "아무거나 아무렇게나 어찌하든지 같다 비슷하다 예컨대 이럴정도로 하면 아니거든"

stop_words = set(stop_words.split(' '))
word_tokens = word_tokenize(example)

result = [word for word in word_tokens if not word in stop_words]

print(word_tokens) 
print(result)

