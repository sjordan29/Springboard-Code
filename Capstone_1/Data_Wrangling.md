# Data Wrangling: Demographic and Cidery Data 

## Pre-Processing

### U.S. Census Bureau 

I gathered multiple data sets from the U.S. census bureau on city demographics, including population, income, and age distribution information. The columns of these datasets are named with codes, and a better description of the columns' contents are in separate files. I ultimately wanted to combine all of this census information into a single dataframe, but each dataset had column names with the same code number, but these codes referred to different titles for different datasets. Therefore, my first step was to rename the columns in each of the dataframes using the column descriptions provided in this other dataframe. 

### Cider Shipment Data 

The cider shipment data was provided by Bart Watson, the economist for the Brewer's Association. This was in good shape, with clear column names. No pre-processing was necessary. 


## Merging Dataframes 

My next step was merging all of my separate dataframes into a single dataframe containing all demographic and cider shipment information. The common column between the U.S. Census data and the cider data was the state name. However, in my demographic data set, city and state were contained in a single column. My first step was splitting this column into two columns, one with the city name and one with the state name.

At this point, I thought I was ready to merge the dataframes. However, I soon realized that there was an issue with the state names in the cidery data: there were leading spaces before each state name, so the merge funciton was unable to identify any overlapping state names. I was able to get rid of the leading spaces and then merge all of my data into a single dataframe. 


## Converting value types 

I realized that all of the numeric values in my dataframe were actually strings! This is no good. I converted all of the numbers to floats and all of the non-numbers to NaN to make my dataframe easier to work with. 


## Reducing the Columns 

There were way more columns in the U.S. Census data than I need. I systematically went through all of the rows I did not need for my analysis, or those that provided redundant information, and removed them. The age breakdown given by the U.S. Census bureau gave much smaller age frames than I require for my analysis: it is broken down into age groups of five years. In the end, Sociable CiderWerks will want to target cities with a high percentage and a high number of people in their twenties to thirties, and maybe stretching into their forties. I therefore combined many age columns into a much smaller number: children (people too young to drink alcoholic beverages), people in their twenties (a target population), people in their thirties (another target population), people in their forties (verging on a target population), and people fifty and older who I assume are less likely to frequent a cider taproom.


## Null values 

Finally, I dealt with null values. Upon examination, I realized that there was just one row with null values. Since I have plenty of city data, I decided to just drop this row rather than imputing data values. 
