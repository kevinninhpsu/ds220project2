Kevin Ninh's data analysis of world happiness and life expectancy, comparing data from 2015/2016 to 2022
In our queries, we are comparing the top 10 countries in various categories from 2015 & 2016 years compared to 2022

We are also looking at GDP, trust in government, and freedom based in 2022 to see if life expectancy and happiness are correlating to any of these three categories

# In order to run the code, you will need the 2015, 2016, and 2022 csv files.

This is the source code.

import numpy as np
import pandas as pd
import os

# List of CSV files in the directory
csv_files = ['2022.csv', '2016.csv', '2015.csv']

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
Results from running queries
-Query #1: Top 10 happiest countries in 2015 & 2016

Year Country
2015
Switzerland 7.587

  Iceland        7.561

  Denmark        7.527

  Norway         7.522

  Canada         7.427

  Finland        7.406

  Netherlands    7.378

  Sweden         7.364

  New Zealand    7.286

  Australia      7.284
2016
Denmark 7.526

  Switzerland    7.509

  Iceland        7.501

  Norway         7.498

  Finland        7.413

  Canada         7.404

  Netherlands    7.339

  New Zealand    7.334

  Australia      7.313

  Sweden         7.291
Name: Happiness Score

-Query #2: Top 10 saddest countries in 2015 & 2016 Year Country
2015
Togo 2.839

  Burundi         2.905

  Syria           3.006

  Benin           3.340

  Rwanda          3.465

  Afghanistan     3.575

  Burkina Faso    3.587

  Ivory Coast     3.655

  Guinea          3.656

  Chad            3.667
2016
Burundi 2.905

  Syria           3.069

  Togo            3.303

  Afghanistan     3.360

  Benin           3.484

  Rwanda          3.515

  Guinea          3.607

  Liberia         3.622

  Tanzania        3.666

  Madagascar      3.695
Name: Happiness Score

-Query #3: Top 10 happiest countries in 2022

   Country
0 Finland

1 Denmark

2 Iceland

3 Switzerland

4 Netherlands

5 Luxembourg*

6 Sweden

7 Norway

8 Israel

9 New Zealand

-Query #4: Top 10 highest life expectancy by countries 2015 & 2016

Year Country
2015
Singapore 1.02525

  Hong Kong      1.01328

  Japan          0.99111

  South Korea    0.96538

  Spain          0.95562

  Italy          0.95446

  Iceland        0.94784

  France         0.94579

  Switzerland    0.94143

  Australia      0.93156
2016
Hong Kong 0.95277

  Singapore      0.94719

  Japan          0.91491

  South Korea    0.88645

  Spain          0.87896

  Iceland        0.86733

  Switzerland    0.86303

  Australia      0.85120

  Italy          0.85102

  Israel         0.84917
-Query #5: Top 10 lowest life expectancy by countries 2015 & 2016

Year Country
2015
Sierra Leone 0.00000

  Botswana                    0.04776

  Central African Republic    0.06699

  Swaziland                   0.07566

  Lesotho                     0.07612

  Mozambique                  0.09131

  Congo (Kinshasa)            0.09806

  Chad                        0.15010

  Ivory Coast                 0.15185

  Nigeria                     0.16007
2016
Sierra Leone 0.00000

  Chad                        0.03824

  Ivory Coast                 0.04476

  Angola                      0.04991

  Nigeria                     0.05108

  Somalia                     0.11466

  Cameroon                    0.12698

  Burundi                     0.15747

  South Sudan                 0.15781

  Zimbabwe                    0.15950
-Query #6: Top 10 life expectancy 2022

                  Country Explained by: Healthy life expectancy
80 Hong Kong S.A.R. of China 0,942

53 Japan 0,866

26 Singapore 0,851

58 South Korea 0,841

3 Switzerland 0,822

78 North Cyprus* 0,819

40 Cyprus 0,819

8 Israel 0,818

19 France 0,808

28 Spain 0,808

-Query #7: Top 10 GDP per Capita 2022

               Country  Economy (GDP per Capita)
951 Qatar 1.82427

935 Luxembourg 1.69752

1100 Qatar 1.69042

937 Singapore 1.64555

956 Kuwait 1.61714

919 Norway 1.57744

943 United Arab Emirates 1.57352

1089 Luxembourg 1.56391

1111 Kuwait 1.55422

917 Switzerland 1.52733

-Query #8: Top 10 most free countries according to residents(2022)

               Country   Freedom
1076 Norway 0.669730

1073 Switzerland 0.665570

1217 Cambodia 0.662460

1080 Sweden 0.659800

807 Uzbekistan 0.658249

1116 Uzbekistan 0.658210

1082 Australia 0.651240

1075 Denmark 0.649380

1078 Finland 0.641690

1092 United Arab Emirates 0.641570

-Query #9: Top 10 most trustworthy countries according to residents(2022) Country Trust (Government Corruption)

1226 Rwanda 0.55191

1100 Qatar 0.52208

1067 Rwanda 0.50521

1096 Singapore 0.49210

1075 Denmark 0.48357

951 Qatar 0.48049

937 Singapore 0.46987

916 Denmark 0.44453

1080 Sweden 0.43844

1081 New Zealand 0.42922

More on Queries and Results
Query #1: Top 10 happiest countries in 2015 & 2016
The years 2015 and 2016 witnessed Switzerland, Iceland, and Denmark emerging as the top three happiest countries. These nations consistently scored high on various metrics related to happiness, including GDP per capita, social support, life expectancy, freedom, and trust in government institutions. The presence of these countries at the top reflects their stable socio-economic environments, high living standards, and robust social welfare systems.

Query #2: Top 10 saddest countries in 2015 & 2016
On the flip side, Togo, Burundi, and Syria ranked among the saddest countries in both 2015 and 2016. These nations faced numerous challenges, including political instability, economic turmoil, social unrest, and armed conflicts. The low happiness scores underscored the profound impact of such adversities on the well-being and happiness of their populations.

Query #3: Top 10 happiest countries in 2022
Fast forward to 2022, and Finland, Denmark, and Iceland continued to lead the pack as the happiest countries. Despite the global challenges posed by events like the COVID-19 pandemic, these nations maintained their high levels of happiness through effective governance, social cohesion, and resilience in the face of adversity. The COVID-19 pandemic presented unprecedented challenges to global happiness and well-being. Lockdowns, economic disruptions, social isolation, and loss of life posed significant threats to mental health and societal stability. However, countries with strong social safety nets, robust healthcare systems, and proactive government responses were better equipped to mitigate the pandemic's adverse effects on happiness and maintain a sense of resilience and solidarity among their citizens.

Query #4: Top 10 highest life expectancy by countries 2015 & 2016
In terms of life expectancy, Singapore, Hong Kong, and Japan consistently boasted the highest life expectancies in both 2015 and 2016. These countries are renowned for their advanced healthcare systems, healthy lifestyles, and access to quality medical services, contributing to the longevity of their populations.

Query #5: Top 10 lowest life expectancy by countries 2015 & 2016
In countries with low life expectancies, access to essential healthcare services is often limited, and preventable diseases are more prevalent. Poor sanitation, lack of clean water, malnutrition, and inadequate healthcare facilities contribute to high mortality rates, particularly among vulnerable populations such as children and the elderly.

Query #6: Top 10 life expectancy 2022
Moving to 2022, Hong Kong, Japan, and Singapore maintained their positions among the top countries with the highest life expectancies. Despite the challenges posed by aging populations and emerging health threats, these countries continued to invest in healthcare innovation, disease prevention, and public health initiatives to ensure the well-being of their citizens. As populations age and healthcare needs evolve, countries must adapt their healthcare systems to meet the changing demands of their citizens.

Query #7: Top 10 GDP per Capita 2022
Qatar, Luxembourg, and Singapore led the charts in terms of GDP per capita in 2022. These nations benefited from diverse economies, strategic investments, and favorable business environments, which propelled their economic growth and prosperity.GDP per capita is a widely used indicator of a country's economic performance and standard of living. It represents the average income per person in a given country and provides insights into the level of economic development, productivity, and wealth distribution.

Query #8: Top 10 most free countries according to residents(2022)
In terms of freedom, Norway, Switzerland, and Cambodia were identified as the most free countries in 2022. These nations scored high on indices measuring civil liberties, political rights, and individual freedoms, providing conducive environments for personal growth, expression, and fulfillment.

Query #9: Top 10 most trustworthy countries according to residents(2022)
When it comes to trust in government institutions, Rwanda, Qatar, and Singapore stood out as the most trustworthy countries in 2022. Citizens in these nations expressed confidence in their governments' transparency, accountability, and integrity, fostering social cohesion and stability.
