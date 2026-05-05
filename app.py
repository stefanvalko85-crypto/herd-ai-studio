import streamlit as st
import pandas as pd
import numpy as np

# 1. KONFIGURÁCIA A ŠTÝL (Sivo-biely NotebookLM look)
st.set_page_config(layout="wide", page_title="Herd AI Studio", page_icon="🧬")

st.markdown("""
    <style>
    /* Hlavné pozadie - svetlo sivé */
    .stApp { 
        background-color: #f8fafc; 
        color: #1e293b; 
        font-family: 'Inter', sans-serif; 
    }
    
    /* Horná lišta / Header */
    .main-header { 
        text-align: center; 
        padding: 30px 20px; 
        background-color: #ffffff;
        border-bottom: 1px solid #e2e8f0; 
        margin-bottom: 30px; 
    }
    .main-header h1 { color: #0f172a; font-size: 2.4rem; font-weight: 800; margin: 0; }
    .main-header p { color: #64748b; font-size: 1.1rem; margin-top: 5px; }

    /* Panely (Stĺpce) - Biele okná s tieňom */
    [data-testid="column"] { 
        background-color: #ffffff; 
        border-radius: 20px; 
        padding: 20px !important; 
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05);
    }

    /* Karty zdrojov (Vľavo) */
    .source-card {
        background-color: #f1f5f9;
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 12px;
        border: 1px solid #e2e8f0;
        font-size: 0.9rem;
        display: flex;
        align-items: center;
        gap: 12px;
        color: #334155;
    }

    /* Chatovacie bubliny (Stred) */
    .stChatMessage { 
        background-color: #f8fafc !important; 
        border-radius: 15px !important; 
        border: 1px solid #e2e8f0 !important; 
        color: #1e293b !important;
    }

    /* Tlačidlá (Vpravo) */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.8em;
        background-color: #ffffff;
        color: #334155;
        border: 1px solid #e2e8f0;
        font-weight: 600;
        text-align: left;
        padding-left: 20px;
        transition: all 0.2s ease;
        margin-bottom: 10px;
    }
    .stButton>button:hover {
        background-color: #f1f5f9;
        border-color: #10b981;
        color: #10b981;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }

    /* Vstupné pole chatu */
    .stChatInputContainer {
        padding-bottom: 20px;
    }

    /* Schovanie Streamlit prvkov */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- HORNÝ NÁPIS (HEADER) ---
st.markdown("""
    <div class="main-header">
        <h1>Herd AI Studio</h1>
        <p>tvoj AI reprodukčný poradca</p>
    </div>
    """, unsafe_allow_html=True)

# --- ROZDELENIE DO 3 STĹPCOV (NotebookLM Kompozícia) ---
col_sources, col_chat, col_tools = st.columns([0.9, 2, 0.9])

# 1. STĹPEC: ZDROJE (ĽAVÁ STRANA)
with col_sources:
    st.markdown("### 📂 Zdroje")
    uploaded_files = st.file_uploader("Nahrať dáta", accept_multiple_files=True, label_visibility="collapsed")
    
    if uploaded_files:
        for f in uploaded_files:
            st.markdown(f"""
                <div class="source-card">
                    <span style="font-size: 1.2rem;">📄</span>
                    <strong>{f.name}</strong>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("<p style='color:#94a3b8; font-size:0.9rem;'>Zatiaľ žiadne zdroje. Nahrajte CSV alebo Excel.</p>", unsafe_allow_html=True)
        # Demo vizuál pre ukážku
        st.markdown("<div class='source-card' style='opacity:0.6;'>📄 Kontrola_uzitkovosti.csv</div>", unsafe_allow_html=True)

# 2. STĹPEC: CHAT (STRED - Hlavné okno)
with col_chat:
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "Vitajte v Herd AI Studio. Nahrajte dáta z vášho stáda a môžeme začať s analýzou."}]

    for m in st.session_state.messages:
        with st.chat_message(m["role"]):
            st.write(m["content"])

    if prompt := st.chat_input("Pýtajte sa na vaše stádo..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"): st.write(prompt)
        
        response = f"Pripravujem analýzu pre: '{prompt}'. Funkcia bude plne dostupná po prepojení s AI modelom."
        st.session_state.messages.append({"role": "assistant", "content": response})
        with st.chat_message("assistant"): st.write(response)

# 3. STĹPEC: NÁSTROJE (PRAVÁ STRANA)
with col_tools:
    st.markdown("### 🛠️ Nástroje")
    
    if st.button("🎯 Zadať cieľ"):
        st.toast("Nastavenie cieľa")
        
    if st.button("🔍 Zhodnoť stádo"):
        st.toast("Spúšťam celkovú analýzu...")
        
    if st.button("🐂 Nájdi býkov"):
        st.toast("Prehľadávam katalógy...")
        
    if st.button("📋 Vytvor priparovací plán"):
        st.toast("Generujem plán...")
    
    st.markdown("<br><hr><p style='color:#94a3b8; font-size:0.8rem; text-align:center;'>Verzia 1.0 Alpha</p>", unsafe_allow_html=True)
