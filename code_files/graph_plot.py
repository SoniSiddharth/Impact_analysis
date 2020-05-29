# Impoerting essential libraries
import os
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import spacy

# Loading the embeddings and test ids
embeddings=np.loadtxt('embeddings.npz')                 
id=np.loadtxt('id.npz')

# PCA - Dimensionality reduction
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
y = pca.fit_transform(embeddings)


# Similarity using a graph
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

data = [
	go.Scatter( x=[i[0] for i in y], y=[j[1] for j in y], mode='markers', text=[k for k in id],
	marker=dict(
			size=16,
			color = [i for i in id], #set color equal to a variable
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
