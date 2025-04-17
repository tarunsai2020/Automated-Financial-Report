import os
import matplotlib.pyplot as plt
def plot_financials(df, company, output_dir="reports"):
    os.makedirs(output_dir, exist_ok=True)

    plt.figure(figsize=(10, 6))

    actuals = df[df["Forecast"] == False]
    forecasts = df[df["Forecast"] == True]

    plt.plot(actuals["Year"], actuals["Revenue"], label="Actual Revenue", marker="o")
    plt.plot(forecasts["Year"], forecasts["Revenue"], label="Forecasted Revenue", linestyle="--", marker="x")
    
    if "Net Income" in actuals.columns:
        plt.plot(actuals["Year"], actuals["Net Income"], label="Net Income", linestyle="dotted", alpha=0.6)

    plt.title(f"{company} - Revenue (Actual vs Forecast)")
    plt.xlabel("Year")
    plt.ylabel("USD (Millions)")
    plt.legend()
    chart_path = os.path.join(output_dir, f"{company}_chart.png")
    plt.savefig(chart_path,dpi=300)
    plt.close()

    return chart_path
