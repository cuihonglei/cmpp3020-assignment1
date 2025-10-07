# Lexical Analyzer / Parser for <average-problem>
# Using the following EBNF grammer:
# <average-problem> = "Given" <number-list> "," "calculate" "the" "average"
# <number-list> = "[" <numbers> "]"
# <numbers> = <number> { "," <number> }
# <number> = <digit> { <digit> }
# <digit> = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"

def tokenize_number_list(number_list_str):
    """
    Parses the <number-list> ::= "[" <numbers> "]"
    Returns a list of integers if valid.
    """
    number_list_str = number_list_str.strip()  # remove leading/trailing spaces

    # check brackets
    if not number_list_str.startswith("[") or not number_list_str.endswith("]"):
        raise ValueError("Invalid number list format! Must start with '[' and end with ']'")

    # extract content inside brackets
    content = number_list_str[1:-1].strip()

    # check empty list
    if content == "":
        raise ValueError("Number list cannot be empty")  

    numbers = []           # list to store parsed integers
    current_number = ""    # temporary string for building each number

    for char in content:
        if char.isdigit():
            current_number += char  # add digit to current number
        elif char == ",":
            if current_number == "":
                raise ValueError("Missing number between commas")
            numbers.append(int(current_number))  # append number to list
            current_number = ""  # reset for next number
        elif char == " ":
            continue  # ignore spaces
        else:
            raise ValueError(f"Invalid character in number list: '{char}'")  # invalid character

    # append last number if exists
    if current_number != "":
        numbers.append(int(current_number))  

    return numbers

def parse_average_problem(input_str):
    """
    Parses the <average-problem> input:
    "Given" <number-list> "," "calculate" "the" "average"
    Returns the list of numbers if valid.
    """
    input_str = input_str.strip()

    # Expected starting literal
    if not input_str.startswith("Given "):
        raise ValueError("Input must start with 'Given'.")

    # Remove "Given " from the start
    rest = input_str[len("Given "):].strip()

    # Find the closing bracket of the number list
    closing_bracket_index = rest.find("]")
    if closing_bracket_index == -1:
        raise ValueError("Missing closing bracket ']' for number list.")

    # Check that the character after ']' is a comma
    if len(rest) <= closing_bracket_index + 1 or rest[closing_bracket_index + 1] != ",":
        raise ValueError("Missing comma after number list.")

    # Extract number list substring and the remaining literal
    number_list_str = rest[:closing_bracket_index + 1].strip()
    after_comma = rest[closing_bracket_index + 2:].strip()  # skip the comma

    # Check the literal after the comma
    expected_literal = "calculate the average"
    if after_comma != expected_literal:
        raise ValueError(f"Expected '{expected_literal}' after comma.")

    # Tokenize the number list
    numbers = tokenize_number_list(number_list_str)
    return numbers

def calculate_average(numbers):
    """Calculates the arithmetic mean of a list of numbers."""
    return sum(numbers) / len(numbers)

def main():
    print("Average Calculator (<average-problem> parser)")
    print("Enter input in the format: Given [5, 8, 12], calculate the average")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter input: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            numbers = parse_average_problem(user_input)
            average = calculate_average(numbers)
            print(f"The average is: {average:.2f}\n")
        except ValueError as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()
