On-the-go-AI-helper (v1.0)
🚀 Welcome to Your Personal AI Sidekick!
Have you ever wished for a smart assistant that's always just a click away, ready to help with quick questions or process information? On-the-go-AI-helper is exactly that! This lightweight desktop application brings the power of Google's Gemini AI directly to your fingertips, designed for speed and convenience in its source code form.

Whether you're brainstorming ideas, summarizing notes, or just curious, this helper makes interacting with AI a seamless part of your workflow. Just set it up, ask away, and let the AI do the heavy lifting!

✨ What Can It Do? (Key Features)
Instant AI Answers: Get rapid responses to your text-based questions and prompts, powered by the advanced Gemini 1.5 Pro model.

Intuitive Text Input: Simply type your queries into the input field.

Drag-and-Drop Text Integration: Easily drag and drop text snippets directly into the input field for quick processing. No more endless copy-pasting!

File Content Insertion: Browse and select text files (.txt) to automatically load their content into your input field, preparing it for an AI query.

Stealth Mode Toggle: Quickly hide or show the application window with the F2 hotkey.

Adjustable Transparency: Fine-tune the app's transparency with the F3 hotkey, allowing you to work with it discreetly in the background.

Draggable Interface: Position the window anywhere on your screen for maximum comfort.

Clear Chat History: Reset the conversation with a dedicated "Clear Chat" button.

🛠️ Getting Started (Installation & Setup)
Getting this helper up and running from source code is straightforward!

Clone the Repository:

git clone https://github.com/YourUsername/On-the-go-AI-helper.git
cd On-the-go-AI-helper

If you're downloading directly from GitHub (via "Code" -> "Download ZIP"), extract the contents and navigate into the folder.

Create a Virtual Environment (Highly Recommended):
This keeps your project dependencies tidy.

python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

Install Dependencies:

pip install requests tkinterdnd2 keyboard

Google Gemini API Key:

For this v1.0 version, the Gemini API key needs to be inserted directly into the src/code_2.py file.

Open src/code_2.py in a text editor.

Find the line: API_KEY = "YOUR_API_KEY_HERE" # Replace with your API key

Replace "YOUR_API_KEY_HERE" with your actual Google Gemini API Key obtained from Google AI Studio.

Save the file.

Important Note for Future Versions: While direct insertion is used for simplicity in this initial release, the plan for upcoming versions is to implement a more secure method (like an interactive input slot or environment variables), ensuring API key confidentiality and best practices for deployment.

🚀 How to Use It
Run the application:

python src/code_2.py

Start Chatting: Type your question or prompt into the input box at the bottom. Press the Enter key on your keyboard or click the "Ask" button to send your query to the AI.

Quick Input: Drag any plain text from another application and drop it onto the input field. It will appear there, ready for you to send to the AI.

Load File Content: Click the "Browse File" button, select a .txt file from your computer, and its content will be loaded into the input field.

Hotkeys for Control:

Press F2 to hide or show the application window instantly.

Press F3 to cycle through transparency levels.

💡 What's Next? (Future Enhancements)
This is just the beginning for On-the-go-AI-helper! Future versions are planned to bring even more convenience and power, including:

Automated Processing of Dropped Files: Directly send the content of dropped files to Gemini without an extra click (planned for v1.1).

Interactive API Key Input: Implement a dedicated slot or dialog for users to securely enter their API key, removing the need for direct code modification.

Secure API Key Management: Transitioning to environment variables or other robust configuration methods for API keys.

Support for a wider range of file types (e.g., PDF, CSV, JSON) for AI analysis.

More robust error handling and user feedback.

Customizable hotkeys and other UI preferences.

Persisting chat history across sessions.

Compile to Executable: Provide a standalone .exe version (and potentially for other OS) once secure API key handling is implemented, for true "no-installation" deployment.

Advanced prompt templating for common tasks.

Stay tuned for updates as this helper evolves!

🤝 Contribution & Support
Ideas, feedback, or suggestions for improvement are always welcome! Feel free to:

Open an issue if you find a bug or have a feature request.

Fork the repository and submit a pull request with your enhancements.

📄 License
This project is open-source and available under the MIT License. For full details, please refer to the LICENSE file in this repository.
