tea_spn = input("How many teaspoons of oil are you using? ")
ml = float(tea_spn) * 4.929
print(str(tea_spn) + " teaspoons is " + str(round(ml,2)) + " milliliters.")

if ml > 100:
    print("This is too much for cooking!")
   
print()
age = input("What is your age? ")
age_2050 = int(age) + 30
print("Today, you are " + age + " years old.")
print("In 2050, you will be " + str(age_2050) + " years old!")

if age_2050 > 80:
    print("You will be very old then.")