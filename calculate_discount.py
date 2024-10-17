def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Apply the discount
        final_price = price - discount_amount
        return final_price
    else:
        # No discount, return the original price
        return price

# Prompt the user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function and print the result
final_price = calculate_discount(price, discount_percent)
print(f"The final price is: {final_price}")