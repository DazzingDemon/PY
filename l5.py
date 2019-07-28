print("Функция определения типа: ")

def type_func(arg):
    #print("Введите аргумент")
    print("Класс аргумента относится к " + str(type(arg)))

    lst = []
    if type(arg) is tuple:
        print("это неизменяемый список и длина его " + str(len(arg)))

        if len(arg) > 1:

            for i in arg:

                 print("список состоит из следующих классов " + str(list(set(lst))))

        return(type(arg),lst)

    elif type(arg) is list:

        print("это кортеж и длина его " + str(len(arg)))

        if len(arg) > 1:

            for i in arg:

                lst.append(type(i))

            print("список состоит из следующих классов " + str(list(set(lst))))

        return(type(arg),lst)


type_func([16, -17, 2, 78.7, False, False, {True: True}, 555, 12, 23, 42, "DD"])


print("Функция сортировки: ")
lst1 = []

def sort (arg):

    lst2 = [i for i in arg if isinstance(i, (int,float))]

    print("Исходный список: " + str(lst2))

    lst2.sort()

    print("Отсортированный список: " + str(lst2))

sort([16, -17, 2, 78.7, False, False, {'True': True}, 555, 12, 23, 42, 'DD'])