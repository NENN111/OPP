from dataclasses import dataclass,field

@dataclass(frozen=True)
class Point:
    
    x: float = 0.0
    y: float = 0.0
    quadrant: int = field(init=False)
    def __post_init__(self):
        if self.x==0 or self.y==0:
            object.__setattr__(self, 'quadrant', 0)
        if self.x>0 and self.y>0:
            object.__setattr__(self, 'quadrant', 1)
        if self.x<0 and self.y>0:
            object.__setattr__(self, 'quadrant', 2)
        if self.x<0 and self.y<0:
            object.__setattr__(self, 'quadrant', 3)
        if self.x>0 and self.y<0:
            object.__setattr__(self, 'quadrant', 4)
            
    def __eq__(self,other):
        return self.x == other.x and self.y==other.y
    def __ne__(self,other):
        return not self.__eq__(other)
    def symmetric_x(self):
        return Point(self.x,-self.y)
    def symmetric_y(self):
        return Point(-self.x,self.y)