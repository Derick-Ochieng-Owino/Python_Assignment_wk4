input_filename = input("Enter the input filename: ")
output_filename = input("Enter the output filename: ")

try:
    with open("names.txt", 'r') as input_file:
        content = input_file.read()
    
    modified_content = content.upper()

    with open(output_filename, 'w') as output_file:
        output_file.write(modified_content)
    
    print(f"File successfully modified and saved as {"output.txt"}")

except FileNotFoundError:
    print(f"Error: The file {"names.txt"} was not found.")
except PermissionError:
    print(f"Error: Permission denied when accessing {"names.txt"}.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")