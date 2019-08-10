def convert_to_float(x):
    result = float(x)
    print(result)


try:
    x = input("Type a number: ")
    convert_to_float(x)
except ValueError:
    print("Invalid input: must be a number!")
