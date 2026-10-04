#!/usr/bin/env python3
# Created By: Maeva Tchuenga
# Date: sep 29 2026
# This program contains constants for the pizza cost calculation
from py_compile import main


TAX_RATE = 0.13
LABOUR_COST = 2.00
RENTAL_COST = 2.25
INGREDIENT_COST = 1.50

subtotal = LABOUR_COST + RENTAL_COST + INGREDIENT_COST * 5
tax = TAX_RATE * subtotal
total = subtotal + tax

    #output

print("The total cost is = ${:,.2f}".format(total))



if __name__ == "__main__":
     main()


