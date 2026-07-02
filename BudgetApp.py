"""
Build a Budget App
In this lab, you will build a simple budget app that tracks spending in different categories and can show the relative spending percentage on a graph.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

You should have a Category class that accepts a name as the argument.

The Category class should have an instance attribute ledger that is a list, and contains the list of transactions.

The Category class should have the following methods:

A deposit method that accepts an amount and an optional description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {'amount': amount, 'description': description}.
A withdraw method that accepts an amount and an optional description (default to an empty string). The method should store in ledger the amount passed in as a negative number, and should return True if the withdrawal succeeded and False otherwise.
A get_balance method that returns the current category balance based on ledger.
A transfer method that accepts an amount and another Category instance, withdraws the amount with description Transfer to [Destination], deposits it into the other category with description Transfer from [Source], where [Destination] and [Source] should be replaced by the name of destination and source categories. The method should return True when the transfer is successful, and False otherwise.
A check_funds method that accepts an amount and returns False if it exceeds the balance or True otherwise. This method must be used by both the withdraw and transfer methods.
When a Category object is printed, it should:

Display a title line of 30 characters with the category name centered between * characters.
List each ledger entry with up to 23 characters of its description left-aligned and the amount right-aligned (two decimal places, max 7 characters).
Show a final line Total: [balance], where [balance] should be replaced by the category total.
Here is an example usage:

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
And here is an example of the output:

*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
You should have a function outside the Category class named create_spend_chart(categories) that takes a list of categories and returns a bar-chart string. To build the chart:

Start with the title Percentage spent by category.
Calculate percentages from withdrawals only and not from deposits. The percentage should be the percentage of the amount spent for each category to the total spent for all categories (rounded down to the nearest 10).
Label the y-axis from 100 down to 0 in steps of 10.
Use o characters for the bars.
Include a horizontal line two spaces past the last bar.
Write category names vertically below the bar.
This function will be tested with up to four categories.

Make sure to match the spacing of the example output exactly:

Percentage spent by category
100|
 90|
 80|
 70|
 60| o
 50| o
 40| o
 30| o
 20| o  o
 10| o  o  o
  0| o  o  o
    ----------
     F  C  A
     o  l  u
     o  o  t
     d  t  o
        h
        i
        n
        g
NOTE: open the browser console with F12 to see a more verbose output of the tests.
"""

import math


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

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
        title = self.name.center(30, "*") + "\n"

        # Ledger entries
        rows = ""
        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amount = f"{item['amount']:.2f}".rjust(7)
            rows += f"{desc}{amount}\n"

        # Total line
        total = f"Total: {self.get_balance():.2f}"

        return title + rows + total


def create_spend_chart(categories):
    # Get total withdrawals per category
    withdrawals = []
    for cat in categories:
        total = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
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
