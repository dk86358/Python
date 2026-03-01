multiples = []
for x in range(1,11):
    multiples.append(x*7)

print(multiples)

#Ex2

multiples = [x*7 for x in range(1,11)]
print(multiples)

#Ex3

languages = ["Python", "Perl", "Ruby", "Go", "Java" ,"C"]
lengths = [len(language) for language in languages]
print(lengths)


