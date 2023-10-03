from datetime import datetime

class Project:
    def __init__(self, name):
        self.name = name
        self.todos = []

    def __add__(self, description):
        self.todos.append(ToDo(description))

    def pending(self):
        return [todo for todo in self.todos if not todo.done]

    def search(self, description):
        return [todo for todo in self.todos if todo.description == description][0]

    def __str__(self):
        return f'{self.name} ({len(self.pending())} tarefa(s) pendente(s))'


class ToDo:
    def __init__(self, description):
        self.description = description
        self.done = False
        self.criatedDate = datetime.now()

    def do(self):
        self.done = True

    def __str__(self):
        return self.description + (' (concluida)' if self.done else ' (pendente)')


def main():
    home = Project('Tarefas de casa')
    home.add('aaaaaaaaaaaaaa')
    home.add('bbbbbbbbbbbbbb')
    home.add('cccccccccccccc')
    print(home)

    home.search('aaaaaaaaaaaaaa').do()
    for todo in home.todos:
        print(f'- {todo}')

if __name__ == '__main__':
    main()