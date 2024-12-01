day= int(input("Enter the number of days"))
year = day//365
remdays = day%365
month = day//30
remdaysm = day%30
print("no of years in",day, "is",year, "and there is",remdays, "remaining days in the year")
print(month, "months in",day, "and",remdaysm, "days remaining in the month")