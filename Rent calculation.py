# rent= int(input("enter your vasa vara="))
# kabar=int(input("mash a koto taka lage total kabar a = "))
# currentBill=int(input("koto tk current lage="))
# wifiBill=int(input("koto tk wifi bill lage ="))
# BuaBill=int(input("koto tk moila bill lage="))
# moilaBill=int(input("koto tk moila bill lage="))
# GasBill=int(input("gasbill mash a koto lage ="))
# person=int(input("basay koto jon thake total= "))
#
#
# output=(rent+kabar+BuaBill+moilaBill+GasBill)//person
# print("potek jone mash a eto tk lagve ",output)
# বাসার ভাড়া, খাবার, বিদ্যুৎ, ওয়াইফাই, বুয়া, ময়লা ও গ্যাস বিল ইনপুট নাও
rent = int(input("Enter your বাসা ভাড়া = "))
kabar = int(input("মাসে মোট খাবারের খরচ কত? = "))
currentBill = int(input("বিদ্যুৎ বিল কত লাগে? = "))
wifiBill = int(input("WiFi বিল কত লাগে? = "))
BuaBill = int(input("বুয়া বিল কত লাগে? = "))
moilaBill = int(input("ময়লা বিল কত লাগে? = "))
GasBill = int(input("গ্যাস বিল কত লাগে? = "))
person = int(input("বাসায় মোট কতজন থাকে? = "))

# মোট খরচ বের করো
total_cost = rent + kabar + currentBill + wifiBill + BuaBill + moilaBill + GasBill

# মাথাপিছু খরচ বের করো
per_person_cost = total_cost // person

print("\n===================================")
print("মাসিক খরচ per person :", per_person_cost, "টাকা")
print("===================================")
