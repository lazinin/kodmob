gitHub = "https://github.com/lazinin/kodmob"

history = []

while True:
    print("\n" + "="*40)
    print("КОНСОЛЬНЫЙ КАЛЬКУЛЯТОР".center(40))
    print("="*40)
    print("\nМЕНЮ:")
    print("1. Выполнить вычисление")
    print("2. Показать историю")
    print("3. Выйти")
    
    choice = input("\nВыберите действие (1-3): ").strip()
    
    if choice == '3':
        break
    elif choice == '2':
        print("\n" + "="*40)
        print("ИСТОРИЯ ВЫЧИСЛЕНИЙ".center(40))
        print("="*40)
        if history:
            for entry in history:
                print(entry)
        else:
            print("История пуста")
        continue
    elif choice == '1':
        try:
            num1 = float(input("Введите первое число: "))
            
            print("Доступные операции: +, -, *, /")
            operation = input("Выберите операцию: ").strip()
            
            if operation not in ['+', '-', '*', '/']:
                print("Ошибка: Некорректная операция. Используйте +, -, *, /")
                continue
            
            num2 = float(input("Введите второе число: "))
            
            if operation == '+':
                result = num1 + num2
                operation_str = "+"
            elif operation == '-':
                result = num1 - num2
                operation_str = "-"
            elif operation == '*':
                result = num1 * num2
                operation_str = "*"
            elif operation == '/':
                if num2 == 0:
                    print("Ошибка: Деление на ноль.")
                    continue
                result = num1 / num2
                operation_str = "/"
            
            print(f"\nРезультат: {result:.1f}")
            
            history_entry = f"{num1:.1f} {operation_str} {num2:.1f} = {result:.1f}"
            history.append(history_entry)
            
        except ValueError:
            print("Ошибка: Введите корректное число.")
            continue
    else:
        print("Ошибка: Выберите 1, 2 или 3")

print("\n" + "="*40)
print("ИСТОРИЯ ВЫЧИСЛЕНИЙ".center(40))
print("="*40)

if history:
    for entry in history:
        print(entry)
else:
    print("История пуста")