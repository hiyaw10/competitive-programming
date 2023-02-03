class Bank:

    def __init__(self, balance: List[int]):
        self.account_balances = balance
    
    def verify_transaction(self, account: int, amount: int = 0, skip_balance_check: bool = False):
        if account >= 0 and account < len(self.account_balances):
            if skip_balance_check: 
                return True
            elif self.account_balances[account] >= amount:
                return True
        return False

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        # 0 index account1 and account2
        account1 -= 1
        account2 -= 1
        if self.verify_transaction(account=account1, amount=money) and self.verify_transaction(account=account2, skip_balance_check=True):
            self.account_balances[account1] -= money
            self.account_balances[account2] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        # 0 index account
        account -= 1
        if self.verify_transaction(account=account, skip_balance_check=True):
            self.account_balances[account] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        # 0 index account
        account -= 1
        if self.verify_transaction(account=account, amount=money):
            self.account_balances[account] -= money
            return True
        return False