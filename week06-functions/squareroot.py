def sqrt(n):
    x = 3
    approx = 0.5 * n

    for i in range(x):
        better_approx = 0.5*(approx + n/approx)
        approx = better_approx 
    print(f"The square root of {n} is approx. {better_approx}. ")

root_num = float(input("Please enter a positive number: "))
sqrt(root_num)