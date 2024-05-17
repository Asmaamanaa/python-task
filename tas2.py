#Write a program to calculate the electricity bill (accept number of unit from user ) according to the following criteria
#First 100 units ---> cost 0
#Next 100 units ----> cost 500
#After 200 units ----> cost 1500
#total paid 2000


units = 350
units = float(input('enter units = '))
if units <= 100:
    print('no charge')
if 100 < units < 200 :
    cost = ('units - 100')*5
    print('2000 =', cost)
if units > 200 :
    cost = ('units - 200')*10
    print('2000 =', cost+500)
else :
    print ('false') 