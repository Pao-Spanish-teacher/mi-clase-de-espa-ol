# --- DISEÑO VISUAL PERSONALIZADO (CSS) ---
st.markdown("""
    <style>
    /* 1. Cambiar el fondo de toda la aplicación */
    .stApp {
        background: linear-gradient(135deg, #e0f2fe 0%, #fdfcfb 100%);
    }

    /* 2. Personalizar la barra lateral (Sidebar) */
    section[data-testid="stSidebar"] {
        background-color: #ffffff !important;
        border-right: 2px solid #1E88E5;
    }

    /* 3. Estilo de los títulos */
    h1 {
        color: #1E88E5 !important;
        font-weight: 800;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }

    /* 4. Estilo de los botones para que resalten */
    .stButton>button {
        background-color: #1E88E5;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 0.6rem 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .stButton>button:hover {
        background-color: #1565C0;
        color: white;
        transform: translateY(-2px);
    }

    /* 5. Estilo de las tarjetas de contenido */
    .stTabs {
        background-color: rgba(255, 255, 255, 0.7);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)
