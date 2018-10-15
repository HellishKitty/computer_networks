import pickle


# Класс с поездо4ками
class Trip:
    def __init__(self, trip_id, bus_type, price, dest):
        self.trip_id = trip_id
        self.bus_type = bus_type
        self.price = price
        self.dest = dest


def view(data):
    for i in range(len(data)):
        print("\ntrip number: ", data[i].trip_id)
        print("   bus type: ", data[i].bus_type)
        print("      price: ", data[i].price)
        print("destination: ", data[i].dest)


"""************************************
Формирование запросов клиента
************************************"""


# Формирование запроса на просмотр элементов
def form_req_print():
    request = ('print',)
    request = pickle.dumps(request)
    return request


# Формирования запроса на добавление элемента
def form_req_add():
    trip_number = input("trip number: ")
    bus_type = input("bus type: ")
    price = input("price: ")
    dest = input("dest: ")
    note = Trip(trip_number, bus_type, price, dest)
    request = ("add", note)
    request = pickle.dumps(request)
    return request


# Формирование запроса на изменение записи
def form_req_edit():
    n = input("choose note to edit: ")
    trip_number = input("trip number: ")
    bus_type = input("bus type: ")
    price = input("price: ")
    dest = input("destination: ")
    note = Trip(trip_number, bus_type, price, dest)
    request = ("edit", note, int(n))
    request = pickle.dumps(request)
    return request


# Формирование запроса на удаление эелемента
def form_req_del():
    to_del = input("number of element to del: ")
    request = ('del', int(to_del))
    request = pickle.dumps(request)
    return request


def form_req_sort():
    print("\nsort by: ")
    print("1. bus type\n2. price\n3. destination")
    sort = input("input> ")
    request = ('sort', sort)
    request = pickle.dumps(request)
    return request
