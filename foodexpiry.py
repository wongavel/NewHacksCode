import csv
import time
import sys

expiryDates = {}
with open('food-and-expiry-dates.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
                expiryDates[row[0]] = row[1]
fruitInput = input("enter fruit: ")
timeToExpiry = expiryDates[fruitInput]

print("Your %s will expire in %d day(s)" %(fruitInput, int(timeToExpiry)))

for countdown in range(int(timeToExpiry),0,-1):
	time.sleep(1)
	if (countdown%2 == 0):
		print("%d days(s) to expiry" % countdown)

print("Your %s is expired." % fruitInput)

