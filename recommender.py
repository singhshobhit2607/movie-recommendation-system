import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
df=pd.read_csv("movies_metadata.csv")
df.head()
df.shape
df.isnull().sum() 
df=df.drop_duplicates().reset_index(drop=True)
print(df.duplicated().sum())
df=df[['title','overview','tagline','genres','vote_average','popularity']]
df=df.dropna(subset=["title"])
df['overview']=df['overview'].fillna('')
df.iloc[0]['genres']
import ast
df['genres']=df['genres'].apply(lambda x:" ".join([i['name']for i in ast.literal_eval(x)]))
df.head()
df['tagline']=df['tagline'].fillna("")
df.isnull().sum()
df["tags"]=df['overview']+" "+df['genres']+" "+df['tagline']
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
nltk.download("stopwords")
nltk.download('wordnet')
stop_words=set(stopwords.words('english'))
lemmatizer=WordNetLemmatizer()
def preprocess_text(text):
    text=str(text).lower()
    text=re.sub(r'[^a-zA-Z\s]','',text)
    words=text.split()
    words=[word for word in words if word not in stop_words]
    words=[lemmatizer.lemmatize(word)for word in words]
    return " ".join(words)
df['tags']=df['tags'].apply(preprocess_text)
df=df.reset_index(drop=True)
indices=pd.Series(df.index,index=df['title']).drop_duplicates()
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf=TfidfVectorizer(stop_words="english",max_features=50000,ngram_range=(1,2))
tfidf_matrix=tfidf.fit_transform(df['tags'])

#cosine similarity 
from sklearn.metrics.pairwise import cosine_similarity
def recommend(title,n=10):
    if title not in indices:
        return ['Movie not found']
    idx=indices[title]
    sim_score=cosine_similarity(tfidf_matrix[idx],tfidf_matrix).flatten()
    similar_index=sim_score.argsort()[::-1][1:n+1]
    return df['title'].iloc[similar_index]
recommend('Toy Story')


import pickle
pickle.dump(tfidf_matrix,open('tfidf_matrix.pkl','wb'))
pickle.dump(indices,open('indices.pkl','wb'))
df.to_pickle('df.pkl')
pickle.dump(tfidf,open("tfidf.pkl","wb"))