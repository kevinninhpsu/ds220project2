import numpy as np
import pandas as pd
import os

# List of CSV files in the directory
csv_files = ['2022.csv', '2021.csv', '2020.csv', '2019.csv', '2018.csv', '2017.csv', '2016.csv', '2015.csv']

# Empty list to store DataFrames
dfs = []

# Loop through each CSV file and load the data
for file_name in csv_files:
    # Extract the year from the file name
    year = int(file_name.split('.')[0])
    # Load the CSV into a DataFrame and append the year column
    df = pd.read_csv(file_name)
    df['Year'] = year
    # Append the DataFrame to the list
    dfs.append(df)

# Concatenate all DataFrames into a single DataFrame
combined_df = pd.concat(dfs, ignore_index=True)

#Queries 1 & 2: Happiest and saddest countries in year 2015 & 2016.

# Group by year and country, calculate average happiness score, and select top 10 for each year
top_10_happy_countries20152016 = combined_df.groupby(['Year', 'Country'])['Happiness Score'].mean().groupby('Year').nlargest(10).reset_index(level=0, drop=True)

# Using this dataset, it seems after 2016 the happiness scores formula changed, therefore only 2015 and 2016 can display a happiness score
#This command removes countries that have a N/A score for this certain metric
top_10_happy_countries20152016 = top_10_happy_countries20152016.dropna()

top_10_saddest_countries20152016 = combined_df.groupby(['Year', 'Country'])['Happiness Score'].mean().groupby('Year').nsmallest(10).reset_index(level=0, drop=True)

#This command removes countries that have a N/A score for this certain metric
top_10_saddest_countries20152016 = top_10_saddest_countries20152016.dropna()


# Display top 10 happiest and saddest countries in 2015&2016
print("Query #1: Top 10 happiest countries in 2015 & 2016")
print(top_10_happy_countries20152016)

print("\nQuery #2: Top 10 saddest countries in 2015 & 2016")
print(top_10_saddest_countries20152016)

# Load the 2022 CSV file into a DataFrame
df_2022 = pd.read_csv('2022.csv')

# Convert "Happiness score" column to numeric
df_2022['Happiness score'] = pd.to_numeric(df_2022['Happiness score'], errors='coerce')

# Select the top 10 happiest countries based on the "Happiness score" column
top_10_happy_2022 = df_2022.nlargest(10, 'Happiness score')[['Country']]

# Select the top 10 saddest countries based on the "Happiness score" column
top_10_sad_2022 = df_2022.nsmallest(10, 'Happiness score')[['Country']]

#Query 3: Happiest countries in 2022

# Display the top 10 happiest countries in 2022
print("\nQuery #3: Top 10 happiest countries in 2022")
print(top_10_happy_2022)

#Query 4: Largest life expectancy in 2015 & 2016

top_10_life_expectancy_countries20152016 = combined_df.groupby(['Year', 'Country'])['Health (Life Expectancy)'].mean().groupby('Year').nlargest(10).reset_index(level=0, drop=True)

#This command removes countries that have a N/A score for this certain metric
top_10_life_expectancy_countries20152016 = top_10_life_expectancy_countries20152016.dropna()

print("\nQuery #4: Top 10 highest life expectancy by countries 2015 & 2016")

print(top_10_life_expectancy_countries20152016)

#Query 5: Lowest life expectancy in 2015 & 2016

top_10_lowest_life_expectancy_countries20152016 = combined_df.groupby(['Year', 'Country'])['Health (Life Expectancy)'].mean().groupby('Year').nsmallest(10).reset_index(level=0, drop=True)

top_10_lowest_life_expectancy_countries20152016 = top_10_lowest_life_expectancy_countries20152016.dropna()

print("\nQuery #5: Top 10 lowest life expectancy by countries 2015 & 2016")

print(top_10_lowest_life_expectancy_countries20152016)

#Query 6: Largest life expectancy in 2022

# Combine country names with life expectancy data
life_expectancy_with_country_2022 = df_2022[['Country', 'Explained by: Healthy life expectancy']]

# Sort the DataFrame by life expectancy in descending order and select the top 10
print("\n")
top_10_life_expectancy_2022 = life_expectancy_with_country_2022.sort_values(by='Explained by: Healthy life expectancy', ascending=False).head(10)

# Display the top 10 countries with the highest life expectancy in 2022
print("Query #6: Top 10 life expectancy 2022")
print(top_10_life_expectancy_2022)

#Query 7: Countries with top 10 GDP per capita in 2022

# Select the subset of columns from the DataFrame and create a copy

top_10_GDP_per_capita_2022 = combined_df[['Country', 'Economy (GDP per Capita)']].copy()

# Convert the "Explained by: GDP per capita" column to numeric

top_10_GDP_per_capita_2022['Economy (GDP per Capita)'] = pd.to_numeric(top_10_GDP_per_capita_2022['Economy (GDP per Capita)'], errors='coerce')

# Sort the DataFrame by GDP per capita in descending order and select the top 10

top_10_GDP_per_capita_2022 = top_10_GDP_per_capita_2022.sort_values(by='Economy (GDP per Capita)', ascending=False).head(10)

# Drop rows with missing or invalid values

#This command removes countries that have a N/A score for this certain metric
top_10_GDP_per_capita_2022 = top_10_GDP_per_capita_2022.dropna()

# Print the resulting DataFrame
print("\nQuery #7: Top 10 GDP per Capita 2022")
print(top_10_GDP_per_capita_2022)

#Query 8: Freedom in 2022, ranked by countries

# Select the subset of columns from the DataFrame and create a copy

top_10_most_free_2022 = combined_df[['Country', 'Freedom']].copy()

# Convert the "Freedom" column to numeric

top_10_most_free_2022['Freedom'] = pd.to_numeric(top_10_most_free_2022['Freedom'], errors='coerce')

# Sort the DataFrame by freedom in descending order and select the top 10

top_10_most_free_2022 = top_10_most_free_2022.sort_values(by='Freedom', ascending=False).head(10)

# Drop rows with missing or invalid values

#This command removes countries that have a N/A score for this certain metric
top_10_most_free_2022 = top_10_most_free_2022.dropna()

# Print the resulting DataFrame
print("\nQuery #8: Top 10 most free countries according to residents(2022)")
print(top_10_most_free_2022)

#Query 9: Government trust in 2022

# Select the subset of columns from the DataFrame and create a copy

top_10_most_trustworthy_2022 = combined_df[['Country', 'Trust (Government Corruption)']].copy()

# Convert the "Trust (Government Corruption)" column to numeric

top_10_most_trustworthy_2022['Trust (Government Corruption)'] = pd.to_numeric(top_10_most_trustworthy_2022['Trust (Government Corruption)'], errors='coerce')

# Sort the DataFrame by Trust (Government Corruption) in descending order and select the top 10

top_10_most_trustworthy_2022 = top_10_most_trustworthy_2022.sort_values(by='Trust (Government Corruption)', ascending=False).head(10)

# Drop rows with missing or invalid values

#This command removes countries that have a N/A score for this certain metric
top_10_most_trustworthy_2022 = top_10_most_trustworthy_2022.dropna()

# Print the resulting DataFrame
print("\nQuery #9: Top 10 most trustworthy countries according to residents(2022)")
print(top_10_most_trustworthy_2022)