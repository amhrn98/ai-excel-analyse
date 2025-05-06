import streamlit as st
import pandas as pd
from pandasai import SmartDataframe
from pandasai.llm.openai import OpenAI

st.title("📊 AI Excel Analyse App")

openai_api_key = st.text_input("Voer je OpenAI API-sleutel in:", type="password")

uploaded_file = st.file_uploader("Upload een Excel-bestand (.xlsx)", type=["xlsx"])
if uploaded_file and openai_api_key:
    df = pd.read_excel(uploaded_file)
    st.write("Voorbeeld van je data:")
    st.dataframe(df)

    vraag = st.text_input("Wat wil je weten over deze data?")

    if vraag:
        llm = OpenAI(api_token=openai_api_key)
        sdf = SmartDataframe(df, config={"llm": llm})
        antwoord = sdf.chat(vraag)
        st.write("🔍 Antwoord van AI:")
        st.write(antwoord)
