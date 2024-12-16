# Classe Tarefa
class Tarefa:
    def __init__(self, id, nome, prazo, urgencia):
        self._id = id
        self._nome = nome
        self._prazo = prazo
        self._urgencia = urgencia

    # Getters
    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @property
    def prazo(self):
        return self._prazo

    @property
    def urgencia(self):
        return self._urgencia

    # Setters
    @id.setter
    def id(self, id):
        self._id = id

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @prazo.setter
    def prazo(self, prazo):
        self._prazo = prazo

    @urgencia.setter
    def urgencia(self, urgencia):
        self._urgencia = urgencia

    # Método para retornar as informações em formato de dicionário
    def para_dict(self):
        return {
            'id': self._id,
            'nome': self._nome,
            'prazo': self._prazo,
            'urgencia': self._urgencia
        }

    # Método para receber dados e criar uma nova tarefa
    @staticmethod
    def receber_dados(id):
        id = id
        nome = input("Nome da Tarefa: ")
        prazo = input("Prazo da Tarefa: ")
        urgencia = input("Nível de Urgência (Baixa, Média, Alta): ")
        return Tarefa(id, nome, prazo, urgencia)

    # Método para deletar uma tarefa da lista
    @staticmethod
    def deletar_tarefa(id, lista):
        for tarefa in lista:
            if tarefa['id'] == id:
                lista.remove(tarefa)
                return True
        return False

    # Método para mostrar todas as tarefas
    @staticmethod
    def mostrar_tarefas(lista):
        if not lista:
            print("Nenhuma tarefa cadastrada.")
        else:
            for tarefa in lista:
                print(f"ID: {tarefa['id']}, Nome: {tarefa['nome']}, Prazo: {tarefa['prazo']}, Urgência: {tarefa['urgencia']}")

    # Método para editar uma tarefa existente
    @staticmethod
    def editar_tarefa(id, lista):
        for tarefa in lista:
            if tarefa['id'] == id:
                print("Edite as informações da tarefa:")
                tarefa['nome'] = input("Nome da Tarefa: ")
                tarefa['prazo'] = input("Prazo da Tarefa (AAAA-MM-DD): ")
                tarefa['urgencia'] = input("Nível de Urgência (Baixa, Média, Alta): ")
                return True
        return False


