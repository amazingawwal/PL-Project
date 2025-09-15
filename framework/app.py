import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("US COVID-19 Data Explorer")
st.write("Interactive exploration of COVID-19 cases and deaths by state")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("data/metadata.csv", low_memory=False)
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['year'] = df['date'].dt.year
    return df

df = load_data()

# Sidebar filter
year_min, year_max = int(df['year'].min()), int(df['year'].max())
year_range = st.slider("Select Year Range", year_min, year_max, (2020, 2021))

filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

st.subheader("Sample Data")
st.dataframe(filtered.head())

# Top 10 states by positive cases
st.subheader("Top 10 States by Total Positive Cases")
top_states = filtered.groupby('state')['positive'].max().sort_values(ascending=False).head(10)
fig, ax = plt.subplots()
sns.barplot(x=top_states.values, y=top_states.index, ax=ax, palette="viridis")
ax.set_xlabel("Total Positive Cases")
ax.set_ylabel("State")
st.pyplot(fig)

# Top 10 states by deaths
st.subheader("Top 10 States by Total Deaths")
top_deaths = filtered.groupby('state')['death'].max().sort_values(ascending=False).head(10)
fig, ax = plt.subplots()
sns.barplot(x=top_deaths.values, y=top_deaths.index, ax=ax, palette="magma")
ax.set_xlabel("Total Deaths")
ax.set_ylabel("State")
st.pyplot(fig)

# Time series: US-wide positive cases
st.subheader("Daily Positive Cases in the US")
us_total = filtered.groupby('date')['positive'].sum()
fig, ax = plt.subplots(figsize=(10,5))
ax.plot(us_total.index, us_total.values, color="blue")
ax.set_xlabel("Date")
ax.set_ylabel("Positive Cases")
ax.set_title("Daily Positive Cases in the US")
st.pyplot(fig)
