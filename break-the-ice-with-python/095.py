# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

# If the following string is given as input to the program:
# 5
# 2 3 6 6 5
# Then, the output of the program should be:
# 5

li_scores = input("Enter the scores with space seperator: ").split(" ")
li_scores = [int(i) for i in li_scores]
li_scores.sort()
li_scores_nodup = []

for i in li_scores:
    if i in li_scores_nodup:
        continue
    li_scores_nodup.append(i)

First_HighScore = li_scores_nodup.pop()
Second_HighScore = li_scores_nodup.pop()

print(Second_HighScore)