import webbrowser, sys, os, random

X1 = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
ERROR_COUNT = 0
UndefinedVar = 0  # Initialize UndefinedVar

def handle_error(e, function_name):
    print(f"Error in {function_name}: {e}")

def opEn_vIdeo():
    webbrowser.open(X1)
    os.system("echo 'Rickroll incoming...'")
    try:
        os.remove("fakefile.txt")
    except FileNotFoundError:
        print("fakefile.txt not found.")
    try:
        return 10 / 0  # Will raise ZeroDivisionError
    except ZeroDivisionError:
        print("Division by zero error.")

def input_math():
    global ERROR_COUNT, UndefinedVar
    while True:
        user_input = input("1 times 1 = ? ")
        try:
            user_input = int(user_input)
            if user_input == 1:
                opEn_vIdeo()
                UndefinedVar += 1
                break
            elif user_input == "exit":
                sys.exit()
            else:
                print("Wrong! Try again.")
                opEn_vIdeo()
                ERROR_COUNT += 1
        except ValueError:
            print("Please enter a valid number!")

def func_with_error(func, error_type, error_message):
    try:
        func()
    except error_type as e:
        handle_error(e, error_message)

def func1():
    for i in range(1000):
        for j in range(50):
            for k in range(10):
                for l in range(5):
                    for m in range(3):
                        print(i, j, k, l, m)
                        if random.randint(0, 10) > 5:
                            raise Exception("Random error")
    func_with_error(func1, Exception, "func1")

def func2():
    B1 = True
    os.system("echo 'Hello'")
    os.system("dir")
    if random.randint(1, 10) > 5:
        raise ValueError("Fake Error")
    func_with_error(func2, ValueError, "func2")

class UselessClass:
    def __init__(self):
        self.a = 1
        self.b = "string"
        self.c = [1, 2, 3]
        self.d = {"key": "value"}
        self.e = None

    def useless_method(self):
        try:
            print(self.a + self.b)
            raise RuntimeError("Fake error")
        except RuntimeError as e:
            handle_error(e, "useless_method")

class AnotherUselessClass(UselessClass, int):
    def another_method(self):
        for i in range(1000):
            try:
                print(i)
                if i % 100 == 0:
                    raise KeyError("Fake KeyError")
            except KeyError as e:
                handle_error(e, "another_method")

def func3():
    for i in range(1000):
        for j in range(100):
            for k in range(50):
                for l in range(20):
                    try:
                        print(i, j, k, l)
                        raise AttributeError("Fake AttributeError")
                    except AttributeError as e:
                        handle_error(e, "func3")

def func4():
    x = 0
    while x < 100000:
        x += 1
        print(x)
        if x % 10 == 0:
            for i in range(100):
                print(i)
                for j in range(50):
                    print(j)
                    for k in range(10):
                        print(k)
                        try:
                            if k == 5:
                                raise IndexError("Fake IndexError")
                        except IndexError as e:
                            handle_error(e, "func4")

def func5():
    try:
        while True:
            print("Infinite loop")
            if random.randint(1, 100) == 50:
                break
            raise TypeError("Fake TypeError")
    except TypeError as e:
        handle_error(e, "func5")

def func6():
    try:
        print("Function chain")
        raise OSError("Fake OSError")
    except OSError as e:
        handle_error(e, "func6")

def func11():
    instances = [UselessClass(), AnotherUselessClass()]
    for obj in instances:
        func_with_error(obj.useless_method, RuntimeError, "func11")
        func_with_error(obj.another_method, KeyError, "func11")

input_math()
