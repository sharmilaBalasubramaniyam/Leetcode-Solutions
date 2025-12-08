import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    res=views[views['author_id']==views['viewer_id']]
    res=res[['author_id']].drop_duplicates()
    return res.rename(columns={'author_id':'id'}).sort_values('id')
