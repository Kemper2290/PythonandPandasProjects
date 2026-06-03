

print("Welcome to the Daily Expense Tracker!\n")

menu_opt = [1,2,3,4,5]

print('Menu:')
print('1. Add a new expense')
print('2. View all expenses')
print('3. Calculate total and average expense')
print('4. Clear all expenses')
print('5. Exit')
expense = []
while True:
    user_input = input('Please input menu option:')

    if user_input == '5':
        print('Exiting the Daily Expense Tracker. Goodbye!')
        break
    elif user_input =='1':
        insrt = float(input("Input new expense amount:"))
        expense.append(insrt)
        print('Expense added successfully!')
    elif user_input == '2':
        if len(expense) == 0:
            print('No expenses recorded yet.')
        else:
            print('Your expenses:')
            for index,num in enumerate(expense):
                print(f'{index+1}.',num)
    elif user_input == '3':
        if len(expense) == 0:
            print('No expenses recorded yet.')
        else:
            total_expense = sum(expense)
            avg_expense = total_expense/len(expense)
            print(f'Total expense: {total_expense}')
            print(f'Average expense: {avg_expense}')

    elif user_input == '4':
        expense.clear()
        print('All expenses cleared.')

    elif user_input not in menu_opt:
        print('Invalid choice. Please try again.')


