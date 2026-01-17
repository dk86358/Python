multiplier = 1
result = multiplier * 5
while result <=60:
    print(result)

    multiplier += 1

    result = multiplier * 5
print("Done")

#Example 2

def count_factors(given_number):

    factor =1
    count = 1

    if given_number == 0:
        return 0 
    
    while factor < given_number:
        if given_number % factor == 0:
            count += 1

        factor +=1
    return count 

print(count_factors(0))
print(count_factors(3))
print(count_factors(6))
print(count_factors(10))

#Example 3 


def addition_table(given_number):

	
	iterated_number = 1
	my_sum = 1

	while iterated_number <= 5:

		
		my_sum = given_number + iterated_number

		# Test to see if the "my_sum" variable is greater than 20.
		if my_sum > 20:
			# If True, then use the break keyword to exit the loop.
			break

		
		print(str(given_number), "+", str(iterated_number), "=", str(my_sum))

		
		iterated_number += 1


addition_table(5)
addition_table(17)
addition_table(30)



