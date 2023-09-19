class Computer:

    def __connect(self):
        print("Connecting to Smtp server .....")
    
    def __content(self):
        print("Dear Murodjon,    Something ....... , Sincerely yours Diyorbek")
    
    def __send(self):
        print("Sending ....")

    def sendEmail(self):
        self.__connect()
        self.__content()
        self.__send()

computer = Computer()
computer.sendEmail()
























