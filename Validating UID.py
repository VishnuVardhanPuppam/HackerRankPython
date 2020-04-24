ABCXYZ company has up to  employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least  uppercase English alphabet characters.
It must contain at least  digits ( - ).
It should only contain alphanumeric characters ( - ,  -  &  - ).
No character should repeat.
There must be exactly  characters in a valid UID.
Input Format

The first line contains an integer , the number of test cases.
The next  lines contains an employee's UID.

Output Format

For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

Sample Input

2
B1CD102354
B1CDEF2354
Sample Output

Invalid
Valid
Explanation

B1CD102354:  is repeating → Invalid
B1CDEF2354: Valid

Solution :

# Enter your code here. Read input from STDIN. Print output to STDOUT

def UIDValidation(UID):
    #UID = "B1CD102354"
    U = 0;
    D = 0
    '''if len(UID) != 10:
        print("Invalid")
    else:'''
    for i in range(len(UID)):
        if UID[i].isupper():
            U += 1
        elif UID[i].isdigit():
            D += 1

    if U >= 2 and D >=3 and UID.isalnum() and len(set(UID)) == len(UID) and len(UID) == 10:
        print("Valid")
    else:
        print("Invalid")
NoOfStudents = int(input())
UIDList = []
for i in range(NoOfStudents):
    UID = input()
    UIDValidation(UID)



