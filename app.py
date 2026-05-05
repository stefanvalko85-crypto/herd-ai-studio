import streamlit as st
import pandas as pd
import numpy as np

# 1. KONFIGURÁCIA
st.set_page_config(layout="wide", page_title="Herd AI Studio", page_icon="🧬")

# 2. FINÁLNY "LIGHT" DIZAJN (NotebookLM štýl)
st.markdown("""
    <style>
    .block-container { padding-top: 0.5rem !important; max-width: 98% !important; }
    .stApp { background-color: #f8fafc; color: #1e293b; font-family: 'Inter', sans-serif; }
    
    /* HEADER LIŠTA */
    .header-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 5px 15px;
        background-color: #ffffff;
        border-bottom: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }
    .brand-section { display: flex; align-items: baseline; gap: 10px; }
    .brand-title { font-size: 1.5rem; font-weight: 800; color: #0f172a; margin: 0; }
    .brand-tagline { color: #94a3b8; font-size: 0.9rem; }

    /* PANELY / OKNÁ */
    [data-testid="column"] { 
        background-color: #ffffff; 
        border-radius: 12px; 
        padding: 20px !important; 
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }

    /* KARTY ZDROJOV */
    .source-card {
        background-color: #f1f5f9;
        border-radius: 8px;
        padding: 10px;
        margin-bottom: 8px;
        border: 1px solid #e2e8f0;
        font-size: 0.85rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* TLAČIDLÁ NÁSTROJOV */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3.5em;
        background-color: #ffffff;
        color: #334155;
        border: 1px solid #e2e8f0;
        font-weight: 600;
        text-align: left;
        padding-left: 15px;
        transition: all 0.2s ease;
        margin-bottom: 10px;
    }
    .stButton>button:hover {
        border-color: #10b981;
        background-color: #f0fdf4;
        color: #10b981;
    }

    /* SCHOVANIE PRVKOV */
    header, footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- 1. HORIZONTÁLNY HEADER ---
col_h1, col_h2 = st.columns([2.5, 1])

with col_h1:
    st.markdown("""
        <div class="brand-section">
            <span style="font-size: 1.6rem;">🧬</span>
            <h1 class="brand-title">Herd AI Studio</h1>
            <span class="brand-tagline">| tvoj AI reprodukčný poradca</span>
        </div>
    """, unsafe_allow_html=True)

with col_h2:
    project_name = st.selectbox(
        "Projekt:",
        ["Farma Východ - Holštajn", "Jalovice 2026", "Testovacie stádo"],
        label_visibility="collapsed"
    )

st.markdown("<hr style='margin: 0 0 20px 0; opacity: 0.1;'>", unsafe_allow_html=True)

# --- 2. HLAVNÁ PLOCHA ---
col_sources, col_chat, col_tools = st.columns([0.8, 2, 0.9])

# --- ĽAVÁ STRANA: ZDROJE ---
with col_sources:
    st.markdown("### 📂 Zdroje")
    st.file_uploader("Nahrať", accept_multiple_files=True, label_visibility="collapsed")
    
    st.markdown("""
        <div class="source-card">📊 KU_export_april.csv</div>
        <div class="source-card">🧬 Genomika_vysledky.xlsx</div>
    """, unsafe_allow_html=True)
    
    st.divider()
    st.caption("Nastavenia projektu")
    st.toggle("Zahrnúť historické dáta", value=True)

# --- STRED: CHAT ---
with col_chat:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": f"Vitajte v projekte **{project_name}**. Čo ideme dnes analyzovať?"}]

    for m in st.session_state.messages:
        with st.chat_message(m["role"]): st.write(m["content"])

    if prompt := st.chat_input("Pýtajte sa na vaše stádo..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.write(prompt)
        
        # Simulácia spracovania
        st.session_state.messages.append({"role": "assistant", "content": "Analyzujem dáta zo zdrojov..."})
        st.rerun()

# --- PRAVÁ STRANA: NÁSTROJE ---
with col_tools:
    st.markdown("### 🛠️ Štúdio")
    
    st.button("🎯 Zadať cieľ šľachtenia")
    
    if st.button("🧬 Genetický Audit stáda"):
        st.toast("Spúšťam hĺbkový audit...")
        # Tu sa neskôr zobrazí textová analýza v chate
        
    st.button("🐂 Nájdi optimálnych býkov")
    
    if st.button("🔮 Simulátor 'Čo ak?'"):
        st.toast("Otváram simulačný modul...")

    st.divider()
    
    with st.expander("📊 Rýchly prehľad", expanded=True):
        st.metric("Počet zvierat", "128 ks")
        st.metric("Genetický trend", "+2.4 %")
    
    st.button("📋 Vytvor priparovací plán")
