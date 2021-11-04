#python

sum_of_squars= 0
for i in range(1,101):
    x= i**2
    sum_of_squars += x
    
    
y=0   
for i in range(1,101):
    y += i
    squar_of_sum = y**2


#The difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
difference =  squar_of_sum - sum_of_squars

print(difference)



    

