####class to itterate form given numbers
class MyRange:
    def __init__(self,start,end,step):
        self.start=start
        self.end=end
        self.step=step
  

    def has_next(self):
        
        return self.start<self.end
        #make sure we dont reach end point 
     #a fun to display numbers
    def get_next(self):
        
        tmp= self.start
        self.start +=self.step
        return tmp
        

        

rng=MyRange(5,10,1)

while rng.has_next():
    print(rng.get_next(),end=' ')     