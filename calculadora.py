import pyautogui

pyautogui.hotkey("Win", 'r')
pyautogui.sleep(1)

pyautogui.write('calc', interval=0.1)
pyautogui.press("Enter")
pyautogui.sleep(1)

pyautogui.write('20')
pyautogui.press('+')
pyautogui.write('20')
pyautogui.press('Enter')

pyautogui.alert('Operaçaõ Concluída! Verifique o resultado na calculadora')