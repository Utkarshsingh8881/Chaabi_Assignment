# Q5. Common, Not Common
# Given 2 lists in input. Write a program to return the elements, which are common to both
# lists(set intersection) and those which are not common(set symmetric difference) between the
# lists.
# Input:
# Mainstream = ["One Punch Man","Attack On Titan","One Piece","Sword
# Art Online","Bleach","Dragon Ball Z","One Piece"]
# must_watch = ["Full Metal Alchemist","Code Geass","Death
# Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack
# On Titan"]
# f(mainstream, must_watch) should return:
# ["One Piece", "Attack On Titan"], ["Dragon Ball Z", "Death Note",
# "One Punch Man", "Stein's Gate", "The Devil is a Part Timer!", "Sword
# Art Online","Full Metal Alchemist","'Bleach", "Code Geass"]


l1 = ["One Punch Man", "Attack On Titan", "One Piece", "Sword Art Online", "Bleach", "Dragon Ball Z", "One Piece"]
l2 = ["Full Metal Alchemist", "Code Geass", "Death Note","Stein's Gate", "The Devil is a Part Timer!", "One Piece", "Attack On Titan"]
complete_list = l1 + l2
common = []
non_common = []

for i in complete_list:
    if i in l1 and i in l2:
        if i not in common:
            common.append(i)
    else:
        if i not in non_common:
            non_common.append(i)

print(common)
print(non_common)
