import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from notion_utils import get_scores_from_notion

st.set_page_config(layout="wide")
st.title("🌅 Horizon – Visualisation quotidienne des scores")

data = get_scores_from_notion()

if data.empty:
    st.warning("Aucune donnée disponible.")
    st.stop()

data = data.sort_values("Date")

fig, ax = plt.subplots(figsize=(12, 4))
colors = ["green" if score >= 15 else "#4682B4" for score in data["Score TOTAL"]]
bars = ax.bar(data["Date"].dt.strftime("%d/%m"), data["Score TOTAL"], color=colors)

# Ligne objectif
ax.axhline(y=15, color="gray", linestyle="--", linewidth=1)
ax.axhline(y=0, color="black", linewidth=2)

ax.set_ylim(0, max(20, data["Score TOTAL"].max() + 2))
ax.set_ylabel("Score")
ax.set_xlabel("Date")
plt.xticks(rotation=45)
st.pyplot(fig)
