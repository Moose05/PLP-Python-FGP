import pandas as pd

# Load the CSV file
df = pd.read_csv("owid-covid-data.csv")

# Show the first few rows
print(df.head())
print(df.columns)

print(df.isnull().sum())
missing_rows = df[df.isnull().any(axis=1)]
print(missing_rows)


# Load the dataset
df = pd.read_csv("owid-covid-data.csv")

# Step 1: Filter for specific countries
countries = ['South Africa', 'Nigeria', 'Kenya', 'United States']
filtered_df = df[df['location'].isin(countries)]

# Step 2: Drop rows with missing critical values
# Let's define "critical" as: missing date, total_cases, or total_deaths
filtered_df = filtered_df.dropna(subset=['date', 'total_cases', 'total_deaths'])

# Step 3: Convert 'date' column to datetime format
filtered_df['date'] = pd.to_datetime(filtered_df['date'])

# Optional: Reset index after filtering
filtered_df.reset_index(drop=True, inplace=True)

# Display the cleaned data
print(filtered_df.head())

import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("owid-covid-data.csv")

# Filter for selected countries
countries = ['South Africa', 'Nigeria', 'Kenya', 'United States']
df = df[df['location'].isin(countries)]

# Drop rows with missing date, total_cases, or total_deaths
df = df.dropna(subset=['date', 'total_cases', 'total_deaths'])

# Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'])

# Calculate death rate
df['death_rate'] = df['total_deaths'] / df['total_cases']


plt.figure(figsize=(10, 6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)
plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_deaths'], label=country)
plt.title("Total COVID-19 Deaths Over Time")
plt.xlabel("Date")
plt.ylabel("Total Deaths")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['new_cases'].fillna(0), label=country)
plt.title("Daily New COVID-19 Cases")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

latest = df.sort_values("date").groupby("location").tail(1)
latest_sorted = latest.sort_values("total_cases", ascending=False)

plt.figure(figsize=(8, 5))
sns.barplot(data=latest_sorted, x="location", y="total_cases", palette="viridis")
plt.title("Total Cases by Country (Most Recent Date)")
plt.xlabel("Country")
plt.ylabel("Total Cases")
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 6))
correlation_data = df[['total_cases', 'new_cases', 'total_deaths', 'new_deaths', 'death_rate']]
sns.heatmap(correlation_data.corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap of COVID-19 Metrics")
plt.tight_layout()
plt.show()







