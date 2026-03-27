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
    Predict pneumonia probability from an uploaded X-ray image.
    Returns:
        float: Probability score between 0.0 and 1.0.
    """
    model = get_model()
    
    if model is None:
        # --- SIMULATION MODE ---
        # If model is not trained/found, return a random score for testing
        import random
        return random.uniform(0.1, 0.9)
        
    try:
        # Load image via PIL (handles Streamlit UploadedFile)
        img = Image.open(image_file)
        
        # Convert to RGB (required if the model expects 3 channels)
        if img.mode != "RGB":
            img = img.convert("RGB")
            
        # Resize to match model input shape (224x224)
        img = img.resize((224, 224))
        
        # Preprocess: convert to array and normalize
        img_array = img_to_array(img)
        img_array = img_array / 255.0
        
        # Expand dims since model expects a batch (1, 224, 224, 3)
        img_array = np.expand_dims(img_array, axis=0)
        
        # Predict
        prediction = model.predict(img_array)
        
        # For a sigmoid output, it's a single float
        probability = float(prediction[0][0])
        return probability
        
    except Exception as e:
        print(f"Prediction error: {e}")
        return None
