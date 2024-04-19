def calculate_chocolate_bars(total_money, price_per_bar):
    # Calculate the number of chocolate bars that can be bought
    number_of_bars = total_money // price_per_bar
    # Calculate the remaining change
    change = total_money % price_per_bar
    return number_of_bars, change

# Example of how to call the function
if __name__ == "__main__":
    # The user has 100 units of currency and each chocolate bar costs 7 units
    total_money = 100
    price = 7
    
    # Call the function and capture the result
    bars_bought, change_left = calculate_chocolate_bars(total_money, price)
    
    # Print the result
    print(f"You can buy {bars_bought} chocolate bars and you will have {change_left} units of currency left.")