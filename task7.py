# =======================================================
# Assignment: Analyzing Data with Pandas & Matplotlib
# =======================================================

# ---- Task 0: Import Libraries ----
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris



# =======================================================
# Task 1: Load and Explore the Dataset
# =======================================================

try:
    # Load Iris dataset from sklearn
    iris = load_iris(as_frame=True)
    df = iris.frame  # Convert to pandas DataFrame
    
    print("✅ Dataset successfully loaded!")
except FileNotFoundError as e:
    print("❌ File not found. Please check the dataset path.")
except Exception as e:
    print("❌ Error loading dataset:", e)

# Display first 5 rows
print("\n--- First 5 rows ---")
print(df.head())

# Data info
print("\n--- Dataset Info ---")
print(df.info())

# Check for missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# =======================================================
# Clean the dataset
# (No missing values in Iris dataset, but showing example)
# =======================================================
df = df.dropna()  # If there were missing rows

# =======================================================
# Task 2: Basic Data Analysis
# =======================================================

# Summary statistics
print("\n--- Summary Statistics ---")
print(df.describe())

# Grouping: mean of each feature per species
grouped = df.groupby("target").mean()
print("\n--- Mean Feature Values per Species ---")
print(grouped)

# Map target numbers to species names
df["species"] = df["target"].map(dict(enumerate(iris.target_names)))

# Interesting Finding Example
print("\nObservation: Iris-virginica tends to have the largest petal length and width on average.")

# =======================================================
# Task 3: Data Visualization
# =======================================================

sns.set_style("whitegrid")

# 1. Line Chart (simulate "trend over index" for petal length)
plt.figure(figsize=(8,5))
plt.plot(df.index, df["petal length (cm)"], label="Petal Length")
plt.title("Line Chart: Petal Length Trend")
plt.xlabel("Index")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart (Average petal length per species)
plt.figure(figsize=(6,4))
df.groupby("species")["petal length (cm)"].mean().plot(kind="bar", color=["#3498db","#2ecc71","#e74c3c"])
plt.title("Average Petal Length per Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram (Sepal Length distribution)
plt.figure(figsize=(6,4))
plt.hist(df["sepal length (cm)"], bins=15, color="#9b59b6", edgecolor="black")
plt.title("Histogram: Sepal Length Distribution")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot (Sepal vs Petal length, colored by species)
plt.figure(figsize=(7,5))
sns.scatterplot(data=df, x="sepal length (cm)", y="petal length (cm)", hue="species", palette="Set2")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()

# =======================================================
# Findings & Observations
# =======================================================

print("""
Findings:
1. Iris-virginica generally has the largest petal dimensions (length & width).
2. Sepal length is more evenly distributed across species, but petal length clearly separates species.
3. The scatter plot shows species are fairly well-separated by sepal vs petal length, 
   making Iris dataset great for classification tasks.
""")
