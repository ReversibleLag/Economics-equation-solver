# Written by Kai South 2021

def total_revenue_solver():
    price = []
    quantity = []
    total_revenue = []
    marginal_revenue = []
    print('\n------------------Total Revenue Solver------------------')
    row_amount = int(input('Please enter the row amount in the table: '))
    for x in range(row_amount):
        print('Row', x, 'Column 1')
        price_amount = int(input('Please enter the price on row: '))
        price.append(price_amount)
    for t in range(row_amount):
        print('Row', t, 'Column 2')
        quantity_amount = int(input('Please enter the quantity on row: '))
        quantity.append(quantity_amount)
    for r in range(row_amount):
        total_revenue.append(price[r] * quantity[r])
        try:
            marginal_revenue.append(int((total_revenue[r] - total_revenue[r - 1]) / ((quantity[r]) - quantity[r - 1])))
        except Exception:
            marginal_revenue.append(0)

    print('\n\|/ Your finished Table below \|/\n')
    print('Price, Quantity, Total Revenue, Marginal Revenue')
    for u in range(row_amount):
        print(price[u], '\t\t', quantity[u], '\t\t\t\t', total_revenue[u], '\t\t\t', marginal_revenue[u])

    print('\n1 - Enter new data?')
    print('2 - Return to menu')

    try:
        option = int(input('Enter your choice: '))
    except Exception as e:
        print('Invalid response returning to menu!')
        return
    if option == 1:
        total_revenue_solver()
    elif option == 2:
        print('\n\n')
        return


def intro():
    option = ''
    print('Welcome to the Economics equation solver!')
    print('\nWhat would you like to do?')
    print('1 - Total Revenue and Marginal Revenue Solver')
    # print('2 - Marginal Revenue')
    print('9 - Quit')
    try:
        option = int(input('Enter choice: '))
    except Exception as e:
        print('Invalid response returning to menu!')
        intro()
    return option


def main():
    option = intro()
    while option != 9:
        if option == 1:
            total_revenue_solver()
        else:
            pass
        option = intro()
    print('Goodbye!')


main()
