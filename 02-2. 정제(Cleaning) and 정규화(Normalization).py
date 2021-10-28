#!/usr/bin/env python
# coding: utf-8

# * 정제(cleaning) : 갖고 있는 코퍼스로부터 노이즈 데이터를 제거한다.
# * 정규화(normalization) : 표현 방법이 다른 단어들을 통합시켜서 같은 단어로 만들어준다.
# 
# 1. 규칙에 기반한 표기가 다른 단어들의 통합
# 2. 대, 소문자 통합
# 3. 불필요한 단어의 제거(Removing Unnecessary Words)
#     (1) 등장 빈도가 적은 단어(Removing Rare words)
#     (2) 길이가 짧은 단어(Removing words with a very short length)

# In[1]:


import re
text = "I was wondering if anyone out there could enlighten me on this car."

# 길이가 1~2인 단어들을 정규 표현식을 이용하여 삭제
shortword = re.compile(r'\W*\b\w{1,2}\b')
print(shortword.sub('', text))
