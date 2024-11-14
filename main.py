#TERM 1
AES1 = int(input("AES1: "))
Maths1 = int(input("Maths1: "))
Physics1 = int(input("Physics1: "))
ComputerProgramming1 = int(input("ComputerProgramming1: "))

#checks term1 grade is between 0 and 100
if AES1 > 100 or AES1 < 0 or Maths1 > 100 or Maths1 < 0 or Physics1 > 100 or Physics1 < 0 or ComputerProgramming1 > 100 or ComputerProgramming1 < 0:
    print("That is not a valid input. Goodbye. ")
else:
    print("Thank you. Term 1 is inputted. ")
#TERM 2
AES2 = int(input("AES2: "))
Maths2 = int(input("Maths1: "))
Physics2 = int(input("Physics1: "))
ComputerProgramming2 = int(input("ComputerProgramming2: "))

#checks term2 grade is between 0 and 100
if AES2 > 100 or AES2 < 0 or Maths2 > 100 or Maths2 < 0 or Physics2 > 100 or Physics2 < 0 or ComputerProgramming2 > 100 or ComputerProgramming2 < 0:
    print("That is not a valid input. Goodbye. ")
else:
    print("Thank you. Term 2 is inputted. ")
#TERM 3
AES3 = int(input("AES3: "))
Maths3 = int(input("Maths3: "))
Physics3 = int(input("Physics3: "))
CreativeDesign = int(input("CreativeDesign: "))

#checks term3 grade is between 0 and 100
if AES3 > 100 or AES3 < 0 or Maths3 > 100 or Maths3 < 0 or Physics3 > 100 or Physics3 < 0 or CreativeDesign > 100 or  CreativeDesign < 0:
    print("That is not a valid input. Goodbye. ")
else:
    print("Thank you. Term 3 is inputted. ")

TotalAverage = (AES1+AES2+AES3+Maths1+Maths2+Maths3+Physics1+Physics2+Physics3+ComputerProgramming1+ComputerProgramming2+CreativeDesign)/12
MathsAverage = (Maths2+Maths3)/2

if AES1<40 or AES2<40 or AES3<40 or Maths1<40 or Maths2<40 or Maths3<40 or Physics1<40 or Physics2<40 or Physics3<40 or ComputerProgramming1<40 or ComputerProgramming2<40 or CreativeDesign<40:
    print("Game over, god bless you.")
elif TotalAverage<60:
    print("Game over, god bless you.")
elif MathsAverage<65:
    print("Game over, god bless you.")
elif AES3<60:
    print("Game over, god bless you.")
else:
    print("You are survived.")

if TotalAverage==100:
    print("Wow, dude.")

quit()