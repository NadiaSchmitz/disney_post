# Donald Duck works as a postman for the Walt Disney Studios. He delivers children’s
# letters from all over the world to his friends, which are cartoon characters.
# The Studios has three cases for the letters, with nine sections in each case.
# Every section has the name of the receiver on it. All cases stand in a row
# as it is shown at the picture below.

# Donald Duck have brought n letters today. Initially, he stands near the leftmost case.
# He has to make one step to go to the neighboring case or to the previous one.
# How many steps will he make until he puts all the letters into the respective sections,
# if he does this in the order they are in his bag?

#         Safe 1                    Safe 2                      Safe 3
# Alice   Ariel  Aurora     Bambi   Belle   Bolt        Dumbo   Genie   Jiminy
# Phil    Peter  Olaf       Mulan   Mowgli  Mickey      Kuzko   Kida    Kenai
# Phoebus Ralf   Robin      Silver  Simba   Stitch      Tarzan  Tiana   Winnie

# Input
# The first line contains an integer n that is the amount of letters in Donald’s bag (1 ≤ n ≤ 1 000).
# The following n lines contain receivers of the letters in the order they are in the bag.

# Output
# Output the number of steps Donald should make to put all the letters into the cases.


from random import randint
from math import fabs

safe_1 = ["Alice", "Ariel", "Aurora", "Phil", "Peter", "Olaf", "Phoebus", "Ralf", "Robin"]
safe_2 = ["Bambi", "Belle", "Bolt", "Mulan", "Mowgli", "Mickey", "Silver", "Simba", "Stitch"]
safe_3 = ["Dumbo", "Genie", "Jiminy", "Kuzko", "Kida", "Kenai", "Tarzan", "Tiana", "Winnie"]
room = safe_1 + safe_2 + safe_3
safe_number = []
check = 0

while check == 0:
    n = int(input("Enter a number of Letters: "))
    i = 0
    post = []
    safe = 0
    position = 1
    step = 0
    while i < n:
        index = randint(0, 26)
        post.append(room[index])
        s1 = 0
        s2 = 0
        s3 = 0
        while s1 < len(safe_1):
            if post[i] == safe_1[s1]:
                safe = 1
                safe_number.append(safe)
            s1 += 1
        while s2 < len(safe_2):
            if post[i] == safe_2[s2]:
                safe = 2
                safe_number.append(safe)
            s2 += 1
        while s3 < len(safe_3):
            if post[i] == safe_3[s3]:
                safe = 3
                safe_number.append(safe)
            s3 += 1
        print("Safe: ", safe)
        if i == 0:
            step = safe_number[0] - 1
        else:
            step = step + fabs(safe_number[i] - safe_number[i - 1])
        i += 1
    if n < 1:
        print("Wrong number.")
    else:
        check = 1

print("Donald received letters for: ", post)
print("Steps: ", step)
