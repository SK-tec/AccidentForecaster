from flask import Flask, request,jsonify, render_template
import pandas as pd
import pickle
import os
import calendar
app = Flask(__name__, template_folder='../templates')

# Load the model
model_path = os.path.join(os.path.dirname(__file__), '../model/prophet_model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])

def predict():
    if request.content_type == 'application/json':
        data = request.get_json()
        year = data['year']
        month = data['month']
        
        # Generate forecast for the specified year and month
        future_date = pd.to_datetime(f'{year}-{month}-01')
        future_df = pd.DataFrame({'ds': [future_date]})
        forecast = model.predict(future_df)
        prediction = int(forecast['yhat'].iloc[0])
        # Return JSON response
        return jsonify({'prediction': prediction})

       
    else:
        year = request.form['year']
        month = request.form['month']
        
        # Generate forecast for the specified year and month
        future_date = pd.to_datetime(f'{year}-{month}-01')
        future_df = pd.DataFrame({'ds': [future_date]})
        forecast = model.predict(future_df)
        prediction = int(forecast['yhat'].iloc[0])
        # Replace with your prediction logic
        prediction = f"Accident's Prediction: <br> Year: {year} <br> Month: {calendar.month_name[int(month)]} <br> Value: {prediction}"
        print(prediction)
        # Render HTML template with the prediction result
        return render_template('index.html', prediction=prediction)

   
if __name__ == '__main__':
    app.run()
