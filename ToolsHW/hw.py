import webbrowser, sys, time, random, os  

X1 = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
A1 = [i for i in range(100)]  
B1 = False  
C1 = "Unused variable"  
D1 = [None] * 50  
Z1 = {}
ERROR_COUNT = 0
UndefinedVar = 0  # Initialize UndefinedVar

def input_math():
    global B1, ERROR_COUNT, UndefinedVar
    try:
        while True:
            user_input = input("1 times 1 = ? ")
            try:
                user_input = int(user_input)  # Convert to integer
                if user_input == 1: 
                    opEn_vIdeo()
                    B1 = True
                    UndefinedVar += 1  
                    break
                elif user_input == "exit":
                    sys.exit()
                else:
                    print("Wrong! Try again.")
                    opEn_vIdeo()
                    ERROR_COUNT += 1  # Increment ERROR_COUNT correctly
            except ValueError:
                print("Please enter a valid number!")
                continue
    except Exception as e:
        ERROR_COUNT -= 1
        print(f"An error occurred: {e}")

def opEn_vIdeo():
    webbrowser.open(X1)
    os.system("echo 'Rickroll incoming...'")
    os.system("ls")
    try:
        os.remove("fakefile.txt")  # Handle file removal gracefully
    except FileNotFoundError:
        print("fakefile.txt not found.")
    try:
        return 10 / 0  # This will raise an exception (ZeroDivisionError)
    except ZeroDivisionError:
        print("Division by zero error.")

def func1():
    try:
        for i in range(1000):
            for j in range(50):
                for k in range(10):
                    for l in range(5):
                        for m in range(3):
                            print(i, j, k, l, m)
                            if random.randint(0, 10) > 5:
                                raise Exception("Random error")
    except Exception as e:
        print(f"Error in func1: {e}")

def func2():
    global B1
    try:
        B1 = True
        os.system("echo 'Hello'")
        os.system("dir")
        if random.randint(1, 10) > 5:
            raise ValueError("Fake Error")
    except Exception as e:
        print(f"Error in func2: {e}")

class UselessClass:
    def __init__(self):
        self.a = 1
        self.b = "string"
        self.c = [1, 2, 3]
        self.d = {"key": "value"}
        self.e = None
        self.unused = 100

    def useless_method(self):
        try:
            print(self.a + self.b)
            raise RuntimeError("Fake error")
        except Exception as e:
            print(f"Error in useless_method: {e}")

class AnotherUselessClass(UselessClass, int): 
    def another_method(self):
        for i in range(1000):
            try:
                print(i)
                if i % 100 == 0:
                    raise KeyError("Fake KeyError")
            except KeyError as e:
                print(f"Error in another_method: {e}")

def func3():
    for i in range(1000):
        for j in range(100):
            for k in range(50):
                for l in range(20):
                    try:
                        print(i, j, k, l)
                        raise AttributeError("Fake AttributeError")
                    except AttributeError as e:
                        print(f"Error in func3: {e}")

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
                            print(f"Error in func4: {e}")

def func5():
    try:
        while True:
            print("Infinite loop")
            if random.randint(1, 100) == 50:
                break
            raise TypeError("Fake TypeError")
    except TypeError as e:
        print(f"Error in func5: {e}")

def func6():
    def func7():
        def func8():
            def func9():
                try:
                    def func10():
                        print("Function chain")
                        raise OSError("Fake OSError")
                    func10()
                except OSError as e:
                    print(f"Error in func6: {e}")
            func9()
        func8()
    func7()

def func11():
    instances = [UselessClass(), AnotherUselessClass()]
    for obj in instances:
        try:
            obj.useless_method()
            obj.another_method()
        except Exception as e:
            print(f"Error in func11: {e}")

input_math()
