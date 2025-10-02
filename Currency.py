# Advanced Currency Converter with Main Menu

import os
import time
import requests
from datetime import datetime
from colorama import Fore, Back, Style, init

# Initialize colorama for cross-platform colored output
init(autoreset=True)

# VATcomply API Base URL
API_BASE_URL = "https://api.vatcomply.com"

def clear_screen():
    """Clear the terminal screen based on operating system"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(show_dollar=True):
    """Print the application header with optional dollar bill ASCII art"""
    clear_screen()
    
    # Dollar Bill ASCII Art Banner with green color
    if show_dollar:
        print(Fore.GREEN + r"""
||====================================================================||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
||(100)==================| FEDERAL RESERVE NOTE |================(100)||
||\\$//        ~         '------========--------'                \\$//||
||<< /        /$\              // ____ \\                         \ >>||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
||<<|        \\ //           || <||  >\  ||                        |>>||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||""")
    
    # Application title
    print(Fore.CYAN + Back.BLACK + Style.BRIGHT + "\n" + "=" * 60)
    print(Fore.CYAN + Back.BLACK + Style.BRIGHT + "                 CURRENCY CONVERTER v1.0                 ")
    print(Fore.CYAN + Back.BLACK + Style.BRIGHT + "=" * 60 + "\n")

def get_exchange_rates():
    """Fetch current exchange rates from VATcomply API"""
    try:
        print(Fore.YELLOW + "Connecting to VATcomply API...")
        response = requests.get(f"{API_BASE_URL}/rates", timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()
        
        # Extract rates and date
        rates = data.get('rates', {})
        # Add USD (base currency) which is not included in the response
        rates['USD'] = 1.0
        date = data.get('date')
        
        # Debug output
        print(Fore.YELLOW + f"API returned {len(rates)} currencies")
        
        # Check if we're getting expected number of currencies
        if len(rates) < 50:
            print(Fore.YELLOW + "Fetching additional currencies...")
            
            # Get all available currencies from the currencies endpoint
            currencies_response = requests.get(f"{API_BASE_URL}/currencies", timeout=10)
            currencies_response.raise_for_status()
            currencies_data = currencies_response.json()
            
            # For currencies not in rates but available in the API, add them with estimates
            base_currency = data.get('base', 'EUR')
            base_rate = rates.get(base_currency, 1.0)
            
            # Get individual currency rates if needed
            for code in currencies_data:
                if code not in rates and code != base_currency:
                    try:
                        # Try to get rate for this specific currency
                        curr_response = requests.get(f"{API_BASE_URL}/rates?base={base_currency}&symbols={code}", timeout=5)
                        if curr_response.status_code == 200:
                            curr_data = curr_response.json()
                            if 'rates' in curr_data and code in curr_data['rates']:
                                rates[code] = curr_data['rates'][code]
                    except Exception:
                        pass  # Skip if we can't get this currency
        
        return True, rates, date
    except (requests.RequestException, ValueError, KeyError) as e:
        return False, str(e), None

def get_user_location():
    """Get user's location to suggest local currency"""
    try:
        response = requests.get(f"{API_BASE_URL}/geolocate", timeout=10)
        response.raise_for_status()
        data = response.json()
        country = data.get('country', {})
        country_name = country.get('name', 'Unknown')
        currency_code = country.get('currency', 'USD')
        return True, currency_code, country_name
    except (requests.RequestException, ValueError, KeyError):
        return False, 'USD', 'Unknown'

def get_fallback_rates():
    """Return static fallback exchange rates if API fails"""
    return {
        # Major currencies
        "USD": 1.00,    # US Dollar
        "EUR": 0.94,    # Euro
        "GBP": 0.82,    # British Pound
        "JPY": 149.30,  # Japanese Yen
        "CNY": 7.23,    # Chinese Yuan
        "AUD": 1.55,    # Australian Dollar
        "CAD": 1.38,    # Canadian Dollar
        "CHF": 0.89,    # Swiss Franc
        "HKD": 7.82,    # Hong Kong Dollar
        "SGD": 1.36,    # Singapore Dollar
        
        # Europe
        "SEK": 10.71,   # Swedish Krona
        "NOK": 10.80,   # Norwegian Krone
        "DKK": 7.01,    # Danish Krone
        "PLN": 4.03,    # Polish Zloty
        "CZK": 23.45,   # Czech Koruna
        "HUF": 358.80,  # Hungarian Forint
        "RON": 4.68,    # Romanian Leu
        "BGN": 1.84,    # Bulgarian Lev
        "ISK": 138.50,  # Icelandic Krona
        "RUB": 92.50,   # Russian Ruble
        
        # Americas
        "MXN": 17.03,   # Mexican Peso
        "BRL": 5.15,    # Brazilian Real
        "ARS": 870.0,   # Argentine Peso
        "COP": 3950.0,  # Colombian Peso
        "CLP": 927.0,   # Chilean Peso
        "PEN": 3.70,    # Peruvian Sol
        
        # Asia
        "INR": 83.39,   # Indian Rupee
        "KRW": 1345.0,  # South Korean Won
        "IDR": 15680.0, # Indonesian Rupiah
        "MYR": 4.72,    # Malaysian Ringgit
        "THB": 36.14,   # Thai Baht
        "PHP": 56.70,   # Philippine Peso
        "PKR": 278.50,  # Pakistani Rupee
        "BDT": 109.50,  # Bangladeshi Taka
        "VND": 24890.0, # Vietnamese Dong
        "ILS": 3.70,    # Israeli Shekel
        
        # Africa & Middle East
        "ZAR": 18.94,   # South African Rand
        "EGP": 46.80,   # Egyptian Pound
        "NGN": 1420.0,  # Nigerian Naira
        "KES": 129.50,  # Kenyan Shilling
        "SAR": 3.75,    # Saudi Riyal
        "AED": 3.67,    # UAE Dirham
        "QAR": 3.64,    # Qatari Riyal
        "TRY": 32.17,   # Turkish Lira
        
        # Oceania
        "NZD": 1.67,    # New Zealand Dollar
        "FJD": 2.27,    # Fijian Dollar
    }

def get_currency_info():
    """Get full currency information from the API"""
    try:
        response = requests.get(f"{API_BASE_URL}/currencies", timeout=10)
        response.raise_for_status()
        currencies = response.json()
        return True, currencies
    except (requests.RequestException, ValueError, KeyError) as e:
        return False, str(e)

def get_all_currency_symbols():
    """Return a comprehensive dictionary of currency symbols"""
    return {
        # Major currencies
        "USD": "$",
        "EUR": "€",
        "GBP": "£",
        "JPY": "¥",
        "CNY": "¥",
        "AUD": "A$",
        "CAD": "C$",
        "CHF": "Fr",
        "HKD": "HK$",
        "SGD": "S$",
        
        # Europe
        "SEK": "kr",
        "NOK": "kr",
        "DKK": "kr",
        "PLN": "zł",
        "CZK": "Kč",
        "HUF": "Ft",
        "RON": "lei",
        "BGN": "лв",
        "ISK": "kr",
        "RUB": "₽",
        "UAH": "₴",
        "HRK": "kn",
        "RSD": "din",
        "MKD": "ден",
        "ALL": "L",
        "MDL": "L",
        "BAM": "KM",
        
        # Americas
        "MXN": "$",
        "BRL": "R$",
        "ARS": "$",
        "COP": "$",
        "CLP": "$",
        "PEN": "S/",
        "UYU": "$",
        "BOB": "Bs",
        "VES": "Bs",
        "PYG": "₲",
        "GTQ": "Q",
        "HNL": "L",
        "NIO": "C$",
        "CRC": "₡",
        "PAB": "B/",
        "DOP": "RD$",
        "JMD": "J$",
        "TTD": "TT$",
        "BMD": "$",
        "BBD": "$",
        
        # Asia
        "INR": "₹",
        "KRW": "₩",
        "IDR": "Rp",
        "MYR": "RM",
        "THB": "฿",
        "PHP": "₱",
        "PKR": "₨",
        "BDT": "৳",
        "VND": "₫",
        "ILS": "₪",
        "TWD": "NT$",
        "LKR": "Rs",
        "NPR": "₨",
        "MMK": "K",
        "KHR": "៛",
        "MNT": "₮",
        "KZT": "₸",
        "UZS": "so'm",
        "KGS": "сом",
        
        # Africa & Middle East
        "ZAR": "R",
        "EGP": "E£",
        "NGN": "₦",
        "KES": "KSh",
        "SAR": "﷼",
        "AED": "د.إ",
        "QAR": "﷼",
        "TRY": "₺",
        "MAD": "د.م.",
        "TND": "د.ت",
        "GHS": "₵",
        "UGX": "USh",
        "TZS": "TSh",
        "ETB": "Br",
        "ZMW": "ZK",
        "BHD": ".د.ب",
        "KWD": "د.ك",
        "IQD": "ع.د",
        "JOD": "د.ا",
        "OMR": "ر.ع.",
        
        # Oceania
        "NZD": "NZ$",
        "FJD": "FJ$",
        "PGK": "K",
        "SBD": "SI$",
        "WST": "WS$",
        "TOP": "T$",
        "VUV": "VT",
        
        # Cryptocurrencies
        "BTC": "₿",
        "ETH": "Ξ",
        "LTC": "Ł",
        "XRP": "XRP",
        "BCH": "BCH",
        "XMR": "ɱ",
        "USDT": "₮",
        "USDC": "USDC",
        "DAI": "DAI",
    }

def categorize_currencies(currencies_dict, rates):
    """Categorize currencies into regions based on ISO codes and available data"""
    # Define regions with their known currencies
    regions = {
        "Major Currencies": ["USD", "EUR", "GBP", "JPY", "CNY", "AUD", "CAD", "CHF", "HKD", "SGD"],
        "Europe": ["SEK", "NOK", "DKK", "PLN", "CZK", "HUF", "RON", "BGN", "ISK", "RUB", "UAH", "HRK", 
                  "RSD", "MKD", "ALL", "MDL", "BAM", "BYN"],
        "Americas": ["MXN", "BRL", "ARS", "COP", "CLP", "PEN", "UYU", "BOB", "VES", "PYG", "GTQ", 
                    "HNL", "NIO", "CRC", "PAB", "DOP", "JMD", "TTD", "BMD", "BBD"],
        "Asia": ["INR", "KRW", "IDR", "MYR", "THB", "PHP", "PKR", "BDT", "VND", "ILS", "TWD", "LKR", 
                "NPR", "MMK", "KHR", "MNT", "KZT", "UZS", "KGS", "TJS", "AFN", "MVR"],
        "Africa & Middle East": ["ZAR", "EGP", "NGN", "KES", "SAR", "AED", "QAR", "TRY", "MAD", "TND", 
                               "GHS", "UGX", "TZS", "ETB", "ZMW", "BHD", "KWD", "IQD", "JOD", "OMR", 
                               "LBP", "DZD", "LYD", "SDG", "XOF", "XAF"],
        "Oceania": ["NZD", "FJD", "PGK", "SBD", "WST", "TOP", "VUV"],
        "Cryptocurrencies": ["BTC", "ETH", "LTC", "XRP", "BCH", "XMR", "USDT", "USDC", "DAI"]
    }
    
    # Create a flattened set of all known categorized currencies
    all_categorized = set()
    for currencies in regions.values():
        all_categorized.update(currencies)
    
    # Get the list of available currencies from rates
    available_currencies = set(rates.keys())
    
    # Create a "Others" region for uncategorized currencies
    others = available_currencies - all_categorized
    if others:
        regions["Others"] = sorted(list(others))
    
    # Filter regions to only include available currencies
    filtered_regions = {}
    for region, currencies in regions.items():
        available = [c for c in currencies if c in available_currencies]
        if available:
            filtered_regions[region] = available
    
    return filtered_regions

def display_main_menu(user_currency=None, country=None):
    """Display the main menu of the application"""
    print_header(show_dollar=False)
    
    location_info = f" - Location: {country} [{user_currency}]" if user_currency else ""
    print(Fore.YELLOW + Style.BRIGHT + f"MAIN MENU{location_info}\n")
    
    # Menu options
    print(Fore.WHITE + " 1. " + Fore.CYAN + "Convert Currency")
    print(Fore.WHITE + " 2. " + Fore.CYAN + "View All Available Currencies")
    print(Fore.WHITE + " 3. " + Fore.CYAN + "Check Exchange Rate")
    print(Fore.WHITE + " 4. " + Fore.CYAN + "Help")
    print(Fore.WHITE + " 0. " + Fore.RED + "Exit")
    
    print(Fore.CYAN + "\n" + "=" * 60)
    
    # Get user choice
    while True:
        try:
            choice = input(Fore.YELLOW + "\nEnter your choice (0-4): " + Style.BRIGHT)
            if choice in ['0', '1', '2', '3', '4']:
                return choice
            print(Fore.RED + "Invalid option. Please enter a number between 0 and 4.")
        except Exception:
            print(Fore.RED + "Invalid input. Please try again.")

def display_currencies(rates, symbols, regions):
    """Display available currencies with colors by region"""
    print_header(show_dollar=False)
    print(Fore.YELLOW + Style.BRIGHT + "🌍 AVAILABLE CURRENCIES\n")
    
    # Display currencies by region with different colors for each region
    region_colors = [Fore.CYAN, Fore.GREEN, Fore.MAGENTA, Fore.RED, Fore.YELLOW, Fore.BLUE, Fore.WHITE]
    
    # Calculate total available currencies
    total_count = len(rates)
    
    # Display number of currencies at the top
    print(Fore.WHITE + f"Total currencies available: {Fore.GREEN}{total_count}")
    print(Fore.WHITE + f"All currencies: {Fore.CYAN}{', '.join(sorted(rates.keys()))}")
    print()
    
    for i, (region, currencies) in enumerate(regions.items()):
        color = region_colors[i % len(region_colors)]
        print(f"{color}{Style.BRIGHT}{region} ({len(currencies)}):{Style.RESET_ALL}")
        
        # Create display strings with symbols
        currency_display = []
        for code in currencies:
            symbol = symbols.get(code, '')
            name = code  # Default to code if we don't have currency info
            currency_display.append(f"{code} {symbol}")
        
        # Display in columns with consistent formatting
        for j in range(0, len(currency_display), 6):
            row = currency_display[j:j+6]
            print("  " + "  ".join(f"{color}{c:<10}" for c in row))
        print()
    
    # Wait for user input before returning to main menu
    input(Fore.YELLOW + "\nPress Enter to return to the main menu...")

def check_exchange_rate(rates, symbols, default_currency):
    """Check exchange rate between two currencies"""
    print_header(show_dollar=False)
    print(Fore.YELLOW + Style.BRIGHT + "💱 EXCHANGE RATE CHECKER\n")
    
    print(Fore.CYAN + "Enter the currency codes to check the exchange rate between them.")
    print(Fore.CYAN + "Available currencies: " + Fore.WHITE + ", ".join(sorted(rates.keys())))
    
    # Get base currency
    base_currency = input(f"\n{Fore.CYAN}Base currency {Fore.YELLOW}(default: {default_currency}): {Style.BRIGHT}").upper() or default_currency
    if base_currency not in rates:
        print(f"\n{Fore.RED}❌ Error: {base_currency} is not supported.")
        input(Fore.YELLOW + "\nPress Enter to return to the main menu...")
        return
    
    # Get target currencies (comma-separated)
    target_input = input(f"{Fore.CYAN}Target currency/currencies (comma separated): {Style.BRIGHT}").upper()
    target_currencies = [c.strip() for c in target_input.split(",")]
    
    print(f"\n{Fore.YELLOW}Exchange rates for {Fore.GREEN}{Style.BRIGHT}1 {base_currency} {symbols.get(base_currency, '')}:")
    
    for target in target_currencies:
        if target not in rates:
            print(f"{Fore.RED}❌ {target}: Not supported")
            continue
        
        # Calculate rate
        rate = rates[target] / rates[base_currency]
        print(f"{Fore.WHITE}→ {Fore.GREEN}{rate:.4f} {target} {symbols.get(target, '')}")
    
    input(Fore.YELLOW + "\nPress Enter to return to the main menu...")

def show_help():
    """Display help information"""
    print_header(show_dollar=False)
    print(Fore.YELLOW + Style.BRIGHT + "ℹ️ HELP INFORMATION\n")
    
    print(Fore.CYAN + "ABOUT THIS APPLICATION")
    print(Fore.WHITE + "This Currency Converter allows you to convert between 50+ currencies using")
    print(Fore.WHITE + "real-time exchange rates fetched from the VATcomply API.")
    
    print(Fore.CYAN + "\nFEATURES")
    print(Fore.WHITE + "• Convert between many world currencies")
    print(Fore.WHITE + "• View up-to-date exchange rates")
    print(Fore.WHITE + "• Automatic location detection")
    print(Fore.WHITE + "• Colorful and easy-to-use interface")
    
    print(Fore.CYAN + "\nHOW TO USE")
    print(Fore.WHITE + "1. From the main menu, select the option you want")
    print(Fore.WHITE + "2. For currency conversion, enter the source currency, amount, and target currency")
    print(Fore.WHITE + "3. For checking rates, specify which currencies you want to compare")
    
    print(Fore.CYAN + "\nCURRENCY CODES")
    print(Fore.WHITE + "Use standard 3-letter currency codes (e.g., USD, EUR, GBP, JPY)")
    
    print(Fore.CYAN + "\nDATA SOURCE")
    print(Fore.WHITE + "Exchange rates are provided by VATcomply API (https://www.vatcomply.com)")
    
    input(Fore.YELLOW + "\nPress Enter to return to the main menu...")

def convert_currency(rates, symbols, suggested_currency):
    """Handle currency conversion workflow"""
    print_header()
    print(Fore.YELLOW + Style.BRIGHT + "💱 CURRENCY CONVERSION\n")
    
    # Help text
    print(Fore.WHITE + "Tip: Enter the 3-letter currency code (e.g., USD, EUR, JPY)")
    
    # Get source currency with suggestion based on location
    suggestion = f"(default: {suggested_currency})" if suggested_currency else "(default: USD)"
    source_currency = input(Fore.CYAN + "Enter source currency " + Fore.YELLOW + f"{suggestion}: " + Style.BRIGHT).upper() or suggested_currency or "USD"
    
    if source_currency not in rates:
        print(f"\n{Fore.RED}❌ Error: {source_currency} is not supported.")
        input(Fore.YELLOW + "\nPress Enter to return to the main menu...")
        return
    
    try:
        amount_prompt = f"Enter amount in {source_currency} {symbols.get(source_currency, '')}: "
        amount = float(input(Fore.CYAN + amount_prompt + Style.BRIGHT))
        if amount < 0:
            print(f"\n{Fore.RED}❌ Error: Amount cannot be negative.")
            input(Fore.YELLOW + "\nPress Enter to return to the main menu...")
            return
    except ValueError:
        print(f"\n{Fore.RED}❌ Error: Please enter a valid number.")
        input(Fore.YELLOW + "\nPress Enter to return to the main menu...")
        return
    
    # Get target currency
    target_currency = input(Fore.CYAN + "Enter target currency: " + Style.BRIGHT).upper()
    if target_currency not in rates:
        print(f"\n{Fore.RED}❌ Error: {target_currency} is not supported.")
        input(Fore.YELLOW + "\nPress Enter to return to the main menu...")
        return
    
    # Convert to USD first if not already USD (because VATcomply rates are based on EUR)
    usd_amount = amount / rates[source_currency] if source_currency != "USD" else amount
    
    # Convert from USD to target currency
    converted_amount = usd_amount * rates[target_currency]
    
    # Display result with colors and formatting
    display_conversion_result(source_currency, amount, target_currency, converted_amount, rates, symbols)
    
    input(Fore.YELLOW + "\nPress Enter to return to the main menu...")

def display_conversion_result(source_currency, amount, target_currency, converted_amount, rates, symbols):
    """Display the conversion result with formatting and colors"""
    print(Fore.CYAN + "\n" + "=" * 60)
    
    # Result box with blue background
    print(Fore.WHITE + Back.BLUE + """
    ╔═══════════════════════════════════════════════════════╗
    ║                   CONVERSION RESULT                    ║
    ╚═══════════════════════════════════════════════════════╝
    """ + Style.RESET_ALL)
    
    source_symbol = symbols.get(source_currency, '')
    target_symbol = symbols.get(target_currency, '')
    
    # Result with bright green color for the amounts
    print(Fore.WHITE + f"      {Fore.GREEN}{Style.BRIGHT}{amount:.2f} {source_currency} {source_symbol}{Fore.WHITE} = ", end="")
    print(f"{Fore.GREEN}{Style.BRIGHT}{converted_amount:.2f} {target_currency} {target_symbol}")
    print(Fore.WHITE + f"      Rate: 1 {source_currency} = {Fore.YELLOW}{rates[target_currency]/rates[source_currency]:.4f} {target_currency}")
    
    print(Fore.CYAN + "\n" + "=" * 60)

def fetch_all_available_currencies():
    """Fetch all available currencies from VATcomply API, regardless of having rates"""
    try:
        print(Fore.YELLOW + "Fetching complete currency list...")
        # First get currencies list
        currencies_response = requests.get(f"{API_BASE_URL}/currencies", timeout=10)
        currencies_response.raise_for_status()
        currencies_data = currencies_response.json()
        
        # Then get rates
        rates_response = requests.get(f"{API_BASE_URL}/rates", timeout=10)
        rates_response.raise_for_status()
        rates_data = rates_response.json()
        rates = rates_data.get('rates', {})
        rates['USD'] = 1.0  # Add USD as base
        
        # Create empty rates for currencies that don't have exchange rates yet
        for code in currencies_data:
            if code not in rates:
                rates[code] = 0.0  # Placeholder
                
        return True, rates, rates_data.get('date')
    except Exception as e:
        return False, str(e), None
    
def main():
    """Main function with menu-driven interface and complete currency support"""
    # Display the startup splash screen
    print_header()
    
    # Small delay for dramatic effect
    time.sleep(0.5)
    
    # First try to fetch ALL available currencies
    print(Fore.YELLOW + "Fetching ALL available currencies...")
    all_success, all_rates, all_date = fetch_all_available_currencies()
    
    # If that worked, use it, otherwise fall back to regular method
    if all_success and len(all_rates) > 31:
        rates = all_rates
        date = all_date
        print(Fore.GREEN + f"✓ Complete currency list loaded with {len(rates)} currencies")
    else:
        # Fall back to regular exchange rates
        print(Fore.YELLOW + "Fetching standard exchange rates...")
        success, rates_data, date = get_exchange_rates()
        
        if success:
            rates = rates_data
        else:
            rates = get_fallback_rates()
            print(Fore.RED + f"✗ Couldn't fetch live rates: {rates_data}")
            print(Fore.YELLOW + "Using stored rates as fallback")
            date = None
    
    print(Fore.GREEN + f"✓ {len(rates)} currencies available as of {date}")
    
    # Get user location for currency suggestion
    location_success, suggested_currency, country = get_user_location()
    if location_success:
        print(Fore.GREEN + f"✓ Detected location: {country} [{suggested_currency}]")
    else:
        suggested_currency = "USD"
        country = "Unknown"
        print(Fore.YELLOW + "Could not detect location. Using USD as default.")
    
    # Try to get detailed currency information
    print(Fore.YELLOW + "Loading currency information...")
    
    # Get comprehensive currency symbols
    symbols = get_all_currency_symbols()
    
    # Categorize currencies by region
    regions = categorize_currencies({}, rates)
    
    # Small delay before showing menu
    time.sleep(1)
    
    # Main application loop
    while True:
        choice = display_main_menu(suggested_currency, country)
        
        if choice == '0':  # Exit
            clear_screen()
            print(Fore.GREEN + Style.BRIGHT + """
Thank you for using Currency Converter!
      .--.
     /.-. '----------.
     \'-' .--"--""-"-'
      '--'
            """)
            break
            
        elif choice == '1':  # Convert Currency
            convert_currency(rates, symbols, suggested_currency)
            
        elif choice == '2':  # View Available Currencies
            display_currencies(rates, symbols, regions)
            
        elif choice == '3':  # Check Exchange Rate
            check_exchange_rate(rates, symbols, suggested_currency)
            
        elif choice == '4':  # Help
            show_help()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print(Fore.YELLOW + "\nProgram terminated by user. Goodbye!")
    except Exception as e:

        print(Fore.RED + f"\nAn unexpected error occurred: {e}")
