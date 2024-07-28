import pandas as pd
from prophet import Prophet
import pickle

#load preprocessed data
data = pd.read_csv('data/processed_data.csv')
# # create Categories list and types list from data
# categories = data['MONATSZAHL'].unique().tolist()
# types = data['AUSPRAEGUNG'].unique().tolist()

# Filter data for 'Alkoholunfälle' and 'insgesamt'
data_alkohol = data[(data['MONATSZAHL'] == 'Alkoholunfälle') & (data['AUSPRAEGUNG'] == 'insgesamt')]
# Prepare data for Prophet
data_alkohol_prophet = data_alkohol[['JAHR', 'MONAT', 'WERT']]
# Create 'ds' column by combining 'JAHR' and 'MONAT' into a datetime format
data_alkohol_prophet['ds'] = pd.to_datetime(data_alkohol_prophet.assign(day=1).rename(columns={'JAHR': 'year', 'MONAT': 'month'})[['year', 'month', 'day']])

data_alkohol_prophet.rename(columns={'WERT': 'y'}, inplace=True)

# Initialize and fit the model
model = Prophet()
model.fit(data_alkohol_prophet)

# Save the model
with open('model/prophet_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved successfully.")