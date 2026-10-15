# gui.py
import tkinter as tk
from tkinter import messagebox
# Importa a função que criamos no arquivo app.py
from app import baixar_video 

def acionar_download():
    # 1. Pega o texto que o usuário digitou no tk.Entry
    url_digitada = entrada_url.get()
    
    # Validação simples para ver se o campo não está vazio
    if not url_digitada.strip():
        messagebox.showwarning("Aviso", "Por favor, insira uma URL do YouTube.")
        return

    # 2. Executa a função do app.py passando a URL capturada
    sucesso = baixar_video(url_digitada)
    
    if sucesso:
        messagebox.showinfo("Sucesso", "O download do vídeo foi concluído!")
    else:
        messagebox.showerror("Erro", "Não foi possível baixar o vídeo. Verifique a URL.")

# --- Configuração básica da GUI ---
janela = tk.Tk()
janela.title("Downloader de YouTube")
janela.geometry("400x150")

# Label explicativo
label = tk.Label(janela, text="Cole a URL do vídeo do YouTube abaixo:")
label.pack(pady=10)

# O seu tk.Entry (onde o link será colado)
entrada_url = tk.Entry(janela, width=50)
entrada_url.pack(pady=5)

# Botão que chama a função 'acionar_download' ao ser clicado
botao_baixar = tk.Button(janela, text="Baixar Vídeo", command=acionar_download)
botao_baixar.pack(pady=10)

janela.mainloop()
