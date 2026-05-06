from operator import truediv


def format_name(f_name, l_name):
    """ take a first and last name and format
    it to  return the title case version of
     the name"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AMAN", "agrawal")
print(formatted_name)
length = len(formatted_name)


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

output = is_leap_year(2024)
print(output)
