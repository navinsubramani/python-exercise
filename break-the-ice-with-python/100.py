'''You are given words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

If the following string is given as input to the program:

4
bcdef
abcdefg
bcde
bcdef
Then, the output of the program should be:

3
2 1 1'''

N = int(input("Enter the number of words that you would like to input (N): "))
li_words = []
for i in range(N):
    li_words.append(input())

print("Output:")

li_count = {}
for i in li_words:
    li_count[i] = li_words.count(i)

print(len(li_count.keys()))
for i in li_count.keys():
    print(str(li_count[i]), end=" ")