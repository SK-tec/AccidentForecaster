import pandas as pd 

#Load the dataset
traffic_accidents_df=pd.read_csv('data/monatszahlen2405_verkehrsunfaelle_export.csv')
# Select most relevant columns
traffic_accidents_df=traffic_accidents_df[['MONATSZAHL','AUSPRAEGUNG','JAHR','MONAT','WERT']]
# Drop the records which come after 2020
traffic_accidents_df=traffic_accidents_df[traffic_accidents_df['JAHR']<=2020]
#check for null value
print(traffic_accidents_df.isnull().any())
#Fill null values with 0
traffic_accidents_df['WERT']=traffic_accidents_df['WERT'].fillna(0)
# Check for null values again
print("Null values after handling:")
print(traffic_accidents_df.isnull().sum())
# Save preprocessed data
traffic_accidents_df.to_csv('data/processed_data.csv',index=False)