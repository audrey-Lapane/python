# Simulate a bank transaction checking if a user has enough money

balance = 500
 
user_withdrawal = float(input("Enter withdrawal amount R "))

if user_withdrawal <= balance :
    balance -= user_withdrawal
    print(f"Withdrawal successful! Remaining balance: R{balance}")
elif user_withdrawal <= 0:
    print('"Invalid amount". You must widthdraw more that "R0" .')
else:
    print("Declined. Insufficient funds!")