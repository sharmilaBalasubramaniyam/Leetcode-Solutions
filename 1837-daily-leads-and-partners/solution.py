import pandas as pd

def daily_leads_and_partners(sales: pd.DataFrame) -> pd.DataFrame:
    result = sales.groupby(['date_id', 'make_name']).agg(
        unique_leads=('lead_id', 'nunique'),
        unique_partners=('partner_id', 'nunique')
    ).reset_index()
    return result

