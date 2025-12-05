import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    condition = (employees['employee_id'] % 2 == 1) & (~employees['name'].str.startswith('M'))
    employees['bonus'] = employees.apply(
        lambda row: row['salary'] if condition.loc[row.name] else 0, axis=1
    )
    return employees[['employee_id', 'bonus']].sort_values('employee_id')
