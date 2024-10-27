import pyautogui
import time
import pyperclip
from openai import OpenAI
client = OpenAI(
  api_key="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 ",
)
def is_last_message_from_sender(chat_log, sender_name="Divanshu Goel"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False

# Step 1: Activate VS Code window by switching with Cmd + Tab
pyautogui.hotkey('command', 'tab')
time.sleep(1)  # Wait to ensure VS Code is active

# Step 2: Click on the text area within VS Code if coordinates need updating
pyautogui.click(1165, 919)  # Adjust coordinates if needed

# Step 3: Small delay to ensure the window is active
time.sleep(1)

# Step 4: Drag from (548, 225) to (1419, 870) to select text
while True:
    pyautogui.moveTo(531, 211)
    pyautogui.dragTo(638, 935, duration=1, button='left')

    # Step 5: Copy the selected text (Cmd + C)
    pyautogui.hotkey('command', 'c')

    # Step 6: Small delay to ensure the text is copied
    time.sleep(0.5)
    pyautogui.click(1019,630)
    # Step 7: Get the copied text from the clipboard
    chat_history = pyperclip.paste()

    # Step 8: Print the copied text or store it for further use
    print(f"Copied text: {chat_history}")
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a person named Tapnanshu who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)"},
            {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] Divanshu Goel  : "},
            {"role": "user", "content": chat_history}
        ]
        )

        response=completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 5: Click at coordinates (1808, 1328)
        pyautogui.click(899, 908)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('command   ', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is completed

        # Step 7: Press Enter
        pyautogui.press('return')    
