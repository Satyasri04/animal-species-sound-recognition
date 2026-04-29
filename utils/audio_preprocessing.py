import librosa
import numpy as np

def load_audio(file_path, sr=16000):
    waveform, _ = librosa.load(file_path, sr=sr, mono=True)
    return waveform
