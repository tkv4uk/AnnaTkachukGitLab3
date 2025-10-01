import math


def calc(a, b, op):
    if op not in '+-*/^%√':
        return 'Пожалуйста, выберите тип операции: "+, -, *, /, ^, %, √,!"!'

    if op == '+':
        return f'{a} + {b} = {a + b}'
    if op == '-':
        return f'{a} - {b} = {a - b}'
    if op == '*':
        return f'{a} * {b} = {a * b}'
    if op == '/':
        return f'{a} / {b} = {a / b}' if b != 0 else 'Ошибка: деление на ноль!'
    if op == '^':
        return f'{a} ^ {b} = {a ** b}'
    if op == '%':
        return f'{b}% от {a} = {a * b / 100}'
    if op == '√':
        return f'√{a} = {math.sqrt(a)}'
    if op == '!':
        if a < 0:
            return 'Ошибка: факториал отрицательного числа не существует!'
        if not a.is_integer():
            return 'Ошибка: факториал определен только для целых чисел!'
        return f'{int(a)}! = {math.factorial(int(a))}'


def main():
    a = float(input('Введите первое число: '))
    op = input('Какой вид операции Вы желаете осуществить?\nВыберите между "+, -, *, /, ^, %, √,!" : ')

    if op == '√':
        print(calc(a, 0, op))
    else:
        b = float(input('Пожалуйста, введите второе число: '))
        print(calc(a, b, op))


if __name__ == '__main__':
    main()