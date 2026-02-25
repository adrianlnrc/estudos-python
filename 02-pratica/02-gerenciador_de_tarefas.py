tarefas = []
tarefa = ''


while True: 
    print("--------------------")
    operacao = int(input("'\033[34m'escolha uma das operacoes: \n(1)Adicionar tarefa\n(2)Listar tarefas\n(3)Remover tarefa\n(4)Sair\n"))
    print("--------------------")
    if operacao == 1:
        nova_tarefa = str(input('Digite a tarefa: '))
        tarefas.append(nova_tarefa)
        continue
    elif operacao == 2:
        for tarefa in tarefas:
            print('\033[1;32m',tarefa)
        continue
    elif operacao == 3:
        tarefa = tarefas.remove(input('Qual tarefa voce deseja remover? '))
        print(f'Tarefas: {tarefas}')
        if tarefa not in tarefas:
            print('Nao esta na lista!') 
    else:
        break