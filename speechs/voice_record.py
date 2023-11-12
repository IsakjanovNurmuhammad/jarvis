import pyaudio
import wave
import os
from pydub import AudioSegment  # Import AudioSegment from pydub
import uuid
path = "/home/isakjanovnurmuhammad/Desktop/jarvis/"

name = str(uuid.uuid4()) + ".wav"
mp3_name = str(uuid.uuid4()) + ".mp3"


def convert_to_mp3(input_filename, output_filename, path=path):  # Include the "path" argument with a default value
    AudioSegment.from_wav(input_filename).export(output_filename, format="mp3")
    return path + output_filename



def record_audio(output_filename=name, duration=15):
    # Parameters for audio recording
    FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
    CHANNELS = 1              # Mono audio
    RATE = 44100              # Sample rate (samples per second)

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Create a stream to capture audio
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=1024)

    print("Recording...")

    frames = []

    # Record audio
    for _ in range(0, int(RATE / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    print("Finished recording.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()

    # Terminate PyAudio
    audio.terminate()

    # Save the recorded audio to a WAV file
    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

def run_all():
    output_filename = name
    mp3_output_filename = mp3_name

    record_audio(output_filename)
    convert_to_mp3(output_filename, mp3_output_filename)

    # Delete the WAV file if you don't need it
    os.remove(output_filename)
    return path + mp3_name
