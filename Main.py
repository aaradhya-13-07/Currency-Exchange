# ==========================================
# 1. EMBEDDED DATA
# All data is stored directly in the program
# ==========================================

# Exchange rates (Base: 1 USD = X Currency)
EXCHANGE_RATES = {
    "AFN": 64.627, "ALL": 79.656, "AMD": 363.75, "AOA": 919.62, "ARS": 1512.06,
    "AWG": 1.7944, "AZN": 1.701, "BAM": 1.7001, "BBD": 2.0204, "BDT": 123.09,
    "BHD": 0.376, "BIF": 3005.09, "BMD": 1.00, "BND": 1.2755, "BOB": 9.9256,
    "BRL": 5.142, "BSD": 1.0105, "BTN": 95.90, "BWP": 13.50, "BYN": 3.0354,
    "BZD": 2.0321, "CAD": 1.3977, "CDF": 2300.65, "CHF": 0.82354, "CLP": 956.83,
    "CNY": 6.7044, "COP": 3151.18, "CRC": 447.90, "CUP": 24.00, "CVE": 95.78,
    "CZK": 21.176, "DJF": 177.94, "DKK": 6.5071, "DOP": 59.657, "DZD": 133.94,
    "EGP": 52.158, "ERN": 15.233, "ETB": 161.64, "EUR": 0.86924, "FJD": 2.2296,
    "FKP": 0.74507, "GBP": 0.7462, "GEL": 2.604, "GHS": 11.555, "GIP": 0.75631,
    "GMD": 73.335, "GNF": 8818.00, "GTQ": 7.6589, "GYD": 210.92, "HKD": 7.8508,
    "HNL": 26.953, "HTG": 131.07, "HUF": 316.51, "IDR": 17756.00, "ILS": 3.0342,
    "INR": 95.88, "IQD": 1311.21, "IRR": 1370941.00, "ISK": 121.78, "JMD": 157.58,
    "JOD": 0.709, "JPY": 155.85, "KES": 129.56, "KGS": 87.55, "KHR": 4066.16,
    "KMF": 429.33, "KRW": 1380.87, "KWD": 0.30786, "KYD": 0.83718, "KZT": 445.81,
    "LAK": 22307.00, "LBP": 89841.00, "LKR": 331.59, "LRD": 173.92, "LSL": 16.324,
    "LYD": 6.3632, "MAD": 9.4874, "MDL": 17.491, "MGA": 4366.71, "MKD": 53.655,
    "MMK": 2101.44, "MNT": 3604.92, "MOP": 8.0864, "MRU": 40.311, "MUR": 47.592,
    "MVR": 15.477, "MWK": 1736.86, "MXN": 17.19, "MYR": 4.0946, "MZN": 63.804,
    "NAD": 16.316, "NGN": 1330.47, "NIO": 36.624, "NOK": 9.4129, "NPR": 153.67,
    "NZD": 1.7428, "OMR": 0.3845, "PAB": 1.0035, "PEN": 3.3666, "PGK": 4.4728,
    "PHP": 62.709, "PKR": 277.98, "PLN": 3.7947, "PYG": 5932.00, "QAR": 3.64,
    "RON": 4.5823, "RSD": 102.34, "RUB": 84.51, "RWF": 1472.69, "SAR": 3.75,
    "SBD": 8.0002, "SCR": 14.26, "SDG": 602.37, "SEK": 9.8153, "SHP": 0.74507,
    "SLE": 24.648, "SOS": 573.40, "SRD": 37.895, "SSP": 5692.00, "STN": 21.505,
    "SVC": 8.7858, "SYP": 122.29, "SZL": 16.309, "THB": 33.318, "TJS": 9.2394,
    "TMT": 3.50, "TND": 2.9287, "TOP": 2.3806, "TRY": 48.688, "TTD": 6.7589,
    "TWD": 31.858, "TZS": 2643.28, "UAH": 44.683, "UGX": 3931.57, "USD": 1.00,
    "UYU": 40.232, "UZS": 11808.00, "VES": 851.42, "VND": 25948.00, "VUV": 117.48,
    "WST": 2.734, "XAF": 570.18, "XCD": 2.7329, "XCG": 1.8067, "XOF": 569.78,
    "XPF": 104.21, "YER": 237.08, "ZAR": 16.253, "ZMW": 19.646, "ZWG": 26.82
}

# Monthly Inflation Rates (Percentage). None = "data not available"
INFLATION_RATES = {
    "AFN": None, "ALL": 0.3, "DZD": None, "AOA": 0.8, "ARS": 1.7, "AMD": 0.4, 
    "AUD": 0.3, "AZN": None, "BSD": None, "BHD": None, "BDT": 0.5, "BBD": None, 
    "BYN": 0.3, "BZD": None, "XOF": 0.1, "BMD": None, "BTN": None, "BOB": 0.4, 
    "BAM": 0.2, "BWP": 0.3, "BRL": 0.3, "BND": None, "BGN": 0.6, "BIF": -0.02, 
    "KHR": None, "CAD": -0.1, "CVE": None, "XAF": 0.1, "CLP": 0.4, "CNY": 0.1, 
    "COP": 0.4, "KMF": None, "CDF": None, "CRC": -0.02, "HRK": 0.3, "CUP": None, 
    "CZK": 0.3, "DKK": -0.4, "DJF": None, "DOP": 0.3, "XCD": None, "EGP": 1.1, 
    "ERN": None, "ETB": 1.2, "EUR": 0.4, "FJD": 0.6, "GMD": None, "GEL": 0.5, 
    "GHS": 0.4, "GTQ": 0.3, "GNF": None, "GYD": None, "HTG": None, "HNL": 0.5, 
    "HKD": None, "HUF": 0.2, "ISK": 0.3, "INR": 0.4, "IDR": 0.3, "IRR": None, 
    "IQD": None, "ILS": 0.2, "JMD": None, "JPY": 0.2, "JOD": 0.2, "KZT": 0.8, 
    "KES": 0.5, "KWD": None, "KGS": None, "LAK": 0.6, "LVL": 0.3, "LBP": None, 
    "LSL": 0.4, "LRD": None, "LYD": None, "MOP": None, "MGA": None, "MWK": None, 
    "MYR": 0.2, "MVR": None, "MRU": None, "MUR": 0.4, "MXN": 0.3, "MDL": 0.6, 
    "MNT": 1.0, "MAD": 0.2, "MZN": 0.5, "MMK": None, "NAD": 0.4, "NPR": None, 
    "TWD": 0.2, "NZD": 0.3, "NIO": None, "NGN": 1.2, "MKD": 0.2, "NOK": -0.5, 
    "OMR": 0.3, "PKR": 0.9, "PAB": None, "PGK": None, "PYG": 0.1, "PEN": 0.4, 
    "PHP": 0.5, "PLN": 0.3, "QAR": None, "RON": 0.3, "RUB": 0.5, "RWF": 3.7, 
    "WST": None, "STN": None, "SAR": None, "RSD": 0.2, "SCR": 0.1, "SLE": None, 
    "SGD": 0.2, "SKK": 0.0, "SIT": 0.3, "SBD": None, "SOS": None, "ZAR": 0.4, 
    "KRW": 0.3, "SSP": None, "LKR": 0.6, "SDG": None, "SRD": None, "SEK": -0.3, 
    "CHF": 0.1, "SYP": None, "TZS": 0.3, "THB": 0.2, "TOP": None, "TTD": None, 
    "TND": 0.4, "TRY": 1.84, "TMT": None, "UGX": 0.3, "UAH": 0.1, "AED": None, 
    "UYU": 0.4, "USD": 0.4, "UZS": 0.5, "VUV": None, "VES": None, "VND": 0.4, 
    "YER": None, "ZMW": 0.5, "ZWG": 0.2
}

# Currency full names mapping
CURRENCY_NAMES = {
    "AED": "United Arab Emirates dirham", "AFN": "Afghan afghani", "ALL": "Albanian lek",
    "AMD": "Armenian dram", "AOA": "Angolan kwanza", "ARS": "Argentine peso", 
    "AUD": "Australian dollar", "AZN": "Azerbaijani manat", "BAM": "Bosnia and Herzegovina convertible mark",
    "BBD": "Barbadian dollar", "BDT": "Bangladeshi taka", "BGN": "Bulgarian lev",
    "BHD": "Bahraini dinar", "BIF": "Burundian franc", "BMD": "Bermudian dollar",
    "BND": "Brunei dollar", "BOB": "Bolivian boliviano", "BRL": "Brazilian real",
    "BSD": "Bahamian dollar", "BTN": "Bhutanese ngultrum", "BWP": "Botswana pula",
    "BYN": "Belarusian ruble", "BZD": "Belize dollar", "CAD": "Canadian dollar",
    "CHF": "Swiss franc", "CLP": "Chilean peso", "CNY": "Chinese yuan (renminbi)", 
    "COP": "Colombian peso", "CRC": "Costa Rican colón", "CUP": "Cuban peso", 
    "CZK": "Czech koruna", "DKK": "Danish krone", "DOP": "Dominican peso", 
    "EGP": "Egyptian pound", "EUR": "Euro", "GBP": "British pound", "HKD": "Hong Kong dollar",
    "IDR": "Indonesian rupiah", "ILS": "Israeli new shekel", "INR": "Indian rupee", 
    "JPY": "Japanese yen", "KRW": "South Korean won", "MXN": "Mexican peso", 
    "MYR": "Malaysian ringgit", "NOK": "Norwegian krone", "NZD": "New Zealand dollar", 
    "PHP": "Philippine peso", "PLN": "Polish złoty", "RUB": "Russian ruble", 
    "SEK": "Swedish krona", "SGD": "Singapore dollar", "THB": "Thai baht", 
    "TRY": "Turkish lira", "TWD": "New Taiwan dollar", "USD": "United States dollar", 
    "ZAR": "South African rand"
}

# ==========================================
# 2. HELPER FUNCTIONS FOR TERMINAL INPUT
# ==========================================

def get_currency_code(prompt_text):
    while True:
        code = input(prompt_text).strip().upper()
        if code in EXCHANGE_RATES:
            return code
        print(f"  [!] Error: '{code}' is not a recognized currency code. Try something like USD, EUR, or JPY.")

def get_positive_number(prompt_text):
    while True:
        try:
            val = float(input(prompt_text).strip())
            if val >= 0:
                return val
            print("  [!] Error: Please enter a positive number.")
        except ValueError:
            print("  [!] Error: Invalid input. Please enter a numerical value.")

# ==========================================
# 3. MAIN PROGRAM LOOP
# ==========================================

def main():
    print("=" * 60)
    print("💱 Terminal Currency & Inflation Calculator 💱")
    print("-" * 60)
    print("Notice: Exchange rates are based on September 20, 2026 data.")
    print("Current date: September 22, 2026.")
    print("=" * 60)
    print()

    # Get inputs from the user
    from_code = get_currency_code("Enter the 'From' currency code (e.g., AUD): ")
    to_code = get_currency_code("Enter the 'To' currency code (e.g., JPY): ")
    amount = get_positive_number(f"Enter the amount in {from_code}: ")
    months = int(get_positive_number("Enter number of months to project for inflation (0 for none): "))
    
    # Step 1: Convert the initial currency into base US Dollars (USD)
    amount_in_usd = amount / EXCHANGE_RATES[from_code]
    
    # Step 2: Convert the US Dollars into the desired target currency
    converted_amount = amount_in_usd * EXCHANGE_RATES[to_code]
    
    print("\n" + "=" * 60)
    print("💵 CONVERSION RESULT")
    print("=" * 60)
    from_name = CURRENCY_NAMES.get(from_code, from_code)
    to_name = CURRENCY_NAMES.get(to_code, to_code)
    
    print(f"From : {amount:,.2f} {from_code} ({from_name})")
    print(f"To   : {converted_amount:,.2f} {to_code} ({to_name})")
    
    # Step 3: Handle Inflation projections if the user asked for > 0 months
    if months > 0:
        print("-" * 60)
        print("📈 INFLATION PROJECTION")
        print("-" * 60)
        
        inflation_rate = INFLATION_RATES.get(to_code)
        
        if inflation_rate is not None:
            # Formula: Future Value = Current Value * (1 + (inflation_rate / 100)) ^ months
            future_value = converted_amount * ((1 + (inflation_rate / 100)) ** months)
            
            print(f"Target Currency ({to_code}) Monthly Inflation Rate: {inflation_rate}%")
            print(f"Future Adjusted Value (after {months} months): {future_value:,.2f} {to_code}")
        else:
            print(f"⚠️ Inflation data is not available for {to_code}.")
            print("Showing result without inflation projection.")
            
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # This catches when a user presses Ctrl+C to forcefully exit
        print("\n\nCalculator closed.")
