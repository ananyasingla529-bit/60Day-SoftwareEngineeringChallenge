import pwinput
print("=== Create Your Account ===")
c_name=input("Set your username: ")
c_password=pwinput.pwinput("Set a strong password: ", mask='*')
print("Account created successfully!")
print("\n=== Login ===")
attempts=3
while(attempts>0):
  name=input("Enter your username: ")
  password=input("Enter your password: ")
  if(name==c_name and password==c_password):
    print("Login successful!")
    break
  else:
    attempts -= 1
    if (attempts>0):
      print("Invalid username or password.")
      print("Attempts remaining:", attempts)
    else:
      print("Invalid username or password.")
      print("Too many failed attempts. Account locked.")
