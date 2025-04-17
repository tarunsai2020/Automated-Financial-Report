import pandas as pd
from company_report import load_company_data
from plot_company import plot_financials
from pdf_generator import generate_pdf_report
from forecast import forecast_revenue_and_income

def main():
    company = input("Enter company name (e.g., AAPL, MSFT, AMZN): ").strip().upper()
    data_path = "data/Financial Statements.csv"

    # Load historical data
    df = load_company_data(data_path, company)
    if df.empty:
        print(f"No data found for company: {company}")
        return

    # Generate forecasted values
    forecast_df = forecast_revenue_and_income(df)

    # Match columns
    for col in df.columns:
        if col not in forecast_df.columns:
            forecast_df[col] = None
    forecast_df["Forecast"] = True
    forecast_df = forecast_df[df.columns]
    df["Forecast"] = False

    # Combine actual and forecast
    df_combined = pd.concat([df, forecast_df], ignore_index=True)

    # Compute summary stats
    total_revenue = df_combined.loc[~df_combined["Forecast"], "Revenue"].sum()
    avg_net_income = df_combined.loc[~df_combined["Forecast"], "Net Income"].mean()
    forecasted_revenue = df_combined.loc[df_combined["Forecast"], "Revenue"].sum()

    summary = {
        "Total Revenue": f"${total_revenue:,.2f}",
        "Average Net Income": f"${avg_net_income:,.2f}",
        "Forecasted Revenue": f"${forecasted_revenue:,.2f}"
    }

    # Generate chart
    chart_path = plot_financials(df_combined, company)

    # Generate PDF report (chart + summary only)
    generate_pdf_report(company, df_combined, chart_path, summary)

    print(f"✅ Report for {company} (with forecast) generated successfully!")

    # Export full data to Excel
    df_combined.to_excel(f"reports/{company}_financials.xlsx", index=False)
    print(f"📊 Excel export created: reports/{company}_financials.xlsx")

if __name__ == "__main__":
    main()
