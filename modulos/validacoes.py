"""Conversores e validadores de entrada.

Todas as funções recebem o texto digitado e devolvem o valor já tratado.
Quando o texto é inválido, levantam ValueError com uma mensagem amigável,
que é exibida pela função `interface.ler_campo`.
"""

import re
from datetime import date, datetime
from typing import Callable

FORMATO_DATA = "%d/%m/%Y"
IDADE_MINIMA = 14


def somente_digitos(texto: str) -> str:
    """Remove qualquer caractere que não seja número."""
    return re.sub(r"\D", "", texto)


def texto_obrigatorio(texto: str) -> str:
    if not texto:
        raise ValueError("Campo obrigatório.")
    return texto


def nome_valido(texto: str) -> str:
    nome = " ".join(texto.split())
    partes = nome.replace("-", "").replace("'", "").split()
    if len(nome) < 3 or not all(parte.isalpha() for parte in partes):
        raise ValueError("Informe um nome válido (apenas letras, mínimo 3).")
    return nome.title()


def cpf_valido(texto: str) -> str:
    """Valida o CPF pelos dígitos verificadores e retorna só os números."""
    cpf = somente_digitos(texto)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        raise ValueError("CPF inválido.")

    for posicao in (9, 10):
        pesos = range(posicao + 1, 1, -1)
        soma = sum(int(digito) * peso for digito, peso in zip(cpf[:posicao], pesos))
        if (soma * 10) % 11 % 10 != int(cpf[posicao]):
            raise ValueError("CPF inválido.")
    return cpf


def telefone_valido(texto: str) -> str:
    telefone = somente_digitos(texto)
    if len(telefone) not in (10, 11):
        raise ValueError("Telefone inválido. Use DDD + número (10 ou 11 dígitos).")
    return telefone


def calcular_idade(nascimento: str, hoje: date | None = None) -> int:
    """Calcula a idade a partir de uma data no formato dd/mm/aaaa."""
    hoje = hoje or date.today()
    data = datetime.strptime(nascimento, FORMATO_DATA).date()
    aniversario_passou = (hoje.month, hoje.day) >= (data.month, data.day)
    return hoje.year - data.year - (not aniversario_passou)


def data_nascimento_valida(texto: str) -> str:
    try:
        data = datetime.strptime(texto, FORMATO_DATA)
    except ValueError:
        raise ValueError("Data inválida. Use o formato dd/mm/aaaa.") from None

    nascimento = data.strftime(FORMATO_DATA)
    idade = calcular_idade(nascimento)
    if idade < 0:
        raise ValueError("A data de nascimento não pode estar no futuro.")
    if idade < IDADE_MINIMA:
        raise ValueError(f"Idade mínima para ser aluno: {IDADE_MINIMA} anos.")
    return nascimento


def inteiro_positivo(texto: str) -> int:
    if not texto.isdigit() or int(texto) <= 0:
        raise ValueError("Digite um número inteiro maior que zero.")
    return int(texto)


def inteiro_entre(minimo: int, maximo: int) -> Callable[[str], int]:
    """Cria um conversor que aceita inteiros dentro do intervalo informado."""

    def conversor(texto: str) -> int:
        if not texto.isdigit() or not minimo <= int(texto) <= maximo:
            raise ValueError(f"Digite um número inteiro entre {minimo} e {maximo}.")
        return int(texto)

    return conversor


def valor_monetario(texto: str) -> float:
    try:
        valor = float(texto.replace(",", "."))
    except ValueError:
        raise ValueError("Valor inválido. Exemplo: 89,90") from None
    if valor <= 0:
        raise ValueError("O valor deve ser maior que zero.")
    return round(valor, 2)