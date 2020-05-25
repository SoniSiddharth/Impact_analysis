import os
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import spacy

nlp = spacy.load("en_core_web_sm")

# calling the USE model
embed = hub.KerasLayer(r'model_use')

# a function for updating the embeddings of the test cases which have been updated
def update_emb(path):
# loading stored embeddings and test ids
    embeddings=np.loadtxt('embeddings.npz')
    id=np.loadtxt('id.npz')

    filename = os.path.basename(path)
    (file, ext) = os.path.splitext(filename)
    tst_id = int(file)
    index_in_embedding=0

# searching for the index of updated test case 
    for i in range(0,len(id)):
        if(id[i]==tst_id):
            index_in_embedding = i 
            break 
# creating the embeddings of the test case again using the USE model
    with open(path, 'r') as fp:
        t=[]
        lines = fp.read()
        doc = nlp(lines)
        t.append(str(doc))
        temprary = embed(t) 
        embeddings[index_in_embedding]=temprary[0]
        print('embeddings updated')

    np.savetxt('embeddings.npz',embeddings)
    np.savetxt('id.npz',id)
    print('embeddings saved')

if __name__ == "__main__":
    print("Hi")
    update_emb(r'path of the text file of the altered test case')
