# main.py
# Interface simples no terminal para coletar fatos e rodar o motor de inferência

from regras import REGRAS
from motor import aplicar_regras

def perguntar_bool(pergunta):
    while True:
        resposta = input(pergunta + " (s/n): ").strip().lower()
        if resposta in ["s", "sim"]:
            return True
        elif resposta in ["n", "nao", "não"]:
            return False
        else:
            print("Resposta inválida. Digite 's' ou 'n'.")

def main():
    print("\n=== Sistema Especialista: Diagnóstico de Falhas em Automóveis ===\n")

    # Coleta de fatos (mínimo 5 perguntas)
    fatos = {}
    fatos["motor_gira"] = perguntar_bool("Ao girar a chave, o motor gira?")
    fatos["luzes_fraqueza"] = perguntar_bool("As luzes do carro estão fracas?")
    fatos["som_click"] = perguntar_bool("Há som de 'click' ao tentar ligar?")
    fatos["tanque_vazio"] = perguntar_bool("O tanque de combustível está vazio?")
    fatos["faísca_velas"] = perguntar_bool("Há faísca nas velas?")
    fatos["bateria_carregada"] = perguntar_bool("A bateria está carregada?")
    fatos["queda_tensao_motor_ligado"] = perguntar_bool("Há queda de tensão com o motor ligado?")
    fatos["luz_injecao"] = perguntar_bool("A luz de injeção está acesa?")
    fatos["fumaça_preta"] = perguntar_bool("Sai fumaça preta do escapamento?")
    fatos["temperatura_alta"] = perguntar_bool("O motor está superaquecendo?")
    fatos["liquido_arrefecimento_baixo"] = perguntar_bool("O nível de líquido de arrefecimento está baixo?")
    fatos["ruido_metalico"] = perguntar_bool("Há ruído metálico alto vindo do motor?")
    fatos["freios_falhando"] = perguntar_bool("Os freios estão falhando?")
    fatos["direcao_dura"] = perguntar_bool("A direção está dura?")

    # Aplicar o motor de inferência
    resultados = aplicar_regras(fatos, REGRAS)

    # Mostrar resultados
    print("\n=== Resultados ===")
    if resultados:
        for r in resultados:
            print(f"\nDiagnóstico: {r['conclusao']}")
            print(f"Recomendação: {r['recomendacao']}")
    else:
        print("Nenhuma falha identificada com base nas respostas.")

if __name__ == "__main__":
    main()
