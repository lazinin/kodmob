history = []

while True:
    print("\n" + "="*40)
    print("КОНСОЛЬНЫЙ КАЛЬКУЛЯТОР".center(40))
    print("="*40)
    
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
        
        if result == int(result):
            result_display = int(result)
            result_store = int(result)
        else:
            result_display = result
            result_store = result
        
        num1_display = int(num1) if num1 == int(num1) else num1
        num2_display = int(num2) if num2 == int(num2) else num2
        
        print(f"\nРезультат: {result_display}")
        
        history_entry = f"{num1_display} {operation_str} {num2_display} = {result_store}"
        history.append(history_entry)
        
    except ValueError:
        print("Ошибка: Введите корректное число.")
        continue
    
