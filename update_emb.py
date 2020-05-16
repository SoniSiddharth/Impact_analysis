import os
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import spacy
nlp = spacy.load("en_core_web_sm")
embed = hub.KerasLayer(r'C:\\Users\\Janvi Thakkar\\Desktop\\projects\\nlp_example')
def update_emb(path):
    embeddings=np.loadtxt('embeddings.npz')
    id=np.loadtxt('id.npz')
    filename = os.path.basename(path)
    (file, ext) = os.path.splitext(filename)
    tst_id = int(file)
    index_in_embedding=0
    for i in range(0,len(id)):
        if(id[i]==tst_id):
            index_in_embedding = i 
            break 
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
    update_emb(r'C:\\Users\\Janvi Thakkar\\Desktop\\projects\\Capegemini\\separate_test_doc\\2293.txt')