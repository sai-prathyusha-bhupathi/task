import pandas as p
df=p.read_csv("county_demographics.csv")
n=df.nlargest(1,['Age.Percent 65 and Older'])
print(n)