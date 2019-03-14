import nltk
import numpy as np
import random
import string


f=open('chatbot.txt','r',errors='ignore')
raw=f.read()
raw=raw.lower() 

nltk.download('punkt')
nltk.download('wordnet')

#  Tokenize the data 
sent_tokens=nltk.sent_tokenize(raw) # convert to list of sentences
word_tokens=nltk.word_tokenize(raw)# convert to list of words

#normalise the tokens

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
	return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct),None) for punct in string.punctuation)

def LemNormalize(text):
	return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#Keyword Matching

GREETING_INPUTS= ("hello","hi","greetings","sup","what's up","hey",)

GREETING_RESPONSES = ["Hi","Hey","*nods*","Hi there","Hello","I am glad! You are talking to me"]

def greeting(sentence):
	for word in sentence.split():
		if word.lower() in GREETING_INPUTS:
			return random.choice(GREETING_RESPONSES)
name_input=("your name")
name_response=["My Name is ROBO"]

def name(sentence): 
	for word in sentence.split():
		if word.lower() in name_input:
			return name_response

def response(user_response):
	robo_reponse=""
	sent_tokens.append(user_response)

	TfidVec= TfidfVectorizer(tokenizer = LemNormalize, stop_words='english')
	tfidf= TfidVec.fit_transform(sent_tokens)
	vals = cosine_similarity(tfidf[-1],tfidf)
	idx= vals.argsort() [0][-2]
	flat = vals.flatten()
	flat.sort()
	req_tfidf= flat[-2]

	if(req_tfidf==0):
		robo_response="I am sorry! I dont understand you"
		return robo_response
	else:
		robo_response = robo_reponse+sent_tokens[idx]
		return robo_response
flag=True
print("ROBO : My name is Robo. I will always answer to your queries.")
name=['whats your name','what is your name','your name']
while(flag==True):
	print("Me:",end=" ")
	user_response=input()
	user_response=user_response.lower()
	if(user_response!='bye'):
		if(user_response=='thanks' or user_response=='thank you'):
			flag=False
			print("ROBO:"+greeting(user_response))
		else:
			if(greeting(user_response)!=None):
				print("ROBO:"+greeting(user_response))
			else:
				print("ROBO:",end="")
				print(response(user_response))
				sent_tokens.remove(user_response)
	elif(user_response.lower()=='whats your name'):
		print("My name is Robo")
	else:
		flag=False
		print("ROBO: Bye! Take Care..")