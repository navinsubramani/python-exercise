'''You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------'''

while True:
    N = int(input("Enter the size of rangoli: "))
    if N > 26 or N <= 0:
        print("Wrong Input. Please enter a number between 1 and 26...")
        continue
    break

alphabets = 'abcdefghijklmnopqrstuvwxyz'
ROWS = N*2 - 1
COLUMNS = (N*2 - 1)*2 - 1
COLUMN_MID = int(COLUMNS//2)
ROW_MID = int(ROWS//2)
FILLERS = '-'
# print(N, ROWS, COLUMNS)

rangoli = []

# Create top half rows
for i in range(1, (ROWS//2)+(ROWS%2)+1):
    Template_ROW = list(COLUMNS*FILLERS)
    for j in range(1, i+1):
        Template_ROW[COLUMN_MID-(j-1)*2] = alphabets[N - (i+1) + j]
        Template_ROW[COLUMN_MID+(j-1)*2] = alphabets[N - (i+1) + j]
    rangoli.append("".join(Template_ROW))

# Create bottom half rows
for i in range(ROW_MID):
    rangoli.append(rangoli[ROW_MID-(i+1)])

# Display rangoli
for i in rangoli:
    print(i)
    
        

