import librosa
import numpy as np

# Load the audio file
audio_path = "./audio/JLS_ATI.mp3"  # Change to your file path
y, sr = librosa.load(audio_path, sr=None)

tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
spectral_bandwidth = np.mean(librosa.feature.spectral_bandwidth(y=y, sr=sr))
zero_crossing_rate = np.mean(librosa.feature.zero_crossing_rate(y))
mfccs = np.mean(librosa.feature.mfcc(y=y, sr=sr), axis=1)

# Display Results
print("Tempo (BPM):", tempo)
print("Spectral Centroid:", spectral_centroid)
print("Spectral Bandwidth:", spectral_bandwidth)
print("Zero Crossing Rate:", zero_crossing_rate)
print("MFCCs:", mfccs)
