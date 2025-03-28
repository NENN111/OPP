from math import sqrt
class Vector:
    def __init__(self,*args):
        self.args = args
    def __str__(self):
        return f"{self.args}"
    def __len__(self):
        return(len(self.args))
    def __add__(self,other):
        if  len(self)==len(other):
            if isinstance(self,Vector) and isinstance(other,Vector):
                return Vector(*[self.args[i]+other.args[i] for i in range(len(self))])
        else:
            raise ValueError("Векторы должны иметь равную длину")
    def __sub__(self,other):
        if  len(self)==len(other):
            if isinstance(self,Vector) and isinstance(other,Vector):
                return Vector(*[self.args[i]-other.args[i] for i in range(len(self))])
        else:
            raise ValueError("Векторы должны иметь равную длину")
    def __mul__(self,other):
        if  len(self)==len(other):
            if isinstance(self,Vector) and isinstance(other,Vector):
                return sum([self.args[i]*other.args[i] for i in range(len(self))])
        else:
            raise ValueError("Векторы должны иметь равную длину")
    def __eq__(self,other):
        if  len(self)==len(other):
            if isinstance(self,Vector) and isinstance(other,Vector):
                return all([self.args[i]==other.args[i] for i in range(len(self))])
        else:
            raise ValueError("Векторы должны иметь равную длину")
    def __ne__(self,other):
        if  len(self)==len(other):
            if isinstance(self,Vector) and isinstance(other,Vector):
                return any([self.args[i]!=other.args[i] for i in range(len(self))])
        else:
            raise ValueError("Векторы должны иметь равную длину")
    def norm(self):
        return sqrt(sum([self.args[i]**2 for i in range(len(self))]))
        

a = Vector(2,2,2)
b = Vector(1,1,3)
print(b+a)
print(b-a)
print(a*b)
print(a.norm())