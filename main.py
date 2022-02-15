from pyeda.inter import *
# example
# x_0_1_2_3 = exprvar('x', (0, 1, 2 ,3))
# print(x_0_1_2_3)
LB = ""


# Introduction
#print("Hello, press any key to continue")


""" The following is a series of input functions 
    for generating ExactUCP/LB function arguments """



"""Function/Global variable for setS"""
# input function for set S to be given by user
def set_s_input(prompt):
    """ set_s_input takes the user input of an integer N, denoting the
         size of set S, for which the set will be constructed from
         1 to N."""
    s = "s"     # stand-in for expvar variable assignment
    # data = setS
    # open('input_file.txt', "x")  # creates new file titled input_file.txt
    """above not needed"""
    while True:
        try:
            with open('input_file.txt', 'r') as f:  # input-file handling
                data = [line.strip() for line in f]  # input-file printout

            correct_input = int(input(prompt))  # take in user input
            print("You have chosen " + str(correct_input))  # echo back user input for confirmation

        except ValueError:
            print("Error; Input shall be int N denoting size of set S from 1 to N. Please try again.")
            exit("Value Error")
        else:
            i = 0  # iterator
            print("The variables in set S are as follows:")
            while i < int(correct_input):
                indexed_S = exprvar(s, i)
                data.append(indexed_S)
                print(indexed_S)
                i += 1  # increment i until i == N
                if i == correct_input:
                    return indexed_S
            with open('input_file.txt', 'w') as nf:
                nf.write('\n'.join(data))
        #return

# Global variable set S from input function
setS = set_s_input("Please input an integer denoting N, the size of set S.\n")
# Printout of set S should be echoed to user for visual inspection.
print(setS)

"""Function/Global variable for subsetS"""
#input function for subset S to be given by user
def subset_s_input(prompt):
    """ subset_s_input takes the user input for the set which is a subset of S"""
    #data = subsetS
    end = str("done")
    while True:
        try:
            correct_input = input(prompt)
        except ValueError:
            print("Error; Set values should be strings corresponding to the subset of S already input. Please try again.")
        else:
            return correct_input
    #elif: data = end
    #        return end



""" Should be in form {a,b} or {a,b,c} etc"""
#Global variable subset S from input function
subsetS = subset_s_input("Please input variables from S to make subsets i.e. {1,3}, {2,3,4}, {1,5}.\n")

"""Function/Global variable for subCost"""
# input function for set S to be given by user
def sub_cost_input(prompt):
    """ Takes the user input for the cost of each subset"""
    #data = setS
    if True:
        try:
            correct_input = input(prompt)
        except ValueError:
            print("Error; Set values should be integers. Please try again.")
        else:
            return correct_input

#Global variable set S from input function
subCost = sub_cost_input("Please input the cost of each subset.")

""" The following are two Lower-Bound functions to be used in ExactUCP"""
# Some options we can use are:
# Maximum Independent Set (MIS)
# Linear Programming Relaxation (LPR)
# Cutting Planes (CP)

def low_bound_1(setS, subsetS, subCost):
    """ lower bound function to be used in ExactUCP """
    print('running lower bound function 1')

def low_bound_2(setS, subsetS, subCost):
    """ lower bound function to be used in ExactUCP """
    print('running lower bound function 2')


"""The following the function definition for ExactUCP 
    utilizing the previous functions for obtaining the user inputs 
    for the specified function arguments"""


def ExactUCP(setS, subsetS, subCost, LB):
    """ Two-level minimization utilizing branch and bound"""
    # The inputs ExactUCP are (1) a SET Sof elements, (2) a SET of Subsets of S, (4) a cost
    # associated with each subset, and (4) a lower bounding function (LB).
    print('running ExactUCP')


#ExactUCP(LB=LB1)
#ExactUCP(LB=LB2)


""" As required in the prompt; the following is a 
    function for debugging, followed by the command 
    at the end of main.py """

def testdebug():
    # debug function to run all parts of code for self-check at end.
    print('running testdebug')


if __name__ == '__main__':
    testdebug()
