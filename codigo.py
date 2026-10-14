import os
import shutil
import datetime
import threading
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

hd_path = "D:\\"

while True:
    if os.path.exists(hd_path):
        
        caminho = "D:/"
        pastas = []
        for root, dirs, files in os.walk(caminho):
            for dir in dirs:
                if "Backup" in dir and "2023" in dir:
                    pastas.append(os.path.join(root, dir))

        pastas.sort(key=lambda x: os.path.getmtime(x))

        if pastas:
            pasta_antiga = pastas[0]
            mensagem = f"Para Liberar espaço no disco conectado, deseja excluir a pasta de backup antiga?\n\n{pasta_antiga}\n\nClique em 'Sim' para excluir ou 'Não' para cancelar."
            resposta_exclusao = messagebox.askquestion("HD está conectado", mensagem, icon="warning")

            if resposta_exclusao == "yes":
                
                shutil.rmtree(pasta_antiga)
                messagebox.showinfo("Excluir Pasta", f"A pasta {pasta_antiga} foi excluída com sucesso.")
        else:
            messagebox.showinfo("Excluir Pasta", "Não foram encontradas pastas para excluir.")
        
        resposta_backup = messagebox.askquestion("HD está conectado", "Deseja iniciar o backup consinco rman?")
        
        if resposta_backup == 'yes':
            
            data_atual = datetime.datetime.now().strftime('%d-%m-%Y')
            nome_pasta = f'Backup_{data_atual}'
            caminho_pasta = os.path.join(hd_path, nome_pasta)
            os.makedirs(caminho_pasta, exist_ok=True)
            
            origem = r"\\192.168.0.100\backup-consinco-rman"
            #origem = r"\\192.168.0.100\consinco\testepython"
            
            destino = caminho_pasta
            
            janela = tk.Tk()
            janela.title("Backup em andamento")
            janela.geometry("300x100")
            
            barra = ttk.Progressbar(janela, orient="horizontal", length=200, mode="determinate")
            barra.pack(pady=10)
            
            total_arquivos = 0
            for root, dirs, files in os.walk(origem):
                   total_arquivos += len(files)
                    
            i = 0
            for root, dirs, files in os.walk(origem):
                   for file in files:
                        try:
                            shutil.copy(os.path.join(root, file), os.path.join(destino, os.path.relpath(os.path.join(root, file), origem)))
                        except Exception as e:
                            print(f"Erro ao copiar o arquivo {file}. Erro: {e}")
                            
                        i += 1
                        porcentagem = i / total_arquivos * 100
                        barra["value"] = porcentagem
                        janela.update()
                        
            messagebox.showinfo("Backup Concluído", "O backup foi concluído com sucesso.")
            janela.destroy()
            
        break
        
    root.after(5)
    
root.destroy()

