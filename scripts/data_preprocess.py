import pandas as pd 

#Load the dataset
traffic_data=pd.read_csv('data/monatszahlen2405_verkehrsunfaelle_export.csv')
# Select most relevant columns
traffic_data=traffic_data[['MONATSZAHL','AUSPRAEGUNG','JAHR','MONAT','WERT']]
# Drop the records which come after 2020
traffic_data=traffic_data[traffic_data['JAHR']<=2020]
#check for null value
print(traffic_data.isnull().any())
#Fill null values with 0
traffic_data['WERT']=traffic_data['WERT'].fillna(0)

# Drop the rows which contains the Summe in JAHR 
traffic_data=traffic_data[traffic_data['AUSPRAEG']!='Summe']



print(traffic_data.isnull().sum())
# Save preprocessed data
traffic_data.to_csv('data/processed_data.csv',index=False)