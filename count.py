def count_10(end):
    count= ""

    for number in range(0,end +1, 10):
        count += str (number) + " "

    return count.strip()


print(count_10((100)))

#Example 2 


def matrix(initial_number, end_of_first_row):
    n1 = initial_number
    n2 = end_of_first_row

    for row in range (n1,n2):
        
        for coloum in range (n1, n2):

            print(coloum * row, end= " ")
        
        print()

matrix(1,4)


#Example 3

for outer_loop in range(10):
    for inner_loop in range (outer_loop):

        print(inner_loop)


#Example 4

for n in range (11, -2):
    if n % 2 != 0:
        print(n,end=" ")


# Example 5

starting_number = 18

while starting_number >= 0:

    print(starting_number, end=" ")

    starting_number -= 3


#Example 6

def x_figure(salary):
    tally = 0

    if salary == 0:
        tally += 1

    while salary >= 1:

        salary = salary/10

        tally += 1

    return tally

print("The CEO has a " + str(x_figure(2300000))+ "-figure salary.")
    


    


