"""
Author : Akshay Joshi
GitHub : https://github.com/ijoshi90
Created on 27-Oct-19 at 20:20
"""

principle = float (input("Enter the Loan Amount : "))
interest = float (input("Enter the Interest Percentage : "))
term = int (input("Enter term in years : "))
simple_interest = (principle * term * interest) / 100
emi = (principle + simple_interest) / (term*12)

print ("Principle : {}".format(principle))
print("Rate of Interest : {}".format(interest))
print("Term in Years : {} ({} months)".format(term,term*12))
print ("Simple Interest : {}".format(simple_interest))
print ("Total to Pay Back : {}".format(principle+simple_interest))
print ("EMI : {}".format(round(emi)))