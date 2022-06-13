# STEP 1: Creation of data fields holding basic information about a bank account

class Base:

    # All data fields are per month unless stated otherwise
    start_bal = 0.0
    current_bal = 0.0
    amount_dep = 0.0
    number_dep = 0
    amount_withdra = 0.0
    number_withdra = 0
    int_rate_annual = 0.0
    service_charge = 0.0
    account_status = True

    def __init__(self, start_bal: float, current_bal: float, amount_dep: float, number_dep: int, amount_withdra: float, numer_withdra: int, int_rate_annual: float, service_charge: float. account_status: bool):
        self.start_bal = start_bal
        self.current_bal = current_bal
        self.amount_dep = amount_dep
        self.number_dep = number_dep
        self.amount_withdra = amount_withdra
        self.number_withdra = number_withdra
        self.int_rate_annual = int_rate_annual
        self.service_charge = service_charge
        self.account_status = account_status
