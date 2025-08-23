import pyautogui

pyautogui.press('Win')
pyautogui.sleep(0.5)
pyautogui.write('Google Chrome', interval=0.1)
pyautogui.press('Enter')
pyautogui.sleep(2)

pyautogui.click(385,54)
pyautogui.write('https://prefeitura.santanadeparnaiba.sp.gov.br/Plataforma/smti/fabrica-de-programadores', interval=0.1)
pyautogui.press('Enter')
pyautogui.sleep(2)

pyautogui.hotkey('Win', 'Shift', 's')
pyautogui.sleep(2)

pyautogui.mouseDown(1918,1078)
pyautogui.sleep(1)
pyautogui.moveTo(1918,1078)
pyautogui.mouseUp(0,0)
pyautogui.sleep(2)
