from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import shutil
import os

def generate_pdf_report(company, df_pdf, chart_path, summary, template_dir="templates", output_path="reports"):
    os.makedirs(output_path, exist_ok=True)
    shutil.copy(chart_path, os.path.join(template_dir, os.path.basename(chart_path)))

    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("report_template.html")
    html_out = template.render(
        company=company,
        chart=os.path.basename(chart_path),
        table_data=df_pdf.fillna("").to_dict(orient="records"),
        columns=df_pdf.columns.tolist(),
        summary=summary
    )

    HTML(string=html_out, base_url=template_dir).write_pdf(os.path.join(output_path, f"{company}_report.pdf"))


# 📁 File: app.py
import streamlit as st
import pandas as pd
from company_report import load_company_data
from forecast import forecast_revenue_and_income
from plot_company import plot_financials
from pdf_generator import generate_pdf_report
import base64
import os

st.set_page_config(layout="wide")
st.title("📈 Automated Financial Report Generator")

company = st.text_input("Enter company symbol (e.g., AAPL, MSFT, AMZN):").strip().upper()
year_range = st.slider("Select year range for summary:", min_value=2009, max_value=2026, value=(2009, 2023))

if st.button("Generate Report") and company:
    df = load_company_data("data/Financial Statements.csv", company)
    if df.empty:
        st.error(f"No data found for {company}")
    else:
        df["Forecast"] = False
        forecast_df = forecast_revenue_and_income(df)
        df_combined = pd.concat([df, forecast_df], ignore_index=True)
        df_combined["Forecast"] = df_combined["Forecast"].fillna(False)

        # Filter full dataset to the selected year range
        df_summary_range = df_combined[(df_combined['Year'] >= year_range[0]) & (df_combined['Year'] <= year_range[1])]

        # Compute summary stats only from filtered range
        summary = {
            "Total Revenue": f"${df_summary_range[df_summary_range['Forecast'] == False]['Revenue'].sum():,.2f}",
            "Average Net Income": f"${df_summary_range[df_summary_range['Forecast'] == False]['Net Income'].mean():,.2f}",
            "Forecasted Revenue": f"${df_summary_range[df_summary_range['Forecast'] == True]['Revenue'].sum():,.2f}",
        }

        # Plot and generate report using the filtered data only
        chart_path = plot_financials(df_summary_range, company)
        df_pdf = df_summary_range[["Year", "Company", "Revenue", "Gross Profit", "Net Income", "Forecast"]].copy()
        generate_pdf_report(company, df_pdf, chart_path, summary)

        st.success("✅ Report Generated!")

        with open(f"reports/{company}_report.pdf", "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
            href = f'<a href="data:application/pdf;base64,{b64}" download="{company}_report.pdf">🗓️ Download PDF</a>'
            st.markdown(href, unsafe_allow_html=True)

        # ✅ Export filtered data to CSV for Power BI (avoids Excel engine issues)
        csv_path = f"reports/{company}_financials_powerbi.csv"
        df_summary_range.to_csv(csv_path, index=False)

        with open(csv_path, "rb") as f_csv:
            b64_csv = base64.b64encode(f_csv.read()).decode()
            href_csv = f'<a href="data:text/csv;base64,{b64_csv}" download="{company}_financials_powerbi.csv">📊 Download CSV for Power BI</a>'
            st.markdown(href_csv, unsafe_allow_html=True)