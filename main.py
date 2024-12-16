from tarefa import Tarefa

# Lista de tarefas para armazenar os dicionários
lista_tarefas = []

# Função principal
def main():
    while True:
        print("\nSeja bem-vindo(a) ao seu Gerenciador de Tarefas")
        print("O que você deseja realizar?")
        print("1 | Criar Tarefa")
        print("2 | Editar Tarefa")
        print("3 | Ver Tarefas")
        print("4 | Excluir Tarefa")
        print("0 | Sair")
        op = int(input("Opção: "))
        
        id = 0
        match op:
            case 1:
                tarefa = Tarefa.receber_dados(id)
                lista_tarefas.append(tarefa.para_dict())
                id +=1
                print("Tarefa criada com sucesso!")
            
            case 2:
                id_tarefa = int(input("Digite o ID da tarefa que deseja editar: "))
                if Tarefa.editar_tarefa(id_tarefa, lista_tarefas):
                    print("Tarefa editada com sucesso!")
                else:
                    print("Tarefa não encontrada.")
            
            case 3:
                Tarefa.mostrar_tarefas(lista_tarefas)
            
            case 4:
                id_tarefa = int(input("Digite o ID da tarefa que deseja excluir: "))
                if Tarefa.deletar_tarefa(id_tarefa, lista_tarefas):
                    print("Tarefa excluída com sucesso!")
                else:
                    print("Tarefa não encontrada.")
            
            case 0:
                print("Saindo...")
                break
            
            case _:
                print("Opção inválida, tente novamente.")

# Execução do programa
if __name__ == "__main__":
    main()