# converts temperature from Celsius to Fahrenheit
def temp_convert(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temp_c = input("What is the temperature in degrees Celsius? ")
temp_f = temp_convert(float(temp_c))

if float(temp_c) > 30:
   print("It is really hot!")

print(temp_c + " degrees Celsius are " + str(temp_f) + " degrees Fahrenheit.")    



