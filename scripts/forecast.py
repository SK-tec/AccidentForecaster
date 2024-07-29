import pandas as pd
from prophet import Prophet
import pickle
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

#load preprocessed data
data = pd.read_csv('data/processed_data.csv')


# Filter data for 'Alkoholunfälle' and 'insgesamt'
data_alkohol = data[(data['MONATSZAHL'] == 'Alkoholunfälle') & (data['AUSPRAEGUNG'] == 'insgesamt')]
# Prepare data for Prophet
data_alkohol_prophet = data_alkohol[['JAHR', 'MONAT', 'WERT']].copy()
# Create 'ds' column by combining 'JAHR' and 'MONAT' into a datetime format
data_alkohol_prophet['ds'] = pd.to_datetime(data_alkohol_prophet.assign(day=1)[['JAHR', 'MONAT', 'day']].rename(columns={'JAHR': 'year', 'MONAT': 'month'}))

data_alkohol_prophet.rename(columns={'WERT': 'y'}, inplace=True)

# Initialize and fit the model
model = Prophet()
model.fit(data_alkohol_prophet)

# Save the model
with open('model/prophet_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved successfully.")
#Model evaluation and compute error

# Make dataframe for predictions
predicted_df = model.make_future_dataframe(periods=12, freq='MS')
forecast = model.predict(predicted_df)
#merge actual data and predicated data
merged_df = pd.merge(data_alkohol_prophet, forecast[['ds', 'yhat']],on='ds', how='left')

# Drop rows where actual values are not available (for future dates)
merged_df.dropna(subset=['y'], inplace=True)

# Compute error metrics
mae = mean_absolute_error(merged_df['y'], merged_df['yhat'])
rmse = np.sqrt(mean_squared_error(merged_df['y'], merged_df['yhat']))

print(f'Mean Absolute Error (MAE): {mae: .2f}')
print(f'Root Mean Squared Error (RMSE): {rmse: .2f}')