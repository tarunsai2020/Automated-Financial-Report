from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import shutil
import os
from datetime import datetime

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
        summary=summary,
        generated_on=datetime.now().strftime("%B %d, %Y %I:%M %p")
    )

    HTML(string=html_out, base_url=template_dir).write_pdf(os.path.join(output_path, f"{company}_report.pdf"))
