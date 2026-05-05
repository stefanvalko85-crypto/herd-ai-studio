import streamlit as st
import pandas as pd
import numpy as np

# 1. NASTAVENIE STRÁNKY
st.set_page_config(layout="wide", page_title="Herd AI Studio", page_icon="🧬")

# 2. DEFINÍCIA TEXTOV (Slovník)
lang_dict = {
    "Slovenčina": {
        "sidebar_data": "📂 ZDROJE DÁT",
        "upload_label": "Nahrať kontrolu úžitkovosti (CSV/XLSX)",
        "chat_title": "💬 AI AGRO KONZULTANT",
        "chat_placeholder": "Pýtajte sa na vaše stádo...",
        "studio_title": "🛠️ ANALYTICKÉ ŠTÚDIO",
        "mating_tool": "🧬 Inteligentný priparovák",
        "mating_btn": "SPUSTIŤ OPTIMALIZÁCIU",
        "prediction": "📈 Trend genetického zisku",
        "download_btn": "📥 EXPORTOVAŤ PLÁN PÁRENIA"
    },
    "Čeština": {
        "sidebar_data": "📂 ZDROJE DAT",
        "upload_label": "Nahrát kontrolu užitkovosti (CSV/XLSX)",
        "chat_title": "💬 AI AGRO KONZULTANT",
        "chat_placeholder": "Ptejte se na vaše stádo...",
        "studio_title": "🛠️ ANALYTICKÉ STUDIO",
        "mating_tool": "🧬 Inteligentní připařovák",
        "mating_btn": "SPUSTIT OPTIMALIZACI",
        "prediction": "📈 Trend genetického zisku",
        "download_btn": "📥 EXPORTOVAT PLÁN PÁŘENÍ"
    }
}

# 3. CUSTOM CSS PRE PROFESIONÁLNY VZHĽAD
st.markdown("""
    <style>
    /* Hlavné pozadie */
    .stApp {
        background-color: #0f172a;
        color: #f8fafc;
    }
    /* Úprava bočného panelu */
    [data-testid="stSidebar"] {
        background-color: #1e293b;
        border-right: 1px solid #334155;
    }
    /* Karty a kontajnery */
    div.stChatMessage {
        background-color: #1e293b;
        border-radius: 15px;
        border: 1px solid #334155;
        margin-bottom: 10px;
    }
    /* Tlačidlá - NotebookLM Štýl */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3.5em;
        background-color: #10b981;
        color: white;
        border: none;
        font-weight: 700;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #059669;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
    }
    /* Expander (harmonika) */
    .streamlit-expanderHeader {
        background-color: #1e293b;
        border-radius: 10px;
        border: 1px solid #334155;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. LOGIKA JAZYKA
with st.sidebar:
    st.image("https://www.svgrepo.com/show/484437/cow.svg", width=60) # Provizórne logo
    st.title("Herd AI")
    selected_lang = st.selectbox("🌍 Jazyk / Jazyk", ["Slovenčina", "Čeština"])
    t = lang_dict[selected_lang]
    st.divider()
    st.subheader(t["sidebar_data"])
    uploaded_file = st.file_uploader(t["upload_label"], type=["csv", "xlsx"])
    
    if uploaded_file:
        st.success("Dáta pripravené")
    else:
        st.info("Nahrajte dáta pre analýzu")

# 5. ROZLOŽENIE PLOCHY
col_main, col_tools = st.columns([2.2, 1])

with col_main:
    st.markdown(f"### {t['chat_title']}")
    
    # Simulačné okno chatu
    chat_container = st.container()
    with chat_container:
        if "messages" not in st.session_state:
            st.session_state.messages = [{"role": "assistant", "content": "Systém pripravený. Čakám na vaše inštrukcie k stádu."}]
        
        for m in st.session_state.messages:
            with st.chat_message(m["role"]):
                st.write(m["content"])

    if prompt := st.chat_input(t["chat_placeholder"]):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.write(prompt)
        
        response = "Spracovávam genetické dáta... (Tento model bude plne aktívny po prepojení Gemini API)."
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"): st.write(response)

with col_tools:
    st.markdown(f"### {t['studio_title']}")
    
    with st.expander(f"**{t['mating_tool']}**", expanded=True):
        st.write("Cieľ šľachtenia:")
        st.select_slider("Zameranie", options=["Produkcia", "Vyvážené", "Zdravie"])
        if st.button(t["mating_btn"]):
            st.info("Generujem optimálne páry...")
            
    with st.expander(f"**{t['prediction']}**"):
        chart_data = pd.DataFrame(np.random.randn(20, 1).cumsum(), columns=['Index'])
        st.line_chart(chart_data)

    st.divider()
    st.button(t["download_btn"])
