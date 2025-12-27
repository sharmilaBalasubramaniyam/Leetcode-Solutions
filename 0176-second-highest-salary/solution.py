import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee=employee[['salary']].drop_duplicates().sort_values(by='salary',ascending=False)
    if len(employee)>1:
        SecondHighestSalary=employee['salary'].iloc[1]
    else:
        SecondHighestSalary=None
    return pd.DataFrame({'SecondHighestSalary':[SecondHighestSalary]})
