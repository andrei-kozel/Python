from sys import argv

# assigning value from comand-line arguments to variables
script = argv

# open text file of the current directory passed by user
filename = input("Filename: ")
txt = open(filename)

print(f"Here's your {filename}")
print(txt.read())

txt.close()
