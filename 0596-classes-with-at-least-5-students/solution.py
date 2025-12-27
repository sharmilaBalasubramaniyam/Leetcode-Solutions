import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    st=courses.groupby(['class']).count().reset_index()
    return st[st['student']>=5][['class']]
