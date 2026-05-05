import streamlit as st
import pandas as pd
import numpy as np

# 1. KONFIGURÁCIA A ŠTÝL
st.set_page_config(layout="wide", page_title="Herd AI Studio", page_icon="🧬")

# HLAVNÝ VIZUÁLNY ŠTÝL (NotebookLM Look)
st.markdown("""
    <style>
    /* Pozadie a písmo */
    .stApp { background-color: #0b0e14; color: #e2e8f0; font-family: 'Inter', sans-serif; }
    
    /* Horná lišta / Header */
    .main-header { text-align: center; padding: 20px; border-bottom: 1px solid #1e293b; margin-bottom: 20px; }
    .main-header h1 { color: #f8fafc; font-size: 2.2rem; font-weight: 800; margin-bottom: 5px; }
    .main-header p { color: #94a3b8; font-size: 1.1rem; }

    /* Panely (Stĺpce) */
    [data-testid="column"] { 
        background-color: #111827; 
        border-radius: 16px; 
        padding: 15px !important; 
        border: 1px solid #1f2937;
    }

    /* NotebookLM Karty zdrojov (Vľavo) */
    .source-card {
        background-color: #1e293b;
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 10px;
        border: 1px solid #334155;
        font-size: 0.9rem;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    /* Chatovacie bubliny (Stred) */
    .stChatMessage { background-color: #1e293b !important; border-radius: 15px !important; border: 1px solid #334155 !important; }

    /* Tlačidlá (Vpravo) */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        background-color: #1e293b;
        color: #f8fafc;
        border: 1px solid #334155;
        font-weight: 600;
        text-align: left;
        padding-left: 15px;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background-color: #334155;
        border-color: #10b981;
        color: #10b981;
    }

    /* Odstránenie Streamlit menu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- HORNÝ NÁPIS (HEADER) ---
st.markdown("""
    <div class="main-header">
        <h1>Herd AI Studio</h1>
        <p>tvoj AI reprodukčný poradca</p>
    </div>
    """, unsafe_allow_html=True)

# --- ROZDELENIE DO 3 STĹPCOV ---
col_sources, col_chat, col_tools = st.columns([0.8, 2, 0.8])

# 1. STĹPEC: ZDROJE (ĽAVÁ STRANA)
with col_sources:
    st.markdown("### 📂 Zdroje")
    uploaded_files = st.file_uploader("Nahrať dáta", accept_multiple_files=True, label_visibility="collapsed")
    
    if uploaded_files:
        for f in uploaded_files:
            st.markdown(f"""
                <div class="source-card">
                    📄 <span>{f.name}</span>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("<p style='color:#64748b; font-size:0.9rem;'>Žiadne nahraté zdroje.</p>", unsafe_allow_html=True)
        # Demo zdroje
        for name in ["Kontrola_uzitkovosti_2026.csv", "Genomika_jalovice.xlsx"]:
            st.markdown(f"<div class='source-card' style='opacity:0.5;'>📄 {name}</div>", unsafe_allow_html=True)

# 2. STĹPEC: CHAT (STRED)
with col_chat:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Vyberte zdroje a môžeme začať s analýzou vášho stáda."}]

    # Zobrazenie správ
    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.write(m["content"])

    # Fixný chat input dole
    if prompt := st.chat_input("Pýtajte sa na vaše stádo..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.write(prompt)
        
        response = f"Analyzujem vaše zdroje pre odpoveď na: '{prompt}'..."
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"): st.write(response)

# 3. STĹPEC: NÁSTROJE (PRAVÁ STRANA)
with col_tools:
    st.markdown("### 🛠️ Nástroje")
    
    if st.button("🎯 Zadať cieľ"):
        st.toast("Nastavenie cieľa otvorené")
        
    if st.button("🔍 Zhodnoť stádo"):
        st.toast("Prebieha analýza stáda...")
        
    if st.button("🐂 Nájdi býkov"):
        st.toast("Prehľadávam katalógy býkov...")
        
    if st.button("📋 Vytvor priparovací plán"):
        st.toast("Generujem optimálne párenie...")
    
    st.markdown("---")
    st.markdown("<p style='color:#64748b; font-size:0.8rem; text-align:center;'>Vytvorené pre moderných farmárov</p>", unsafe_allow_html=True)
