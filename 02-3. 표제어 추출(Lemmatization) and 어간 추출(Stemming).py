#!/usr/bin/env python
# coding: utf-8

# 1. 표제어 추출(Lemmatization)
#     1) 어간(stem)
#     : 단어의 의미를 담고 있는 단어의 핵심 부분.
# 
#     2) 접사(affix)
#     : 단어에 추가적인 의미를 주는 부분.

# In[3]:


pip install nltk


# In[4]:


import nltk
nltk.download('wordnet')
nltk.download('punkt')


# In[5]:


from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
words = ['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']
print([lemmatizer.lemmatize(w) for w in words])


# In[8]:


dies = lemmatizer.lemmatize('dies', 'v')
print('dies : ', dies)

watched = lemmatizer.lemmatize('watched', 'v')
print('watched : ', watched)

has = lemmatizer.lemmatize('has', 'v')
print('has : ', has)


# 2. 어간 추출(Stemming)

# In[9]:


from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
stemmer = PorterStemmer()
text = "This was not the map we found in Billy Bones's chest, but an accurate copy, complete in all things--names and heights and soundings--with the single exception of the red crosses and the written notes."
words = word_tokenize(text)
print(words)


# In[10]:


print([stemmer.stem(w) for w in words])


# In[11]:


words = ['formalize', 'allowance', 'electricical']
print([stemmer.stem(w) for w in words])


# In[12]:


from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
words = ['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']
print([stemmer.stem(w) for w in words])


# In[13]:


from nltk.stem import LancasterStemmer
lancaster_stemmer = LancasterStemmer()
words = ['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has', 'starting']
print([lancaster_stemmer.stem(w) for w in words])


# **1) 표제어 추출(Lemmatization)**   
# am → be   
# the going → the going   
# having → have   
# 
# **2) 어간 추출(Stemming)**   
# am → am   
# the going → the go   
# having → hav

# 3. 한국어에서의 어간 추출
# 
# (1) 활용(conjugation)   
#     
#     어간(stem) : 용언(동사, 형용사)을 활용할 때, 원칙적으로 모양이 변하지 않는 부분. 활용에서 어미에 선행하는 부분. 때론 어간의 모양도 바뀔 수 있음(예: 긋다, 긋고, 그어서, 그어라).
# 
#     어미(ending): 용언의 어간 뒤에 붙어서 활용하면서 변하는 부분이며, 여러 문법적 기능을 수행
#     
# (2) 규칙 활용   
#     잡/어간 + 다/어미
#     
# (3) 불규칙 활용   
# 어간이 어미를 취할 때 어간의 모습이 바뀌거나 취하는 어미가 특수한 어미일 경우
