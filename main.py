gitHub = "https://github.com/lazinin/kodmob"


def run_calculator():
    """Основная функция консольного калькулятора."""
    history = []

    while True:
        try:
            num1_input = input("Введите первое число: ")
            num1 = float(num1_input)

            operation = input("Выберите операцию (+, -, *, /): ").strip()
            if operation not in ('+', '-', '*', '/'):
                print("Ошибка: Неверная операция. Попробуйте еще раз.")
                continue

            num2_input = input("Введите второе число: ")
            num2 = float(num2_input)

            result = None
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Ошибка: Деление на ноль.")
                else:
                    result = num1 / num2

            if result is not None:
                print(f"Результат: {result}")
                history.append(f"{num1} {operation} {num2} = {result}")

        except ValueError:
            print("Ошибка: Пожалуйста, вводите только числа.")
            continue

        print()
        choice = input("Хотите продолжить? (да/нет): ").strip().lower()
        if choice == 'нет':
            break
        elif choice != 'да':
            print("Некорректный ввод. Программа будет завершена.")
            break

    print("\nИстория вычислений:")
    if not history:
        print("История пуста.")
    else:
        for entry in history:
            print(entry)


if __name__ == "__main__":
    run_calculator()