class Myclass:
    def __init__(self, mylist):
        self.mylist1 = mylist
        self.mylist2 = mylist[:]
        mylist[0] = -1

cls = Myclass([1,2,3])
print(cls.mylist1)
print(cls.mylist2)
