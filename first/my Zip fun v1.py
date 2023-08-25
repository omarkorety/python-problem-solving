class OurZip:
        #receive varying numbers of of iterables: assume only list,tuble,string
    def __init__(self,*iterables):
        self.iterables=iterables
        self.cur_col_idx = 0 

    def has_next(self):
        for lst in self.iterables:
            if self.cur_col_idx >= len(lst):
                return False
        return True

    def get_next(self):
        zipped=[0] * len(self.iterables)
        for idx , seq in enumerate(self.iterables):
            zipped[idx]=self.iterables[idx][self.cur_col_idx]
        self.cur_col_idx += 1

        return tuple(zipped)
        
if __name__ == '__main__':
    
    z =OurZip(list(range(10,15)),list(range(100)),'mostafa')
    while z.has_next():
        print(z.get_next())
