"""
Q14. Create variables for:
principal
rate
time
and calculate Simple Interest SI = (P × R × T) / 100.
"""
principal = float(input("Enter the principle amount: "))
rate = float(input("Enter the rate: "))
time = float(input("Enter the time(in year): "))
Simple_Interest_SI = (principal * rate * time) / 100
print(f"Simple Interest as per calculation is: {Simple_Interest_SI}.")
