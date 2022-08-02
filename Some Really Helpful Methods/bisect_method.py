#printing grades for the numbers earned, according to the pre-defined grades

# biscet.left(Does the operation from left) is similar to biscet.right (Does the operation from right)

import bisect
def get_grade(score,cutoff=[50,60,70,80,90],grades='FEDCBA'):
    item=bisect.bisect_right(cutoff,score)
    return grades[item]

grades=[get_grade(score) for score in [44,57,90,67,82,77,100]]
print(grades)