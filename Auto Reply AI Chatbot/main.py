import pyautogui
import time
import pyperclip
from openai import OpenAI

client = OpenAI(
    api_key="your opoenai api key"
)

def is_last_message_from_sender(caht_log,sender_name="Rito"):
    messages = caht_log.strip().split("/2025]")[-1]

    if sender_name in messages:
        return True
    return False


#s1:click on the /chrome icon at the cordinates (1238,1055)
pyautogui.click(1293,1057)
time.sleep(1) #wait for one sec to ensure the click is registered

while True:
    # s2:darg the mouse form (678,200) to (1885,926) to select the text
    pyautogui.moveTo(678,200)
    pyautogui.dragTo(1885,926, duration=1.0,button='left')


    # s3:vopy the selected text tyo clipboard
    pyautogui.hotkey('ctrl','c')
    time.sleep(1) #wait for one sec to ensure the copy command is completed
    pyautogui.click(1669,591) #to exit the selection mode


    #s4:retrive the text from the clipboard and stroe it in a variable
    chat_history= pyperclip.paste()


    #print the copied text to verify
    print(chat_history)

    if is_last_message_from_sender(chat_history):

        completion = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages=[
                {"role":"system", "content" : "You are a person named bhabani who speaks bengali as well as english as well as hindi. You is from india and you are a coder. You analyze the chat hitory and repond like B S Jana doing chat in whatsapp. Output sould be next chat reponse as B S Jana.Give short but resonable answer."},
                {"role": "user", "content":chat_history}
            ]
            )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        #s5:click
        pyautogui.click(864,976)
        time.sleep(1)

        # s6:paste
        pyautogui.hotkey('ctrl','v')
        time.sleep(1)

        # s7:enter
        pyautogui.press('enter')