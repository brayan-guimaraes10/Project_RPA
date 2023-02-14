import pyautogui as PosicaoMouse
import pyautogui as TempoEspera

TempoEspera.sleep(2)

# Abrir o Windows
PosicaoMouse.press('win')

TempoEspera.sleep(2)

# Escrever Google e abrir Google
PosicaoMouse.typewrite('Google Chrome');PosicaoMouse.press('enter')

TempoEspera.sleep(2)

# Maximizar o Google
PosicaoMouse.hotkey('win', 'Up')

TempoEspera.sleep(2)

# Move o mouse até o SOLMAN e Clicar
PosicaoMouse.moveTo(x=200, y=86,duration=1);PosicaoMouse.click(x=200, y=86)

TempoEspera.sleep(2)

# Abrir o SOLMAN

PosicaoMouse.press('enter')

TempoEspera.sleep(1)

PosicaoMouse.press('enter')

TempoEspera.sleep(4)


PosicaoMouse.moveTo(x=1359, y=354,duration=1);PosicaoMouse.click(x=1359, y=354)

# Ir para o final da página 
PosicaoMouse.scroll(-1300)  # scroll down 10 "clicks"

TempoEspera.sleep(2)

# Clica para baixar a planilha
PosicaoMouse.moveTo(x=1260, y=339,duration=1);PosicaoMouse.click(x=1260, y=339)

TempoEspera.sleep(3)

PosicaoMouse.moveTo(x=117, y=700,duration=1);PosicaoMouse.click(x=117, y=700)

TempoEspera.sleep(3)

PosicaoMouse.hotkey('win', 'Up')

TempoEspera.sleep(2)

PosicaoMouse.moveTo(x=1263, y=176,duration=1);PosicaoMouse.click(x=1263, y=176)

TempoEspera.sleep(2)

PosicaoMouse.typewrite('Teste_RPA')

TempoEspera.sleep(2)

PosicaoMouse.press('tab')

TempoEspera.sleep(2)

PosicaoMouse.press('Down')

TempoEspera.sleep(2)

for i in range(4):
    PosicaoMouse.press('Up')
    TempoEspera.sleep(1)
    
TempoEspera.sleep(1)

for i in range(2):
    PosicaoMouse.press('enter')
    TempoEspera.sleep(1)
    
TempoEspera.sleep(2)

# print(PosicaoMouse.position())
