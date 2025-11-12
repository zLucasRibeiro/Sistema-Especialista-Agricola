# Arquivo: Sistema_Especialista_Agricola.py
import tkinter as tk
from tkinter import ttk, font as tkfont # Importa tkfont para facilitar a definição de fontes

# IMPORTAÇÃO DA LÓGICA:
# A base de conhecimento, as opções gerais e a função recomendar_cultivo 
# foram movidas para 'logica_agricola.py' para permitir testes em ambientes headless (sem interface gráfica).
from logica_agricola import recomendar_cultivo, base_de_conhecimento, opcoes_gerais 

def obter_recomendacao():
    escolhas = {
        "tipo_solo": tipo_solo_var.get(),
        "clima": clima_var.get(),
        "estacao": estacao_var.get(),
        "irrigacao": irrigacao_var.get()
    }
    # Esta função é importada de logica_agricola
    recomendacao = recomendar_cultivo(escolhas, base_de_conhecimento) 
    resultado_texto.set(recomendacao)

# Cria a janela principal
janela = tk.Tk()
janela.title("Sistema Especialista Agrícola - UERJ")
janela.geometry("550x550") # Define um tamanho inicial para a janela

# --- Título UERJ com Fonte Grande ---
# Define uma fonte personalizada para o título "UERJ"
try:
    fonte_titulo_uerj = tkfont.Font(family="Helvetica", size=30, weight="bold")
except tk.TclError: # Fallback se a fonte não for encontrada
    fonte_titulo_uerj = tkfont.Font(family="Arial", size=30, weight="bold")

# Cria o Label para "UERJ"
label_uerj = tk.Label(janela, text="UERJ", font=fonte_titulo_uerj, fg="#004080") # Um tom de azul UERJ
label_uerj.grid(row=0, column=0, columnspan=2, pady=(20, 25)) # pady adiciona espaço vertical (em cima, embaixo)
# --- Fim do Título UERJ ---

# Variáveis para armazenar as escolhas do usuário
tipo_solo_var = tk.StringVar(janela)
clima_var = tk.StringVar(janela)
estacao_var = tk.StringVar(janela)
irrigacao_var = tk.StringVar(janela)
resultado_texto = tk.StringVar(janela, value="Aguardando seleção...")

# Os widgets de input agora começam da linha 1
# Frame para os campos de entrada, para melhor organização
frame_inputs = tk.Frame(janela)
frame_inputs.grid(row=1, column=0, columnspan=2, padx=20, pady=5)

tk.Label(frame_inputs, text="Tipo de Solo:").grid(row=0, column=0, padx=5, pady=8, sticky="w")
# 'opcoes_gerais' é importado de logica_agricola
tipo_solo_combo = ttk.Combobox(frame_inputs, textvariable=tipo_solo_var, values=opcoes_gerais["tipo_solo"], state="readonly", width=25) 
tipo_solo_combo.grid(row=0, column=1, padx=5, pady=8, sticky="ew")
if opcoes_gerais["tipo_solo"]: tipo_solo_combo.set(opcoes_gerais["tipo_solo"][0])

tk.Label(frame_inputs, text="Clima:").grid(row=1, column=0, padx=5, pady=8, sticky="w")
clima_combo = ttk.Combobox(frame_inputs, textvariable=clima_var, values=opcoes_gerais["clima"], state="readonly", width=25)
clima_combo.grid(row=1, column=1, padx=5, pady=8, sticky="ew")
if opcoes_gerais["clima"]: clima_combo.set(opcoes_gerais["clima"][0])

tk.Label(frame_inputs, text="Estação do Ano:").grid(row=2, column=0, padx=5, pady=8, sticky="w")
estacao_combo = ttk.Combobox(frame_inputs, textvariable=estacao_var, values=opcoes_gerais["estacao"], state="readonly", width=25)
estacao_combo.grid(row=2, column=1, padx=5, pady=8, sticky="ew")
if opcoes_gerais["estacao"]: estacao_combo.set(opcoes_gerais["estacao"][0])

tk.Label(frame_inputs, text="Disponibilidade de Irrigação:").grid(row=3, column=0, padx=5, pady=8, sticky="w")
irrigacao_combo = ttk.Combobox(frame_inputs, textvariable=irrigacao_var, values=opcoes_gerais["irrigacao"], state="readonly", width=25)
irrigacao_combo.grid(row=3, column=1, padx=5, pady=8, sticky="ew")
if opcoes_gerais["irrigacao"]: irrigacao_combo.set(opcoes_gerais["irrigacao"][0])

frame_inputs.columnconfigure(1, weight=1) # Faz a coluna dos comboboxes expandir

# Botão para obter a recomendação
recomendar_botao = tk.Button(janela, text="Recomendar", command=obter_recomendacao, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", relief="raised", borderwidth=2, padx=10, pady=5)
recomendar_botao.grid(row=2, column=0, columnspan=2, padx=20, pady=(15,10), sticky="ew")

# Frame para o resultado
frame_resultado = tk.Frame(janela, bd=1, relief="sunken")
frame_resultado.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

tk.Label(frame_resultado, text="Recomendação:", font=("Helvetica", 11, "italic")).pack(pady=(5,2), anchor="w", padx=5)
resultado_label = tk.Label(frame_resultado, textvariable=resultado_texto, wraplength=480, justify="left", anchor="nw", padx=5, pady=5, height=6) # altura para texto
resultado_label.pack(fill="both", expand=True, padx=5, pady=5)

# Configuração de layout para redimensionamento da janela principal
janela.columnconfigure(0, weight=1) # Permite que a coluna principal expanda
# janela.columnconfigure(1, weight=1) # Desnecessário se columnspan=2 é usado amplamente
janela.rowconfigure(3, weight=1) # Permite que o frame_resultado (linha 3) expanda verticalmente

if __name__ == "__main__":
    janela.mainloop() # Inicia o loop de eventos do Tkinter apenas se o arquivo for executado diretamente
