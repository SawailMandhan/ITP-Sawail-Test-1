#defining variables
PENNY_VALUE =1
NICKEL_VALUE =5
DIME_VALUE =10
QUARTER_VALUE =25
PENNIES_IN_DOLLAR =100

a=int(input("Enter the number of pennies: "))
b =int(input("Enter the number of nickel: "))
c = int(input("Enter the number of dimes: ")) 
d =int(input("Enter the number of quater:"))  
 
totalcent= PENNY_VALUE*a + NICKEL_VALUE*b + DIME_VALUE*c + QUARTER_VALUE*d
totaldollar = totalcent/100
if totaldollar == 1:
 print("Congratulations!''The amount you entered was exactly one dollar!''You win the game!!")
else:
   if totaldollar >1:
     print("Sorry, the amount you entered was more than one dollar.")
 