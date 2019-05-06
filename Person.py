class Person:
    """
    Person class to test on __new__, and __init___
    """

    def __new__(cls, name, age):
        print("__new__ called")
        print(cls)
        print(type(cls))
        print(type(super().__new__(cls)))
        return super().__new__(cls)
    
    def __init__(self, name, age):
        print("__init__ called")
        self.name = name
        self.age = age
        print(type(self))
    
    def __str__(self):
        return "<Person: {}, {}>".format(self.name, self.age)

# def main():
#     person = Person("Chen", 29)
#     print(person)
if __name__ == '__main__':
    # print("type of __new__ return: {}".format(type(Person.__new__(type,'Bob', 11))))
    # print("type of __init__ return: {}".format(type(Person.__init__("Alice", 12))))
    person = Person("Chen", 29)
    print(person)
    
