def convert_to_seconds(hours):
    return hours*3600

def sum_of_three(a, b, c):
    return a+b+c

def is_greater_than_five(n):
    return n>5

def meters_to_centimeters(meters):
    return meters*100

def is_multiple_of_ten(n):
    return n%10 == 0


def convert_to_titlecase(s):
    result = ""
    capitalize_next = True  # Capitalize the first letter and letters after spaces

    for letter in s:
        if capitalize_next and letter.isalpha():
            result += letter.upper()
            capitalize_next = False
        else:
            result += letter
        if letter == " ":
            capitalize_next = True

    return result
