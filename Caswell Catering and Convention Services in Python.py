import random
#defining constants
costForDeluxeMeal = 25.95
costForStandardMeal = 21.75
hallAPrice = 1000
hallBPrice = 850
hallCPrice = 750
weekendSurchargepercentage = 10
discountIfBillLessThan1000 = 2
discountIfBillLessThan2000 = 4
discountIfBillLessThan2000 = 5
discountIfBillMoreThan2000 = 7
gratuity = 20
weekendSurcharge = 10
salesTax = 6.875
#function to calculate ammounts
def CalculateBill(numberOfAdults,numberOfChildren, adultMealType, hallType, isItWeekend, speedyPayment, DepositAmount):
    if adultMealType==1:
        totalCostForAdultMeals = numberOfAdults*costForDeluxeMeal
        totalCostForChildMeals = numberOfChildren*(costForDeluxeMeal/2)
    else:
        totalCostForAdultMeals = numberOfAdults*costForStandardMeal
        totalCostForChildMeals = numberOfChildren*(costForStandardMeal/2)
    
    totalFoodCost = totalCostForAdultMeals + totalCostForChildMeals
    gratuityAmount = round(((gratuity/100)*totalFoodCost),2)

    if hallType.upper() == "A":
        hallName = "Hall A Room Fee" 
        hallFee = hallAPrice
    elif hallType.upper() == "B":
        hallName = "Hall B Room Fee" 
        hallFee = hallBPrice
    elif hallType.upper() == "C":
        hallName = "Hall C Room Fee" 
        hallFee = hallCPrice
    else:
        hallName = "Hall Fee"
        hallFee = 0
    if isItWeekend == "yes":
        weekendFee =  round(((weekendSurcharge/100)*totalFoodCost),2)
    else:
        weekendFee = 0
    Total = totalFoodCost + hallFee + weekendFee + gratuityAmount
    salesTaxonFood = round(((salesTax/100)*(Total-gratuityAmount)),2)
    subTotal = round((totalFoodCost + hallFee + weekendFee + gratuityAmount + salesTaxonFood),2)
    if speedyPayment == "yes":
        if subTotal<1000:
            discount = round(((2/100)*subTotal),2)
        elif subTotal<2000:
             discount = round(((4/100)*subTotal),2)
        elif subTotal<5000:
             discount = round(((5/100)*subTotal),2)
        elif subTotal>5000:
             discount = (7/100)*subTotal
    balance = round((subTotal - DepositAmount),2)

    if adultMealType == 1:
        mealType = "Deluxe "
        chargesPerMeal = costForDeluxeMeal
    else:
        mealType = "Standard "
        chargesPerMeal = costForStandardMeal

    return {"gratuity":gratuity, "mealType":mealType, "chargesPerMeal": chargesPerMeal, "numberOfAdults":numberOfAdults, "numberOfChildren":numberOfChildren,
     "totalCostForAdultMeals": totalCostForAdultMeals,
     "totalCostForChildMeals": totalCostForChildMeals,
    "totalFoodCost": totalFoodCost,"gratuityAmount": gratuityAmount,"hallName":
     hallName, "hallFee": hallFee,"weekendFee": weekendFee, "salesTaxOnFood":
      salesTaxonFood,"subTotal": subTotal, "discount": discount, "balance": balance}


def printReceipt(calculations):
    invoiceNumber = random.randint(100,999)
    print(""" /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-
    Caswell Catering and Convention Services
    """)
    print("     Final Bill           Invoice#",invoiceNumber)
    print("/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")    
    print("Number of adult:               ",calculations["numberOfAdults"])
    print("Number of children:            ",calculations["numberOfChildren"])
    print("gratuity :                     ", calculations["gratuity"],"%")
    
    print("cost per "+calculations["mealType"]+" for adult: ", calculations["chargesPerMeal"])
    print("cost per "+calculations["mealType"]+" for adult: ", calculations["chargesPerMeal"]/2)

    print("------------------------------------------")
    print("Total cost for adult meals:   $",calculations["totalCostForAdultMeals"])  
    print("Total cost for Child meals:   $",calculations["totalCostForChildMeals"])  
    print("\n")
    print("Total Food Cost:              $",calculations["totalFoodCost"])
    print("------------------------------------------")
    print("Gratuity:                     $",calculations["gratuityAmount"])
    if calculations["hallFee"]!=0:
        print(calculations["hallName"] ," Room Fee:     ",calculations["hallFee"])
    print("Weekend Charge:               $",calculations["weekendFee"])
    print("Taxes:                        $",calculations["salesTaxOnFood"])
    print("------------------------------------------")
    print("Subtoal:                      $",calculations['subTotal'])
    print("Less speedy Amount:           $",calculations["discount"])
    print("Balance Due:                  $",calculations["balance"])
    print("/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")    
    print("\t Thank you for using Caswell Catering  ")






def main():
    numberOfAdults = int(input("Enter number of Adults: "))
    numberOfChildren = int(input("Enter number of Children: "))
    adultMealType = input("Enter meal type Number:\n1. Deluxe Meal\n2. Standard Meal")
    hallType = input("Enter Hall by just Alphabet:\nA. Hall A\nB. Hall B\nC. Hall C\nH. Hall H(home)")
    isItWeekend = input("is it weekend(yes/no): ")
    if isItWeekend.lower()=="y" or isItWeekend.lower() == "yes":
        isItWeekend = "yes"
    else:
        isItWeekend = "no"
    speedyPayment = input("is it speedy payment(yes/no): ")
    if speedyPayment.lower()=="y" or speedyPayment.lower() == "yes":
        speedyPayment = "yes"
    else:
        speedyPayment = "no"
    DepositAmount = int(input("Enter deposit amount: "))
    
    printReceipt(CalculateBill(numberOfAdults,numberOfChildren, adultMealType, hallType, isItWeekend, speedyPayment, DepositAmount))
main()


