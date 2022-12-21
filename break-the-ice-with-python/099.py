'''Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

Input

The first line of input contains an integer, M.The second line contains M space-separated integers.The third line contains an integer, N.The fourth line contains N space-separated integers.

4
2 4 5 9
4
2 4 11 12
Output

Output the symmetric difference integers in ascending order, one per line.

5
9
11
12'''

M = input("Enter the set of integers for M: ").split(" ")
N = input("Enter the set of integers for N: ").split(" ")

M = [int(x) for x in M]
N = [int(x) for x in N]

MN = list(set(M) ^ set(N))
MN.sort()

for i in MN:
    print(i)