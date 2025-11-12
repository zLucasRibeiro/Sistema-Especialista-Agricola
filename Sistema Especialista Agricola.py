import tkinter as tk
from tkinter import ttk, font as tkfont # Importa tkfont para facilitar a definição de fontes

# Base de conhecimento
base_de_conhecimento = [
    {
        "condicoes": {"tipo_solo": "argiloso", "clima": "tropical", "estacao": "verao", "irrigacao": "sim"},
        "recomendacao": "Arroz (ideal para solos argilosos que retêm água, clima quente e úmido, com irrigação)"
    },
    {
        "condicoes": {"tipo_solo": "argiloso", "clima": "tropical", "estacao": "chuvosa", "irrigacao": "sim"},
        "recomendacao": "Arroz (ideal para solos argilosos, clima quente e úmido, especialmente durante a estação chuvosa com irrigação suplementar)"
    },
    {
        "condicoes": {"tipo_solo": "arenoso", "clima": "semiarido", "estacao": "primavera", "irrigacao": "sim"},
        "recomendacao": "Melancia (adapta-se bem a solos arenosos com irrigação, especialmente em climas quentes e secos)"
    },
    {
        "condicoes": {"tipo_solo": "humoso", "clima": "subtropical", "estacao": "outono", "irrigacao": "nao"},
        "recomendacao": "Batata Doce (tolera solos humosos e climas subtropicais, podendo ser cultivada sem irrigação se houver umidade residual)"
    },
    {
        "condicoes": {"tipo_solo": "calcario", "clima": "tropical", "estacao": "verao", "irrigacao": "sim"},
        "recomendacao": "Cana-de-açúcar (desenvolve-se em solos calcários sob clima tropical com boa disponibilidade de água)"
    },
    {
        "condicoes": {"tipo_solo": "argiloso", "clima": "subtropical", "estacao": "inverno", "irrigacao": "nao"},
        "recomendacao": "Trigo (cultura de inverno que se adapta a solos argilosos e climas subtropicais, pode não necessitar de irrigação dependendo das chuvas de inverno)"
    },
    {
        "condicoes": {"tipo_solo": "humoso", "clima": "tropical", "estacao": "primavera", "irrigacao": "sim"},
        "recomendacao": "Milho (prefere solos férteis como os humosos, clima tropical e irrigação para garantir a produtividade)"
    },
    {
        "condicoes": {"tipo_solo": "arenoso", "clima": "tropical", "estacao": "verao", "irrigacao": "nao"},
        "recomendacao": "Mandioca (rústica, tolera solos arenosos e períodos de seca, embora a produtividade seja maior com água no início)"
    },
    {
        "condicoes": {"tipo_solo": "argiloso", "clima": "semiarido", "estacao": "verao", "irrigacao": "sim"},
        "recomendacao": "Sorgo (resistente à seca e altas temperaturas, ideal para solos argilosos em regiões semiáridas com irrigação)"
    },
    {
        "condicoes": {"tipo_solo": "humoso", "clima": "tropical", "estacao": "verao", "irrigacao": "sim"},
        "recomendacao": "Feijão Caupi (Feijão de Corda) (adaptado a climas tropicais e solos férteis, necessita de irrigação no verão)"
    },
    {
        "condicoes": {"tipo_solo": "arenoso", "clima": "tropical", "estacao": "primavera", "irrigacao": "sim"},
        "recomendacao": "Abacaxi (desenvolve-se bem em solos arenosos, bem drenados, sob clima tropical e com irrigação)"
    },
    {
        "condicoes": {"tipo_solo": "argiloso", "clima": "equatorial", "estacao": "chuvosa", "irrigacao": "sim"},
        "recomendacao": "Açaí (nativo de regiões equatoriais com solos argilosos e úmidos, a irrigação complementa as chuvas)"
    },
    {
        "condicoes": {"tipo_solo": "humoso", "clima": "subtropical", "estacao": "primavera", "irrigacao": "sim"},
        "recomendacao": "Soja (requer solos férteis e bem drenados, clima subtropical e irrigação para altas produtividades)"
    },
    {
        "condicoes": {"tipo_solo": "arenoso", "clima": "semiarido", "estacao": "outono", "irrigacao": "nao"},
        "recomendacao": "Palma Forrageira (extremamente resistente à seca, ideal para solos arenosos no semiárido, não exige irrigação)"
    },
    {
        "condicoes": {"tipo_solo": "calcario", "clima": "subtropical", "estacao": "primavera", "irrigacao": "sim"},
        "recomendacao": "Uva (adapta-se a solos calcários com boa drenagem, clima subtropical e irrigação controlada)"
    },
    {
        "condicoes": {"tipo_solo": "humoso", "clima": "temperado", "estacao": "primavera", "irrigacao": "sim"},
        "recomendacao": "Alface (cresce bem em solos ricos em matéria orgânica, clima temperado e com irrigação constante)"
    },
    {
        "condicoes": {"tipo_solo": "argiloso", "clima": "temperado", "estacao": "verao", "irrigacao": "sim"},
        "recomendacao": "Tomate (requer solo bem drenado mas com boa retenção, clima temperado a quente, e irrigação regular)"
    },
    {
        "condicoes": {"tipo_solo": "arenoso", "clima": "temperado", "estacao": "primavera", "irrigacao": "nao"},
        "recomendacao": "Cenoura (prefere solos leves e arenosos para desenvolvimento da raiz, clima temperado, pode precisar de irrigação inicial mas menos depois)"
    }
]

# Opções válidas para cada fator
opcoes_gerais = {
    "tipo_solo": ["arenoso", "argiloso", "humoso", "calcario"],
    "clima": ["tropical", "subtropical", "semiarido", "equatorial", "temperado"],
    "estacao": ["primavera", "verao", "outono", "inverno", "chuvosa", "seca"],
    "irrigacao": ["sim", "nao"]
}

def recomendar_cultivo(escolhas_usuario, base_conhecimento):
    for regra in base_conhecimento:
        condicoes_satisfeitas = True
        for fator, valor_condicao in regra["condicoes"].items():
            if escolhas_usuario.get(fator) != valor_condicao:
                condicoes_satisfeitas = False
                break
        if condicoes_satisfeitas:
            return regra["recomendacao"]
    return "Desculpe, não foi encontrada uma recomendação específica para as condições fornecidas."

def obter_recomendacao():
    escolhas = {
        "tipo_solo": tipo_solo_var.get(),
        "clima": clima_var.get(),
        "estacao": estacao_var.get(),
        "irrigacao": irrigacao_var.get()
    }
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
# Você pode adicionar uma cor (fg) se desejar, por exemplo, um azul escuro: fg="#003366"
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
