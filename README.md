# OpenVoice Local LLM Interaction

This project combines OpenVoice TTS (Text-to-Speech) with a local LLM (Language Model) to create an interactive voice assistant. You can speak to the assistant using your microphone, and it will transcribe your speech, generate a response using the local LLM, and then speak the response back to you using OpenVoice TTS.

![OpenVoice Logo](images/openvoice_logo.png)

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Configuration](#configuration)
5. [Tips and Advanced Usage](#tips-and-advanced-usage)
6. [Windows Installation (VS Code)](#windows-installation-vs-code)
7. [License](#license)
8. [Acknowledgements](#acknowledgements)
9. [Contributing](#contributing)
10. [Contact](#contact)

## Prerequisites

Before running the code, make sure you have the following dependencies installed:

- Python 3.7+
- PyTorch
- OpenAI Whisper
- OpenVoice
- Simpleaudio
- Sounddevice

## Installation

### LM Studio

1. Visit the [LM Studio website](https://lm-studio.org/) and follow the installation instructions for your operating system.
2. Make sure to set up the LM Studio API key and endpoint URL.

### OpenVoice

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/openvoice-local-llm.git
   ```

2. Navigate to the project directory:
   ```bash
   cd openvoice-local-llm
   ```

3. Install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. Install OpenVoice:
   ```bash
   conda create -n openvoice python=3.9
   conda activate openvoice
   git clone git@github.com:myshell-ai/OpenVoice.git
   cd OpenVoice
   pip install -e .
   ```

5. Download and install the necessary models and checkpoints for OpenVoice and Whisper:
   - OpenVoice TTS: Download the checkpoint from [here](https://github.com/myshell-ai/OpenVoice/releases) and extract it to the `checkpoints` folder.
   - Whisper: The model will be automatically downloaded when you run the code for the first time.

## Usage

1. Make sure your microphone is connected and properly configured.
2. Run the `test_ai.py` script:
   ```bash
   python test_ai.py
   ```

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

## Tips and Advanced Usage

### Flexible Voice Style Control
Please see [demo_part1.ipynb](demo_part1.ipynb) for an example usage of how OpenVoice enables flexible style control over the cloned voice.

### Cross-Lingual Voice Cloning
Please see [demo_part2.ipynb](demo_part2.ipynb) for an example for languages seen or unseen in the MSML training set.

### Gradio Demo
We provide a minimalist local gradio demo. Launch it with `python -m openvoice_app --share`.

### Advanced Usage
The base speaker model can be replaced with any model (in any language and style) that the user prefers. Use the `se_extractor.get_se` function as demonstrated in the demo to extract the tone color embedding for the new base speaker.

### Tips to Generate Natural Speech
There are many single or multi-speaker TTS methods that can generate natural speech and are readily available. By simply replacing the base speaker model with the model you prefer, you can push the speech naturalness to a level you desire.

## Windows Installation (VS Code)
Please use this guide if you want to install and use OpenVoice on Windows.

## License
This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements
- [OpenVoice](https://github.com/myshell-ai/OpenVoice) - Open-source voice cloning project
- [OpenAI Whisper](https://github.com/openai/whisper) - Automatic speech recognition (ASR) system

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Contact
If you have any questions or inquiries, please contact the project maintainer at prestonux@gmail.com - Preston McCauley

Happy interacting with your voice assistant!
