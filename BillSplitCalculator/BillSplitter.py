


print('Bill Split Calculator\n')

#inputs
print("Input the bill amount")
bill_amount = float(input())
print("Input the tip percentage you want")
tip_percent=float(input())
print("Input the number of people splitting the bill")
num_people = int(input())


tip_amount = ((tip_percent/100)*bill_amount)
print(f'tip amount based of given tip percentage: {tip_amount}')

bill_total = bill_amount + tip_amount
bill_total_per_person = bill_total/num_people
print(f'the bill total is: {bill_total}')
print(f'the bill total per person is: {bill_total_per_person}')

#print(bill_total)
#print(bill_total_per_person)

