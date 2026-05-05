import streamlit as st
import pandas as pd
import numpy as np

# 1. DEFINÍCIA TEXTOV (Slovník pre SK a CZ)
lang_dict = {
    "Slovenčina": {
        "title": "Herd AI Studio - Inteligentná Farma",
        "sidebar_data": "📁 Zdroje dát",
        "upload_label": "Nahrať súbor (CSV alebo Excel)",
        "status_label": "📊 Stav stáda",
        "demo_info": "Aktuálne vidíte ukážkové dáta. Nahrajte vlastné pre analýzu.",
        "chat_title": "💬 AI Konzultant nad stádom",
        "chat_placeholder": "Pýtajte sa na vaše stádo...",
        "studio_title": "🛠️ Štúdio nástrojov",
        "mating_tool": "🧬 Inteligentný priparovák",
        "mating_btn": "Vytvoriť návrh párenia",
        "prediction": "📈 Predikcia plemenných hodnôt",
        "download_btn": "📥 Stiahnuť plán pre inseminátora (PDF)"
    },
    "Čeština": {
        "title": "Herd AI Studio - Inteligentní Farma",
        "sidebar_data": "📁 Zdroje dat",
        "upload_label": "Nahrát soubor (CSV nebo Excel)",
        "status_label": "📊 Stav stáda",
        "demo_info": "Aktuálně vidíte ukázková data. Nahrát vlastní pro analýzu.",
        "chat_title": "💬 AI Konzultant nad stádem",
        "chat_placeholder": "Ptejte se na vaše stádo...",
        "studio_title": "🛠️ Studio nástrojů",
        "mating_tool": "🧬 Inteligentní připařovák",
        "mating_btn": "Vytvořit návrh páření",
        "prediction": "📈 Predikce plemenných hodnot",
        "download_btn": "📥 Stáhnout plán pro inseminátora (PDF)"
    }
}

# 2. NASTAVENIE STRÁNKY
st.set_page_config(layout="wide", page_title="Herd AI Studio")

with st.sidebar:
    selected_lang = st.selectbox("🌍 Vyberte jazyk / Vyberte jazyk", ["Slovenčina", "Čeština"])
    t = lang_dict[selected_lang]

# --- VIZUÁLNY ŠTÝL (Tmavý režim) ---
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: white; }
    .stButton>button { width: 100%; border-radius: 8px; height: 3em; background-color: #16a34a; color: white; border: none; font-weight: bold; }
    .stButton>button:hover { background-color: #15803d; border: none; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. ROZLOŽENIE APLIKÁCIE ---
with st.sidebar:
    st.divider()
    st.title(t["sidebar_data"])
    uploaded_file = st.file_uploader(t["upload_label"], type=["csv", "xlsx"])
    
    if uploaded_file:
        df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('csv') else pd.read_excel(uploaded_file)
        st.success(f"Dáta: {len(df)} zvierat")
    else:
        # Demo dáta pre štart
        df = pd.DataFrame({
            'Ušné číslo': [f"SK {np.random.randint(1000, 9999)}" for _ in range(5)],
            'Mlieko (kg)': np.random.randint(7000, 11000, 5),
            'Somatické bunky': np.random.randint(80, 400, 5)
        })
        st.info(t["demo_info"])

col_chat, col_studio = st.columns([2, 1])

# --- STRED: CHAT ---
with col_chat:
    st.subheader(t["chat_title"])
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Dobrý deň! Som váš digitálny šľachtiteľ. Čo vás dnes zaujíma?"}]

    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.write(m["content"])

    if prompt := st.chat_input(t["chat_placeholder"]):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.write(prompt)
        
        response = f"Analyzujem vaše dáta ohľadom: '{prompt}'. Táto funkcia bude aktívna po prepojení s AI mozgom."
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"): st.write(response)

# --- VPRAVO: ŠTÚDIO ---
with col_studio:
    st.subheader(t["studio_title"])
    with st.expander(t["mating_tool"], expanded=True):
        st.selectbox("Priorita", ["Produkcia", "Zdravie", "Exteriér"])
        if st.button(t["mating_btn"]):
            st.success("Analýza prebieha...")
            st.table(df.head(3))
    
    with st.expander(t["prediction"]):
        st.line_chart(np.random.randn(15, 1).cumsum())
    
    st.button(t["download_btn"])
