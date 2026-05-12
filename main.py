from fastapi import FastAPI, UploadFile, File
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import io

# Initialisation de l'application
app = FastAPI(title="API de classification de fruits avec CNN")

# Chargement du modèle entraîné (MobileNetV2)
model = load_model("model_cnn.h5")

# Les labels des classes (dans le même ordre que train_gen.class_indices)
class_labels = ["Apple", "Banana", "Grape", "Guava", "Jujube",
                "Mango", "Orange", "Papaya", "Pineapple", "Watermelon"]

@app.get("/")
def accueil():
    return {"message": "Bienvenue sur l'API de classification de fruits avec CNN!"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if model is None:
        return {"error": "Modèle non chargé"}

    # Lire le contenu du fichier et le convertir en flux BytesIO
    contents = await file.read()
    img = load_img(io.BytesIO(contents), target_size=(128,128))

    # Prétraitement
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0) / 255.0

    # Prédiction
    prediction = model.predict(x)
    pred_class = np.argmax(prediction, axis=1)[0]
    predicted_label = class_labels[pred_class]

    return {"predicted_fruit": predicted_label}

@app.get("/health")
def health_check():
    return {"status": "santé de l'API", "model_charge": model is not None}
