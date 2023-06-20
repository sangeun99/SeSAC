#1 -> 리팩토링 필요..

word_list = ['게맛살', '구멍', '글라이더', '기차', '대롱', '더치페이', '롱다리', '리본', 
             '멍게', '박쥐', '본네트', '빨대', '살구', '양심', '이빨', '이자', '자율', '주기', '쥐구멍', '차박', '트라이앵글']

def searching_com (word) :
    last_letter = word[len(word)-1]
    for searching in word_list :
        if searching[0] == last_letter :
            used.append(searching)
            last_letter = searching[len(searching)-1]
            print(searching)
            return last_letter
    return None
          
print('<시작> 끝말잇기를 하자. 내가 먼저 말할게. 기차')
last_letter = ['차']
used = ['기차']
while 1 :
    word = input()
    if last_letter != word[0] :
        print("글자가 안 이어져. 내가 이겼다! <끝>")
        break
    elif word in used :
        print("아까 했던 말이야. 내가 이겼어! <끝>")
        break
    else :
        last_letter = searching_com(word)
        if not last_letter :
            print ("모르겠다. 내가 졌어.<끝>")
            break
    
used.append(word)

# 2
# 두음법칙 ‘ㅣ, ㅑ, ㅕ, ㅛ, ㅠ’ 앞의  ‘ㄹ’과 ‘ㄴ’이 ‘ㅇ’이 되고,
# ‘ㅏ, ㅓ, ㅗ, ㅜ, ㅡ, ㅐ, ㅔ, ㅚ’ 앞의 ‘ㄹ’이 ‘ㄴ’으로 변하는 것을 말한다. 

# dueum1
dueum1_vowel = ['ㅣ', 'ㅑ', 'ㅕ', 'ㅛ', 'ㅠ']
dueum1_consonent = ['ㄹ', 'ㄴ']

# dueum2
dueum2_vowel = ['ㅏ', 'ㅓ', 'ㅗ', 'ㅜ', 'ㅐ', 'ㅔ', 'ㅚ']
dueum2_consonent = ['ㄹ']

# last_letter 초성이 ㄹ, ㄴ이고 모음이 두음법칙 모음 리스트에 포함되면 last_letters에 append

import hgtk

def dueum(last_letter):    
    last_letter_decompose = hgtk.letter.decompose(last_letter)
    chosung = last_letter_decompose[0] # 초성
    jungsung = last_letter_decompose[1] # 중성
    jongsung = last_letter_decompose[2] # 종성
    if (chosung in dueum1_consonent) and (jungsung in dueum1_vowel) : # 두음법칙1
        alternative = hgtk.letter.compose('ㅇ', jungsung, jongsung)
    elif (chosung in dueum2_consonent) and (jungsung in dueum2_vowel) : # 두음법칙2
        alternative = hgtk.letter.compose('ㄴ', jungsung, jongsung)
    else :
        alternative = None
    return alternative
    

#1 -> 리팩토링 필요..

word_list = ['게맛살', '구멍', '글라이더', '기차', '대롱', '더치페이', '롱다리', '리본', 
             '멍게', '박쥐', '본네트', '빨대', '살구', '양심', '이빨', '이자', '자율', '주기', '쥐구멍', '차박', '트라이앵글']

def searching_com (word) :
    last_letter = word[len(word)-1]
    alternative = dueum(last_letter)
    for searching in word_list :
        if searching[0] == last_letter or searching[0] == alternative :
            used.append(searching)
            last_letter = searching[len(searching)-1]
            print(searching)
            return last_letter
    return None
          
print('<시작> 끝말잇기를 하자. 내가 먼저 말할게. 기차')
last_letter = '차'
used = ['기차']
while 1 :
    word = input()
    alternative = dueum(last_letter)
    if last_letter != word[0] and  word[0] != alternative:
        print("글자가 안 이어져. 내가 이겼다! <끝>")
        break
    elif word in used :
        print("아까 했던 말이야. 내가 이겼어! <끝>")
        break
    else :
        last_letter = searching_com(word)
        if not last_letter :
            print ("모르겠다. 내가 졌어.<끝>")
            break
    
used.append(word)