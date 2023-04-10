# Forecasting of future climate changes using ARIMA

ARIMA, as opposed to ARMA, is used when the time series display non-stationary behavior, which means that the mean and/or variance of the series is not constant over time. The ARIMA model is a generalization of the ARMA model that allows for the incorporation of the differencing of raw observations (i.e. subtracting an observation from an observation at the previous time step) in order to make the time series stationary. The ARIMA model is denoted ARIMA(p,d,q) where parameters p, d, and q are non-negative integers, p is the order of the autoregressive model, d is the degree of differencing (the number of times that the data have had past values subtracted), and q is the order of the moving-average model. The parameters of the ARIMA model are selected by minimizing a criterion, such as the Akaike information criterion (AIC) or the Schwarz criterion (SC). 

In this experiment, we use ARIMA (or more exactly, an extension called SARIMAX) to analyse and forecast multi-variate time series that denote climate change for Managua, Nicaragua. The data set can be retrieved using the following command:

$ \
source venv/bin/activate &&\
pip install -r requirements.txt && \
echo "MY_WWO_KEY" > wwo.key && \
python fetch-dataset.py

The WWO key is a World Weather Online API key, which you can get by signing up for an account at worldweatheronline.com

The dataset by default gets 1 month worth of data, from the current date to 1 month before. This is done like this to avoid exhausting API calls. You can change the number of days to fetch by changing the value of the variable days in the fetch-dataset.py file.

# How the ARIMA model is trained

We use AIC (Akaike Information Criterion) to select the best model for the data. The AIC is a measure of how well a model fits the data. The lower the AIC, the better the model fits the data. The AIC is calculated as:

AIC = 2k - 2ln(L)

where k is the number of parameters in the model and L is the maximum value of the likelihood function for the model. The AIC is a relative measure of model fit, so it can be used to compare models with different numbers of parameters. The AIC is a good measure of model fit when the sample size is large, but it can overestimate the quality of the model when the sample size is small.

We use this criterion to calculate the best order p, d, q for the ARIMA model, so we can fit the model accurately. Note that calculating the proper order is computationally expensive, so it is recommended that you use a dedicated server for computing
