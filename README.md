# TaskTracker

Gerenciador de tarefas em linha de comando (CLI), desenvolvido em Python como
parte do trabalho de Planejamento Lógico e Versionamento de Código.

## Documentação

O planejamento lógico do sistema (Fase 1) está em
[`docs/planejamento_logico.pdf`](docs/planejamento_logico.pdf).

## Funcionalidades

- Cadastro de tarefas com título, descrição (opcional), prioridade e data limite
- Visualização das tarefas ordenadas por prioridade e data limite, com status
  (pendente ou concluída) e totais de concluídas e pendentes
- Marcação de tarefas como concluídas, mantendo o histórico

## Regras do sistema

- Não é possível cadastrar uma tarefa sem título
- A prioridade aceita apenas `Alta`, `Média` ou `Baixa`
- Só é possível concluir uma tarefa que exista na lista
- A data limite (`DD/MM/AAAA`) não pode ser anterior à data atual

## Como executar

Requer Python 3.8 ou superior.

```bash
python src/main.py
```

## Estrutura do projeto

```
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```
docker build
docker run -it
docker compose run

## Autor

Lucas Roriz Blumm — Ciência da Computação (Noturno)
