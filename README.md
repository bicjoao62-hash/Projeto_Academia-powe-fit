# 🏋️ Academia Power Fit — Sistema de Gerenciamento

Sistema de terminal em Python para gerenciar uma academia: alunos, planos,
instrutores e matrículas, com cadastro rápido e relatórios gerenciais.

**Projeto Avaliativo — Coding (2ª Avaliação)**
Curso Superior de Tecnologia em Análise e Desenvolvimento de Sistemas — UNINASSAU João Pessoa
Professor: Joseph Donald de Maceno Vieira

## 👥 Integrantes

- João Victor Almeida Mâncio Da Silva - 03360900
- Saphyra Francisca Medeiros Da Silva - 03365434

## 🎯 Objetivo

Resolver um problema real de negócio — o controle de alunos, planos e matrículas
de uma academia — aplicando funções, módulos, validações e desenvolvimento
colaborativo com Git/GitHub.

## 🖥️ Menu principal

```
========================================
          ACADEMIA POWER FIT
        Sistema de Gerenciamento
========================================

MENU PRINCIPAL
1 - Gerenciar Alunos
2 - Gerenciar Planos
3 - Gerenciar Instrutores
4 - Matrículas
5 - Relatórios
6 - Cadastro Rápido (aluno + matrícula)
0 - Sair do Sistema
========================================
Digite a opção desejada:
```

## ✅ Funcionalidades

| Módulo | Operações |
|---|---|
| **Alunos** | Cadastrar, listar, buscar (nome/CPF), alterar, excluir |
| **Planos** | Cadastrar, listar, buscar, alterar, excluir |
| **Instrutores** | Cadastrar, listar, buscar (nome/CPF/especialidade), alterar, excluir |
| **Matrículas** | Nova matrícula, listar, cancelar |
| **Cadastro Rápido** | Cadastra um aluno novo e, na sequência, já o matricula escolhendo plano e instrutor |
| **Relatórios** | Alunos ativos, receita mensal prevista, matrículas por plano, alunos por instrutor |

## 🧭 Como matricular um aluno

### Opção A — Aluno já cadastrado (menu 4 → 1)

1. No menu principal, digite **4** (Matrículas) e depois **1** (Nova matrícula).
2. Informe o **ID do aluno** na lista exibida.
3. Informe o **ID do plano** e o **ID do instrutor**.
4. Confira o resumo (desconto, mensalidade, total e validade) e confirme com **s**.

### ⚡ Opção B — Cadastro Rápido (menu 6 → 1)

Fluxo único para recepção, para alunos novos:

1. O sistema pede nome, CPF, telefone e data de nascimento do novo aluno.
2. Pergunta se deseja matricular o aluno agora.
3. Se sim, exibe os planos e os instrutores para escolha.
4. Mostra o resumo (desconto, mensalidade, total e validade) e pede confirmação.

Para conferir, use **4 → 2 (Listar matrículas)** ou o menu **5 (Relatórios)**.

## 📦 Dados iniciais

Para facilitar os testes e a demonstração, o sistema já inicia com planos,
alunos e instrutores de exemplo (definidos em `modulos/banco_dados.py`). Eles
podem ser alterados ou excluídos pelo menu durante a execução.

### Planos

| ID | Plano | Duração | Valor de tabela | Desconto | Mensalidade final |
|---|---|---|---|---|---|
| 1 | Mensal | 1 mês | R$ 120,00 | — | R$ 120,00 |
| 2 | Trimestral | 3 meses | R$ 110,00 | — | R$ 110,00 |
| 3 | Semestral | 6 meses | R$ 100,00 | 10% | R$ 90,00 |
| 4 | Anual | 12 meses | R$ 95,00 | 15% | R$ 80,75 |

### Alunos

| ID | Nome |
|---|---|
| 1 | Lucas Ferreira |
| 2 | Mariana Costa |
| 3 | Rafael Souza |
| 4 | Camila Santos |
| 5 | Pedro Henrique Lima |
| 6 | Ana Beatriz Oliveira |

### Instrutores

| ID | Nome | Especialidade |
|---|---|---|
| 1 | Carlos Eduardo Mendes | Musculação |
| 2 | Juliana Rocha | Spinning |
| 3 | Thiago Barbosa | Funcional |

> Matrículas **não** possuem dados iniciais: são criadas durante o uso do sistema.

## 📏 Regras de negócio

- CPF validado pelos dígitos verificadores e **único** entre alunos (e entre instrutores).
- Aluno precisa ter no mínimo **14 anos**.
- Telefone com DDD (10 ou 11 dígitos); nomes apenas com letras.
- Nome de plano **único**; duração de 1 a 24 meses; valor maior que zero.
- Um aluno só pode ter **uma matrícula ativa** por vez.
- **Desconto de fidelidade:** 10% em planos de 6+ meses e 15% em planos de 12+ meses.
- O valor da mensalidade é "congelado" na matrícula: alterar o plano depois não afeta matrículas existentes.
- Matrícula tem validade (30 dias × duração) e fica **Vencida** automaticamente.
- Não é possível excluir aluno, plano ou instrutor com **matrícula ativa**.
- Apenas matrículas ativas podem ser canceladas.
- Matrícula exige aluno, plano e instrutor cadastrados.

## ▶️ Como executar

Requisito: **Python 3.10+** (nenhuma biblioteca externa).

```bash
git clone <url-do-repositorio>
cd academia_power_fit
python app.py
```

> Execute sempre o `app.py` a partir da pasta raiz do projeto.
> Os dados ficam apenas em memória (listas Python) e são perdidos ao encerrar o programa.
> Os dados iniciais são recarregados a cada execução.

## 🗂️ Organização do código

```
academia_power_fit/
├── app.py                  # Ponto de entrada e menu principal
├── modulos/
│   ├── banco_dados.py      # Listas em memória, dados iniciais e busca por ID
│   ├── interface.py        # Menus, tabelas e leitura de dados (input/print)
│   ├── validacoes.py       # Validadores/conversores de entrada
│   ├── formatacao.py       # Formatação de CPF, telefone, moeda e data
│   ├── regras.py           # Regras compartilhadas (status, desconto)
│   ├── alunos.py           # CRUD de alunos
│   ├── planos.py           # CRUD de planos
│   ├── instrutores.py      # CRUD de instrutores
│   ├── matriculas.py       # Matrículas (nova, listar, cancelar)
│   ├── cadastro_rapido.py  # Fluxo aluno novo + matrícula
│   └── relatorios.py       # Relatórios
└── docs/prompts_ia.md      # Prompts de IA utilizados
```

Princípios adotados: uma responsabilidade por módulo, funções pequenas,
nomes descritivos, type hints, docstrings, validação centralizada
(`ler_campo` + conversores em `validacoes.py`) e reaproveitamento de código
(o Cadastro Rápido reutiliza `alunos.cadastrar` e `matriculas.matricular_aluno`).

## 🤖 Uso de IA

Os prompts utilizados estão documentados em [`docs/prompts_ia.md`](docs/prompts_ia.md).

## 🌿 Fluxo de trabalho no GitHub

Branches por funcionalidade (`feature/alunos`, `feature/planos`,
`feature/cadastro-rapido`, ...), commits pequenos e descritivos e Pull Requests
revisados pelo outro integrante antes do merge na `main`.