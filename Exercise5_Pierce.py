'''
Date: Sep 18, 2023
@author: Benjamin Pierce
This program calculates compound interest after a specific number of months.  
User will enter the principle amount, followed by interest accrued in account, then number of months invested.
'''
#function with principal (P), interestRate (r), and months (t)
def calc_future_value(P, r, t):
    #calculate monthly interest rate
    i = r/12/100
    
    #calculate future value
    F = P * (1 + i)**t
    
    return F

#user inputs values
P = float(input("Enter principle: "))
r = float(input("Enter annual interest rate in percentage: "))
t = int(input("Enter number of months: "))

#calculate and display future value
future_value = calc_future_value(P, r, t)
print(f'The future value of your account after {t} months is: ${future_value:.2f}')    