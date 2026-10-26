"""TaskTracker - gerenciador de tarefas em linha de comando."""
from datetime import date, datetime
PRIORIDADES = {"alta": "Alta", "media": "Média", "média": "Média", "baixa": "Baixa"}
ORDEM_PRIORIDADE = {"Alta": 0, "Média": 1, "Baixa": 2}
TAMANHO_MINIMO_TITULO = 3
FORMATO_DATA = "%d/%m/%Y"
tarefas = []
def exibir_menu():
    print("\n=== TaskTracker ===")
    print("1 - Cadastrar tarefa")
    print("2 - Visualizar tarefas")
    print("3 - Marcar tarefa como concluída")
    print("0 - Sair")
def ler_titulo():
    """Pede o título até receber um valor válido (obrigatório)."""
    while True:
        titulo = input("Título da tarefa: ").strip()
        if not titulo:
            print("Erro: o título não pode ser vazio.")
        elif len(titulo) < TAMANHO_MINIMO_TITULO:
            print(f"Erro: o título deve ter pelo menos {TAMANHO_MINIMO_TITULO} caracteres.")
        else:
            return titulo
def ler_prioridade():
    """Pede a prioridade até receber exatamente Alta, Média ou Baixa."""
    while True:
        entrada = input("Prioridade (Alta/Média/Baixa): ").strip().lower()
        if entrada in PRIORIDADES:
            return PRIORIDADES[entrada]
        print("Erro: prioridade inválida. Use apenas Alta, Média ou Baixa.")
def ler_data_limite():
    """Pede a data limite (DD/MM/AAAA), que não pode ser anterior a hoje."""
    while True:
        entrada = input("Data limite (DD/MM/AAAA): ").strip()
        try:
            data = datetime.strptime(entrada, FORMATO_DATA).date()
        except ValueError:
            print("Erro: data inválida. Use o formato DD/MM/AAAA.")
            continue
        if data < date.today():
            print("Erro: a data limite não pode ser anterior à data atual.")
            continue
        return data
def cadastrar_tarefa():
    titulo = ler_titulo()
    descricao = input("Descrição (opcional): ").strip()
    prioridade = ler_prioridade()
    data_limite = ler_data_limite()
    tarefas.append({
        "id": len(tarefas) + 1,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "concluida": False,
    })
    print("Tarefa cadastrada com sucesso!")
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    ordenadas = sorted(
        tarefas, key=lambda t: (ORDEM_PRIORIDADE[t["prioridade"]], t["data_limite"])
    )
    print("\n--- Tarefas cadastradas ---")
    for t in ordenadas:
        status = "concluída" if t["concluida"] else "pendente"
        print(
            f"[{t['id']}] {t['titulo']} | prioridade: {t['prioridade']} | "
            f"limite: {t['data_limite'].strftime(FORMATO_DATA)} | status: {status}"
        )
        if t["descricao"]:
            print(f"     {t['descricao']}")
    concluidas = sum(1 for t in tarefas if t["concluida"])
    print(f"\nConcluídas: {concluidas} | Pendentes: {len(tarefas) - concluidas}")
def concluir_tarefa():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    entrada = input("Número (ID) da tarefa a concluir: ").strip()
    if not entrada.isdigit():
        print("Erro: informe um número válido.")
        return
    for t in tarefas:
        if t["id"] == int(entrada):
            if t["concluida"]:
                print("Essa tarefa já está concluída.")
            else:
                t["concluida"] = True
                print("Tarefa marcada como concluída!")
            return
    print("Erro: tarefa não encontrada.")
def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "0":
            print("Encerrando o TaskTracker. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
if __name__ == "__main__":
    main()
