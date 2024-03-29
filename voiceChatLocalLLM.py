import os
import torch
import argparse
import gradio as gr
from zipfile import ZipFile
import langid
from openvoice import se_extractor
from openvoice.api import BaseSpeakerTTS, ToneColorConverter
import simpleaudio as sa
import whisper
import sounddevice as sd
import numpy as np

# Chat with an intelligent assistant in your terminal
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# Instantiate OpenVOICE TTS
tts = BaseSpeakerTTS(config_path="/Users/imaginethepoet/Documents/Github/OpenVoice/openvoice/checkpoints/base_speakers/EN/config.json", device="cpu")
tts.load_ckpt("/Users/imaginethepoet/Documents/Github/OpenVoice/openvoice/checkpoints/base_speakers/EN/checkpoint.pth")

# Load Whisper model
whisper_model = whisper.load_model("base")

# Define the sample rate for audio recording
sample_rate = 16000

history = [
    {"role": "system", "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."},
    {"role": "user", "content": "Hello, introduce yourself to someone opening this program for the first time. Be concise."},
]

def record_audio(duration=5):
    print("Recording audio...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)
    sd.wait()
    print("Recording finished.")
    return recording.squeeze()

while True:
    print("Press Enter to start recording (or type 'quit' to exit)...")
    user_input = input("> ")

    if user_input.lower() == "quit":
        break

    # Record audio from the microphone
    audio = record_audio()

    # Transcribe the recorded audio using Whisper
    result = whisper.transcribe(whisper_model, audio, language="en", fp16=False)
    user_input = result["text"]

    history.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        model="local-model",
        messages=history,
        temperature=0.7,
        stream=True,
    )

    new_message = {"role": "assistant", "content": ""}
    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            new_message["content"] += chunk.choices[0].delta.content

    history.append(new_message)
    print()

    # Generate audio from assistant's response
    assistant_response = new_message["content"]
    output_path = "/Users/imaginethepoet/Documents/Github/OpenVoice/openvoice/outputs/output.wav"
    tts.tts(assistant_response, output_path, speaker="default", language="English", speed=1.0)

    # Play the generated audio using simpleaudio
    wave_obj = sa.WaveObject.from_wave_file(output_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()