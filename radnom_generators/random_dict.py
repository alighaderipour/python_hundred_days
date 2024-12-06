import random


def generate_random_data(size):
    """Generate a specified number of random Persian names and random integers."""

    # List of Persian names
    persian_names = [
        "Ali",
        "Reza",
        "Maryam",
        "Koroush",
        "Narges",
        "Fatemeh",
        "Sara",
        "Amir",
        "Mohammad",
        "Aryian",
        "Nima",
        "Zahra",
        "Shirin",
        "Arash",
        "Bahar",
    ]

    # Ensure the size does not exceed the available names
    if size > len(persian_names):
        raise ValueError(f"Maximum size is {len(persian_names)}.")

    # Randomly select names and generate integers
    selected_names = random.sample(persian_names, size)
    random_integers = [random.randint(1, 100) for _ in range(size)]

    return selected_names, random_integers


def create_name_value_dict(names, integers):
    """Create a dictionary from names and integers."""
    return {names[i]: integers[i] for i in range(len(names))}


# Main function to generate and return the data
def gen_dict(size):
    names, integers = generate_random_data(size)
    result = create_name_value_dict(names, integers)
    return result


# Example usage: Change the size parameter to the desired size
print(gen_dict(7))  # Generates a dictionary with 7 key-value pairs
