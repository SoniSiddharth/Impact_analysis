import os
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import spacy
import textract

nlp = spacy.load("en_core_web_sm")

def creat_emb(path):
# For very first formation of embeddings and id
    try:
        embeddings=np.loadtxt('embeddings.npz')                     # loading the already existing embeddings and test ids
        id=np.loadtxt('id.npz')
    except:
        id=[]                                                       # initializing the lists if they do not exist
        embeddings=[]
# Text preprocessing
    import re
    text = textract.process(path)
    text = str(text)
    text = text.lower().replace('\n', ' ').replace('\t', ' ').replace('\xa0',' ')
    text = ' '.join(text.split())
    text = text.split("test id : ")
    text = text[1:]
    lst = {}
    for i in text:
        temp = ""
        for j in i:
            if j==" ":
                break
            else:
                temp+=j
        lst[int(temp)] = i

# lst -> a dictionary containing the test ids
# loading the Universal Sentence Encoder (USE) pre-trained model 
    embed = hub.KerasLayer(r'address of the directory where model has been extracted')

# storing the text separately for each test case using their test ids
    path = r'path of the folder containing the text files of each test case separate_test_doc'

# Creating embeddings of each test case seaparately and storing it in the list of lists - embeddings
    for j in lst:
        file = str(j)+'.txt'
        dir_list = os.listdir(path)
        if(file not in dir_list):
            with open(os.path.join(path, file), 'w') as fp:
                doc = nlp(lst[j])
                print(str(doc))
                fp.write(str(doc))

    for k in dir_list:
        with open(os.path.join(path, k), 'r') as fp:
            (file, ext) = os.path.splitext(k)
            if(int(file) not in id):
                id.append(int(file))
                t=[]
                lines = fp.read()
                doc = nlp(lines)
                t.append(str(doc))
                temprary = embed(t)
                embeddings.append(temprary[0])
    # print(id)
    # print(embeddings)
    np.savetxt('embeddings.npz',embeddings)                     # an npz file for storing the embeddings
    np.savetxt('id.npz',id)                                     # an npz file to store the corresponding test ids    
    print("saved")
    # print(embeddings)

if __name__ == "__main__":
    print("Hi")
    creat_emb("SampleTests.docx")
