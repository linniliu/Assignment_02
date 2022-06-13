# STEP 2: Creation of a base class that defines the basic operations of the banking system

from Base import *

class Account(Base):

    dep = 0.0
    with = 0.0
    int_rate_monthly = 0.0
    monthly_int = 0.0

    def __init__(self, start_bal: float, current_bal: float, amount_dep: float, number_dep: int, amount_withdra: float, numer_withdra: int, int_rate_annual: float, service_charge: float. account_status: bool):
        super().__init__(start_bal)
        super().__init__(current_bal)
        super().__init__(amount_dep)
        super().__init__(number_dep)
        super().__init__(amount_withdra)
        super().__init__(number_withdra)
        super().__init__(int_rate_annual)
        super().__init__(service_charge)
        super().__init__(account_status)

    def deposit(self):
        return dep + self.current_bal # adds amount being deposited to account balance
        return dep + self.amount_dep # adds amount being deposited to total deposits
        return 1 + self.number_dep # increments the number of deposits

    def withdraw(self):
        return self.current_bal - with
        return self.amount_withdra + with
        return 1 + self.number_withdra

    def calc_interest(self):
        return int_rate_monthly = self.int_rate_annual / 12
        return monthly_int = self.current_bal * int_rate_monthly
        return self.current_bal = self.current_bal + monthly_int

    #def close_month(self):
        #return = self.current_bal -

