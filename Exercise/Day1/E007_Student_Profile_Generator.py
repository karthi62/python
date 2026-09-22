first_name=input("Enter the first name:")
last_name=input("Enter the last name:")
first_name=first_name.strip()
last_name=last_name.strip()
full_name=first_name + " " + last_name
print("Full Name:",full_name)
print("Uppercase:",full_name.upper())
print("Characters:",len(full_name))