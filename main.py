#!/usr/bin/env python3
"""
# could make chmod a+x [main].py
# cp main.py Wullen_UCP chmod +x Wullen_UCP could be developed for more intricate executable
"""
#from pyeda.inter import *  # shouldnt be needed anymore; kept in for development possibility
import os
import numpy as np
"""Importing OS for file-checking"""
"""Importing numpy for matrix operations"""
# print(os.path.basename(__file__))  # self check of file executable name

def set_s_input(prompt):
    """ set_s_input takes the user input of an integer N, denoting the
         size of set S, for which the set will be constructed from
         1 to N.
         This integer N corresponds to the number of rows in the Matrix to
         be generated for UCP, and also represents the minterms."""
    S = []  # empty list to build set S
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
                S.append(i)
                i += 1  # increment i until i == N
                if i == correct_input:
                    with open('input_file.txt', 'a') as f:
                        #f.write(str(np.array(S)))
                        f.write(str(S))
                        f.write('\n')  # separation to distinguish input types
                        print(np.array(S))
                        f.close()
                    return S


setS = set_s_input("Please input an integer denoting N, the size of set S.\n")


def subset_s_input(prompt):
    """ subset_s_input takes the user input for the sets which are subsets of S.
        This input will correspond to the onset values of each row, corresponding
        to the prime implicants.
        The number of subsets generated will also correspond to the  number of
        columns for the Matrix to be generated for UCP."""
    S = []
    while True:
        try:
            correct_input = input(prompt)
            with open('input_file.txt', 'r') as f:
                data = [line.strip() for line in f]
#                print("Recall, the set S input is: ", dataset, "\n")
#                if not set(correct_input).issubset(set(data)):
#                    raise ValueError
        except ValueError:
            print("Error; Set values should be corresponding to the subset of S "
                  "already input.\n Please try again.")
        else:
            if correct_input == 'done':
                return
            with open('input_file.txt', 'a') as nf:
                S.append(correct_input)
                #indexed_subS = exprvar(correct_input)
                #nf.write(str(indexed_subS) + ',')
                nf.write(str(S))
                nf.write(';')  # for separation after each subset
                subset_s_input(prompt)
            nf.close()
            #return correct_input
            return S


subsetS = subset_s_input("\nPlease input each subset one at a time in the form: \n"
                         "1,3, 2,3,4, 1,5, etc. (Comma separated set-subset relations)\n"
                         "Once done, type 'done' to move to cost assignment.\n\n")

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


subCost = sub_cost_input("\nPlease input the cost of each subset in the form:\n "
                         "1, 2, etc. (in order). This will be connected to the subsets "
                         "previously input.\n Please use form of space delimiters as shown.\n ")

""" The following are two Lower-Bound functions to be used in ExactUCP"""
# Some options we can use are:
# Maximum Independent Set (MIS)
# Linear Programming Relaxation (LPR)
# Cutting Planes (CP)

def low_bound_mis(matrix):
    """ low_bound_mis is a lower bound function utilizing the Maximum
        Independent Set (MIS).
        MIS of rows is defined as: A set of independent rows such that
        if another row is added to the set, it ceases to be an
        independent set.

        For this function we will utilize the minimized matrix to
        operate implicit enumeration on."""
    print('running lower bound function 1')

def low_bound_lpr(matrix):
    """ low_bound_lpr is a lower bound function to be used in ExactUCP
        that utilizes the Linear Programming Relaxation (LPR) method."""
    print('running lower bound function 2')


def ExactUCP(prompt):
    """ ExactUCP reads in the user decision of a lower bounding function to solve the
        exact unate covering problem.
        The inputs of setS, subsetS, and subCost from the input file are read out to
        generate the matrix which column/row dominance operations will solve UCP on. """
    while True:
        try:
            LB = input(prompt)
            if int(LB) < 1 or int(LB) > 2:
                raise ValueError
        except ValueError:
            print("Error; input was not 1 or 2 corresponding to LB functions. Please try again.")
        else:
            f = open('input_file.txt', 'r')  # input-file handling
            data = [line.strip() for line in f]  # input-file printout
           # print("The data gathered is ", data)  # self check
            #print(data[0])  # self check
            numCol = len(data[0].split(" "))
           # print("The number of columns is ", numCol)  # self check
            numRow = len(data[1].split(";")) - 1  # -1 is for offset of final ;
           # print("The number of rows is ", numRow)  # self check
            rowWeight = data[2].split(" ")
            a = []  # empty list to be created
            sliced_data0 = str(data[0])[1:-1]  # slice data0 for comparisons
            for i in set(data[1].split(";")[:-1]):
                for j in sorted(set(sliced_data0.split(", "))):
                   # print(i, j)   # self check
                    if not set(j).issubset(i):  # set(sorted(sliced_data0)).issubset(set(data[1][:-1])):
                        k = 0
                        a.append(k)
                    elif set(j).issubset(i):  # set(sorted(sliced_data0)).issubset(set(data[1][:-1]))
                        k = 1
                        a.append(k)
           # print(a)  # self check
            matrix = np.array(a).reshape(numRow, numCol)
            print("\nThe matrix generated from the inputs gathered is:\n")
            print(matrix, '\n')
            """Now we have our matrix and can move forward with row/column domination."""
            mat_copy = matrix
            row = np.vsplit(mat_copy, 1)
            col = np.hsplit(mat_copy, 1)
            splitsr = np.array_split(row, numCol)
            splitsc = np.array_split(col, numRow)
            #idx = list(classes).index(var)
            """ For defining the rows available to be deleted for minimization:
                Row_i dominates Row_j if Col(Row_i) contains Col(Row_j):
                can then delete Row_i (dominating row)"""
            #for row in matrix:  # utilize rowi and rowj for indicies
            rowi = data[1].split(";")
            rowj = data[1].split(";")
            for row in splitsr:
                #for rowi in splitsr:
                    #for rowj in splitsr:
                        while len(row) <= numRow:
                            #rowi += 1
                            if row[rowj] in row[rowi]:
                                del rowi
                            else:
                                rowj += 1
                                if row[rowj] in row[rowi]:
                                    del row
            print("After row dominance procedure: \n", matrix, '\n')

            """ For defining columns available to be deleted for minimization:
                Col_i dominated Col_j if Row(Col_i) contains Row(Col_j); and 
                if: Cost(Col_i) <= Cost(Col_j) --> del Col_j (dominated col)"""
            for col in matrix:
                for coli in splitsc:
                    for colj in splitsc:
                        while len(col) <= numCol:
                            coli += 1
                            if col[colj] in col[coli]:
                                if sum(coli) < sum(colj):
                                    del colj
                            else:
                                colj += 1
                                if col[colj] in col[coli]:
                                    if sum(coli) < sum(colj):
                                        del colj
            print("After column dominance procedure: \n", matrix, '\n')

            """ Now apply Implicit Enumeration through 
            Branch&Bound lower bounding funct."""
            if LB == 1:
                low_bound_mis(matrix)
            elif LB == 2:
                low_bound_lpr(matrix)


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
