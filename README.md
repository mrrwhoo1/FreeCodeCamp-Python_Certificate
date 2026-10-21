# freeCodeCamp Python Certificate

My solutions to the labs and projects from the **freeCodeCamp Python certification**, written while working through the course. Each file begins with the original task description (as a docstring), followed by my implementation.

## Projects

| File | What it does | Concepts practised |
|---|---|---|
| [`BudgetApp.py`](BudgetApp.py) | A `Category` class that tracks deposits, withdrawals and transfers in a ledger, prints a formatted statement, and a `create_spend_chart()` function that draws a bar chart of spending per category | Classes, `__str__`, string formatting and alignment, list comprehensions |
| [`ConfigurationManager.py`](ConfigurationManager.py) | Functions to add, update, delete and view user settings (theme, language, notifications) stored in a dictionary | Dictionaries, tuples, functions, string handling |
| [`HashTable.py`](HashTable.py) | A hash table built from scratch. The hash is the sum of the Unicode values of the key, and keys with the same hash share a nested dictionary | Classes, hashing, collisions, dictionaries |
| [`Polygone_Area_Calculator.py`](Polygone_Area_Calculator.py) | `Rectangle` and `Square` classes with area, perimeter, diagonal, an ASCII picture, and how many times one shape fits inside another | Object-oriented programming, inheritance, method overriding, `super()` |
| [`TowerHenoi.py`](TowerHenoi.py) | A recursive solver for the Tower of Hanoi puzzle that returns every move, in 2^n - 1 steps | Recursion, nested functions, list manipulation |

## Usage examples

Run these from a Python shell in the project folder.

### Budget App

```python
from BudgetApp import Category, create_spend_chart

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

clothing = Category("Clothing")
food.transfer(50, clothing)

print(food)
print(create_spend_chart([food, clothing]))
```

```text
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

### Polygon Area Calculator

```python
from Polygone_Area_Calculator import Rectangle, Square

rect = Rectangle(4, 8)
print(rect)                           # Rectangle(width=4, height=8)
print(rect.get_area())                # 32
print(rect.get_amount_inside(Square(4)))  # 2

sq = Square(9)
print(sq)                             # Square(side=9)
```

### Hash Table

```python
from HashTable import HashTable

table = HashTable()
table.add("name", "Maron")
print(table.lookup("name"))           # Maron
print(table.lookup("missing"))        # None
table.remove("name")
```

### Tower of Hanoi

```python
from TowerHenoi import hanoi_solver

print(hanoi_solver(3))
```

```text
[3, 2, 1] [] []
[3, 2] [] [1]
[3] [2] [1]
[3] [2, 1] []
[] [2, 1] [3]
[1] [2] [3]
[1] [] [3, 2]
[] [] [3, 2, 1]
```

## Requirements

Python 3. There are no external dependencies; only the standard library (`math`) is used.

## About

Part of my journey learning Python and computer science. More of my work is on my [GitHub profile](https://github.com/mrrwhoo1).
