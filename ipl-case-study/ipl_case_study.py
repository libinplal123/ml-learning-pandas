import pandas as pd
df=pd.read_csv("ipl-case-study\\ipl_data.csv")
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())
# FILLING MISSING VALUES
df["match_id"].fillna(549, inplace=True)
df["season"].fillna(df["season"].mode()[0], inplace=True)
df["city"].fillna(df["city"].mode()[0], inplace=True)
df["team1"].fillna(df["team1"].mode()[0], inplace=True)
df["team2"].fillna(df["team2"].mode()[0], inplace=True)
df["winning_team"].fillna("unknown", inplace=True)
df["player_of_match"].fillna("unknown", inplace=True)
df["venue"].fillna(df["venue"].mode()[0], inplace=True)
df["runs_scored"].fillna(round(df["runs_scored"].mean()), inplace=True)
df["wickets"].fillna(round(df["wickets"].mean()), inplace=True)
print(df.isnull().sum())
# ANALYSIS
# matches per season
print("matches per season", df["season"].value_counts())
# top match count 
print("top match count season", df["season"].value_counts().idxmax())
# total match count by each team
print("winning team total matches", df["winning_team"].value_counts())
# average runs per season
print("average runs per season", df.groupby("season")["runs_scored"].mean())
# venue wise match count
print("venue wise match count", df["venue"].value_counts())
# venue wise avg runs
print("average runs by venue", df.groupby("venue")["runs_scored"].mean())
# city wise match count
print("city wise match count", df["city"].value_counts())
# city wise avg runs
print("average runs by city", df.groupby("city")["runs_scored"].mean())
# which winning team has highest average
print("highest average run of winning team", (df.groupby("winning_team")["runs_scored"].mean()).idxmax())
# top five highest venues by count
print("top five highest match counts in venues", df["venue"].value_counts().head())

