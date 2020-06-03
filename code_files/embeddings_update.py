import pickle
from pre_process import creat_emb

id=[]
embeddings=[]

with open('mainfile.data','rb') as filehandler:
			main = pickle.load(filehandler)  
for j in range(len(main)):
	if(j==0):
    		creat_emb(main[j],id,embeddings)
	else:
		embeddings=np.loadtxt('embeddings.npz')
		id=np.loadtxt('id.npz')
		creat_emb(main[j],id,embeddings)

 
