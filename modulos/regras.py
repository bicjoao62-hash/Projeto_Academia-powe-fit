"""Regras de negócio compartilhadas entre os módulos."""

from datetime import date

from modulos import banco_dados as bd

DIAS_POR_MES = 30
# (duração mínima em meses, desconto) — do maior para o menor.
DESCONTOS_POR_DURACAO = ((12, 0.15), (6, 0.10))


def calcular_desconto(duracao_meses: int) -> float:
    """Planos mais longos ganham desconto de fidelidade."""
    return next(
        (desconto for minimo, desconto in DESCONTOS_POR_DURACAO if duracao_meses >= minimo),
        0.0,
    )


def status_matricula(matricula: dict, hoje: date | None = None) -> str:
    hoje = hoje or date.today()
    if matricula["cancelada"]:
        return "Cancelada"
    if hoje > matricula["fim"]:
        return "Vencida"
    return "Ativa"


def esta_ativa(matricula: dict) -> bool:
    return status_matricula(matricula) == "Ativa"


def matriculas_ativas() -> list[dict]:
    return [m for m in bd.matriculas if esta_ativa(m)]


def contar_matriculas_ativas(campo: str, id_registro: int) -> int:
    """Conta matrículas ativas ligadas a um aluno, plano ou instrutor.

    `campo` deve ser 'aluno_id', 'plano_id' ou 'instrutor_id'.
    """
    return sum(1 for m in matriculas_ativas() if m[campo] == id_registro)