import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

 #declsare sampling frequency and recording duration
freq = 44100
duration = 5  # seconds

#creating channel 1 or 2
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
sd.wait()  # Wait until recording is finished

# Save the recording as a WAV file
write("recording0.wav", freq, recording)  # Using scipy.io.wavfile

wv.write("recording1.wav", recording, freq, sampwidth=2)  # Using wavio
