"""Funções de formatação de dados para exibição no terminal."""

from datetime import date


def formatar_cpf(cpf: str) -> str:
    """Converte '12345678909' em '123.456.789-09'."""
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def formatar_telefone(telefone: str) -> str:
    """Converte '83999998888' em '(83) 99999-8888'."""
    numero = telefone[2:]
    return f"({telefone[:2]}) {numero[:-4]}-{numero[-4:]}"


def formatar_moeda(valor: float) -> str:
    """Converte 1234.5 em 'R$ 1.234,50'."""
    texto = f"{valor:,.2f}"
    return "R$ " + texto.replace(",", "X").replace(".", ",").replace("X", ".")


def formatar_data(data: date) -> str:
    """Converte um objeto date em 'dd/mm/aaaa'."""
    return data.strftime("%d/%m/%Y")