import streamlit as st
import google.generativeai as genai

# Configuração da API
genai.configure(api_key="AIzaSyBr61nQsrr2GqP_HUFGp1tOpPycBNtFtZ8")

# Configuração do modelo
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# Interface Streamlit
st.set_page_config(page_title="Assistente Gemini", page_icon="🤖", layout="centered")

st.title("🤖 Assistente com Google Gemini")
st.markdown("Digite sua pergunta abaixo e receba uma resposta gerada por IA.")

# Campo de entrada
prompt = st.text_area("Pergunta:", placeholder="Exemplo: Qual a capital do Brasil?")

if st.button("Gerar Resposta"):
    if prompt.strip() == "":
        st.warning("Por favor, digite uma pergunta antes de enviar.")
    else:
        with st.spinner("Gerando resposta..."):
            try:
                response = model.generate_content(prompt)
                st.success("✅ Resposta gerada com sucesso!")
                st.markdown(f"**Resposta:**\n\n{response.text}")
            except Exception as e:
                st.error(f"Erro ao gerar resposta: {e}")


# streamlit run app.py
