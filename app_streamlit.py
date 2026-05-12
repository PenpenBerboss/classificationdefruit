# app_streamlit.py
import streamlit as st
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

# Charger le modèle CNN
model = load_model("model_cnn.h5")

# Labels des classes (dans le même ordre que train_gen.class_indices)
class_labels = ["Apple", "Banana", "Grape", "Guava", "Jujube",
                "Mango", "Orange", "Papaya", "Pineapple", "Watermelon"]

# Titre de l'application
st.title("🍎🍌🍍 Classification de fruits avec CNN")

st.write("Upload une image de fruit pour tester la prédiction.")

# Upload de fichier
uploaded_file = st.file_uploader("Choisir une image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Afficher l'image uploadée
    st.image(uploaded_file, caption="Image uploadée", use_container_width=True)

    # Prétraitement
    img = load_img(uploaded_file, target_size=(128,128))
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0) / 255.0

    # Prédiction
    prediction = model.predict(x)
    pred_class = np.argmax(prediction, axis=1)[0]
    predicted_label = class_labels[pred_class]

    # Résultat
    st.success(f"✅ Le modèle prédit que le fruit est : **{predicted_label}**")
