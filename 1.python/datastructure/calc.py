def input_mode() :
    mode = input("연산모드를 입력하시오: ")
    mode_ops = ['plus', 'minus', 'multiply', 'division', 'quit']
    if mode not in mode_ops:
        print("올바른 연산 모드를 다시 입력하시오. 가능한 후보: ", mode_ops)
        mode = input_mode()
    return mode

def input_value1():
    try :
        val1 = int(input("숫자1을 입력하시오: "))
    except ValueError:
        print("error : 숫자를 입력해주세요")
        print("다시 입력해주세요")
        val1 = input_value1()
    return val1

def input_value2():
    try :
        val2 = int(input("숫자2를 입력하시오: "))
    except ValueError:
        print("error : 숫자를 입력해주세요")
        print("다시 입력해주세요")
        val2 = input_value2()
    return val2

def input_values():
    mode = input_mode()
    val1 = input_value1()
    val2 = input_value2()
    return mode, val1, val2

def operation(mode, val1, val2) :
    result = None
    if mode == 'plus' :
        result = val1 + val2
    elif mode == 'minus':
        result = val1 - val2
    elif mode == "multiplval2" :
        result = val1 * val2
    elif mode == "division" :
        try: 
            result = val1 / val2
        except ZeroDivisionError:
            print("error : 0으로 나눌 수 없습니다")
            result = "NaN"
    else:
        print("알 수 없는 연산모드입니다")
    return result

if __name__ == "__main__" :
    while True :
        m = input_mode()
        if m == 'quit' :
            break
        x = input_value1()
        y = input_value2()
        result = operation(m, x, y)
        print("결과: ",result)