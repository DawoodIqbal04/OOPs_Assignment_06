
class Bank:
    bank_name = 'Meezan Islamic Bank' # Class Variable / Attribute

    @classmethod 
    def change_bank_name(cls, name): # Class Method For Changing Class Variable
        print(f'Bank name before changing: {cls.bank_name}') # Before Changing
        cls.bank_name = name # Changed Here
        print(f'Bank name after changing: {cls.bank_name}') # After Changing

bank1 = Bank() # Instance Created Here
bank1.change_bank_name('Bank Al-Habib LTD') # Calls the Name Changing Function Here

# Changing Class Variable Effect All Class Instances

bank2 = Bank() # Second Instance
print(bank2.bank_name) # Changing The Class Variable Effects All Instances So Output = Bank Al-Habib LTD

bank3 = Bank() # Third Instance
print(bank3.bank_name) # Also For This One