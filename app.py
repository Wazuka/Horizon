import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from notion_utils import get_scores_from_notion
import sys

st.set_page_config(layout="wide")
st.title("🌅 Horizon – Visualisation quotidienne des scores")

data = get_scores_from_notion()

if data.empty:
    st.warning("Aucune donnée disponible.")
    st.stop()

# 🧪 Diagnostic – Affiche les données brutes
st.write("🧪 Données brutes récupérées de Notion :")
st.write(data)

# 🔍 Diagnostic – Affiche juste la colonne des scores
st.write("📊 Scores extraits :")
st.write(data["Score TOTAL"].tolist())

# Tri chronologique
data = data.sort_values("Date")
data["Score TOTAL"] = data["Score TEST"]  # 🔧 remplacement temporaire

# Affichage du graphique (même si vide pour l’instant)
fig, ax = plt.subplots(figsize=(12, 4))

colors = ["green" if score >= 15 else "#4682B4" for score in data["Score TOTAL"]]
bars = ax.bar(data["Date"].dt.strftime("%d/%m"), data["Score TOTAL"], color=colors)

# Ligne objectif et base
ax.axhline(y=15, color="gray", linestyle="--", linewidth=1)
ax.axhline(y=0, color="black", linewidth=2)

ax.set_ylim(0, 21)
ax.set_ylabel("Score")
ax.set_xlabel("Date")
plt.xticks(rotation=45)

st.pyplot(fig)
