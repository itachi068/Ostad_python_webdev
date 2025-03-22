def fibonacci_by_terms(n):
    """Generate Fibonacci series for a given number of terms."""
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

def fibonacci_by_max_value(max_value):
    """Generate Fibonacci series up to a given maximum value."""
    fib_series = []
    a, b = 0, 1
    while a <= max_value:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

def display_fibonacci(series):
    """Display the Fibonacci series """
    for i in range(len(series)):
        if i == len(series) - 1:  
            print(series[i], end="")
        else:
            print(series[i], end=", ")
    print()  


while True:
    print("\nChoose an option:")
    print("1. Generate Fibonacci series by number of terms")
    print("2. Generate Fibonacci series by maximum value")
    print("3. Exit")
    
    choice = int(input("\nEnter your choice: "))
    
    if choice == 1:
        terms = int(input("\nEnter the number of terms: "))
        series = fibonacci_by_terms(terms)
        print(f"\nFibonacci series ({terms} terms): ", end="")
        display_fibonacci(series)
    elif choice == 2:
        max_value = int(input("\nEnter the maximum value: "))
        series = fibonacci_by_max_value(max_value)
        print(f"\nFibonacci series (up to {max_value}): ", end="")
        display_fibonacci(series)
    elif choice == 3:
        print("\nGoodluck!")
        break
    else:
        print("\nInvalid choice! Please try again.")
