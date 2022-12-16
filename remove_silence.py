import librosa
import soundfile as sf
import os

files = os.listdir('wavs2')

for f in files:
    audio, sr = librosa.load('wavs2/' + f, sr= 16000, mono=True)
    clip = librosa.effects.trim(audio, top_db= 10)
    sf.write('wavs/'+f, clip[0], sr,format='wav')
