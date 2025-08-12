def aplicar_regras(fatos, regras):
    conclusoes = []

    for regra in regras:
        condicoes = regra["condicoes"]

        # Verifica se todas as condições da regra são atendidas
        if all(fatos.get(campo) == valor for campo, valor in condicoes.items()):
            conclusoes.append({
                "conclusao": regra["conclusao"],
                "recomendacao": regra["recomendacao"],
                "gravidade": regra.get("gravidade", "Média"),   # Usa gravidade se existir, senão padrão
                "baseado_em": list(condicoes.keys())            # Lista de fatos usados
            })

    # Remover conclusões duplicadas para evitar repetir diagnósticos
    conclusoes_unicas = []
    vistos = set()
    for c in conclusoes:
        if c["conclusao"] not in vistos:
            conclusoes_unicas.append(c)
            vistos.add(c["conclusao"])

    return conclusoes_unicas
