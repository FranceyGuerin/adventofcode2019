import pandas as pd

#Opcode 1 adds together numbers read from two positions and stores the result in a third position.
#The three integers immediately after the opcode tell you these three positions - the first two indicate the positions
#from which you should read the input values, and the third indicates the position at which the output should be stored.

#For example, if your Intcode computer encounters 1,10,20,30, it should read the values at positions 10 and 20,
#add those values, and then overwrite the value at position 30 with their sum.

values_master = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,13,27,1,10,27,31,2,31,13,35,1,10,35,39,2,9,39,43,2,43,9,47,1,6,47,51,1,10,51,55,2,55,13,59,1,59,10,63,2,63,13,67,2,67,9,71,1,6,71,75,2,75,9,79,1,79,5,83,2,83,13,87,1,9,87,91,1,13,91,95,1,2,95,99,1,99,6,0,99,2,14,0,0
]


def calculate_opcode(opcodes):
    for i in range(len(opcodes)):
        address = i*4
        opcode = opcodes[address]

        if opcode == 99:
            break

        noun = opcodes[address+1]
        verb = opcodes[address+2]
        output_position = opcodes[address+3]

        if opcode == 1:
            opcodes[output_position] = opcodes[noun] + opcodes[verb]

        if opcode == 2:
            opcodes[output_position] = opcodes[noun] * opcodes[verb]
    return opcodes

def test_opcode_calculation():
    if calculate_opcode([1,0,0,0,99]) == [2,0,0,0,99]:
        print('Passed Opcode 1 Test')

    if calculate_opcode([2,3,0,3,99]) == [2,3,0,6,99]:
        print('Passed Opcode 2 Test')

    if calculate_opcode([2,4,4,5,99,0]) == [2,4,4,5,99,9801]:
        print('Passed Opcode 2 Test')

    input = [1,1,1,4,99,5,6,0,99]
    expected_result = [30,1,1,4,2,5,6,0,99]
    opcodes = calculate_opcode(input)
    if opcodes == expected_result:
        print('Passed Opcode 2 Test')
    else:
        raise Exception('Failed multiplication and summation test.  Expected ', expected_result,' received: ', opcodes)


    values = values_master.copy()
    values[1] = 12
    values[2] = 2
    opcodes = calculate_opcode(values)
    if opcodes[0] == 3085697:
        print('Passed Opcode value change test')
    else:
        raise Exception('Failed value change test.  Expected 3085697, received:', opcodes[0])


test_opcode_calculation()

def find_opcodes():
    for i in range(100):
        for j in range(100):
            values = values_master.copy()
            values[1] = i
            values[2] = j

            opcodes = calculate_opcode(values)
            
            if opcodes[0] == 19690720:
                print(i, j)

find_opcodes()
