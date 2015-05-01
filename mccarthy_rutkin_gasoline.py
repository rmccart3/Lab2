"""
File: mccarthy_rutkin_gasoline.py
Author: Ryan McCarthy and Brad Rutkin
Description:
 Prints the pounds of carbon dioxide produced by a given number of 
 gallons of gasoline, the number of barrels of crude oil produced by
 the given gallons of gasoline, and the average US dollar cost for
 that much gasoline
"""
#ask user to input number of gallons of gasoline
gas_gallons = float(raw_input\
        ('Please enter the number of gallons of gasoline: '))
#1 gallon of gasoline produces approximately 19.64 pounds of carbon dioxide
carbon_dioxide_pounds = gas_gallons*19.64
#output the pounds of carbon dioxide produced
#19 gallons of gasoline produced from aproximately 1 barrels of crude oil
crude_oil_barrels = gas_gallons / 19
#use conversion factor to output crude oil barrels
#$2.60 current average for 1 gallon of gasoline
avgcost = gas_gallons * 2.60
#multiply gas gallons by current average to output average cost

print gas_gallons,'gallons of gasoline produces approximately',\
        carbon_dioxide_pounds,'pounds of carbon dioxide.'
print crude_oil_barrels,'barrels of crude oil produced from',\
        gas_gallons,'gallons of gas.'
print 'The average cost for',gas_gallons,'gallons of gas is $',avgcost
