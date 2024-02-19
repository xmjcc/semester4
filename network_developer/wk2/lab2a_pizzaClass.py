class Pizza:
 

    _id=100000

    def __init__(self, name):
        # initiate an object of this class
        self.name = name
        self.id = Pizza._id
        Pizza._id +=1

pizza1 = Pizza("intalian")
print(pizza1.name)