# 📊 Automated Financial Report Generator

**Generate professional PDF financial reports with visualizations and machine learning-based forecasting.**

![Preview](reports/sample_preview.png)

---

## ✨ Features

- 📁 Upload financial datasets (CSV format)
- 📈 Plot historical revenue and net income
- 🤖 Forecast future performance using Linear Regression
- 🧾 Generate and download beautiful PDF reports
- 📊 Export summarized data as Excel
- 🎯 Filter data by year range and focus on key financials
- 📤 Power BI integration for end-to-end analytics

---

## 🚀 Technologies Used

| Tool          | Description                                         |
|---------------|-----------------------------------------------------|
| Python        | Core development language                           |
| Streamlit     | Interactive frontend web application                |
| Scikit-learn  | Linear Regression model for financial forecasting   |
| Pandas        | Data transformation and filtering                   |
| Matplotlib    | Revenue & income plotting                           |
| WeasyPrint    | HTML to PDF engine for report generation            |
| Jinja2        | PDF layout templating                               |
| Power BI      | Connect to Excel exports for advanced analytics     |

---

## 📂 Project Structure

```bash
automated-financial-report/
│
├── app.py                     # Streamlit frontend
├── main.py                   # CLI script for PDF generation
├── company_report.py         # CSV data loading and filtering
├── forecast.py               # ML model for forecasting
├── plot_company.py           # Chart creation using matplotlib
├── pdf_generator.py          # PDF generation logic
│
├── templates/
│   └── report_template.html  # Jinja2 HTML template for PDF
│
├── reports/                  # Output folder for PDFs, charts, Excel
├── data/                     # Sample financial CSV data
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation


##📥 Installation:

git clone https://github.com/tarunsai2020/automated-financial-report.git
cd automated-financial-report
python -m venv .venv
.venv\Scripts\activate  # On Windows
pip install -r requirements.txt


##▶️ Run the Application

Launch the Streamlit app:
-streamlit run app.py
Or generate PDF reports from CLI:
-python main.py


##📊 Sample Dataset

You can use the Financial Statements.csv from Kaggle to try it out.


##📁 Output Example

PDF Report: /reports/MSFT_report.pdf
Excel Export: /reports/MSFT_financials.xlsx
Chart Image: /reports/MSFT_chart.png


##🤖 Forecasting Model

Uses LinearRegression to predict:
Revenue
Net Income
Based on last N years of actual data


##📌 To Do

 Add multi-model support (Prophet, LSTM)
 Customize color themes for charts
 Deploy on Streamlit Cloud
 Build GitHub Action for auto PDF generation


##🙋‍♂️ Author

Tarun Sai Tirumala
📧 tarunsaitirumala@gmail.com


