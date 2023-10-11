import math
import ezdxf
import os
from datetime import date

def get_todays_date():
    today = date.today()
    formatted_date = today.strftime("%d-%m-%Y")
    return formatted_date

pi = math.pi
n = 0
mass = 0
air_density = 1.25
velocity = 7
Coeficient_drag = 0.62
Spill_percent = 0.03
gravity = 9.81
overlap = 15
area_choice = False

while True:
    calculation = input("Do you know the value of Area * Coeficient drag for All other objects creating air drag?\nIf you do not know it select no (n), but be ready that the real falling speed will be a little slower\nIf you assume there is no air drag without parachute select no (n)\nIf you know the A*C_d, then select yes (y)\nInput answer (y/n):")
    if calculation == 'y':
        area_choice = True
        while True:
            A_CD = float(input("Enter the A_1*C_d1 value in SI units:"))
            if A_CD >= 0:
                break
            else:
                print("Input value must be greater than 0!\n")
        while True:
            mass = float(input("Input the net mass in kg:"))
            if mass > 0:
                break
            else:
                print("The mass must be positive!")
        break
    elif calculation == 'n':
        area_choice = False
        while True:
            mass = float(input("Input the net mass in kg:"))
            if mass > 0:
                break
            else:
                print("The mass must be positive!")
        break
    else:
        print("When answering the question, the answer must be \"y\" or \"n\"!")
while True:
    n = int(input("Input the number of gores:"))
    if n >= 4:
        break
    else:
        print("The number of gores must be 4 or larger!")
while True:
    velocity = float(input("Input the desired landing velocity in m/s:"))
    if velocity > 0:
        break
    else:
        print("Velocity must be positive!\n")
while True:
    atbilde = input("Do you want to change any other constant? (y/n)\n")
    if atbilde == 'n':
        break
    elif atbilde == 'y':
        while True:
            ko_mainit = int(input("What constant do you want to change?\nNumber of gores - 1\nNet mass - 2\nAir density ar ground level - 3\nLanding speed - 4\nDrag coefficient - 5\nSpill hole area percentage - 6\nGravitational constant - 7\nOverlap for manufacturer - 8\n"))
            match ko_mainit:
                case 1:
                    while True:
                        print("Input the desired number of gores! The current value is ", n,". The value must be 4 or larger!")
                        n = int(input())
                        if n >= 4:
                            break
                        else:
                            print("Input a value thati is 4 or larger!\n")
                    break
                case 2:
                    while True:
                        print("Input the net mass in kg, the current mass is ", mass, ". The mass must be greater than 0!")
                        mass = float(input())
                        if mass > 0:
                            break
                        else:
                            print("Input value must be greater than 0!\n")
                    break
                case 3:
                    while True:
                        print("Input the value of air density at ground level in kg/m^3! The current value is ", air_density, ". The value must be positive!")
                        air_density = float(input())
                        if air_density > 0:
                            break
                        else:
                            print("Input value must be greater than 0!\n")
                    break
                case 4:
                    while True:
                        print("Input the desired landing speed in m/s! The current value is ", velocity, ". The input value must be greater than 0!")
                        velocity = float(input())
                        if velocity > 0:
                            break
                        else:
                            print("Input value must be greater than 0!\n")
                    break
                case 5:
                    while True:
                        print("Input the drag coefficient! The current value is ", Coeficient_drag, ". The input value must be greater than 0!\nNote that this change is advised only if the new drag coefficient is experimentally determined to be better than the one used by default!\nInput value:")
                        Coeficient_drag = float(input())
                        if Coeficient_drag > 0:
                            break
                        else:
                            print("Input value must be greater than 0!\n")
                    break
                case 6:
                    while True:
                        print("Highly advised to not change this value! Do change at your own risk! By changing this value Coefficient drag will change!\nInput the desired spillhole area fraction! The current value is ", Spill_percent, ". The value must be greater than 0!")
                        Spill_percent = float(input())
                        if Spill_percent > 0:
                            break
                        else:
                            print("Input value must be greater than 0!\n")
                    break
                case 7:
                    while True:
                        print("Unless you are going to another planet, do not change this!\nInput the value for accelaration due to gravity in m/s^2! The current value is ", gravity, ". The value must be greater than 0!")
                        gravity = float(input())
                        if gravity > 0:
                            break
                        else:
                            print("Input value must be greater than 0!\n")
                    break
                case 8:
                    while True:
                        print("Input the value of overlap in mm for manufacturer! The current value is ", overlap, ". The value must be positive and in mm!")
                        overlap = float(input())
                        if overlap > 0:
                            break
                        else:
                            print("Input value must be greater than 0!\n")
                    break
                case _:
                    print("The value must be an number from 1-8!")
                    input()
    else:
        print("When answering the question, the answer must be \"y\" or \"n\"!")

# Defines some constants
if area_choice == True:
    area = (((2*mass*gravity)/(air_density*pow(velocity, 2))))/(Coeficient_drag)
    R = 1000*(math.sqrt(((2*mass*gravity)/(air_density*pow(velocity, 2))-A_CD)/(2*pi*(1-Spill_percent)*Coeficient_drag))) 
elif area_choice == False:
    area = (2*mass*gravity)/(air_density*pow(velocity, 2)*Coeficient_drag*(1-Spill_percent))
    R = 1000*(math.sqrt((2*mass*gravity)/(air_density*pow(velocity, 2)*Coeficient_drag*2*pi*(1-Spill_percent))))
else:
    print("ERROR")
Y_max = R*((pi)/(2)-math.acos(1-Spill_percent))
A_x = (pi*R*math.sqrt(-pow((math.cos(-(2*R*((pi)/(2)-math.acos(1-Spill_percent))-pi*R)/(2*R))), 2)+1))/(n)
# Defines the equation to draw
def x_realais(y):
    x_faktiskais = (pi*R*math.sqrt(-pow((math.cos(-(2*y-pi*R)/(2*R))), 2)+1))/(n)
    return x_faktiskais + (overlap)/(math.sqrt(1+pow(((math.sqrt(pow(pi, 2)*pow(R, 2)-pow(n, 2)*pow(x_faktiskais, 2)))/(n*R)), 2)))

def y_realais(y):
    x_faktiskais = (pi*R*math.sqrt(-pow((math.cos(-(2*y-pi*R)/(2*R))), 2)+1))/(n)
    return y + ((math.sqrt(pow(pi, 2)*pow(R, 2)-pow(n, 2)*pow(x_faktiskais, 2)))/(n*R)) * (overlap)/(math.sqrt(1+pow(((math.sqrt(pow(pi, 2)*pow(R, 2)-pow(n, 2)*pow(x_faktiskais, 2)))/(n*R)), 2)))

# Creates a new DXF file
doc = ezdxf.new('R2010')

firstmax1=0
firstmax2=0

# Add a new line to the file for each point on the equation
msp = doc.modelspace()
for i in range(1, 1002):
    y = Y_max - (i-1)*((Y_max)/(1000))
    ieprieksejais = Y_max - (i-2)*((Y_max)/(1000))
    if i == 1:
        msp.add_line((0, Y_max + overlap +overlap), (A_x, Y_max + overlap+overlap))
        msp.add_line((A_x, Y_max + overlap+overlap), (A_x, Y_max+overlap))
        msp.add_line((A_x, Y_max+overlap), (x_realais(y), y_realais(y)+overlap))
    elif i > 1 and i < 1001:
        #print("y = ", y, "x_1 = ", x_realais(ieprieksejais), "y_1 = ", y_realais(ieprieksejais)+overlap, "x_2 = ", x_realais(y), "y_2 = ", y_realais(y)+overlap)
        msp.add_line((x_realais(ieprieksejais), y_realais(ieprieksejais)+overlap), (x_realais(y), y_realais(y)+overlap))
        firstmax1 = x_realais(y)
        firstmax2 = y_realais(y)+overlap
    elif i == 1001:
        msp.add_line((firstmax1, firstmax2), (x_realais(ieprieksejais), overlap))
        msp.add_line((x_realais(ieprieksejais), overlap), ((pi*R)/(n)+overlap, overlap))
        msp.add_line(((pi*R)/(n)+overlap, overlap), ((pi*R)/(n), overlap))
        msp.add_line(((pi*R)/(n), overlap), ((pi*R)/(n), 0))
        msp.add_line(((pi*R)/(n), 0), (0, 0))

for i in range (2, 1002):
    y = (i-1)*((Y_max)/(1000)) 
    ieprieksejais = (i-2)*((Y_max)/(1000))
    if i == 2:
        msp.add_line((0, 0), (-(pi*R)/(n), 0))
        msp.add_line((-(pi*R)/(n), 0), (-(pi*R)/(n), overlap))
        msp.add_line((-(pi*R)/(n), overlap), (-((pi*R)/(n)+overlap), overlap))
        msp.add_line((-((pi*R)/(n)+overlap), overlap), (-x_realais(y), y_realais(y)+overlap))
    elif i > 2 and i < 1001:
        msp.add_line((-x_realais(ieprieksejais), y_realais(ieprieksejais)+overlap), (-x_realais(y), y_realais(y)+overlap))
        firstmax1 = -x_realais(y)
        firstmax2 = y_realais(y)+overlap
    elif i == 1001:
        msp.add_line((firstmax1, firstmax2), (-x_realais(y), y_realais(y)+overlap))
        msp.add_line((-x_realais(y), y_realais(y)+overlap), (-A_x, Y_max+overlap))
        msp.add_line((-A_x, Y_max+overlap), (-A_x, Y_max + overlap+overlap))
        msp.add_line((-A_x, Y_max + overlap+overlap), (0, Y_max + overlap +overlap))

# Saves the DXF file
print("Your parachutes area is: " + str(round(area, 2)) + "m^2")
print("Your parachutes angular diameter is: " + str(round(R*0.002, 2)) + "m long!")
print("Your parachute lines should be: " + str(round(2*R*2.15*0.001, 2)) + "m long!")
date_string = get_todays_date()
filename = "Gore_shape-"+date_string+".dxf"
doc.saveas(filename)
print("All done!\nFile saved in:", os.getcwd())
input()