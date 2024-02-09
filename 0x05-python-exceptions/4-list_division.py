#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                num1 = float(my_list_1[i])
            except (ValueError, TypeError):
                num1 = None
            try:
                num2 = float(my_list_2[i])
            except (TypeError, ValueError):
                num2 = None
            if num1 is None or num2 is None:
                print("wrong type")
            elif num2 == 0:
                print("division by 0")
                result.append(0)
            else:
                result.append(num1 / num2)
    except IndexError:
        print("out of range")
        result.append(0)
    except ZeroDivisionError:
        print("division by 0")
        result.append(0)
    finally:
        return result
