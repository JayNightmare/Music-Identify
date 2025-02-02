"""
This script uses the librosa library to analyze an audio file and generate a beat map.
The beat map is output as a list of milliseconds corresponding to detected beat positions.
Make sure to install librosa (pip install librosa) before running this script.
"""

import librosa

audio_path = './audio/JLS_ATI.mp3'
y, sr = librosa.load(audio_path)

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
print(f"Estimated Tempo: {tempo.item():.2f} BPM")

beat_times = librosa.frames_to_time(beat_frames, sr=sr)
beat_map_ms = [int(time * 1000) for time in beat_times]

print("Beat Map (ms):")
print(beat_map_ms)