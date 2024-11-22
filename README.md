# Auto-reply-AI-chatbot
Python based auto reply AI chatbot

01_get_cursor.py cotains
This code uses the pyautogui library to continuously monitor and display the current position of the mouse cursor. It runs an infinite loop (while True) that repeatedly retrieves the mouse's x and y coordinates using pyautogui.position(), then prints these coordinates to the console in real-time. The program will keep printing the cursor's position until manually interrupted, making it useful for tracking mouse movement on the screen.


02_openai.py contains
This script uses the Groq API with OpenAI's GPT-3.5-turbo model to analyze and respond to a chat history in a personalized and contextual manner. It simulates a WhatsApp-style conversation where the input is a Hindi-English mixed dialogue. The system is set up with a persona—"Tapnanshu," an Indian coder fluent in Hindi and English—to ensure responses are natural and relevant. The chat history is provided as input, and the API processes it using a prompt that describes the assistant's persona and response style. The model analyzes the conversation's tone and context, then generates a response as "Tapnanshu" would, reflecting the informal, relatable tone of the chat. This setup is ideal for building bots that provide realistic, culturally-aware interactions.


03_bot.py contains
This Python script automates chat interactions by combining GUI control, clipboard operations, and AI-driven text analysis. Using PyAutoGUI, it monitors a chat application by selecting and copying the chat history, while Pyperclip retrieves the content from the clipboard. It then checks if the last message was sent by a specific user ("Tapnanshu") and determines the tone of the conversation (professional or casual) using the Groq API. Based on the tone, it generates contextually appropriate responses with predefined styles—formal for professional chats and witty for casual ones—using an AI language model. Finally, the response is pasted into the chat and sent automatically, with the entire process running in a loop until interrupted by the user.
