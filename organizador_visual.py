import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# --- LÓGICA DO SISTEMA (Igual ao anterior, mas encapsulada) ---
def organizar_arquivos():
    diretorio_alvo = entrada_caminho.get()
    
    if not diretorio_alvo:
        messagebox.showwarning("Aviso", "Por favor, selecione uma pasta primeiro!")
        return

    if not os.path.exists(diretorio_alvo):
        messagebox.showerror("Erro", "Pasta não encontrada!")
        return

    # Dicionário de extensões
    tipos_arquivos = {
        "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
        "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
        "Instaladores": [".exe", ".msi", ".iso", ".zip", ".rar"],
        "Audios": [".mp3", ".wav"],
        "Videos": [".mp4", ".mov", ".avi", ".mkv"],
        "Codigos": [".py", ".js", ".html", ".css", ".sql"]
    }

    contador = 0
    
    try:
        arquivos = os.listdir(diretorio_alvo)
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(diretorio_alvo, arquivo)

            if os.path.isdir(caminho_arquivo):
                continue

            _, extensao = os.path.splitext(arquivo)
            extensao = extensao.lower()

            moved = False
            for pasta, extensoes_lista in tipos_arquivos.items():
                if extensao in extensoes_lista:
                    pasta_destino = os.path.join(diretorio_alvo, pasta)
                    if not os.path.exists(pasta_destino):
                        os.makedirs(pasta_destino)
                    
                    shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))
                    contador += 1
                    moved = True
                    break
            
            # Move desconhecidos para "Outros"
            if not moved:
                pasta_outros = os.path.join(diretorio_alvo, "Outros")
                if not os.path.exists(pasta_outros):
                    os.makedirs(pasta_outros)
                shutil.move(caminho_arquivo, os.path.join(pasta_outros, arquivo))
                contador += 1

        lbl_status.config(text=f"Sucesso! {contador} arquivos organizados.", fg="green")
        messagebox.showinfo("Concluído", f"Organização finalizada!\n{contador} arquivos movidos.")
        
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

# --- INTERFACE GRÁFICA (GUI) ---
def selecionar_pasta():
    pasta_selecionada = filedialog.askdirectory()
    if pasta_selecionada:
        entrada_caminho.delete(0, tk.END)
        entrada_caminho.insert(0, pasta_selecionada)
        lbl_status.config(text="Pasta selecionada. Pronto para organizar.", fg="blue")

# Configuração da Janela Principal
janela = tk.Tk()
janela.title("Organizador de Arquivos Pro")
janela.geometry("500x250")
janela.resizable(False, False)

# Título
lbl_titulo = tk.Label(janela, text="Organizador Automático de Arquivos", font=("Arial", 14, "bold"))
lbl_titulo.pack(pady=15)

# Área de seleção
frame_selecao = tk.Frame(janela)
frame_selecao.pack(pady=10)

entrada_caminho = tk.Entry(frame_selecao, width=40)
entrada_caminho.pack(side=tk.LEFT, padx=5)

btn_selecionar = tk.Button(frame_selecao, text="📂 Selecionar Pasta", command=selecionar_pasta)
btn_selecionar.pack(side=tk.LEFT)

# Botão de Ação
btn_organizar = tk.Button(janela, text="ORGANIZAR AGORA", font=("Arial", 10, "bold"), 
                          bg="#4CAF50", fg="white", height=2, width=20, command=organizar_arquivos)
btn_organizar.pack(pady=20)

# Status
lbl_status = tk.Label(janela, text="Selecione uma pasta para começar...", font=("Arial", 9, "italic"))
lbl_status.pack(side=tk.BOTTOM, pady=10)

# Iniciar o loop da interface
janela.mainloop()