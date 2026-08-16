#from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=300)

documents =[]

query="Tell me about virat kohli"

doc_embeddings = embedding.embed_documents(documents) #5 vectors

query_embedding = embedding.embed_query(query) #1 vector

scores = cosine_similarity([query_embedding],doc_embeddings)[0] # pass in 2d list doc_embedding is already in 2d 

print(list(enumerate(scores))) #index attached

index,score = sorted(list(enumerate(scores)),key=lambda x : x[1][-1])  #ascending order highest similarity score will be at last
print(query)
print(documents[index])
print("Similarity Score is:",score)







