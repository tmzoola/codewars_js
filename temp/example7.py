class Animal:

    def legs(self,quantity):
        if quantity == 2:
            print("Kengoru","Monkey")
        elif quantity == 4:
            print("Lion","Elephant")
        else:
            print("Snake")


animal = Animal()

animal.legs(0)