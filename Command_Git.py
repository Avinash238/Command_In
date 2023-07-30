from forex_python.converter import CurrencyRates
def convert_currency(amount, from_currency, to_currency):
    """Convert currency using real-time exchange rates."""
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)
    return converted_amount
if __name__ == "__main__":
    print("Currency Converter")
    print("Supported Currencies: USD, EUR, GBP, JPY, INR, AUD, CAD, and more...")
    from_currency = input("Enter the source currency code (e.g., USD): ").upper()
    to_currency = input("Enter the target currency code (e.g., EUR): ").upper()
    try:
        amount = float(input("Enter the amount to convert: "))
        converted_amount = convert_currency(amount, from_currency, to_currency)
        print(f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
    except ValueError:
        print("Invalid amount. Please enter a valid number.")
    except Exception as e:
        print("An error occurred during conversion:", e)
