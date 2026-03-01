years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

updated_years =[]
for year in years:
    if year.endswith("2023"):

        new = year.replace("2023","2024")

        updated_years.append(new)

    else:
        updated_years.append(year)

print(updated_years)

#2

def squares (start,end):

    return[n*n for n in range (start,end+1)]

print(squares(2,3))
print(squares(1,5))
print(squares(0,10))

#3

years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

updated_years = [year.replace("2023","2024")if year[-4:] == "2023" else year for year in years]

print(updated_years)

#4 

def list_elements(list_name, elements):

    return "The " + list_name + " list includes: " + ", ".join(elements)

print(list_elements("Printers", ["Color Printer", "Black and White Printer", "3-D Printer"]))




