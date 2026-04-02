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
df['overview']=df['overfiew'].fillna('')
df.iloc[0]['genres']