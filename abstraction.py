from abc import ABC, abstractmethod
class debt(ABC):
    def debt(self, amount):
        print("Your card is declined: ",amount)
# this function is telling customer their card is declined but won't know why
    @abstractmethod
    def payment(self, amount):
        pass

class CreditCardPayment(debt):
# here we've defined how to implement the payment function from its parent paySlip clas
      def debt(self, amount):
          print('You have exceeded the amount of $1200 on this card {}'.format(amount))
obj = CreditCardPayment()
obj.PaySlip("1200")
obj.debt("1200")
