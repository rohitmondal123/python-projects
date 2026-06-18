# ------------------------------------------------------------------------
# Simple calculator with function, calculation history, clear, and exit  |
# ------------------------------------------------------------------------



def show_history():
    f = open("../history.txt", "r")
    lines = f.readlines()
    if len(lines) == 0:
        print("No History Found ....")
    else:
        for i in reversed(lines):
            print(i.strip())
    f.close()


def clear_history():
    f = open("../history.txt", "w")
    f.close()
    print("History cleared")


def save_history(equation, result):
    f = open("../history.txt", "a")
    f.write(equation + " = " + str(result) + "\n")
    f.close()


def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input. Use format like: 8 + 8")
        return
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print(num1, "is not divisible by", num2)
            return
        else:
            result = num1 / num2
    else:
        print("Invalid operation. USE ONLY + - * /")
        return
    if result == int(result):
        result = int(result)
    print("Result is", result)
    save_history(user_input, result)


def main():
    print("------ SIMPLE CALCULATOR USING PYTHON -------")
    while True:
        user_input = input("Enter calculation (+ - * /) or command (history, clear, exit): ").strip().lower()
        if user_input.lower() == "exit":
            print("GOOD BYE ...!  THANKS FOR VISITING ROHIT'S CALCULATOR")
            input("Press Enter to exit...")  # <-- Add this line
            break
        elif user_input.lower() == "history":
            show_history()
        elif user_input.lower() == "clear":
            clear_history()
        else:
            calculate(user_input)
main()

  