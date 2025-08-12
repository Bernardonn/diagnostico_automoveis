# regras.py
REGRAS = [
    {
        "condicoes": {
            "motor_gira": False,
            "bateria_carregada": False,
        },
        "conclusao": "Bateria descarregada",
        "recomendacao": "Verificar e recarregar a bateria ou substituir se necessário.",
        "gravidade": "Baixa"
    },
    {
        "condicoes": {
            "motor_gira": False,
            "som_click": True,
            "tanque_vazio": False
        },
        "conclusao": "Problema no motor de partida ou relé",
        "recomendacao": "Verificar motor de partida e sistema elétrico.",
        "gravidade": "Média"
    },
    {
        "condicoes": {
            "motor_gira": True,
            "faísca_velas": False,
        },
        "conclusao": "Problema no sistema de ignição",
        "recomendacao": "Verificar velas e bobina de ignição.",
        "gravidade": "Média"
    },
    {
        "condicoes": {
            "tanque_vazio": True,
        },
        "conclusao": "Veículo sem combustível",
        "recomendacao": "Abastecer o veículo.",
        "gravidade": "Baixa"
    },
    {
        "condicoes": {
            "temperatura_alta": True,
            "liquido_arrefecimento_baixo": True,
        },
        "conclusao": "Superaquecimento por falta de líquido de arrefecimento",
        "recomendacao": "Completar líquido e verificar possíveis vazamentos.",
        "gravidade": "Alta"
    },
    {
        "condicoes": {
            "luzes_fraqueza": True,
            "queda_tensao_motor_ligado": True,
        },
        "conclusao": "Alternador com defeito",
        "recomendacao": "Verificar alternador e regulador de tensão.",
        "gravidade": "Alta"
    },
    {
        "condicoes": {
            "freios_falhando": True,
        },
        "conclusao": "Sistema de freios comprometido",
        "recomendacao": "Verificar pastilhas, discos e fluido de freio.",
        "gravidade": "Média"
    },
    {
        "condicoes": {
            "direcao_dura": True,
        },
        "conclusao": "Problema na direção hidráulica ou assistida",
        "recomendacao": "Verificar fluido e bomba de direção.",
        "gravidade": "Baixa"
    },
    {
        "condicoes": {
            "ruido_metalico": True,
        },
        "conclusao": "Ruído metálico no motor - possível desgaste ou folga",
        "recomendacao": "Levar para análise mecânica detalhada.",
        "gravidade": "Alta"
    },
    {
        "condicoes": {
            "luz_injecao": True,
            "fumaça_preta": True,
        },
        "conclusao": "Problema na injeção eletrônica",
        "recomendacao": "Levar para diagnóstico com scanner automotivo.",
        "gravidade": "Alta"
    }
]
