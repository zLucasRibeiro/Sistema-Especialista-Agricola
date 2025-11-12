# Arquivo: logica_agricola.py
# Contém apenas a base de conhecimento e a função de recomendação para testes e importação.

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
