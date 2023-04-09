import itertools
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.arima.model import ARIMA
from sklearn.preprocessing import OneHotEncoder

# Load data
data = pd.read_csv('managua.csv', parse_dates=['date_time'])

# Convert categorical variable "location" to dummy variables
encoder = OneHotEncoder(sparse_output=False)
location_encoded = encoder.fit_transform(data[['location']])
location_encoded_columns = [f"location_{i}" for i in range(len(encoder.categories_[0]))]
data_encoded = pd.concat([data.drop('location', axis=1), pd.DataFrame(location_encoded, columns=location_encoded_columns)], axis=1)

# Split data into train and test sets
train_size = int(len(data_encoded) * 0.8)
train_data, test_data = data_encoded[:train_size], data_encoded[train_size:]

# Fit ARIMA model
# First we need to find the best parameters for the model
# We will use the AIC (Akaike Information Criterion) to find the best parameters
# Define the range of values for the ARIMA parameters
p = d = q = P = D = Q = range(0, 6)

# Generate all possible combinations of the parameters
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0], x[1], x[2], 24) for x in list(itertools.product(P, D, Q))]

# Fit the ARIMA model and find the best parameters based on the AIC value
best_aic = np.inf
best_params = None
for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(train_data['tempC'], order=param, seasonal_order=param_seasonal, enforce_stationarity=False, enforce_invertibility=False)
            results = mod.fit()
            if results.aic < best_aic:
                best_aic = results.aic
                best_params = (param, param_seasonal)
        except:
            continue

# Fit the model with the best parameters on the training data
mod = sm.tsa.statespace.SARIMAX(train_data['tempC'], order=best_params[0], seasonal_order=best_params[1], enforce_stationarity=False, enforce_invertibility=False)
results = mod.fit()

# Make predictions on the test data using the fitted model
pred = results.get_prediction(start=test_data.index[0], end=test_data.index[-1], dynamic=False)

# Get the predicted and actual values of the test data
pred_values = pred.predicted_mean
actual_values = test_data['tempC']

# Calculate the mean squared error (MSE) and root mean squared error (RMSE) of the predictions
mse = ((pred_values - actual_values) ** 2).mean()
rmse = np.sqrt(mse)

# Store the results as a csv file, including the error metrics, the best parameters and the predictions
results_df = pd.DataFrame({'actual': actual_values, 'predicted': pred_values})
results_df.to_csv('results.csv', index=False)
with open('results.csv', 'a') as f:
    f.write(f"mse={mse}, rmse={rmse}, best_params={best_params}")

print("Finished")
