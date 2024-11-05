import random

def generate_random_number(num_digits):
    """Generates a random number with the specified number of digits."""
    range_start = 10**(num_digits - 1)
    range_end = (10**num_digits) - 1
    return random.randint(range_start, range_end)

def generate_file(filename, num_lines):
    """Generates a file with random numbers."""
    with open(filename, 'w') as f:
        for _ in range(num_lines):
            num_digits = random.randint(10, 100)
            random_number = generate_random_number(num_digits)
            f.write(str(random_number) + '\n')

# Generate a file named 'random_numbers.txt' with 100,000 lines
generate_file('langdata/sgb.training_text', 100000)
