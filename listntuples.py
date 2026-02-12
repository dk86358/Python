animals =["Lions" , "Zebra" , "Dolphin" , "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)
    
print("Total charachters: {}, Average length: {}".format(chars , chars/len(animals)))

#EX 2

winners = ["Ashley" ,  "Deep" , "Resee"]
for index, person in enumerate(winners):
    print("{} - {}".format(index+1, person))


#Ex 3

def full_emails(people):
    result= []
    for email, name in people:
        result.append("{} <{}>".format(name,email))
    return result
print(full_emails([("Alex@gmail.com", "Alex Diegot"),("shay@gmail.com", "Shay Brandt")]))




