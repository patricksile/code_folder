# Problem: Write Number In Expanded Form. (6kyu)
"""
You will be given a number and you will need to return it as a string in expanded
form.
Examples:
expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
"""

# My Solution:
def expanded(integer):
    

def expanded(integer):

    int_len = len(str(integer))  # Lenght of the initial integer.
    if int_len == 1:
        return str(integer)  # Returns integer in string (one unit integer here).
    counter = 1  # Counter to keep up with some tweaks.........
    expanded_form_str = ""
    while int_len >= 1:  # Looping while int_len is greater than 1.
        if int_len == 1:
            if integer == 0:  # Controlling the case of the last integer being 0.
                # Returning the expanded_form_str without concatenating 0.
                return expanded_form_str
            else:
                expanded_form_str += (" + " + str(integer))
                # Returning the expanded_form_str with the last integer (one digit > 0)
                return expanded_form_str
        pow_ten = 10 ** (int_len - 1)   # Ten to the power(1,3,6 etc..) at each step
        expanded_integer = (integer // pow_ten) * pow_ten   # Expanded integer
        if counter == 1:
            expanded_form_str += str(expanded_integer)  # Expanded integer in string form
            counter += 1    # From here this form of concatenation will not be repeated
        else:
            expanded_form_str += (" + " + str(expanded_integer))
        integer = integer % pow_ten  # New value of integer, previous integer erased in the loop.
        int_len = len(str(integer))  # New integer lenght


print expanded(70304)

# Other Solutions:


def expanded_form(n):
    result = []
    for a in range(len(str(n)) - 1, -1, -1):
        current = 10 ** a
        # divmod(n, current) returns the quotient to quo and the remainder to n
        quo, n = divmod(n, current)
        if quo:
            result.append(str(quo * current))
    return ' + '.join(result)
