import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    n_data = employee['salary'].sort_values(ascending=False)
    n_data = n_data.drop_duplicates()
    if N > len(n_data) or N <= 0:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    else:
        result = n_data.iloc[N-1]
        return pd.DataFrame({f'getNthHighestSalary({N})': [result]})
    
