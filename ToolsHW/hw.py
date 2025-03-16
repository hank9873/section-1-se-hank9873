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



input_math()
