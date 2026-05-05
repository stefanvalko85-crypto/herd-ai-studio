import streamlit as st
import pandas as pd
import numpy as np

# 1. KONFIGURÁCIA
st.set_page_config(layout="wide", page_title="Herd AI Studio", page_icon="🧬")

# 2. AKTUALIZOVANÝ ŠTÝL (Posunutie nahor + Sivo-biely vzhľad)
st.markdown("""
    <style>
    /* ODSTRÁNENIE VRCHNÉHO OKRAJA STREAMLITU */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
    }
    
    /* Hlavné pozadie */
    .stApp { 
        background-color: #f8fafc; 
        color: #1e293b; 
        font-family: 'Inter', sans-serif; 
    }
    
    /* Horná lišta / Header - KOMPAKTNEJŠIA */
    .main-header { 
        text-align: center; 
        padding: 10px 0px 20px 0px; /* Zmenšené paddingy */
        background-color: #ffffff;
        border-bottom: 1px solid #e2e8f0; 
        margin-bottom: 25px; 
        margin-top: -10px; /* Posunutie ešte vyššie */
    }
    .main-header h1 { color: #0f172a; font-size: 2.1rem; font-weight: 800; margin: 0; }
    .main-header p { color: #64748b; font-size: 1rem; margin-top: 2px; }

    /* Okná (Stĺpce) */
    [data-testid="column"] { 
        background-color: #ffffff; 
        border-radius: 16px; 
        padding: 20px !important; 
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }

    /* Karty zdrojov (ĽAVÁ STRANA) */
    .source-card {
        background-color: #f1f5f9;
        border-radius: 10px;
        padding: 12px;
        margin-bottom: 10px;
        border: 1px solid #e2e8f0;
        font-size: 0.85rem;
        display: flex;
        align-items: center;
        gap: 10px;
        color: #334155;
    }

    /* Chat bubliny (STRED) */
    .stChatMessage { 
        background-color: #f8fafc !important; 
        border-radius: 12px !important; 
        border: 1px solid #e2e8f0 !important;
    }

    /* Tlačidlá (PRAVÁ STRANA) */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3.4em;
        background-color: #ffffff;
        color: #475569;
        border: 1px solid #e2e8f0;
        font-weight: 600;
        text-align: left;
        padding-left: 15px;
        transition: all 0.2s ease;
        margin-bottom: 8px;
    }
    .stButton>button:hover {
        background-color: #f8fafc;
        border-color: #10b981;
        color: #10b981;
    }

    /* Schovanie prebytočných prvkov */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- HLAVNÝ HEADER ---
st.markdown("""
    <div class="main-header">
        <h1>Herd AI Studio</h1>
        <p>tvoj AI reprodukčný poradca</p>
    </div>
    """, unsafe_allow_html=True)

# --- 3-STĹPCOVÁ KOMPOZÍCIA ---
col_sources, col_chat, col_tools = st.columns([0.9, 2, 0.9])

with col_sources:
    st.markdown("### 📂 Zdroje")
    uploaded_files = st.file_uploader("Upload", accept_multiple_files=True, label_visibility="collapsed")
    
    if uploaded_files:
        for f in uploaded_files:
            st.markdown(f"<div class='source-card'>📄 <strong>{f.name}</strong></div>", unsafe_allow_html=True)
    else:
        # Ukážka prázdneho stavu
        st.markdown("<p style='color:#94a3b8; font-size:0.8rem;'>Nahrajte CSV alebo Excel...</p>", unsafe_allow_html=True)

with col_chat:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Vitajte. Som pripravený analyzovať vaše dáta."}]

    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.write(m["content"])

    if prompt := st.chat_input("Pýtajte sa..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.write(prompt)
        
        # Simulácia odpovede
        response = f"Pripravujem odpoveď..."
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"): st.write(response)

with col_tools:
    st.markdown("### 🛠️ Nástroje")
    
    st.button("🎯 Zadať cieľ")
    st.button("🔍 Zhodnoť stádo")
    st.button("🐂 Nájdi býkov")
    st.button("📋 Vytvor priparovací plán")
    
    st.markdown("<p style='color:#cbd5e1; font-size:0.7rem; text-align:center; margin-top:20px;'>Verzia 1.0 Alpha</p>", unsafe_allow_html=True)
