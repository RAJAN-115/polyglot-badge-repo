#!/usr/bin/env python3
"""Simple Python Hello World program"""

def main():
    print('Hello, World!')
    
    # Function to greet a user
    def greet_user(name):
        return f"Hello, {name}! Welcome to the polyglot repository."
    
    # Example usage
    user_name = "GitHub User"
    print(greet_user(user_name))
    
    # Simple math operation
    def add(a, b):
        return a + b
    
    print(f"5 + 3 = {add(5, 3)}")
    
    # List comprehension example
    squares = [x**2 for x in range(1, 6)]
    print(f"Squares of 1-5: {squares}")

if __name__ == "__main__":
    main()
