# 3.Capitals
# Using a dictionary comprehension, write a program that receives country names on the first line, separated by comma and space ", ", and their corresponding capital cities on the second line (again separated by comma and space ", "). Print each country with their capital on a separate line in the following format: "{country} -> {capital}".
#
# Input
# Bulgaria, Romania, Germany, England
# Sofia, Bucharest, Berlin, London
#
# Output
# Bulgaria -> Sofia
# Romania -> Bucharest
# Germany -> Berlin
# England -> London

def capitals():
    countries = input().split(", ")
    capitals_line = input().split(", ")

    result_dict = dict(zip(countries, capitals_line))

    for (country, capital) in result_dict.items():
        print(f"{country} -> {capital}")


capitals()
