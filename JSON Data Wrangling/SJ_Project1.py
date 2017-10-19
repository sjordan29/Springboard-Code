# Slide Rule Exercise: Springboard Data Wrangling 
# Sarah Jordan

# Import necessary packages

import pandas as pd
import json
from pandas.io.json import json_normalize

# Open json as a string

#json.load((open('data/world_bank_projects.json')))


# Create a dataframe 
world_bank_projects_df = pd.read_json('data/world_bank_projects.json')


# Question 1: find the 10 countries with the most projects 
print("The 10 countries with the most projects are:")
print(world_bank_projects_df['countryname'].value_counts().head(10))

# Africa is not a country
# So the 10 countries ith the most projects will be:
print("Excluding Africa, which is not a country, the 10 countries with the most projects are:")
print(world_bank_projects_df['countryname'].value_counts().drop('Africa').head(10))

# Question 2: Find the top 10 major project themes
major_theme = json.load((open('data/world_bank_projects.json')))
major_theme_norm = json_normalize(major_theme, 'mjtheme_namecode')

print("The top 10 major project themes are:")
print(major_theme_norm.name.value_counts()[:10])

# The 7th most common major project theme is blank
# Find the blank entries
blank = major_theme_norm.name == ''
blank_codes = major_theme_norm.code[blank]
# print(blank_codes)

# Find out how many unique names and number codes exist
unique_names = pd.Series(major_theme_norm.name.unique())
# print(unique_names)
unique_codes = pd.Series(major_theme_norm.code.unique())
# print(unique_codes)

# Explore major_theme_norm to find corresponding code and name pairs
# print(major_theme_norm.head(15))

# Make unique_codes list that matches the order found in major_theme_norm 
part1 = pd.Series(unique_codes[0:6])
part1[6] = '11'
part2 = pd.Series(unique_codes[6:11]) 

code_reference = pd.concat([part1,part2],ignore_index='TRUE')


# Make a reference data frame to pair corresponding codes and themes 
reference = pd.DataFrame([code_reference,unique_names])

reference_df = pd.DataFrame([code_reference, unique_names])
reference_df = reference_df.transpose()

# Need to drop index 1 to get rid of the blank entry
reference_df = reference_df.drop(1)
reference_df = reference_df.reset_index(drop=True)
reference_df.columns = ['code', 'name']

# Merge reference_df with major_theme_norm to fill in missing names
complete = pd.merge(major_theme_norm,reference_df, on = ['code'], right_index = True, how= 'outer', suffixes = ('_original', '_filled'))
complete = complete.sort_index()

print("The top 10 major project themes -- excluding blanks -- are:")
#print(complete.name.value_counts()[:10])
#print(complete.head(10))
print(complete.name_filled.value_counts()[:10])
