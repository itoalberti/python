# ARITHMETIC ARRANGER - FREECODECAMP
# TASK:
# Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side.
# The function should optionally take a second argument.
# When the second argument is set to True, the answers should be displayed.
# The function will return the correct conversion if the supplied problems are properly formatted,
# otherwise, it will return a string that describes an error that is meaningful to the user.

# Situations that will return an error:

# 1 OK) If there are too many problems supplied to the function. The limit is five
# ERROR MESSAGE: Error: Too many problems.

# 2 OK) The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error.
# Other operators not mentioned in this bullet point will not need to be tested.
# ERROR MESSAGE: Error: Operator must be '+' or '-'.

# 3 OK) Each number (operand) should only contain digits.
# ERROR MESSAGE: Error: Numbers must only contain digits.

# 4 OK) Each operand (aka number on each side of the operator) has a max of four digits in width. 
# ERROR MESSAGE: Error: Numbers cannot be more than four digits.

# If the user supplied the correct format of problems, the conversion you return will follow these rules:
# 1) There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).

# 2) Numbers should be right-aligned.

# 3) There should be four spaces between each problem.

# 4) There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually.
# (The example above shows what this should look like.)

# DEVELOPMENT
# Write your code in arithmetic_arranger.py. For development, you can use main.py to test your arithmetic_arranger() function. Click the "run" button and main.py will run.

# TESTING
# The unit tests for this project are in test_module.py. We are running the tests from test_module.py in main.py for your convenience. The tests will run automatically whenever you hit the "run" button. Alternatively you may run the tests by inputting pytest in the console.
# from macpath import split
from ctypes import sizeof
import re
import string

#exp = matrix to input the mathematical expressions

def arithmetic_arranger(exp):
    # n1, n2 and op are, respectively, the 1st number, the 2nd number and the mathematical operation from the expressions in exp
    n1=[]
    op=[]
    n2=[]
    # dashes = matrix to input the dashes above the calculation result 
    dashes=[]
    # res = matrix with the results of the mathematical operations
    res=[]
    # arranged_exp=[]

    if len(exp)>5:
        return "Error: Too many problems."
    # 'for' function to scan through the lines of exp:
    for i in range(0, len(exp)):
        separation_dummy=exp[i].split(' ')
        # assembly of arrays n1, n2, op and dashes
        n1.append(separation_dummy[0])
        op.append(separation_dummy[1])
        n2.append(separation_dummy[2])
        if len(n1[i])>4 or len(n2[i])>4:
            return "Error: Numbers cannot be more than four digits."
        dashes.append("-"*(2+max(len(n1[i]), len(n2[i]))))

        if n1[i].isdigit()==False or n2[i].isdigit()==False:
            return "Error: Numbers must only contain digits."
        if op[i]=="*" or op[i]=="/":    
            return "Error: Operator must be '+' or '-'."
        if op[i]=="+":
            operation=int(n1[i])+int(n2[i])
        elif op[i]=="-":
            operation=int(n1[i])-int(n2[i])
        res.append(operation)
    # print("n1 = ", n1)
    # print("n2 = ", n2)
    # print("op = ", op)
    # print("res = ", res)
    line1=''
    line2=''
    line3=''
    line4=''
    for i in range(0, len(exp)):
        # line1+=str((n1[i].rjust(8)))
        # line2+=str((op[i]+' '+n2[i]).rjust(8))
        # line3+=str(dashes[i].rjust(8))
        # line4+=str(str(res[i]).rjust(8))
        line1+=str(n1[i].rjust(3+max(len(str(n1[i])), len(str(n2[i])), len(dashes[i]), len(str(res[i])))))
        line2+=str(op[i]+' '+n2[i]).rjust(3+max(len(str(n1[i])), len(str(n2[i])), len(dashes[i]), len(str(res[i]))))
        line3+=str(dashes[i].rjust(3+max(len(str(n1[i])), len(str(n2[i])), len(dashes[i]), len(str(res[i])))))
        line4+=str(res[i]).rjust(3+max(len(str(n1[i])), len(str(n2[i])), len(dashes[i]), len(str(res[i]))))
   
    # arranged_exp = strin with the whole expression arranged
    arranged_exp=line1+'\n'+line2+'\n'+line3+'\n'+line4 
    return arranged_exp

print(arithmetic_arranger(["3209 + 668", "3801 - 2", "45 + 43", "1343 + 49", "999 - 12"]))