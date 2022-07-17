
## Multi Label Inheritance :
class bank:
    def transaction(self):
        print('total transaction value')

    def account_opening(self):
        print('this will show you your account open status')

    def deposite(self):
        print('this will show your desposited amount')

class hdfc_bank(bank):

    def hdfc_to_icici(self):
        print('this will show u transaction happened to icici via hdfc')


class icici(hdfc_bank):
    pass

i1=icici()
print(i1.transaction())
print(i1.account_opening())
print(i1.transaction())





