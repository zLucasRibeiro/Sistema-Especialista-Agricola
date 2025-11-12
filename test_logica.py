# Arquivo: test_logica.py
# Este arquivo roda testes unitários na lógica de recomendação usando pytest.

# CORRIGIDO: A importação agora aponta para o arquivo de lógica pura (logica_agricola.py), 
# que não inicia a interface gráfica (Tkinter).
from logica_agricola import recomendar_cultivo, base_de_conhecimento

# Requisito RF.04: Retornar uma recomendação válida se a combinação existir (T.04)
def test_T04_caminho_feliz_regra_1():
    """Testa a Regra 1: argiloso, tropical, verao, sim -> Arroz."""
    escolhas = {
        "tipo_solo": "argiloso",
        "clima": "tropical",
        "estacao": "verao",
        "irrigacao": "sim"
    }
    resultado = recomendar_cultivo(escolhas, base_de_conhecimento)
    assert "Arroz" in resultado

# Requisito RF.04: Retornar uma recomendação válida (T.05)
def test_T05_caminho_feliz_regra_2():
    """Testa a Regra 2: humoso, subtropical, outono, nao -> Batata Doce."""
    escolhas = {
        "tipo_solo": "humoso",
        "clima": "subtropical",
        "estacao": "outono",
        "irrigacao": "nao"
    }
    resultado = recomendar_cultivo(escolhas, base_de_conhecimento)
    assert "Batata Doce" in resultado

# Requisito RF.05: Retornar mensagem de "não encontrada" se a regra não existir (T.06)
def test_T06_excecao_nao_encontrada():
    """Testa uma combinação inexistente: calcario, equatorial, inverno, nao."""
    escolhas = {
        "tipo_solo": "calcario",
        "clima": "equatorial",
        "estacao": "inverno",
        "irrigacao": "nao"
    }
    resultado = recomendar_cultivo(escolhas, base_de_conhecimento)
    assert "não foi encontrada" in resultado
