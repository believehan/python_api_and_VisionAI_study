# pyfiglet => 함수화

import pyfiglet

# sentence = pyfiglet.figlet_format(sentence)
# print(sentence)

# text를 받아서 pyfilget이 적용된 텍스가 출력되는 함수
def figlet_sentence(text : str):
    '''
    함수 설명 : 입력된 문자를 pyfiglet 형식으로 출력
    매개 변수 : text (str) : 입력 문자
    '''
    sentence = pyfiglet.figlet_format(text)
    print(sentence)
    
figlet_sentence("I can do it !")
figlet_sentence("You can do it !")
figlet_sentence("We can do it !")
