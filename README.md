# OpenVoice Local LLM Interaction

This project combines OpenVoice TTS (Text-to-Speech) with a local LLM (Language Model) to create an interactive voice assistant. You can speak to the assistant using your microphone, and it will transcribe your speech, generate a response using the local LLM, and then speak the response back to you using OpenVoice TTS.

## Prerequisites

Before running the code, make sure you have the following dependencies installed:

- Python 3.7+
- PyTorch
- OpenAI Whisper
- OpenVoice
- Simpleaudio
- Sounddevice

## Installation

1. Clone the repository:

2. Navigate to the project directory:

3. Install the required dependencies using pip:

4. 4. Download the necessary models and checkpoints for OpenVoice and Whisper:
- OpenVoice TTS: Download the checkpoint files and place them in the `openvoice/checkpoints/base_speakers/EN` directory.
- Whisper: The model will be automatically downloaded when you run the code for the first time.

## Usage

1. Make sure your microphone is connected and properly configured.

2. Run the `test_ai.py` script:

3. Press Enter to start recording your speech. Speak clearly into the microphone.

4. The assistant will transcribe your speech, generate a response using the local LLM, and then speak the response back to you using OpenVoice TTS.

5. To exit the program, type 'quit' and press Enter.

## Configuration

You can customize the following parameters in the `test_ai.py` script:

- `base_url`: The URL of your local LLM server.
- `api_key`: The API key for your local LLM server.
- `config_path`: The path to the OpenVoice TTS configuration file.
- `checkpoint_path`: The path to the OpenVoice TTS checkpoint file.
- `whisper_model`: The name of the Whisper model to use for speech recognition.
- `sample_rate`: The sample rate for audio recording.
- `output_path`: The path where the generated audio files will be saved.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements

- [OpenVoice](https://github.com/myshell-ai/OpenVoice) - Open-source voice cloning project
- [OpenAI Whisper](https://github.com/openai/whisper) - Automatic speech recognition (ASR) system

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Contact

If you have any questions or inquiries, please contact the project maintainer at prestonux@gmail.com - Preston McCauley

Happy interacting with your voice assistant! - 
