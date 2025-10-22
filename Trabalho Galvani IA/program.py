# pip install google-generativeai

import google.generativeai as genai
import os

# Tenta obter a chave da API a partir de uma variável de ambiente
try:
    # Substitua pelo nome da sua variável de ambiente, se for diferente
    genai.configure(api_key="AIzaSyBr61nQsrr2GqP_HUFGp1tOpPycBNtFtZ8")

except AttributeError:
    print("Erro: A chave da API não foi encontrada.")
    print("Por favor, defina a variável de ambiente 'GOOGLE_API_KEY'.")
    exit()

# Configurações do modelo
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

# Configurações de segurança
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

# Inicializa o modelo
# Para a versão gratuita, 'gemini-2.5-flash' é uma ótima escolha.
model = genai.GenerativeModel(model_name="gemini-2.5-flash",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

# Envia o prompt e obtém a resposta
prompt = input("Digite sua Pergunta. ")
response = model.generate_content(prompt)

# Imprime a resposta
print(response.text)
