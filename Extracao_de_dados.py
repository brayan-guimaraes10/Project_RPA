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
PosicaoMouse.moveTo(x=1252, y=404,duration=1);PosicaoMouse.click(x=1252, y=404)

TempoEspera.sleep(3)

# Clica para abrir a planilha
PosicaoMouse.moveTo(x=117, y=700,duration=1);PosicaoMouse.click(x=117, y=700)

TempoEspera.sleep(3)

# Maximiza a aba
PosicaoMouse.hotkey('win', 'Up')

TempoEspera.sleep(2)

# Move e clica em Salva como
PosicaoMouse.moveTo(x=1263, y=176,duration=1);PosicaoMouse.click(x=1263, y=176)

TempoEspera.sleep(2)

# Escreve o nome da planilha e salva
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
    
PosicaoMouse.press('tab');PosicaoMouse.press('enter')

TempoEspera.sleep(2)

# Coloca filtro em todas as colunas
PosicaoMouse.hotkey('ctrl', 'shift', 'l')

TempoEspera.sleep(2)

# Coloca o espaçamento correto
PosicaoMouse.moveTo(x=88, y=214,duration=1);PosicaoMouse.doubleClick(x=88, y=214)

TempoEspera.sleep(2)

PosicaoMouse.moveTo(x=612, y=214,duration=1);PosicaoMouse.doubleClick(x=612, y=214)

TempoEspera.sleep(2)

PosicaoMouse.moveTo(x=485, y=212,duration=1);PosicaoMouse.doubleClick(x=485, y=212)

TempoEspera.sleep(2)

# import Nomes

# if Nomes:
    
#     PosicaoMouse.press('enter')
#     PosicaoMouse.sleep(2)

PosicaoMouse.moveTo(x=693, y=235,duration=1);PosicaoMouse.click(x=693, y=235)

PosicaoMouse.sleep(2)

PosicaoMouse.moveTo(x=492, y=470,duration=1);PosicaoMouse.click(x=492, y=470)

PosicaoMouse.sleep(2)

PosicaoMouse.moveTo(x=490, y=490,duration=1);PosicaoMouse.click(x=490, y=490)

TempoEspera.sleep(2)

PosicaoMouse.press('enter')

TempoEspera.sleep(2)

PosicaoMouse.moveTo(x=699, y=234,duration=1);PosicaoMouse.click(x=699, y=234)

TempoEspera.sleep(2)

# print(PosicaoMouse.position())
