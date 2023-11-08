import math
import sys 


def summa (first, second):

    return first + second


def sub (first, second):

    return first - second


def mult (first, second):

    return first * second


def div (first, second):

    return first / second




def calc(first, second, oper):

    result = None

    if oper == 1:

        result = summa(first, second)

    elif oper == 2:

        result = sub(first, second)

    elif oper == 3:

        result = mult(first, second)

    elif oper == 4:

        if (second == 0):

            print('Деление на ноль запрещено!')

            return

        result = div(first, second)

    elif oper == 5:

        result = first ** second

    elif oper == 6:
        if (first <= 0):

            print('Введите значение больше нуля!')

            return

        result = math.sqrt(first)

    elif oper == 7:

        if (first <= 0):

            print('Введите значение больше нуля!')

            return

        result = math.factorial(first)

    elif oper == 8:

        result = math.cos(first)

    elif oper == 9:

        result = math.sin(first)

    elif oper == 10:

        result = math.tan(first)
    
    elif oper == 11:

        sys.exit()

    else:

        print('Нет такого действия')

    return result

def run():
    print(      "1. Сложить 2 числа\n" +
                "2. Вычесть второе из первого\n" +
                "3. Перемножить два числа\n" +
                "4. Разделить первое на второе\n" +
                "5. Возвести в степень N первое число\n" +
                "6. Найти квадратный корень из числа\n" +
                "7. Найти факториал из числа\n" +
                "8. Найти косинус\n" +
                "9. Найти Синус\n" +
                "10. Найти тангенс\n" +
                "11. Выйти из программы")
    
    try:
        op = int(input('Выбор действия: '))

    except ValueError:
        op = int(input('Некорректные данные.'))

    if op == 11:
        result = calc(0, 0, 11)
    else:
        try:
            first = int(input('Введите первое число: '))

        except ValueError:
            first = int(input('Некорректные данные.'))

        try:
            second = int(input('Введите второе число: '))

        except ValueError:
            second = int(input('Некорректные данные.'))

    result = calc(first, second, op)
    

    print(result)
    run()

run()
