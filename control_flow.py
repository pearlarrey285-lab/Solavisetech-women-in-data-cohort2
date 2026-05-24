import time

age = 16
print("--- Age Eligibility ---")
if age < 13:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
else:
    print("Adult")

print("\n--- Password Validator ---")
password = "securePassword123"
if len(password) >= 8:
    print("Password is strong.")
else:
    print("Password is too short.")

print("\n--- Grade Classification ---")
score = 83
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

print("\n--- Multiplication Table ---")
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print("\n--- Guessing Game ---")
secret_number = 7
guess = 0
while guess != secret_number:
    guess = int(input("Guess the secret number (1-10): "))
    if guess == secret_number:
        print("Correct! You win!")
    else:
        print("Wrong, try again.")

print("\n--- Countdown Timer ---")
count = 10
while count > 0:
    print(count)
    count -= 1
    time.sleep(1)
print("Time's up!")

print("\n--- ATM Simulation ---")
balance = 1000
withdrawal = 400
if withdrawal <= balance:
    balance -= withdrawal
    print(f"Withdrawal successful. Remaining balance: ${balance}")
else:
    print("Insufficient funds.")

print("\n--- Login System ---")
stored_user = "admin"
stored_pass = "password123"
username = input("Username: ")
password = input("Password: ")
if username == stored_user and password == stored_pass:
    print("Login successful!")
else:
    print("Invalid credentials.")
