import os
import numpy as np
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import spacy
import docx2txt

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
    text = docx2txt.process(path)
    text = text.lower().replace('\n', ' ').replace('\t', ' ').replace('\xa0',' ')
    text = ' '.join(text.split())
    text = text.split("test id : ")
    text = text[1:]
    test_ids = {}
    for i in text:
        temp = ""
        for j in i:
            if j==" ":
                break
            else:
                temp+=j
        test_ids[int(temp)] = i

# loading the Universal Sentence Encoder (USE) pre-trained model 
    embed = hub.KerasLayer("C:/Users/HP/Desktop/Capgemini", trainable= True)

# storing the text separately for each test case using their test ids
    path = r'C:/Users/HP/Desktop/Capgemini/separate_test_doc'
    dir_list = os.listdir(path)
    sep_files = {}
    for m in dir_list:
        sep_files[m] = 0

# Creating embeddings of each test case seaparately and storing it in the list of lists - embeddings
    for j in test_ids:
        file = str(j)+'.txt'
        if(file not in sep_files):
            with open(os.path.join(path, file), 'w') as fp:
                id.append(j)
                t=[]
                doc = nlp(test_ids[j])
                fp.write(str(doc))
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
    print("Process begin")
    creat_emb("C:/Users/HP/Desktop/Capgemini/main_document/SampleTests.docx")