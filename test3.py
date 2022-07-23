## Multiple Inheritance
## Inheritance sets priority as per sequence written inside class argument
class bank:
    __yash= "satyam"  ## private variable
    def transaction(self):
        print('total transaction value')

    def account_opening(self):
        print('this will show you your account open status')

    def deposite(self):
        print('this will show your desposited amount')

    def test(self):
        print('this is test method from bank class')

class hdfc_bank:

    def hdfc_to_icici(self):
        print('this will show u transaction happened to icici via hdfc')

    def test(self):
        print('this is test method for hdfc class')

class ineuron_bank:

    def ineuron_status_icici(self):
        print('account status in icici')



class icici(hdfc_bank, bank, ineuron_bank):
    pass


i1=icici()
i1.hdfc_to_icici()
i1.transaction()
i1.test()
i1.ineuron_status_icici()
print(i1._bank__yash)

