def mirror_string(my_string):

    forwards = ""
    backwards = ""

    for charachter in my_string:

        if charachter.isalpha():

            forwards += charachter
            backwards = charachter + backwards

    if forwards.lower() == backwards.lower():
        return True
    return False

print(mirror_string("12 Noon"))
print(mirror_string("Was it a car or cat I saw"))
print(mirror_string("eve, Madam Eve"))

#Example 2 
def replace_date(schedule, old_date, new_date):

    if schedule.endswith(old_date):
        
        p = len(old_date)
    
        new_schedule = schedule[:-p] + schedule [-p:].replace(old_date,new_date)

        return new_schedule

    return schedule 

print(replace_date("Last year annual report will be reelased in March 2023", "2023", "2024"))

print(replace_date("In April , the CEO will hold a conference","April","May"))

print(replace_date("The convention is schedule for october ", "October", "June"))



    
    


