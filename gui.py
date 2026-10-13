import tkinter as tk
from tkinter import messagebox   

#pegar o texto

def pegar_texto():
    texto_digitado = (
        entrada.get()
    )
    if texto_digitado.strip() =="":
        messagebox.showwarning("Aviso", "Cole seu Link!")
    else:
        messagebox.shwoinfo("texto Digitado", f"Você: Digitou: {texto_digitado}")



root = tk.Tk()

root.title("dwyt")
root.geometry("400x300")

root.resizable(True, True)

#label test
# label = tk.Label (
#     root,
#     text="Redimensione a Janela para ver o botão se adaptar!",
#     bg="Lightblue",
#     font=("Arial,11"),
# )


label = tk.Label(
    root, text="Cole o link do Youtube abaixo", font=("arial",11)
)

label.pack(padx=10, pady=(20, 5))

entrada = tk.Entry(root, font=("Arial", 12))
entrada.pack(fill=tk.X, padx=20, pady=5)

label.pack(fill=tk.BOTH, expand=True, padx=10, pady=18)

botao = tk.Button (
    root, 
    text="Processar Link", 
    bg="white", 
    font=("Arial", 10, "bold"),
    command=pegar_texto,
)

botao.pack(fill=tk.X, padx=10, pady=10)

root.mainloop()