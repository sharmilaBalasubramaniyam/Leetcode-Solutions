import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    cc = orders.groupby('customer_number').size().reset_index(name='count')
    sc = cc.sort_values(by='count', ascending=False)
    mf= sc.head(1)[['customer_number']]
    return mf
