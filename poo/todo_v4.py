from datetime import datetime, timedelta

class Project:
    def __init__(self, name):
        self.name = name
        self.todos = []

    def __iter__(self):
        return self.todos.__iter__()

    def add(self, description, expiration=None):
        self.todos.append(ToDo(description, expiration))

    def pending(self):
        return [todo for todo in self.todos if not todo.done]

    def search(self, description):
        return [todo for todo in self.todos if todo.description == description][0]

    def __str__(self):
        return f'{self.name} ({len(self.pending())} tarefa(s) pendente(s))'


class ToDo:
    def __init__(self, description, expiration=None):
        self.description = description
        self.done = False
        self.criatedDate = datetime.now()
        self.expiration = expiration

    def do(self):
        self.done = True

    def __str__(self):
        status = []
        if self.done:
            status.append('(Concluida')
        elif self.expiration:
            if datetime.now() > self.expiration:
                status.append('(vencida)')
            else:
                days = (self.expiration - datetime.now())
                status.append(f"(Vence em {days} dias)")

        return f'{self.description} ' + ' '.join(status)


def main():
    home = Project('Tarefas de casa')
    home.add('aaaaaaaaaaaaaa', datetime.now())
    home.add('bbbbbbbbbbbbbb', datetime.now() + timedelta(days=3, minutes=12))
    home.add('cccccccccccccc')
    print(home)

    home.search('aaaaaaaaaaaaaa').do()
    for todo in home:
        print(f'- {todo}')

if __name__ == '__main__':
    main()