def divisible_by_ten(num):
    # Calculate the remainder of num divided by 10
    remainder = num % 10
    
    # Use an if statement to check if the remainder is 0
    if remainder == 0:
        return True
    else:
        return False

# Example usage:
print(divisible_by_ten(20))  # Output will be True
