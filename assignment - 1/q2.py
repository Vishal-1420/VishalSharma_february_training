# Online Shopping Discount System 

customer_name = input("Enter customer name: ")
price = float(input("Enter product price: "))
premium_input = input("Is the customer a premium member? (True/False): ")
coupon_code = input("Enter coupon code: ").strip().upper()

premium = premium_input.strip().lower() == "true"

discount = 0
discount_reason = "No discount applied"


if price > 5000 and premium:
    discount = 0.20 * price
    discount_reason = "20% Premium High-Value Discount"

elif premium:
    discount = 0.10 * price
    discount_reason = "10% Premium Member Discount"

elif coupon_code == "SAVE20" and price >= 4000:
    discount = 0.20 * price
    discount_reason = "20% Coupon Discount (SAVE20)"

elif coupon_code == "SAVE10" and price >= 1000:
    discount = 0.10 * price
    discount_reason = "10% Coupon Discount (SAVE10)"

final_price = price - discount

# Output
print("\n===== Bill Details =====")
print(f"Customer Name: {customer_name}")
print(f"Original Price: ₹{price:.2f}")
print(f"Discount Applied: ₹{discount:.2f}")
print(f"Final Price: ₹{final_price:.2f}")
print(f"Offer Applied: {discount_reason}")

if premium:
    print("Premium benefits applied ")
