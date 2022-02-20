from pyeda.inter import *
import os
# example
# x_0_1_2_3 = exprvar('x', (0, 1, 2 ,3))
# print(x_0_1_2_3)

"""Function/Global variable for setS"""
def set_s_input(prompt):
    """ set_s_input takes the user input of an integer N, denoting the
         size of set S, for which the set will be constructed from
         1 to N.
         This integer N corresponds to the number of rows in the Matrix to
         be generated for UCP, and also represents the minterms."""
    s = "s"     # stand-in for expvar variable assignment
    file_exists = os.path.exists('input_file.txt')
    if file_exists:
        with open('input_file.txt', 'w') as f:
            f.write("")  # clears previous test inputs
    else:
        open('input_file.txt', "x")  # creates new file titled input_file.txt
    while True:
        try:
            correct_input = int(input(prompt))  # take in user input
        except ValueError:
            print("Error; Input shall be int N denoting size of set S from 1 to N.")
            exit("Value Error")
        else:
            i = 0  # iterator
            print("The minterms in set S are as follows:")
            while i < int(correct_input):
                indexed_S = (exprvar(s, i))  # exprvar yields variable
                str_indexed_S = repr(indexed_S)  # file writing to txt requires str
                with open('input_file.txt', 'a') as f:
                    f.write(str_indexed_S + ',')
                    print(indexed_S)
                    i += 1  # increment i until i == N
                if i == correct_input:
                    with open('input_file.txt', 'a') as f:
                        f.write('\n')  # separation to distinguish input types
                        f.close()
                    return indexed_S


# Global variable set S from input function
setS = set_s_input("Please input an integer denoting N, the size of set S.\n")


"""Function/Global variable for subsetS"""
def subset_s_input(prompt):
    """ subset_s_input takes the user input for the sets which are subsets of S.
        This input will correspond to the onset values of each row, corresponding
        to the prime implicants.
        The number of subsets generated will also correspond to the  number of
        columns for the Matrix to be generated for UCP."""
    s = "s"  # stand in for consistency in sets and subsets
    while True:
        try:
            correct_input = input(prompt)
            with open('input_file.txt', 'r') as f:
                data = [line.strip() for line in f]
                dataset = set(data)
#                print("Recall, the set S input is: ", dataset, "\n")
#                if not set(correct_input).issubset(dataset):
#                    raise ValueError
        except ValueError:
            print("Error; Set values should be corresponding to the subset of S "
                  "already input.\n Please try again.")
        else:
            if correct_input == 'done':
                return
            with open('input_file.txt', 'a') as nf:
                indexed_subS = exprvar(correct_input)
                nf.write(str(indexed_subS) + ',')
                nf.write(' ')  # for separation after each subset
                subset_s_input(prompt)
            nf.close()
            return correct_input


# Global variable subset S from input function
subsetS = subset_s_input("\nPlease input variables from S to make a subset in form: "
                         "s[1],s[3], s[2],s[3],s[4], s[1],s[5], etc.\n"
                         "Once done, type 'done' to move to cost assignment.\n")

"""Function/Global variable for subCost"""
# input function for set S to be given by user
def sub_cost_input(prompt):
    """ sub_cost_input takes the user input for the cost of each subset as
        it is read from the input file.
        Generally the cost of the subsets will be the number of literals in
        the subset, however since the input arguments for subset_s_input
        and set_s_input don't  explicitly define the literals, we leave the
        input available to the user. """
    while True:
        try:
            correct_input = input(prompt)
        except ValueError:
            print("Error; Set values should be integers. Please try again.")
        else:
            with open('input_file.txt', 'a+') as f:  # input-file handling
                f.write('\n')  # for separation between subset and cost
                f.write(correct_input + ',')
                f.write("\n")
            f.close()
            return correct_input


# Global variable set S from input function
subCost = sub_cost_input("\nPlease input the cost of each subset in the form:\n "
                         "1, 2, etc. (in order). This will be connected to the subsets "
                         "previously input.\n")

""" The following are two Lower-Bound functions to be used in ExactUCP"""
# Some options we can use are:
# Maximum Independent Set (MIS)
# Linear Programming Relaxation (LPR)
# Cutting Planes (CP)

def low_bound_mis(setS, subsetS, subCost):
    """ low_bound_mis is a lower bound function utilizing the Maximum
        Independent Set (MIS).
        MIS of rows is defined as: A set of independent rows such that
        if another row is added to the set, it ceases to be an
        independent set."""
    print('running lower bound function 1')

def low_bound_2(setS, subsetS, subCost):
    """ lower bound function to be used in ExactUCP """
    print('running lower bound function 2')


"""The following the function definition for ExactUCP 
    utilizing the previous functions for obtaining the user inputs 
    for the specified function arguments"""


def ExactUCP(prompt):
    """ ExactUCP reads in the user decision of a lower bounding function to solve the
        exact unate covering problem.
        The inputs of setS, subsetS, and subCost from the input file are read out to
        generate the matrix which column/row dominance operations will solve UCP on. """
    print('running ExactUCP')
    while True:
        try:
            LB = input(prompt)
            if int(LB) < 1 or int(LB) > 2:
                raise ValueError
        except ValueError:
            print("Error; input was not 1 or 2 corresponding to LB functions. Please try again.")
        else:
            with open('input_file.txt', 'r') as f:  # input-file handling
                data = [line.strip() for line in f]  # input-file printout
                print(data)
                f.readline()
    # The inputs ExactUCP are (1) a SET Sof elements, (2) a SET of Subsets of S, (4) a cost
    # associated with each subset, and (4) a lower bounding function (LB).


ExactUCP("Please select a lower bounding function for ExactUCP to run on:\n"
         "1 = (MIS) Maximum Independent Set.\n"
         "2 = (LPR) Linear Programming Relaxation\n")

""" As required in the prompt; the following is a 
    function for debugging, followed by the command 
    at the end of main.py """
def testdebug():
    # debug function to run all parts of code for self-check at end.
    print('running testdebug')


if __name__ == '__main__':
    testdebug()
