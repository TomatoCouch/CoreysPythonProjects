#Will C.
#Python 1
#Final Project, Standard 2.01

import datetime

#Standard 2.01: Sequence Indexes
#ok so basically
counter=0
listAgain=["this is the ",3,"rd list I've made today (",datetime.date(2022,5,27),")"]
for item in listAgain:
    print(listAgain[counter],end="")
    counter+=1
listEntryOne=listAgain[0]
listEntryThree=listAgain[2]
print()
print(listEntryThree[18:23],listEntryOne[5:7],listAgain[3])
bigString="the quick brown fox jumps over the lazy dog"
#now's time for some counting
print(bigString[-7]+bigString[10]+bigString[7]+bigString[-3]+bigString[2]+bigString[16]+bigString[-1]+bigString[1]+bigString[6]+bigString[20]+bigString[8]+bigString[-8]+bigString[22]+bigString[14]+bigString[12]+bigString[23]+bigString[4]+bigString[11]+bigString[24]+bigString[0]+bigString[5]+bigString[-16]+bigString[13]+bigString[18]+bigString[-5]+bigString[-6])
#                a             b            c             d            e             f             g            h            i             j            k             l             m             n             o             p            q             r             s            t            u              v             w             x             y             z
