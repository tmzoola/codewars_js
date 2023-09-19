
class Post():
    def __init__(self,senderName,receiverName):
        self.senderName = senderName
        self.receiverName=receiverName

    def sendEmail(self):
        self.__connect()
        self.__content()
        self.__send()

    def __connect(self):
        print("Connecting ...")
    
    def __content(self):
        print(f"Dear {self.receiverName},   Something ...   ,   Sincerele yours {self.senderName}")
    
    def __send(self):
        print("Sending ...")
        


post = Post("Murodjon","Sanjar")
post.sendEmail()

