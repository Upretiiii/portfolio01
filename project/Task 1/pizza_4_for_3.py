def get_valid_price(pizza_number):
    while True:
        try:
            price = float(input(f"Enter Price of Pizza #{pizza_number}: "))
            if price <= 0:
                print("Please enter a valid price!")
            else:
                return price
        except ValueError:
            print("Please enter a valid price!")


def main():
    print("Beckett Pizza Plaza 4-for-3 Offer")
    print("=================================\n")

    prices = []
    for i in range(1, 5):
        prices.append(get_valid_price(i))

    total_price = sum(prices)
    cheapest = min(prices)
    discounted_total = total_price - cheapest

    discount_percentage = (cheapest / total_price) * 100

    print(f"\nOrder Total is £{discounted_total:.2f}, "
          f"a fabulous discount of {discount_percentage:.0f}%!")


if __name__ == "__main__":
    main()
