import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_revenue_and_income(df, forecast_years=3):
    model_revenue = LinearRegression()
    model_income = LinearRegression()

    df_train = df[df['Forecast'] == False]
    X = df_train[['Year']].values
    y_revenue = df_train['Revenue'].values
    y_income = df_train['Net Income'].values

    model_revenue.fit(X, y_revenue)
    model_income.fit(X, y_income)

    last_year = df_train['Year'].max()
    future_years = np.arange(last_year + 1, last_year + forecast_years + 1).reshape(-1, 1)

    revenue_pred = model_revenue.predict(future_years)
    income_pred = model_income.predict(future_years)

    forecast_df = pd.DataFrame({
        'Year': future_years.flatten(),
        'Company': df_train['Company'].iloc[0],
        'Revenue': revenue_pred,
        'Net Income': income_pred,
        'Forecast': True
    })

    return forecast_df