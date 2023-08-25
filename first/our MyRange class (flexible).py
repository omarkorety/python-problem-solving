####class to itterate form given numbers
class MyRange:
    def __init__(self,start,end,step):
        self.start=start
        self.end=end
        self.step=step
        self.indx=0

    def has_next(self):
        if self.step > 0:
            return self.start < self.end
        elif self.step<0:
            return self.start > self.end
        else:
            print("Error")
        

    #make sure we dont reach end point 
    #a fun to display numbers
    def get_next(self):
        tmp = self.start
        self.start += self.step
        self.indx +=1
        return self.indx,tmp

rng=MyRange(10,5,-1)

while rng.has_next():
    print(rng.get_next())     