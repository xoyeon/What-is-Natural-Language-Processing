#!/usr/bin/env python
# coding: utf-8

# In[1]:


# word_tokenize를 사용해서 NLTK에서는 아포스트로피를 어떻게 처리하는지 확인
import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize
print(word_tokenize("Don't be fooled by the dark sounding name, Mr.Jone's Orphanage is as cheery as cheery goes for a pastry shop."))


# In[2]:


# WordPunctTokenizer를 사용해서 NLTK에서는 아포스트로피를 어떻게 처리하는지 확인
from nltk.tokenize import WordPunctTokenizer  
print(WordPunctTokenizer().tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))


# In[3]:


# 케라스의 text_to_word_sequence로 토큰화 수행
from tensorflow.keras.preprocessing.text import text_to_word_sequence
print(text_to_word_sequence("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))


# In[4]:


# Penn Treebank Tokenization
## 규칙 1. 하이푼으로 구성된 단어는 하나로 유지한다.
##규칙 2. doesn't와 같이 아포스트로피로 '접어'가 함께하는 단어는 분리해준다.

from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
text = "Starting a home-based restaurant may be an ideal. it doesn't have a food chain or restaurant of their own."
print(tokenizer.tokenize(text))


# In[5]:


# NLTK의 sent_tokenize를 사용하여 문장 토큰화 실습
from nltk.tokenize import sent_tokenize
text = "His barber kept his word. But keeping such a huge secret to himself was driving him crazy. Finally, the barber went up a mountain and almost to the edge of a cliff. He dug a hole in the midst of some reeds. He looked about, to make sure no one was near."
print(sent_tokenize(text))


# In[6]:


from nltk.tokenize import sent_tokenize
text = "I am actively looking for Ph.D. students. and you are a Ph.D student."
print(sent_tokenize(text))

### NLTK는 단순히 마침표를 구분자로 하여 문장을 구분하지 않았기 때문에, Ph.D.를 문장 내의 단어로 인식하여 성공적으로 인식


# In[8]:


# KSS(Korean Sentence Splitter를 사용하여 한국어 문장 토큰화
import kss
text = '딥 러닝 자연어 처리가 재미있기는 합니다. 그런데 문제는 영어보다 한국어로 할 때 너무 어렵습니다. 이제 해보면 알걸요?'
print(kss.split_sentences(text))
#### AttributeError: 'NoneType' object has no attribute 'do_analysis' / kss.Version: 3.3.0


# In[9]:


# 마침표의 처리를 위해서 입력에 따라 두 개의 클래스로 분류하는 이진 분류기(binary classifier)를 사용하기도 함.
## 1. 마침표(.)가 단어의 일부분일 경우. 즉, 마침표가 약어(abbreivation)로 쓰이는 경우
## 2. 마침표(.)가 정말로 문장의 구분자(boundary)일 경우


# In[10]:


# NLTK를 이용한 영어 토큰화 실습


# In[11]:


from nltk.tokenize import word_tokenize
text = "I am actively looking for Ph.D. students. and you are a Ph.D. student."
print(word_tokenize(text))


# In[12]:


nltk.download('averaged_perceptron_tagger')

from nltk.tag import pos_tag
tokenized_sentence = word_tokenize(text)
print(pos_tag(tokenized_sentence))


# In[13]:


# KoNLPy를 이용한 한국어 토큰화 실습
## -- Okt(Open Korea Text), 메캅(Mecab), 코모란(Komoran), 한나눔(Hannanum), 꼬꼬마(Kkma
import konlpy
### tweepy 버전 오류. pip install tweepy==3.10.0 로 해결


# In[14]:


from konlpy.tag import Okt
okt = Okt()

# morphs : 형태소 추출
print(okt.morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))


# In[15]:


# pos : 품사 태깅(Part-of-speech tagging)
print(okt.pos("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))


# In[16]:


# nouns : 명사 추출
print(okt.nouns("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))


# In[17]:


from konlpy.tag import Kkma  
kkma = Kkma()  
print(kkma.morphs("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))


# In[18]:


print(kkma.pos("열심히 코딩한 당신, 연휴에는 여행을 가봐요"))


# In[19]:


print(kkma.nouns("열심히 코딩한 당신, 연휴에는 여행을 가봐요")) 

