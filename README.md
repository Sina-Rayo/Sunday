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
- There are three check-boxes here that are explained at checkbox part, below

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

## Advanced Command Customization (checkboxes)
Sunday allows users to define custom sentences with three powerful options to shape how it processes commands:

1- Variable Sentences (Dynamic Function Calls)
When Variable is checked, the sentence becomes a function-like command.
If users say the sentence followed by additional words, those extra words will be passed as parameters to the function.

### Example:
Let's say a user adds:
```
Open website
```
as a Variable sentence. Then, later they say:
```
Open website google.com
```
Sunday will recognize "google.com" as a parameter and pass it to the function handling the sentence.

This allows for highly flexible commands without requiring predefined variations for every request.

2- Listen After (Sequential Execution)
If Listen After is checked, Sunday will wait and listen after executing the first command.
This is useful when the user wants to issue follow-up commands after a task is completed.

3- Add Here (Chained Commands)
If Add Here is checked, the sentence attaches itself after another sentence, forming a chain of execution.
The new sentence can only be called after the initial sentence but cannot be run independently.

### Example:
Sentence A: "Prepare a report" (added with **Listen After**).
Sentence B: "Send report to manager" (added after Sentence A using **Add Here**).

Now:

If the user calls Sentence A, it automatically leads to Sentence B after completion.
But if the user tries to call Sentence B directly, Sunday won't recognize it unless Sentence A was executed first.

These features make Sunday intelligent, responsive, and capable of contextual conversation flows, ensuring smoother interactions for users.


