import math

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination.name}")
            destination.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        # Title line — 30 chars with name centered between *
        title = self.name.center(30, '*') + '\n'

        # Ledger entries
        rows = ""
        for item in self.ledger:
            desc = item['description'][:23].ljust(23)
            amount = f"{item['amount']:.2f}".rjust(7)
            rows += f"{desc}{amount}\n"

        # Total line
        total = f"Total: {self.get_balance():.2f}"

        return title + rows + total


def create_spend_chart(categories):
    # Get total withdrawals per category
    withdrawals = []
    for cat in categories:
        total = sum(-item['amount'] for item in cat.ledger if item['amount'] < 0)
        withdrawals.append(total)

    total_spent = sum(withdrawals)

    # Round down to nearest 10
    percentages = [math.floor(w / total_spent * 100 / 10) * 10 for w in withdrawals]

    # Build chart
    chart = "Percentage spent by category\n"

    for level in range(100, -1, -10):
        row = str(level).rjust(3) + "| "
        for pct in percentages:
            row += "o  " if pct >= level else "   "
        chart += row + "\n"

    # Horizontal line — 4 spaces + dash for each category + extra dash
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Category names vertically
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        row = "     "
        for cat in categories:
            if i < len(cat.name):
                row += cat.name[i] + "  "
            else:
                row += "   "
        chart += row + "\n"

    return chart.rstrip("\n")
