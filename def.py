#Example 1 
def product (a,b):
    return (a*b)

print(product(product(2,4),product(3,5)))

##################################

#Example 2 
def difference (a,b):
    return(a-b)

def sum (a,b):
    return(a+b)

print(difference(sum(2,2),sum(3,3)))

###################################

#Example 3

print((5 > 2 *4 ) and ( 5 <= 4 * 3))

####################################

#Example 4

x = 3
if x + 5 >x**2 or x % 4 != 0:
    print("this comparison is true")

####################################

#Example 5 

number = 6
if number * 2 < 14:
    print(number * 6 % 3)
elif number > 7:
    print( 100/ number)
else:
    print(7- number)

