import pyautogui
import time
import pyperclip
from groq import Groq  # Import Groq client for API interactions

# Initialize Groq client
client = Groq(api_key="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")

# Function to check if the last message is from a specific sender
def is_last_message_from_sender(chat_log):
    # chat_log.strip().split("/2024] ")[-1]
    messages = chat_log.strip().split("/2024] ")[-1]
    if "Tapnanshu:" not in messages:
        return True 
    """
    Check if the last message in the chat log is from someone other than 'Tapnanshu'.
    Returns True if the last message is NOT from 'Tapnanshu', otherwise False.
    """
    if not chat_log:  # Handle empty or None chat log
        return False

    # Extract the last non-empty line
    lines = [line.strip() for line in chat_log.split("\n") if line.strip()]
    if not lines:
        return False

    last_message = lines[-1]  # Get the last line
    print(f"Last message: {last_message}")

    # Check if the last message is sent by 'Tapnanshu'
    return "Tapnanshu" not in last_message



# Function to determine the chat tone (professional or casual)
def detect_chat_tone(chat_history):
    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a classifier. Analyze the chat history and determine whether the tone is professional or casual. Reply only with 'professional' or 'casual'."},
            {"role": "user", "content": chat_history},
        ],
        temperature=0,
        max_tokens=10,
        top_p=1,
    )
    response = completion.choices[0].message.content.strip().lower()
    print("Detected chat tone:", response)
    return response
pyautogui.click(1215, 916)
time.sleep(1)

# Function to automate chat interaction
def automate_chat():
    while True:
        time.sleep(5)  # Interval between checks

        # Step 1: Select and copy chat history
        pyautogui.moveTo(553, 217)  # Move to start of chat
        pyautogui.dragTo(575, 932, duration=2.0, button="left")  # Select chat
        pyautogui.hotkey("command", "c")  # Copy text to clipboard
        time.sleep(1)  # Wait for clipboard update

        # Step 2: Retrieve chat history
        chat_history = pyperclip.paste()
        print("Chat History:", chat_history)

        # Step 3: Check if the last message is from the target sender
        if is_last_message_from_sender(chat_history):
            # Step 4: Detect chat tone
            tone = detect_chat_tone(chat_history)

            # Generate an appropriate response based on the tone
            prompt_content = "You are Tapnanshu, a coder from India who speaks both Hindi and English."
            if tone == "professional":
                prompt_content += " Respond professionally, concisely, and formally. Keep your response brief."
            elif tone == "casual":
                prompt_content += " Respond casually, humorously, and wittily. Keep your response short and creative."

            completion = client.chat.completions.create(
                model="llama-3.1-70b-versatile",
                messages=[
                    {"role": "system", "content": prompt_content},
                    {"role": "user", "content": chat_history},
                ],
                temperature=0.7,
                max_tokens=50,  # Short response
                top_p=1,
                stream=False,  # Disable streaming for simplicity
            )

            # Step 5: Extract and print the response
            response = completion.choices[0].message.content.strip()
            print("Generated Response:", response)

            # Step 6: Paste and send the response
            pyperclip.copy(response)
            pyautogui.click(1808, 1328)  # Click to activate chat input
            pyautogui.hotkey("command", "v")  # Paste response
            pyautogui.press("return")  # Send message
        else:
            print("No relevant message from sender.")

# Run the script
if __name__ == "__main__":
    try:
        print("Starting chat automation...")
        automate_chat()
    except KeyboardInterrupt:
        print("\nAutomation stopped by user.")
