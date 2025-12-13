import pandas as pd

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    p=r'^[a-zA-z0-9_]+@[A-Za-z]+[.]com$'
    valid=users[users["email"].str.match(p)]
    v_s=valid.sort_values(by='user_id')
    return v_s
    
