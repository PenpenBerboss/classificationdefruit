# app_streamlit.py
import streamlit as st
import requests

# URL de ton API FastAPI déployée sur Render
API_URL = "https://model-de-classification-de-fruit.onrender.com/predict"

# Titre de l'application
st.title("🍎🍌🍍 Classification de fruits avec CNN (API Render)")

st.write("Upload une image de fruit pour tester la prédiction via l'API déployée.")

# Upload de fichier
uploaded_file = st.file_uploader("Choisir une image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Afficher l'image uploadée
    st.image(uploaded_file, caption="Image uploadée", use_container_width=True)

    # Envoyer l'image à l'API FastAPI
    files = {"file": uploaded_file.getvalue()}
    response = requests.post(API_URL, files=files)

    if response.status_code == 200:
        result = response.json()
        st.success(f"✅ Le modèle prédit que le fruit est : **{result['predicted_fruit']}**")
    else:
        st.error("❌ Erreur lors de la prédiction. Vérifie que l'API est en ligne.")
