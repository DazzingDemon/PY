class Human:
    pass

#print(Human)
#print(Human())



class Human:
    height = 192

    def __init__(self, name = None, age = None):
        self.age = age
        self.name = name

    def show_info(self):
        return  str(self.name) + ' '+  str(self.age)   
#1
    def say_hello(self):
        return  'hello, my name is ' + str(self.name)

i = Human(name = 'Ivan', age = 24)
n = Human(name = 'Nick', age = 32)
print(i.show_info())
print(i.say_hello())

print(n.show_info())
print(n.say_hello())

#2
class Builder(Human):

    def __init__(self, name = None, age = None, post = None):
        self.age = age
        self.name = name
        self.post = post


    def say_hello(self):
        return  'hello, my name is ' + str(self.name)+ ', ' + str(self.post)

l = Builder(name = 'Ivan', age = 24, post = 'builder')
print(l.say_hello())

class Writer(Human):

    def my_books (*args):
        print('I write ' + str(len(args)))
    
    my_books('Михаил Булгаков — Мастер и Маргарита','Федор Достоевский — Преступление и наказание','Лев Толстой — Война и мир','Михаил Булгаков — Собачье сердце')

    

