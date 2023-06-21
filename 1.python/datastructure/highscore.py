# --------------------------
# 전역 변수
# --------------------------

histories = []
highscore = 0
highmember = ''

# --------------------------
# 각종 함수
# --------------------------

def input_info():
    try : 
        score = int(input("점수를 입력하세요: "))
        name = input("이름을 입력하세요: ")
        global highscore, highmember
        if highscore < score :
            highscore = score
            highmember = name
    except ValueError:
        print("점수를 숫자 형태로 입력해주세요")
        score, name = input_info()
    return score, name

def store_info() :
    score, name = input_info()
    histories.append((score, name))

def print_highscore():
    print(f'최고 점수 : {highscore}, 사용자 : {highmember}')

def print_histories():
    print('--------')
    print('점수, 이름')
    print('--------')
    for score, name in histories :
        print(score, name)

def input_mode():
    mode = input("모드를 입력해주세요 (score / high / history / quit): ")
    mode_ops = ['score', 'high', 'history', 'quit']
    if mode not in mode_ops :
        print("다시 입력해주세요")
        mode = input_mode()
    return mode

# --------------------------
# 메인 함수
# --------------------------

if __name__ == "__main__":
    while True:
        mode = input_mode()
        if mode == 'score' :
            store_info()
        elif mode == 'high' :
            print_highscore()
        elif mode == 'history' :
            print_histories()
        else :
            quit