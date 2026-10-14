import pyautogui
import pyperclip
from datetime import datetime
import shutil
import os



#pyautogui.write("\\\\192.168.0.100\\backup-consinco-rman")
#pyperclip.copy(\\192.168.0.100\backup-consinco-rman)
#pyperclip.copy(r"\\192.168.0.100\backup-consinco-rman")
#pyperclip.copy(r"c:\Users\pablo\Downloads\Material Didático-20230419")

pyautogui.PAUSE = 1

pyautogui.hotkey("win" , "r")
pyperclip.copy(r"c:\Users\pablo\Downloads\Material Didático-20230419")
pyautogui.hotkey("ctrl" , "v")
pyautogui.press("enter")
pyautogui.hotkey("ctrl" , "a")
pyautogui.hotkey("ctrl" , "c")

data_atual = datetime.now().strftime('%d-%m-%Y')
nome_pasta = f'Backup_{data_atual}'
caminho_pasta = os.path.join("E:/", nome_pasta)
os.makedirs(caminho_pasta, exist_ok=True)

arquivo = pyperclip.paste()
nome_arquivo = os.path.basename(arquivo)
shutil.copy(arquivo, os.path.join(caminho_pasta, nome_arquivo))




#pyautogui.hotkey("win" , "r")
#pyautogui.write("e:\\")
#pyautogui.press("enter")
#pyautogui.hotkey("ctrl" , "v")

import pyautogui
import time

time.sleep (5)
pyautogui.position()

import os
from datetime import datetime

data_atual = datetime.now().strftime('%d-%m-%Y')

nome_pasta = f'Backup_{data_atual}'

# caminho completo para a nova pasta
caminho_pasta = os.path.join("E:/", nome_pasta)

# criar a nova pasta
os.makedirs(caminho_pasta, exist_ok=True)

# obter a data atual
data_atual = datetime.now().strftime('%Y-%m-%d')

# nome da nova pasta com a data atual
nome_pasta = f'Pasta_{data_atual}'

# caminho completo para a nova pasta
caminho_pasta = os.path.join('C:\\Users\\MeuUsuario\\Downloads', nome_pasta)

# criar a nova pasta
os.makedirs(caminho_pasta, exist_ok=True)

# acessar o conteúdo da área de transferência
arquivo = pyperclip.paste()

# mover o arquivo para a nova pasta
shutil.move(arquivo, caminho_pasta)

arquivo = pyperclip.paste()

# obter o nome do arquivo a partir do caminho completo
nome_arquivo = os.path.basename(arquivo)

# copiar o arquivo para a nova pasta
shutil.copy(arquivo, os.path.join(caminho_pasta, nome_arquivo))

import shutil
import os
from datetime import datetime

# criar pasta de backup com a data atual
data_atual = datetime.now().strftime('%Y-%m-%d')
nome_pasta = f'backup_{data_atual}'
caminho_pasta = os.path.join('E:', nome_pasta)
os.makedirs(caminho_pasta, exist_ok=True)

# copiar todos os arquivos da pasta de origem para a pasta de backup
caminho_origem = '\\\\192.168.0.100\\consinco\\testepython'
for root, dirs, files in os.walk(caminho_origem):
    for file in files:
        shutil.copy(os.path.join(root, file), caminho_pasta)