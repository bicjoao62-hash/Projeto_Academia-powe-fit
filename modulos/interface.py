"""Funções de interação com o usuário via terminal (input/print)."""

import os
from typing import Any, Callable

from modulos.banco_dados import buscar_por_id
from modulos.validacoes import inteiro_positivo, texto_obrigatorio

LARGURA = 40
Opcoes = dict[str, tuple[str, Callable[[], None]]]


# --------------------------------------------------------------- Exibição
def limpar_tela() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def linha(caractere: str = "=") -> None:
    print(caractere * LARGURA)


def exibir_banner() -> None:
    linha()
    print("ACADEMIA POWER FIT".center(LARGURA))
    print("Sistema de Gerenciamento".center(LARGURA))
    linha()


def exibir_titulo(titulo: str) -> None:
    print(f"\n--- {titulo} ---\n")


def exibir_sucesso(mensagem: str) -> None:
    print(f"\n[OK] {mensagem}")


def exibir_erro(mensagem: str) -> None:
    print(f"[ERRO] {mensagem}")


def exibir_aviso(mensagem: str) -> None:
    print(f"[!] {mensagem}")


def pausar() -> None:
    input("\nPressione ENTER para continuar...")


def exibir_tabela(colunas: list[str], linhas: list[list[Any]]) -> None:
    """Imprime uma tabela de texto com colunas alinhadas à esquerda."""
    larguras = [
        max([len(coluna)] + [len(str(registro[i])) for registro in linhas])
        for i, coluna in enumerate(colunas)
    ]

    def formatar(valores: list[Any]) -> str:
        return " | ".join(str(v).ljust(larg) for v, larg in zip(valores, larguras))

    print(formatar(colunas))
    print("-+-".join("-" * largura for largura in larguras))
    for registro in linhas:
        print(formatar(registro))


# ---------------------------------------------------------------- Entrada
def ler_campo(
    mensagem: str,
    conversor: Callable[[str], Any] = texto_obrigatorio,
    padrao: Any = None,
    formato: Callable[[Any], str] = str,
) -> Any:
    """Lê um valor repetindo a pergunta até que o conversor o aceite.

    Se `padrao` for informado, pressionar ENTER mantém o valor atual
    (útil nas telas de alteração).
    """
    sufixo = f" [{formato(padrao)}]" if padrao is not None else ""
    while True:
        entrada = input(f"{mensagem}{sufixo}: ").strip()
        if not entrada and padrao is not None:
            return padrao
        try:
            return conversor(entrada)
        except ValueError as erro:
            exibir_erro(str(erro))


def confirmar(mensagem: str) -> bool:
    while True:
        resposta = input(f"{mensagem} (s/n): ").strip().lower()
        if resposta in ("s", "n"):
            return resposta == "s"
        exibir_erro("Responda com 's' ou 'n'.")


def selecionar_registro(rotulo: str, registros: list[dict]) -> dict | None:
    """Pede um ID e retorna o registro correspondente (ou None, com aviso)."""
    id_registro = ler_campo(f"ID do {rotulo.lower()}", inteiro_positivo)
    registro = buscar_por_id(registros, id_registro)
    if registro is None:
        exibir_erro(f"{rotulo} não encontrado.")
    return registro


# ------------------------------------------------------------------ Menus
def executar_menu(
    titulo: str,
    opcoes: Opcoes,
    rotulo_saida: str = "Voltar",
    pausar_apos: bool = True,
) -> None:
    """Exibe o menu em loop até o usuário escolher a opção 0."""
    while True:
        limpar_tela()
        exibir_banner()
        print(f"\n{titulo}")
        for chave, (rotulo, _) in opcoes.items():
            print(f"{chave} - {rotulo}")
        print(f"0 - {rotulo_saida}")
        linha()

        escolha = input("Digite a opção desejada: ").strip()
        if escolha == "0":
            return
        if escolha not in opcoes:
            exibir_erro("Opção inválida.")
            pausar()
            continue

        limpar_tela()
        opcoes[escolha][1]()
        if pausar_apos:
            pausar()