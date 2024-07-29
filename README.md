# AccidentForecaster

AI-powered web application that allows users to input a specific input parameters like year,month etc. Upon submission, it predicts the number of traffic accidents for the given period and displays the results.

## Demo link

https://serene-thicket-27393-a24abd46fe60.herokuapp.com/

### How to Use

1. Click on or Open the link in your browser.
2. Enter the required input parameters like year and month.
3. Click on the "Predict" button to get the predicted number of traffic accidents for the given period.

or use the API endpoint
curl -X POST https://serene-thicket-27393-a24abd46fe60.herokuapp.com/predict -H "Content-Type: application/json" -d "{\"year\": 2020, \"month\": 10}"

or You can test the endpoint using Postman

#### Note

The endpoint accepts a POST request with a JSON body like this:

```
{
"year" : 2020,
"month" : 10
}
```

It returns prediction in the following format:

```
{
"prediction" : 36
}
```

## DataSource

Downloaded from
<a href="https://opendata.muenchen.de/dataset/monatszahlen-verkehrsunfaelle/resource/40094bd6-f82d-4979-949b-26c8dc00b9a7"><b>Monatszahlen Verkehrsunfälle Dataset from the München Open Data Portal</b></a>

### Libraries Used

- Flask
- Pandas
- Scikit-learn
- numpy
- matplotlib
- pickle
- Prophet

### Solution Overview

- **Downloaded Dataset**: Acquired the dataset from the München Open Data Portal.
- **Prepared Data**: Selected relevant columns and filtered records up to the year 2020.
- **Visualized Data**: Used Matplotlib to plot historical accident numbers by category.
- **Built Forecasting Model**: Developed a forecasting model using Prophet.
- **Generated Forecasts**: Predicted future accident trends with the model.
- **Evaluated Model**: Compared forecasted values with actual data to compute error metrics.

  - **Mean Absolute Error (MAE):** 5.94
  - **Root Mean Squared Error (RMSE):** 7.69

- **Created API**: Implemented a Flask API endpoint for generating predictions.
- **Developed UI**: Designed an HTML template for user input through a web interface.
