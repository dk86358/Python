def area_triangle(base, height):
    return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))

#Different code

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours *3600) // 60
    remain_seconds = seconds - hours  * 3600 - minutes * 60
    return hours, minutes, remain_seconds

hours, minutes, seconds = convert_seconds (5000)
print(hours, minutes, seconds)

#Next code
def greeting(name):
    print("Welcome, " + name)

result = greeting("Deep")
print(result)