class Student():

    def __init__(self, name=None, age=None):
        self.__name = name
        self.__age = age

    def __str__(self):
        return '信息：'+str(self.__name)+','+ str(self.__age)

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_name(self, new_name):
        self.__name = new_name
    def set_age(self, new_age):
        self.__age = new_age



