#to check if year is leap or not
year = int(input("enter the year "))
if year%4==0:
    print('%d is a leap year' % (year))
else:
    print("%d is not a leap year" % (year))
