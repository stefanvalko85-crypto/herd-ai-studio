import streamlit as st
import pandas as pd
import numpy as np

# 1. KONFIGURÁCIA
st.set_page_config(layout="wide", page_title="Herd AI Studio", page_icon="🧬")

# 2. CSS PRE MAXIMÁLNE POSUNUTIE NAHOR A ZAROVNANIE DOĽAVA
st.markdown("""
    <style>
    /* ODSTRÁNENIE KOMPLETNÉHO VRCHNÉHO OKRAJA */
    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 0rem !important;
        max-width: 98% !important;
    }
    
    /* Hlavné pozadie */
    .stApp { 
        background-color: #f8fafc; 
        color: #1e293b; 
        font-family: 'Inter', sans-serif; 
    }
    
    /* HORIZONTÁLNY HEADER ÚPLNE DOĽAVA */
    .header-container {
        display: flex;
        align-items: baseline;
        justify-content: flex-start;
        gap: 12px;
        padding: 0px 0px 15px 10px;
        border-bottom: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }
    .header-logo { font-size: 1.8rem; }
    .header-title { 
        color: #0f172a; 
        font-size: 1.6rem; 
        font-weight: 800; 
        margin: 0;
    }
    .header-subtitle { 
        color: #94a3b8; 
        font-size: 0.95rem; 
        font-weight: 400;
    }

    /* Okná (Stĺpce) */
    [data-testid="column"] { 
        background-color: #ffffff; 
        border-radius: 12px; 
        padding: 20px !important; 
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }

    /* Tlačidlá (PRAVÁ STRANA) */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3.2em;
        background-color: #ffffff;
        color: #475569;
        border: 1px solid #e2e8f0;
        font-weight: 600;
        text-align: left;
        padding-left: 15px;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #f8fafc;
        border-color: #10b981;
        color: #10b981;
    }

    /* Schovanie Streamlit prvkov */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- HEADER S IKONOU A NÁZVOM V JEDNOM RIADKU ---
st.markdown("""
    <div class="header-container">
        <span class="header-logo">🧬</span>
        <span class="header-title">Herd AI Studio</span>
        <span class="header-subtitle">| tvoj AI reprodukčný poradca</span>
    </div>
    """, unsafe_allow_html=True)

# --- 3-STĹPCOVÁ KOMPOZÍCIA ---
col_sources, col_chat, col_tools = st.columns([0.8, 2.2, 0.8])

with col_sources:
    st.markdown("### 📂 Zdroje")
    st.file_uploader("Upload", accept_multiple_files=True, label_visibility="collapsed")
    st.markdown("<p style='color:#94a3b8; font-size:0.8rem;'>Vložte dáta (CSV, XLSX)</p>", unsafe_allow_html=True)

with col_chat:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Systém je pripravený na analýzu vášho stáda."}]

    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.write(m["content"])

    if prompt := st.chat_input("Pýtajte sa..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.write(prompt)
        st.session_state.messages.append({"role": "assistant", "content": "Analyzujem..."})
        st.rerun()

with col_tools:
    st.markdown("### 🛠️ Nástroje")
    st.button("🎯 Zadať cieľ")
    st.button("🔍 Zhodnoť stádo")
    st.button("🐂 Nájdi býkov")
    st.button("📋 Vytvor priparovací plán")
