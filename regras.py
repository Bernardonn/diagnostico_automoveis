REGRAS = [
    {
        "condicoes": {
            "motor_gira": False,
            "luzes_fraqueza": True,
            "som_click": True
        },
        "conclusao": "Bateria fraca ou descarregada.",
        "recomendacao": "Verificar carga da bateria e cabos de conexão."
    },
    {
        "condicoes": {
            "motor_gira": False,
            "luzes_fraqueza": False,
            "som_click": False
        },
        "conclusao": "Possível problema no motor de arranque ou relé.",
        "recomendacao": "Verificar motor de partida e sistema elétrico."
    },
    {
        "condicoes": {
            "motor_gira": True,
            "tanque_vazio": True
        },
        "conclusao": "Veículo sem combustível.",
        "recomendacao": "Abastecer o veículo."
    },
    {
        "condicoes": {
            "motor_gira": True,
            "faísca_velas": False
        },
        "conclusao": "Problema no sistema de ignição.",
        "recomendacao": "Verificar velas e bobina de ignição."
    },
    {
        "condicoes": {
            "bateria_carregada": False,
            "queda_tensao_motor_ligado": True
        },
        "conclusao": "Alternador com defeito.",
        "recomendacao": "Verificar alternador e regulador de tensão."
    },
    {
        "condicoes": {
            "luz_injecao": True,
            "fumaça_preta": True
        },
        "conclusao": "Problema na mistura ar/combustível.",
        "recomendacao": "Verificar injetores e sensor de oxigênio."
    },
    {
        "condicoes": {
            "temperatura_alta": True,
            "liquido_arrefecimento_baixo": True
        },
        "conclusao": "Superaquecimento por falta de líquido de arrefecimento.",
        "recomendacao": "Completar líquido e verificar possíveis vazamentos."
    },
    {
        "condicoes": {
            "ruido_metalico": True
        },
        "conclusao": "Problema mecânico interno grave.",
        "recomendacao": "Não dirigir; levar para oficina imediatamente."
    },
    {
        "condicoes": {
            "freios_falhando": True
        },
        "conclusao": "Sistema de freios comprometido.",
        "recomendacao": "Verificar pastilhas, discos e fluido de freio."
    },
    {
        "condicoes": {
            "direcao_dura": True
        },
        "conclusao": "Problema na direção hidráulica/assistida.",
        "recomendacao": "Verificar fluido e bomba de direção."
    }
]
