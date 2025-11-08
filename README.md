# AI Coding Agent

A command-line tool that uses Google’s Gemini API to read, update, and run Python code.

This is the starter code used in Boot.dev's [Build an AI Agent in Python](https://www.boot.dev/courses/build-ai-agent-python) course.

---

## Requirements

- Python 3
- Gemini API key (from [Google AI Studio](https://aistudio.google.com/))

---

## Installation

1. Clone the Repository

2. Create virtual environment and activate:
```bash
python3 -m venv env
source env/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file and put Gemini API key here:
```
GEMINI_API_KEY=your_api_key_here
```

---

## Usage

### Run the AI Agent
```bash
python3 main.py "your prompt here"
```

#### Example
```bash
python3 main.py "create a new README.md file with the contents '# calculator'"
```

#### Output
```bash
 - Calling function: write_file
Final response:
OK. I've created a new file named `README.md` with the content '# calculator'.
```

---

### Verbose Mode
```bash
python3 main.py "your prompt here" --verbose
```

#### Example
```bash
python3 main.py "what files are in the root?" --verbose
```

#### Output
```bash
User prompt: what files are in the root?

Prompt tokens: 352
Response tokens: 7
Calling function: get_files_info({'directory': '.'})
-> {'result': '- main.py: file_size=576 bytes, is_dir=False\n- tests.py: file_size=1343 bytes, is_dir=False\n- pkg: file_size=4096 bytes, is_dir=True'}
Prompt tokens: 429
Response tokens: 30
Final response:
Okay, I see the following files in the root directory: `main.py`, `tests.py`, and a directory named `pkg`.
```
