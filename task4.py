# Program that reads a file

with open('greetings.txt', 'r') as greet:
    greeting = greet.read()
    print(greeting)

# writes a modified version to a new file.
with open('response.txt', 'w') as response:
    response.write(f"{greeting}, How are you all doing today?")

# Error Handling
file_name = input("Enter your file name: ")

try:
    if file_name:
        file = open(file_name, 'r')
        print(file.read())
    else:
        raise Exception
except:
    print("No file name provided")