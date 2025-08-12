def aplicar_regras(fatos, regras):
    conclusoes = []

    for regra in regras:
        condicoes = regra["condicoes"]

        # Verifica se todas as condições da regra são atendidas
        if all(fatos.get(campo) == valor for campo, valor in condicoes.items()):
            conclusoes.append({
                "conclusao": regra["conclusao"],
                "recomendacao": regra["recomendacao"]
            })

    return conclusoes
