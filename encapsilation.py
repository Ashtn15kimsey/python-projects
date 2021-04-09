# Creating a protected class
class Protected:

    def __init__(self):
        self.__privateVar = 12
# calling contruction of protected class
    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(45)
obj.getPrivate()
