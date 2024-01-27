class Atm:
    # construcotr
    def __init__(self):
        self.pin = ''
        self.blance = 0
        self.manu()
        
    def manu(self):
        while True:
            user_input = input('''
                                hello,how would you like to proceed?
                                1.Enter 1 to create pin
                                2.Enter 2 to deposit
                                3.Enter 3 to withdraw
                                4.Enter 4 to check balance
                                5.Enter 5 to exit
                                Enter this : ''')
            if user_input == '1':
                self.c_pin()
            elif user_input == '2':
                    self.diposot()
            elif user_input == '3':
                    self.withdraw()
            elif user_input == '4':
                    self.ckeck_blance()
            else:
                print('exit')
                break

    def c_pin(self):
        self.pin = input("Enter pin : ")
        print('pin set')

    def diposot(self):
        temp = input("Enter pin : ")
        if temp == self.pin:
            deposit = int(input("Enter deposot : "))
            self.blance += deposit
            print('Deposit successful')
        else:
            print('Worng pin')

    def withdraw(self):
        temp = input("Enter pin : ")
        if temp == self.pin:
            amount = int(input("Enter withdraw : "))
            if self.blance >= amount:
                self.blance -= amount
                print('withdraw successful')
            else:
                print('found')
        else:
            print('Worng pin')

    def ckeck_blance(self):
        temp = input("Enter pin : ")
        if temp == self.pin:
            print(f"Balance = {self.blance}")
        else:
            print('Worng pin')


sbi = Atm()
sbi

