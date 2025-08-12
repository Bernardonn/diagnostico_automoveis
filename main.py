# main.py
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

def coletar_fatos():
    fatos = {}
    print("\n🔋 Categoria: Elétrica e Partida")
    fatos["motor_gira"] = perguntar_bool("Ao girar a chave, o motor gira?")
    fatos["luzes_fraqueza"] = perguntar_bool("As luzes do carro estão fracas?")
    fatos["som_click"] = perguntar_bool("Há som de 'click' ao tentar ligar?")
    fatos["bateria_carregada"] = perguntar_bool("A bateria está carregada?")
    fatos["queda_tensao_motor_ligado"] = perguntar_bool("Há queda de tensão com o motor ligado?")

    print("\n⛽ Categoria: Combustível e Injeção")
    fatos["tanque_vazio"] = perguntar_bool("O tanque de combustível está vazio?")
    fatos["luz_injecao"] = perguntar_bool("A luz de injeção está acesa?")
    fatos["fumaça_preta"] = perguntar_bool("Sai fumaça preta do escapamento?")
    fatos["faísca_velas"] = perguntar_bool("Há faísca nas velas?")

    print("\n🌡 Categoria: Superaquecimento")
    fatos["temperatura_alta"] = perguntar_bool("O motor está superaquecendo?")
    fatos["liquido_arrefecimento_baixo"] = perguntar_bool("O nível de líquido de arrefecimento está baixo?")

    print("\n⚙ Categoria: Mecânica")
    fatos["ruido_metalico"] = perguntar_bool("Há ruído metálico alto vindo do motor?")

    print("\n🛑 Categoria: Freios e Direção")
    fatos["freios_falhando"] = perguntar_bool("Os freios estão falhando?")
    fatos["direcao_dura"] = perguntar_bool("A direção está dura?")

    return fatos

def exibir_resultados(resultados):
    print("\n=== 🔍 RESULTADOS DO DIAGNÓSTICO ===")
    if resultados:
        for r in resultados:
            print(f"\n⚠ Problema: {r['conclusao']}")
            print(f"📋 Baseado em: {', '.join(r['baseado_em'])}")
            print(f"🛠 Recomendação: {r['recomendacao']}")
            print(f"🔴 Gravidade: {r['gravidade']}")
    else:
        print("✅ Nenhuma falha identificada com base nas respostas.")

def main():
    print("="*60)
    print("   SISTEMA ESPECIALISTA - DIAGNÓSTICO DE FALHAS AUTOMOTIVAS   ")
    print("="*60)
    print("Responda as perguntas com 's' para sim ou 'n' para não.\n")

    fatos = coletar_fatos()
    resultados = aplicar_regras(fatos, REGRAS)
    exibir_resultados(resultados)

    if perguntar_bool("\nDeseja realizar outro diagnóstico?"):
        main()

if __name__ == "__main__":
    main()
