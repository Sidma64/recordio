import sounddevice as sd
import numpy as np

def record_audio(duration):
    # Set the sample rate and duration of the recording
    sample_rate = 44100  # Standard sample rate for audio
    total_samples = int(duration * sample_rate)

    # Start recording audio
    print("Recording started...")
    audio_data = sd.rec(total_samples, samplerate=sample_rate, channels=1)
    sd.wait()  # Wait until the recording is complete

    print("Recording finished.")
    return audio_data

def save_audio(filename, audio_data, sample_rate):
    # Save the recorded audio to a WAV file
    print("Saving audio...")
    sd.write(filename, audio_data, sample_rate)
    print(f"Audio saved as {filename}")

# Example usage
duration = 5  # Duration of the recording in seconds
filename = "recorded_audio.wav"

# Record audio
audio_data = record_audio(duration)

# Save the recorded audio to a file
save_audio(filename, audio_data, sample_rate=44100)