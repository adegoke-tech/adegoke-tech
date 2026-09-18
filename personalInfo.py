first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
phone_number = input("Enter your phone number: ")
job_duty = input("Enter your job duty/role: ")

# Print a clean, formatted summary
print("\n" + "="*30)
print("       USER PROFILE       ")
print("="*30)
print(f"Full Name:  {first_name} {surname}")
print(f"Phone:      {phone_number}")
print(f"Job Duty:   {job_duty}")
print("="*30)