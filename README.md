# Sunday - Python Voice Assistant
> Sunday is a smart, offline voice assistant built with Python, featuring text-to-speech, command execution, and speech recognition using Vosk.

## Features
- Text-to-Speech : Converts text to spoken words.
- Command Execution: Runs system commands directly via voice input.
- Speech Recognition: Uses Vosk for accurate offline speech processing.
- Hands-Free Activation: Say "Sunday", and it starts listening.
  
## Command Handling Buttons: If a command isn’t recognized, users can:
- Add New Sentences – Expand Sunday’s knowledge by adding custom responses.
- Listen Again – Retry recognizing the speech
- Edit Sentence & Run Again – Modify the detected text manually before execution
- Exit – Stop interaction

## Installation

Install dependencies:

``` bash
pip install -r requirements.txt
```

## Setting Up Vosk Speech Recognition
Download the Vosk model from [Vosk Models](https://alphacephei.com/vosk/models).

Extract the model files and place them in the models/ directory.

Ensure your code correctly references the model path.

## Usage
Before running the assistant, activate the virtual environment:

Windows:

```bash
.\Gvenv\Scripts\activate
```
Them run the main file
```bash
python main.py
```

Once running, simply say "Sunday", and it will start listening for commands.
If it doesn’t recognize a command, use the available buttons to add a sentence, listen again, edit text, or exit for a smoother experience.

## Command Handling Options
If Sunday doesn't correctly capture your command, you have several options to refine the interaction:

### Add New Sentences

- Expands Sunday’s knowledge by storing new responses.
- Users can teach Sunday custom commands or personalized interactions.
- Great for tailoring responses—e.g., changing "How’s the weather?" to "Looking outside, it’s a good day to code!"
- Enables dynamic learning without modifying the core code.

### Listen Again

- Prompts Sunday to re-listen for your command.
- Useful if there was background noise or unclear speech.

### Edit Sentence & Run Again

- Allows users to modify the detected text before executing the command.
- Ensures accuracy in cases where recognition is slightly off.

### Exit

- Stops interaction with Sunday gracefully.
- Prevents the need to manually close the program when finished.

These refinements ensure that voice recognition is flexible, reducing frustration and increasing accuracy.
