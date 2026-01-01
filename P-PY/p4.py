first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
birth_year = input("Enter Birth Year: ")

yy = birth_year[-2:]

email = first_name.lower() + "." + last_name.lower() + "@uvpce.edu.in"
username = last_name.lower() + "_" + first_name.lower() + yy

print("Email ID:", email)
print("Username:", username)
