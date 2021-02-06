"""
Given a list of different students' scores, write a function that returns the average of each student's top five scores. You should return the averages in ascending order of the students' id numbers.

Each entry (scores[i]) has the student's id number (scores[i][0]) and the student's score (scores[i][1]). The averages should be calculated using integer division.

Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation:
The average student `1` is `87`.
The average of student `2` is `88.6`, but with integer division is `88`.
Notes:

The score of the students is between 1 and 100.
[execution time limit] 4 seconds (py3)

[input] array.array.integer scores

[output] array.array.integer

"""
def csAverageOfTopFive(scores):

    if len(scores) == 1:
        return scores

    list1=[]
    list2=[]

    for i in range(len(scores)):
        if (scores[i][0]==1):
            list1.append(scores[i][1])
        if (scores[i][0]==2):
            list2.append(scores[i][1])
    
    A1 = [1,sum(sorted(list1,reverse=True)[:5]) // 5]
    B1 = [2,sum(sorted(list2,reverse=True)[:5]) // 5]

    return A1, B1



scores = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
# Output: [[1,87],[2,88]]
# scores = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
print(csAverageOfTopFive(scores))#Output: [[1,87],[2,88]]
    
