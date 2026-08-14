password=input("Please Enter Your Password:")
password_length = len(password)
if password_length < 6:
    print("Thats So Weak, Your password must be at least 6 characters long")
elif password.isdigit():
    print("Weak.Your password consists only of numbers. You must add letters and special characters.")
elif password.isalpha():
    print("Weak. Your password consists only of letters. You must add numbers and special characters.")    
elif password_length < 10:
    print("Middle. That's not Bad. But İt can be stronger.")
else:
    print("Strong! Congratulations thats awesome")
