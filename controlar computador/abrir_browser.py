import pyautogui as posicao_mouse

posicao_mouse.sleep(4)
print(posicao_mouse.position())

posicao_mouse.moveTo(x=413, y=1407)
posicao_mouse.doubleClick(x=413, y=1407)
posicao_mouse.sleep(4)

posicao_mouse.typewrite("https://www.google.com/")
posicao_mouse.sleep(3)
posicao_mouse.press("enter")
posicao_mouse.sleep(5)

posicao_mouse.typewrite("Dolar Hoje")
posicao_mouse.sleep(3)
posicao_mouse.press("enter")
posicao_mouse.sleep(5)