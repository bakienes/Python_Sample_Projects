import pyautogui, time
time.sleep(s)
f = open("spamwords","r")
for word in f:
    pyautogui.typerwrite(word)
    pyautogui.press("Enter")
    
