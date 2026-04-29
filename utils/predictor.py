import tensorflow_hub as hub
import tensorflow as tf
import numpy as np
import pickle
from .audio_preprocessing import load_audio

# Load YAMNet from TF Hub
yamnet_model = hub.load("https://tfhub.dev/google/yamnet/1")

# Load trained classifier
classifier = tf.keras.models.load_model("models/animal_species_classifier.h5")

# Load label encoder
with open("models/label_encoder.pkl", "rb") as f:
    le = pickle.load(f)

def predict_species(audio_path):
    waveform = load_audio(audio_path)
    _, embeddings, _ = yamnet_model(waveform)
    embedding_vector = np.mean(embeddings.numpy(), axis=0)
    embedding_vector = np.expand_dims(embedding_vector, axis=0)
    
    pred_probs = classifier.predict(embedding_vector)
    pred_class_idx = np.argmax(pred_probs)
    pred_class_name = le.inverse_transform([pred_class_idx])[0]
    confidence = float(pred_probs[0][pred_class_idx])
    
    return pred_class_name, confidence
