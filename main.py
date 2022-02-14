# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pyeda.inter import *
#include


LB = ""
# Series of input functions for generating ExactUCP/LB function arguments

# input function for set S to be given by user
def setSinput(setS):
    data = setS
    if data:
        try:
            correct_input = int(data)
        except ValueError:
            print("Error; Set values should be integers. Please try again.")
        else:
            return correct_input

#Global variable set S from input function
setS = setSinput()
#input function for subset S to be given by user
def subsetSinput(subsetS):
    data = subsetS
    if data:
        try:
            correct_input = int(data)
        except ValueError:
            print("Error; Set values should be integers. Please try again.")
        else:
            return correct_input

#Global variable subset S from input function
subsetS = subsetSinput()

# input function for set S to be given by user
def subCostinput(subCost):
    data = setS
    if data:
        try:
            correct_input = int(data)
        except ValueError:
            print("Error; Set values should be integers. Please try again.")
        else:
            return correct_input

#Global variable set S from input function
subCost = subCostinput()

def LB1(setS, subsetS, subCost):
    # lower bound function to be used in ExactUCP
    print('running lower bound function 1')

def LB2(setS, subsetS, subCost):
    # lower bound function to be used in ExactUCP
    print('running lower bound function 2')

def ExactUCP(setS, subsetS, subCost, LB):
    # The inputs ExactUCP are (1) a SET Sof elements, (2) a SET of Subsets of S, (4) a cost
    # associated with each subset, and (4) a lower bounding function (LB).
    print('running ExactUCP')


ExactUCP(LB=LB1)
ExactUCP(LB=LB2)


def testdebug():
    # debug function to run all parts of code for self-check at end.
    print('running testdebug')

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

if __name__ == '__main__':
    testdebug()
