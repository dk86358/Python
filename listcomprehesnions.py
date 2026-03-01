multiples =[]
for x in range(1,11):
    multiples.append(x*7)
print(multiples)

#2

multiples = [x*7 for x in range(1,11)]
print(multiples)

#3 

languages = ["Python", "java", "C","Ruby","Perl"]
length = [len(language) for language in languages]
print(length)

# 4

z= [x for x in range(0,101) if x % 3 == 0]
print(z)