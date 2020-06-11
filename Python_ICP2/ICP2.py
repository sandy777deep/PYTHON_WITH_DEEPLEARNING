"""
Weights_list = []
Number_students = int(input('please enter number of students'))
# print('Enter the Weights')

# Using LOOPS
for i in range(Number_students):
    pounds = (float(input('Enter weight in Pounds(Lbs) to Convert into Kilograms:')))
    kilo_grams = round(pounds * 0.453592,2)
    Weights_list.append(kilo_grams)

print(Weights_list)
"""

list_str = input("Enter list of weights in pounds separated by \"comma\": ")

pounds = list_str.split(",")

# Using LIST-comprehensions

kgs = [str(round(int(pound)/2.205 , 2) ) for pound in pounds]

print(','.join(kgs))