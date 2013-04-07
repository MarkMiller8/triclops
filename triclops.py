# Triclops, a quantitative prediction model for future household economic security

import math

initialOilPrice = 100.
oilprice = initialOilPrice
decadalOilPriceRate = 5.

initialWeeklyFoodPrice = 150.
#weeklyFoodPrice = initialWeeklyFoodPrice
oilFractionOfFoodCost = 0.07
nonOilFoodCosts = (1-oilFractionOfFoodCost)*initialWeeklyFoodPrice
oilComponentOfFoodCosts = oilFractionOfFoodCost*initialWeeklyFoodPrice
weeklyFoodPrice = nonOilFoodCosts + oilComponentOfFoodCosts


initialHouseholdIncome = 50000.
householdIncome = initialHouseholdIncome
finalHouseholdIncome = 50000.

automationRate = 0.01 # change in the unemployment rate per annum (dU/dt)

populationArray = []
populationSize = 101

initialUnemploymentRate = 0.08
unemploymentRate = initialUnemploymentRate

for i in xrange(0,populationSize):
	populationArray.append([i + 1]) # each individual member of the population gets  an integer 
	if i < unemploymentRate * 100:  # currently set for array of 100 members.  rewrite logic for other population sizes.
		populationArray[i].append(-1)	
	else:
		populationArray[i].append(1)

	if populationArray[i][1] == 1:
		populationArray[i].append(householdIncome)
	else:
		populationArray[i].append(0)
	
print populationArray

numberOfYears = 10
hoursInYear = 365*24
hoursInDecade = 10*hoursInYear
daysInYear = 365
daysInDecade = 365*10
weeksInMonth = 4.1
monthsInYear = 12
modelHour = 0
modelDay = 0


file = open("triclops.txt", "wb")

def writeToFile(file):
	file.write(str(month + 1))
	file.write(' ')
	file.write(str(oilprice))
	file.write(' ')
	file.write(str(weeklyFoodPrice))
	file.write(' ')
	file.write(str(foodFractionOfIncome))
	file.write("\n")


for month in range(0,numberOfYears*12):
	for day in range(0,30):
		
		modelDay = modelDay + 1
		
		unemploymentRate = automationRate/daysInYear*modelDay + initialUnemploymentRate
		
		for hour in range(0,24):
			modelHour = modelHour + 1
			oilprice = (decadalOilPriceRate*initialOilPrice - initialOilPrice)/(numberOfYears*hoursInYear - 0)*modelHour + initialOilPrice
		
	oilComponentOfFoodPrice = oilFractionOfFoodCost*oilprice/initialOilPrice*initialWeeklyFoodPrice		
	weeklyFoodPrice = nonOilFoodCosts + oilComponentOfFoodPrice
	#print "{}, {}".format(month + 1, weeklyFoodPrice)
	
		#weeklyFoodPrice = decadalOilPriceRate/daysInDecade*modelDay + initialWeeklyFoodPrice

		#weeklyFoodPrice = weeklyFoodPrice + oilFractionOfFoodCost*(decadalOilPriceRate*initialOilPrice - initialOilPrice)/(numberOfYears*hoursInYear - 0)*modelHour

	finalHouseholdIncome = (-1)*automationRate*(numberOfYears*12) + initialHouseholdIncome

	print "{}, {}".format(month + 1, unemploymentRate)

	householdIncome = initialHouseholdIncome + (finalHouseholdIncome - initialHouseholdIncome)/(numberOfYears*12)*month	

	foodFractionOfIncome = (weeklyFoodPrice*weeksInMonth)/(householdIncome/monthsInYear)
	
	writeToFile(file)

file.close()
					 
