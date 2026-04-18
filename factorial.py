def factorial(n):
    """
    Calculate the factorial of a number.
    Factorial of n (n!) = n × (n-1) × (n-2) × ... × 1
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Calculate factorial recursively
    return n * factorial(n - 1)


def factorial_iterative(n):
    """
    Calculate the factorial of a number using iteration.
    This approach is more efficient for large numbers.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    
    return result


# Main program
if __name__ == "__main__":
    print("=== Factorial Calculator ===\n")
    
    try:
        # Get user input
        num = int(input("Enter a non-negative integer: "))
        
        # Calculate factorial using iterative method (more efficient)
        result = factorial_iterative(num)
        
        print(f"\nFactorial of {num} is: {result}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
