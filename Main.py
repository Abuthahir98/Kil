import numpy as np
import matplotlib.pyplot as plt
import pyaudio

# Parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open a stream
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Recording...")

frames = []

# Record audio
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Finished recording")

# Close the stream and terminate PyAudio
stream.stop_stream()
stream.close()
audio.terminate()

# Process and plot the recorded audio
audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)
time = np.linspace(0, len(audio_data) / RATE, num=len(audio_data))

plt.figure(figsize=(10, 4))
plt.plot(time, audio_data)
plt.title("Recorded Audio")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()
