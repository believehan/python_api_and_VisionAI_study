# pyfiglet + termcolor를 적용한 함수!
import pyfiglet
from termcolor import colored

def decorate_txt(text:str, color:str):
    '''
    함수 설명 : 
        1. 폰트 적용
        2. 색상 적용
        3. 출력
    매개 변수 :
        1. text : str
        2. color : str
    '''
    sentence = pyfiglet.figlet_format(text)
    decorate_sentence = colored(sentence, color)
    # print(decorate_sentence)
    return decorate_sentence

# 출력1
print(decorate_txt("Fiy to the sky", "blue"))

# 출력2
print_txt = decorate_txt("Fiy to the sky", "blue")
print(print_txt)

