"""Armazenamento em memória (listas Python) e funções genéricas de acesso.

Os dados existem apenas durante a execução do programa.
"""

# Planos que já existem quando o sistema é iniciado.
# O desconto de fidelidade (6+ e 12+ meses) é aplicado na matrícula,
# por isso o valor mensal abaixo é o valor "de tabela".
PLANOS_INICIAIS: list[dict] = [
    {"id": 1, "nome": "Mensal", "duracao_meses": 1, "valor_mensal": 120.00},
    {"id": 2, "nome": "Trimestral", "duracao_meses": 3, "valor_mensal": 110.00},
    {"id": 3, "nome": "Semestral", "duracao_meses": 6, "valor_mensal": 100.00},
    {"id": 4, "nome": "Anual", "duracao_meses": 12, "valor_mensal": 95.00},
]

# Alunos que já existem quando o sistema é iniciado.
# CPFs de exemplo (válidos); nascimento no formato dd/mm/aaaa.
ALUNOS_INICIAIS: list[dict] = [
    {"id": 1, "nome": "Lucas Ferreira", "cpf": "28451739628",
     "telefone": "83991234567", "nascimento": "14/03/1998"},
    {"id": 2, "nome": "Mariana Costa", "cpf": "17642895364",
     "telefone": "83988776655", "nascimento": "22/07/2001"},
    {"id": 3, "nome": "Rafael Souza", "cpf": "39284516773",
     "telefone": "83999887766", "nascimento": "05/11/1995"},
    {"id": 4, "nome": "Camila Santos", "cpf": "51827364955",
     "telefone": "83987654321", "nascimento": "30/01/2003"},
    {"id": 5, "nome": "Pedro Henrique Lima", "cpf": "64193728528",
     "telefone": "83996543210", "nascimento": "18/09/1990"},
    {"id": 6, "nome": "Ana Beatriz Oliveira", "cpf": "82736459164",
     "telefone": "83992345678", "nascimento": "09/06/2000"},
]

# Instrutores que já existem quando o sistema é iniciado.
INSTRUTORES_INICIAIS: list[dict] = [
    {"id": 1, "nome": "Carlos Eduardo Mendes", "cpf": "31627485937",
     "especialidade": "Musculação"},
    {"id": 2, "nome": "Juliana Rocha", "cpf": "45298163700",
     "especialidade": "Spinning"},
    {"id": 3, "nome": "Thiago Barbosa", "cpf": "68925431700",
     "especialidade": "Funcional"},
]

alunos: list[dict] = [aluno.copy() for aluno in ALUNOS_INICIAIS]
planos: list[dict] = [plano.copy() for plano in PLANOS_INICIAIS]
instrutores: list[dict] = [instrutor.copy() for instrutor in INSTRUTORES_INICIAIS]
matriculas: list[dict] = []


def proximo_id(registros: list[dict]) -> int:
    """Retorna o próximo ID sequencial disponível para a lista informada."""
    return max((registro["id"] for registro in registros), default=0) + 1


def buscar_por_id(registros: list[dict], id_registro: int) -> dict | None:
    """Retorna o registro com o ID informado ou None se não existir."""
    return next((r for r in registros if r["id"] == id_registro), None)


def buscar_nome(registros: list[dict], id_registro: int) -> str:
    """Retorna o nome do registro ou um texto padrão se ele foi removido."""
    registro = buscar_por_id(registros, id_registro)
    return registro["nome"] if registro else "(removido)"