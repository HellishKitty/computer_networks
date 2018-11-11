"""
Модуль для формирования запросов
для отправки на сервер
"""


import pickle


class Worker:
    def __init__(self, surname, position, salary, birth):
        self.surname = surname
        self.position = position
        self.salary = salary
        self.birth = birth


    def printw(self):
        print('   surname: ', self.surname)
        print('  position: ', self.position)
        print('    salary: ', self.salary)
        print('birth date: ', self.birth)


def print_data(data):
    print('-------------------')
    for i in range(len(data)):
        data[i].printw()
        print('-------------------')


# Формирования запроса на просмотра данных
def print_request():
    request = ('print',)
    request = pickle.dumps(request)
    return request


# Формирвоания запроса на добавление элемента
def add_request():
    surname = input('enter surname: ')
    position = input('enter position: ')
    salary = input('enter salary: ')
    birth = input('enter birth date: ')
    tmp = Worker(surname, position, salary, birth)
    request = ('add', tmp)
    request = pickle.dumps(request)
    return request


# Формирование запроса для редактирвоание записи
def edit_request():
    n = input('enter element to edit: ')
    print('1. - rewrite note\n2. - edit note field')
    switch = input('input> ')
    # Выбираем, редактировать поле
    # Или же полностью перезаписать элемент
    if switch == '1':
        # Формируем запроса на перезаписывание элемента
        surname = input('enter new surname: ')
        position = input('enter new position: ')
        salary = input('enter new salary: ')
        birth = input('enter new birth date: ')
        tmp = Worker(surname, position, salary, birth)
        request = ('edit', int(n), 'rewrite', tmp)
        return request
    elif switch == '2':
        # Формируем запрос на редактирования поля записи
        print('enter number of field to edit (1, 2, 3,4)')
        print('or enter "/field_name", for example "/surname"')
        f = input('input> ')
        # Выбираем поле для редактирования
        if f == '2' or f == '/surname':
            field = input('enter new surname: ')
            request = ('edit', int(n), 'edit', 'surname', field)
            request = pickle.dumps(request)
            return request
        elif f == '2' or f == '/position':
            field = input('enter new position: ')
            request = ('edit', int(n), 'edit', 'position', field)
            request = pickle.dumps(request)
            return request
        elif f == '3' or f == '/salary':
            field = input('enter new salary: ')
            request = ('edit', int(n), 'edit', 'salary', field)
            request = pickle.dumps(request)
            return request
        elif f == '4' or f == '/birth':
            field = input('enter new birth date: ')
            request = ('edit', int(n), 'edit', 'birth', field)
            request = pickle.dumps(request)
            return request
        else:
            print('input error!')
            return False
    else:
        print('input error!')
        return False


# Формирование запроса на удаление элемента
def delete_request():
    n = input('enter number of lement to delete: ')
    request = ('delete', int(n))
    request = pickle.dumps(request)
    return request


# Формирование запроса на сортировку
def sort_request():
    print('enter number of field to sort by (1, 2, 3 ,3)')
    print('or enter "/field_name", for example "/surname"')
    f = input('input> ')
    if f == '1' or f == '/surname':
        request = ('sort', 'surname')
        request = pickle.dumps(request)
        return request
    elif f == '2' or '/position':
        request = ('sort', 'position')
        request = pickle.dumps(request)
        return request
    elif f == '3' or '/salary':
        request = ('sort', 'position')
        request = pickle.dumps(request)
        return request
    elif f == '4' or f == 'birth':
        request = ('sort', 'birth')
        request = pickle.dumps(request)
        return request
    else:
        print('input error!')
        return False