'''You are given a string.Your task is to count the frequency of letters of the string and print the letters in descending order of frequency.

If the following string is given as input to the program:

aabbbccde
Then, the output of the program should be:

b 3
a 2
c 2
d 1
e 1'''

input_string = input("Enter the string input: ")

count = {}

for i in input_string:
    if i not in count.keys():
        count[i] = input_string.count(i)

li_count = []
for i in count.keys():
    li_count.append((count[i], i))

li_count.sort(reverse=True)
print(li_count)