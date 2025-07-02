def fibonacci(number_of_terms):
    if number_of_terms == 1:
        return 0
    elif number_of_terms  == 2:
        return 1
    else:
        return fibonacci(number_of_terms - 1) + fibonacci(number_of_terms - 2)

def print_fibonacci_series(number_of_terms):
    for i in range(1, number_of_terms + 1):
        print(fibonacci(i), end=' ')

number_of_terms = 10
print_fibonacci_series(number_of_terms)