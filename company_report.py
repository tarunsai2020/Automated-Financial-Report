import pandas as pd

def load_company_data(filepath, company):
    df = pd.read_csv(filepath)
    df.columns = df.columns.str.strip()  # remove trailing spaces
    df = df[df["Company"] == company].sort_values("Year")
    df = df.reset_index(drop=True)
    return df
