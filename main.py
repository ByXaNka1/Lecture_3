#Завдання 1
def calculator():
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    operator = input("Введіть операцію (+, -, /, *, mod, pow, div): ")
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '/':
        if num2 == 0:
            print("Ділення на 0!")
            return
        else:
            result = num1 / num2
    elif operator == '*':
        result = num1 * num2
    elif operator == 'mod':
        result = num1 % num2
    elif operator == 'pow':
        result = num1 ** num2
    elif operator == 'div':
        result = num1 // num2
    else:
        print("Невірна операція!")
        return
    print("Результат:", result)
calculator()
#Завдання 2
def format_programmer(num):
    if num % 10 == 1 and num % 100 != 11:
        return f"{num} програміст"
    elif num % 10 in [2, 3, 4] and num % 100 not in [12, 13, 14]:
        return f"{num} програміста"
    else:
        return f"{num} програмістів"
n = int(input("Введіть кількість програмістів: "))
result = format_programmer(n)
print(result)
#Завдання 3
def is_lucky_ticket(ticket_number):
    digits = [int(digit) for digit in str(ticket_number)]
    if sum(digits[:3]) == sum(digits[3:]):
        return "Щасливий"
    else:
        return "Звичайний"
ticket = input("Введіть номер квитка: ")
result = is_lucky_ticket(ticket)
print(result)
#Завдання 4
def can_queen_capture(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return "YES"
    else:
        return "NO"
x1, y1, x2, y2 = map(int, input("Введіть координати: ").split())
result = can_queen_capture(x1, y1, x2, y2)
print(result)
#Завдання 5
def min_distance(N, M, x, y):
    return min(x, y, N - x, M - y)
N, M, x, y = map(int, input("Введіть розміри басейну та координати: ").split())
result = min_distance(N, M, x, y)
print(result)
