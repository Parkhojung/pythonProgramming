tName = input("Enter name of team: ")
wCnt = int(input("Enter number of games won: "))
lCnt = int(input("Enter number of games lost: "))
res = wCnt/(wCnt+lCnt)
print("{0:s} won {1:.1%} of their games.".format(tName,res))