class ArithmeticProgression:
    def __init__(self,a0,q):
        if q == 0:
            raise ValueError("Коэффициент не может быть равен нулю.")
        self.a0 = a0
        self.q = q
        self.n = 0
    def __iter__(self):
        return self
    def __next__(self):
        temp = self.a0+self.q*self.n
        self.n+=1
        return temp
class GeometricProgression(ArithmeticProgression):
    def __init__(self, a0, q):
        super().__init__(a0, q)
        self.n = 0 
        

    def __next__(self):
        temp = self.a0 * (self.q ** self.n) 
        self.n += 1
        return temp
        
#пример использования
progression = GeometricProgression(1, 2)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')    # 1 2 4 8