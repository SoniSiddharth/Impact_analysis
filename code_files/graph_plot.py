# Importing essential libraries
import os
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import spacy
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
from matplotlib.widgets import TextBox
import csv

# Loading the embeddings and test ids
embeddings=np.loadtxt('embeddings.npz')                 
id=np.loadtxt('id.npz')

# PCA - Dimensionality reduction
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
y = pca.fit_transform(embeddings)
y1 = pca.fit_transform(embeddings)
# print(y)
names1=id 
x=[i[0] for i in y]
y=[j[1] for j in y]
fig1,ax = plt.subplots()
sc1 = plt.scatter( x,y,s=50,c=[[0.2,0.4,0.7]])
# sc1 = plt.text(x+.03,y+.03,[k for k in id])

for i,txt in enumerate(id):
	ax.annotate(int(txt),(x[i],y[i]))

annot = ax.annotate("", xy=(0,0), xytext=(10,10),textcoords="offset points",
					bbox=dict(boxstyle="round", fc="w"),
					arrowprops=dict(arrowstyle="->"))
annot.set_visible(True)

default_t = pd.read_csv('threshold.csv')
X = default_t.iloc[:,:].values
threshold_testid = X[0][3]

def update_annot(ind):

	pos1 = sc1.get_offsets()[ind["ind"][0]]
	annot.xy = pos1
	annot.get_bbox_patch().set_facecolor([1,1,1])
	annot.get_bbox_patch().set_alpha(1)

def hover(event):
	vis = annot.get_visible()
	if event.inaxes == ax:
		cont, ind = sc1.contains(event)
		if cont:
			update_annot(ind)
			annot.set_visible(True)
			fig1.canvas.draw_idle()
		else:
			if vis:
				annot.set_visible(False)
				fig1.canvas.draw_idle()

def subplt(ind):
	output =[]

	def update_bnnot(ind):
		pos2 = sc2.get_offsets()[ind["ind"][0]]
		bnnot.xy = pos2
 
		bnnot.get_bbox_patch().set_facecolor([1,1,1])
		bnnot.get_bbox_patch().set_alpha(1)
	def hove(event):
		vis = bnnot.get_visible()
		if event.inaxes == bx:
			cont, ind = sc2.contains(event)
			if cont:
				update_bnnot(ind)
				bnnot.set_visible(True)
				fig2.canvas.draw_idle()
			else:
				if vis:
					bnnot.set_visible(False)
					fig2.canvas.draw_idle()

	k_largest=[]
	n=[]
	threshold=float(threshold_testid)
	cosine_similarities = pd.Series(cosine_similarity([embeddings[ind]], embeddings).flatten())
	for i,j in cosine_similarities.nlargest(len(id)).iteritems():
		output.append(int(id[int(i)]))
		if (j>threshold):
			# print(i)
			n.append(int(id[int(i)]))
			k_largest.append(y1[i])
	# print(k_largest)
	subx=[i[0] for i in k_largest]
	suby=[i[1] for i in k_largest]
	fig2,bx = plt.subplots()
	sc2 = plt.scatter(subx,suby,s=50,c=[[0.2,0.4,0.7]])
	
	for i,txt in enumerate(n):
		bx.annotate(txt,(subx[i],suby[i]))
	bnnot = bx.annotate("", xy=(0,0), xytext=(10,10),textcoords="offset points",
					bbox=dict(boxstyle="round", fc="w"),
					arrowprops=dict(arrowstyle="->"))
	bnnot.set_visible(False)
	fig2.canvas.mpl_connect("motion_notify_event", hove)
	plt.show()

def onclick(event):
		id_name=annot.get_text()
		
		if(str(event.button)=='MouseButton.RIGHT' and id_name not in names1):
			print("Please enter a valid test id")
		elif(str(event.button)=='MouseButton.RIGHT'):
			knn=input("enter k-- ")
			print(id_name)
			ind=id.index(id_name)
			subplt(ind,knn)

def submit(text):
	# print(text)
	data = str(text.split('-')[0])
	# print(data)
	if(int(data) not in id):
		print("Please enter a valid test id")
	else:
		for j in range(len(names1)):
			if(names1[j]==int(data)):
				break
		ind=j
		subplt(ind)

axbox = plt.axes([0.2, 0.005, 0.5, 0.05])
text_b = TextBox(axbox, 'Enter test-id')
text_b.on_submit(submit)
fig1.canvas.mpl_connect('button_press_event', onclick)

fig1.canvas.mpl_connect("motion_notify_event", hover)
plt.show()
