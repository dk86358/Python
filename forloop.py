for x in range (5):
    print(x)


# Example 2
friends = ['Tylor','Alex','Pat','Eli']
for friend in friends:
    print("Hi" +  friend)

# Example 3

values = [23, 52, 59, 37, 48]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1

print("Total sum:" + str(sum) + " - Average:" + str(sum/length))
    