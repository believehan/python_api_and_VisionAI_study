# 1. 클래스 정의는 자유롭게
# 2. 파라미터는 self제외 3개
# 3. 메서드 2개
# 4. 객체 생성 => 총 3개

class Argument:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def syllogism(self):
        print(f"{self.a}는 {self.b}이다. {self.b}는 {self.c}다. 고로 {self.a}는 {self.c}다.")
    
    def induction(self):
        return f"{self.a}는 1이다. {self.b}는 1이다. {self.c}도 1이다. 따라서 self는 1이다."
    
t = Argument("가", "나", "다")

t.syllogism()
print(t.induction())