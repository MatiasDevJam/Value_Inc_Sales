import pandas as pd

data_df = pd.read_csv('../data/transaction.csv', sep=';')

# summary of the data
data_df

# working with calculations
# defining variables

cost_per_item = data_df['CostPerItem']

number_of_item_purchased = data_df['NumberOfItemsPurchased']

cost_per_transaction = cost_per_item * number_of_item_purchased

# add a new column

data_df['CostPerTransaction'] = data_df['CostPerItem'] * data_df['NumberOfItemsPurchased']

# sales per transaction

data_df['SalesPerTransaction'] = data_df['SellingPricePerItem'] * data_df['NumberOfItemsPurchased']

# profit calculation

data_df['ProfitPerTransaction'] = data_df['SalesPerTransaction'] - data_df['CostPerTransaction']

# markup = ( sales - cost) / cost

data_df['Markup'] = ( data_df['ProfitPerTransaction'] ) / data_df['CostPerTransaction']

# round Markup

data_df['Markup'] = round(data_df['Markup'], 2)

# change column type

day = data_df['Day'].astype(str)
year = data_df['Year'].astype(str)

my_date = day + '-' + data_df['Month'] + '-' + year

data_df['Date'] = my_date

# using iloc to view specific columns / rows
data_df.iloc[0] # views the row with index = 0

data_df.iloc[0:3] # first 3 rows

data_df.iloc[-5:] # last 5 rows

data_df.head(5) # brings in first 5 rows

data_df.iloc[:,2]

data_df.iloc[4:2]

# using split to split the client_keyword field

split_column = data_df['ClientKeywords'].str.split(',', expand=True)

# creating new columns for the split columns in ClientKeywords
data_df['ClientAge'] = split_column[0]
data_df['ClientType'] = split_column[1]
data_df['LengthOfContract'] = split_column[2]

#using replace function
data_df['ClientAge'] = data_df['ClientAge'].str.replace('[', '')
data_df['LengthOfContract'] = data_df['LengthOfContract'].str.replace(']', '')

# using lowercase function

data_df['ItemDescription'] = data_df['ItemDescription'].str.lower() 

# adding a new dataset to merge files

seasons_df = pd.read_csv('../data/value_inc_seasons.csv', sep=';')

# merging files

data_df = pd.merge(data_df, seasons_df, on='Month')

# droping columns

data_df = data_df.drop('ClientKeywords', axis= 1)
data_df = data_df.drop('Day', axis= 1)
data_df = data_df.drop(['Month', 'Year'], axis= 1)

# FINAL export to CSV

data_df.to_csv('../data/ValueInc_Cleaned.csv', index= False)

data_df.info()
