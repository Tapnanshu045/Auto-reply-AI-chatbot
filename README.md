# Auto-reply-AI-chatbot
Python based auto reply AI chatbot

01_get_cursor.py cotains
This code uses the pyautogui library to continuously monitor and display the current position of the mouse cursor. It runs an infinite loop (while True) that repeatedly retrieves the mouse's x and y coordinates using pyautogui.position(), then prints these coordinates to the console in real-time. The program will keep printing the cursor's position until manually interrupted, making it useful for tracking mouse movement on the screen.

02_openai.py contains
This code uses the OpenAI Python client to interact with the GPT API, simulating a chatbot persona named "Harry," a bilingual coder from India who speaks both Hindi and English. After importing the OpenAI library and initializing the client with an API key, a chat history between two users, "Naruto" and "Rohan Das," is provided as input. The client.chat.completions.create() method sends this chat history, along with a system message describing Harry's persona, to the GPT-3.5-turbo model to generate a contextual response. Finally, the model's response is printed, completing the conversation analysis based on the given persona.

03_bot.py contains
This Python script automates a chat interaction using PyAutoGUI for mouse and keyboard automation, pyperclip for clipboard management, and OpenAI's API for generating responses. The script continuously monitors chat history in a Chrome window by simulating mouse clicks and dragging to select and copy the latest chat content. It checks if the last message is from a specific sender ("Rohan Das"). If true, it uses OpenAI's GPT-3.5 model to generate a humorous response from the persona of "Naruto," a bilingual coder who roasts people in Hindi and English. The generated response is copied to the clipboard, pasted into the chat window, and sent by simulating a keystroke of "Enter." The automation runs in a loop with intervals for each action.
