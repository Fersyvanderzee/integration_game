import pygame


def cards_function(name):
    def function1():
        print("Carried out function of Test1")

    def function2():
        print("Carried out function of Test2")

    def function3():
        print("Carried out function of Test3")

    def function4():
        print("Carried out function of Test4")

    if name == "Test1":
        function1()
    elif name == "Test2":
        function2()
    elif name == "Test3":
        function3()
    elif name == "Test4":
        function4()