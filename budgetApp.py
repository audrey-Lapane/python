# A simple budget app that tracks spending in different categories and can show the relative spending percentage on a graph.

import math

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            'amount': amount,
            'description': description})
       

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -amount,
                'description': description
                })
            return True
        return False
       
       
    def get_balance(self):
        return sum(entry['amount'] for entry in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -amount,
                'description': f"Transfer to {category.name}"
            })
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return  amount <= self.get_balance()


    def __str__(self):

        title = self.name.center(30, '*')

        rows = []
        for entry in self.ledger:
            desc = entry['description'][:23].ljust(23)   # truncate & left-align
            amount = f"{entry['amount']:.2f}"[:7].rjust(7)  # truncate & right-align
            rows.append(desc + amount)

       
        total = f"Total: {self.get_balance():.2f}"

        return '\n'.join([title] + rows + [total])


# Graphing
def create_spend_chart(categories):

    withdrawals = []
    for category in categories:
        total = sum(-e['amount'] for e in category.ledger if e['amount'] < 0)
        withdrawals.append(total)
   
    grand_total = sum(withdrawals)
   
    # Round DOWN to nearest 10
    percentages = [math.floor(w / grand_total * 10) * 10 for w in withdrawals]
   
   
    lines = ["Percentage spent by category"]
   
    # Y-axis bars
    for level in range(100, -1, -10):
        row = f"{level:>3}| "
        for pct in percentages:
            row += "o  " if pct >= level else "   "
        lines.append(row)
   
    # Horizontal line
    lines.append("    -" + "---" * len(categories))
   
    # Category names vertically
    names = [c.name for c in categories]
    max_len = max(len(n) for n in names)
   
    for i in range(max_len):
        row = "     "  # 5 spaces to align under bars
        for name in names:
            row += (name[i] if i < len(name) else " ") + "  "
        lines.append(row)
   
    return "\n".join(lines)