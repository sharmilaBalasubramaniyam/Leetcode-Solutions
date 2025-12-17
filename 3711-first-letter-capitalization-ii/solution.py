import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    def cap_text(text:str)->str:
        ws=text.split(" ")
        nw=[]
        for w in ws:
            if "-" in w:
                p=w.split("-")
                p=[ps.capitalize() for ps in p]
                nw.append("-".join(p))
            else:
                nw.append(w.capitalize())
        return " ".join(nw)
    
    user_content["converted_text"]=user_content["content_text"].apply(cap_text)
    user_content["original_text"]=user_content["content_text"]
    return user_content[["content_id","original_text","converted_text"]]
