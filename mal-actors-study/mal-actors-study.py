import pandas as pd
df=pd.read_csv("mal-actors-study\\malayalam_actors_actresses.csv")
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())
# all actors name and gender
print(df[["name","gender"]])
# debut year for each actor
print(df[["name","debut_year"]])
# avg age for actors
actors=df[df["gender"]=="Male"]
print(actors["age"].mean())
# avg age for actresses
actresses=df[df["gender"]=="Female"]
print(actresses["age"].mean())
# actor with max no. of films
print(df.loc[df["no_of_films"].idxmax()])
# max no. of awards
print(df.loc[df["no_of_awards"].idxmax()])
# place of birth and count
print(df["place_of_birth"].value_counts())