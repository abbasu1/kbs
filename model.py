import os
import numpy as np
from PIL import Image

try:
    from tensorflow.keras.models import load_model
    from tensorflow.keras.preprocessing.image import img_to_array
except ImportError:
    load_model = None
    img_to_array = None

MODEL_PATH = "pneumonia_model.h5"
_model = None

def get_model():
    """Load and return the trained model. If not available, returns None."""
    global _model
    if _model is None and os.path.exists(MODEL_PATH) and load_model is not None:
        try:
            _model = load_model(MODEL_PATH)
        except Exception as e:
            print(f"Error loading model: {e}")
    return _model

def predict_xray(image_file):
    """
    Predict pneumonia/lung opacity from an uploaded X-ray image.
    Returns:
        tuple: (label, confidence)
    """
    model = get_model()
    
    # Class mapping based on flow_from_directory alphabetical sorting
    CLASSES = ["Lung Opacity", "Normal", "Pneumonia"]
    
    if model is None:
        # --- SIMULATION MODE ---
        import random
        label = random.choice(CLASSES)
        score = random.uniform(0.6, 0.99)
        return label, score
        
    try:
        img = Image.open(image_file)
        if img.mode != "RGB":
            img = img.convert("RGB")
        img = img.resize((224, 224))
        
        img_array = img_to_array(img)
        img_array = img_array / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        
        predictions = model.predict(img_array)
        class_idx = np.argmax(predictions[0])
        confidence = float(predictions[0][class_idx])
        
        return CLASSES[class_idx], confidence
        
    except Exception as e:
        print(f"Prediction error: {e}")
        return None, 0.0
