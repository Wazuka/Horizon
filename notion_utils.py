import requests
import pandas as pd
from datetime import datetime

import streamlit as st

NOTION_DATABASE_ID = "22ad9baa-f013-8070-8fc2-c9268774603d"
NOTION_API_TOKEN = st.secrets["notion_token"]

def get_scores_from_notion():
    url = f"https://api.notion.com/v1/databases/{NOTION_DATABASE_ID}/query"
    headers = {
        "Authorization": f"Bearer {NOTION_API_TOKEN}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }

    res = requests.post(url, headers=headers)
    if res.status_code != 200:
        return pd.DataFrame()

    results = res.json().get("results", [])
    data = []
    for r in results:
        props = r["properties"]
        date_str = props.get("Date", {}).get("date", {}).get("start")
        score_total = props.get("Score TEST", {}).get("number", 0)
        if date_str:
            try:
                date = datetime.fromisoformat(date_str)
                data.append({"Date": date, "Score TEST": score_total})
            except:
                continue

    return pd.DataFrame(data)
