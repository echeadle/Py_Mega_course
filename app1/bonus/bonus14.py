from modules.parsers14 import parse
from modules.converters14 import convert

feet_inches = input("Enter feet and inches separated by a space: ")

parsed = parse(feet_inches)
result = convert(parsed["feet"], parsed["inches"])


print(f"{parsed['feet']} feet and {parsed['inches']} inches is {result} meters .")

if result < 1:
    print("Kid is too short.")
else:
    print("Kid is tall enough to use the slide.")
