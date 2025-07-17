class Map:
    def __init__(self,iterate) :
        self.list = []
        self.__geek(iterate)
    def geek(self,iterate):
        for item in iterate:
            self.list.append(item)  
    def __geek(self,iterate):
        self.geek(iterate)
    def __str__(self):
        return str(self.list)   
        