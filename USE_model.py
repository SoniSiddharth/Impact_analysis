# Libraries
import os
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
from sklearn import preprocessing

import spacy
nlp = spacy.load("en_core_web_sm")
from IPython.display import HTML
import logging
logging.getLogger('tensorflow').disabled = True 				#OPTIONAL - to disable outputs from Tensorflow

# dataset and preprocessing
import docx2txt
import nltk
from nltk.tokenize import word_tokenize
text = docx2txt.process("C:/Users/HP/Desktop/Capgemini/SampleTests.docx")
import re
text = text.lower().replace('\n', ' ').replace('\t', ' ').replace('\xa0',' ')
text = ' '.join(text.split())
text = text.split("test id : ")
text = text[1:]

# creating dictionaries for keeping embeddings and test ids
test_ids = {}
index_keeper = {}
count = 0
for i in text:
	temp = ""
	for j in i:
		if j==" ":
			break
		else:
			temp+=j
	test_ids[int(temp)] = i
	index_keeper[count] = int(temp)
	count+=1

# print(test_ids)
for j in test_ids:
	t = []
	doc = nlp(test_ids[j])
	t.append(str(doc))
	test_ids[j] = t
# print(test_ids)

# importing elmo model
# module_url = "https://tfhub.dev/google/nnlm-en-dim128/2"
embed = hub.KerasLayer("C:/Users/HP/Desktop/Capgemini", trainable= True)   # place the address of the directory in which the model is downloaded

# making embeddings
embeddings = []
for j in test_ids:
	temprary = embed(test_ids[j])											# temprary is a 2-D array returned from the embed function
	test_ids[j] = temprary[0]												# temprary contains only 1 element (list) because we are creating embeddings separately for each test case
	embeddings.append(temprary[0])


# PCA - Dimensionality reduction
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
y = pca.fit_transform(embeddings)
# print(y)


# Similarity using a graph

import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

data = [
	go.Scatter( x=[i[0] for i in y], y=[j[1] for j in y], mode='markers', text=[k for k in test_ids],
	marker=dict(
			size=16,
			color = [len(test_ids[i]) for i in test_ids], #set color equal to a variable
			opacity= 0.8,
			colorscale='Viridis',
			showscale=False
	)
	)
]
layout = go.Layout()
layout = dict(yaxis = dict(zeroline = False), xaxis = dict(zeroline = False))
fig = go.Figure(data=data, layout=layout)
file = plot(fig, filename='Sentence encode.html')


# Search Engine
from sklearn.metrics.pairwise import cosine_similarity

print("Enter some keywords or a test ID number")
search_string = input()
try:
	no = int(search_string)
	if no in test_ids:
		embeddings2 = [test_ids[int(search_string)]]
	else:
		print("You entered an invalid test ID")
except:
	embeddings2 = embed([search_string])

print("Enter the number of results expected")
results_returned = int(input())  														# showing 5 best matched test cases
if results_returned >= count:
	results_returned = count

output =[]
cosine_similarities = pd.Series(cosine_similarity(embeddings2, embeddings).flatten())
for i,j in cosine_similarities.nlargest(int(results_returned)).iteritems():
	output.append(index_keeper[i])
print(output)
