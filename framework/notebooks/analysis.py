import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load dataset
df = pd.read_csv("data/metadata.csv", low_memory=False)
# url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
# df = pd.read_csv(url, low_memory=False)


# Preview
print("Shape:", df.shape)
print(df.head())

# Check missing values
print(df.isnull().sum().head())

# Clean & prepare
df['date'] = pd.to_datetime(df['date'], errors="coerce")
df['year'] = df['date'].dt.year

# Total positive cases by state
top_states = df.groupby('state')['positive'].max().sort_values(ascending=False).head(10)
plt.figure(figsize=(8,5))
sns.barplot(x=top_states.values, y=top_states.index, palette="viridis")
plt.title("Top 10 States by Total Positive Cases")
plt.xlabel("Total Positive Cases")
plt.ylabel("State")
plt.show()

# Total deaths by state
top_deaths = df.groupby('state')['death'].max().sort_values(ascending=False).head(10)
plt.figure(figsize=(8,5))
sns.barplot(x=top_deaths.values, y=top_deaths.index, palette="magma")
plt.title("Top 10 States by Total Deaths")
plt.xlabel("Deaths")
plt.ylabel("State")
plt.show()

# Time series: US-wide positive cases over time
us_total = df.groupby('date')['positive'].sum()
plt.figure(figsize=(10,5))
plt.plot(us_total.index, us_total.values, color="blue")
plt.title("Daily Positive Cases in the US")
plt.xlabel("Date")
plt.ylabel("Positive Cases")
plt.show()