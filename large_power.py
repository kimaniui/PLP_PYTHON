def large_power(base, exponent):
    # Calculate the result of base to the power of exponent
    result = base ** exponent
    
    # Use an if statement to test if the result is greater than 5000
    if result > 5000:
        return True
    else:
        return False

# Example usage:
print(large_power(10, 3))  # Output will be True
