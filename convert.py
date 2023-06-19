

# 사용자로부터 문장을 입력받아 대문자로 변환하시오
def convert_case(text) :
    result = ""
    for c in text :
        if c.isupper() :
            result += c.lower()
        else :
            result += c.upper()

    return result

text = input()
print(convert_case(text))

