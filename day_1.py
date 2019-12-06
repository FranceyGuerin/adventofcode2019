#Fuel required to launch a given module is based on its mass.
#Specifically, to find the fuel required for a module,
#take its mass, divide by three, round down, and subtract 2.
# divide by 3
# round down
#subtract 2


#At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel. So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
#The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.

#sum all results
import math
import pandas as pd

modules = pd.read_csv('modules.csv')

def calculate_fuel(mass):
    fuel = mass/3
    fuel = math.floor(fuel)
    fuel -= 2
    if fuel < 0:
        fuel = 0
    else:
        fuel += calculate_fuel(fuel)
    return fuel

def test_fuel_calculation(mass, expected_result):
    fuel = calculate_fuel(mass)
    if fuel == expected_result:
        print('Test passed')
    else:
        raise Exception('Incorrect result.  Expected output of 966, got:', )

test_fuel_calculation(1969, 966)
test_fuel_calculation(100756, 50346)


fuel = 0
for i in range(len(modules)):
    fuel += calculate_fuel(modules.loc[i])

print(fuel)
