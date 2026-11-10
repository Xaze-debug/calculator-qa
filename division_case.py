def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Деление на ноль запрещено контрактом функции")
    return a / b
