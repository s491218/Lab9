print "What is your temperture?"
userTemp = int(raw_input())
if userTemp > 105:
    print "You need to see a doctor!"
if (userTemp > 99 and userTemp <105):
    if userTemp < 100:
        print "You should be fine"
    print "How many hours have you been sick?"
    userSick = int(raw_input())
    if userSick > 23:
        print "You need to see a doctor!"

