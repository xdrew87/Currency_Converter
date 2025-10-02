# 💱 Currency Converter

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
[![API: VATcomply](https://img.shields.io/badge/API-VATcomply-orange.svg)](https://www.vatcomply.com/documentation)

A feature-rich command-line currency converter application with real-time exchange rates and interactive menu.

```
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
||====================================================================||
```

## 📝 Description

This Currency Converter is a Python application that allows users to convert between 50+ currencies using real-time exchange rates from the VATcomply API. The application features a colorful, user-friendly command-line interface with interactive menus and ASCII art for enhanced visual appeal.

## ✨ Features

- 🔄 Convert between 50+ world currencies with real-time rates
- 🌎 Live exchange rate data via VATcomply API
- 🧭 Automatic location detection to suggest your local currency
- 🎨 Colorful interactive menu interface
- 💱 Comprehensive currency symbols display
- 📊 Exchange rate comparison tool
- 🖥️ Clear organized display of currencies by region
- 🧮 Accurate conversion with 4 decimal precision
- ⚠️ Robust error handling with fallbacks
- 🔢 Intuitive input validation

## 🔧 Installation

### Requirements
- Python 3.6+
- Internet connection for real-time rates
- Required packages: requests, colorama

### Option 1: Clone the Repository

```bash
# Clone this repository
git clone https://github.com/xdrew87/currency_converter.git

# Navigate to the project directory
cd currency_converter

# Install required packages
pip install -r requirements.txt

# Run the application
python Currency.py
```

### Option 2: Manual Setup

1. Download the `Currency.py` file from this repository
2. Install required packages: `pip install colorama requests`
3. Run it with Python 3.6+: `python Currency.py`

## 🚀 Usage

Run the program using Python:

```bash
python Currency.py
```

The interactive menu allows you to:
1. Convert Currency - Convert amounts between any supported currencies
2. View All Available Currencies - Browse all supported currencies by region
3. Check Exchange Rate - Compare exchange rates between currencies
4. Help - View application information and instructions
0. Exit - Exit the application

## 💰 Supported Currencies

The application supports 50+ currencies from around the world including:

### Major Currencies
USD (US Dollar), EUR (Euro), GBP (British Pound), JPY (Japanese Yen), CNY (Chinese Yuan), etc.

### Regional Currencies
- **Europe**: SEK, NOK, DKK, PLN, CZK, HUF, RON, etc.
- **Americas**: MXN, BRL, ARS, COP, CLP, PEN, etc.
- **Asia**: INR, KRW, IDR, MYR, THB, PHP, etc.
- **Africa & Middle East**: ZAR, EGP, NGN, KES, SAR, AED, etc.
- **Oceania**: NZD, FJD, PGK, etc.

*All currencies are automatically fetched from the VATcomply API and categorized by region.*

## 📸 Screenshots

### Main Menu
```
MAIN MENU - Location: United States [USD]

 1. Convert Currency
 2. View All Available Currencies
 3. Check Exchange Rate
 4. Help
 0. Exit

============================================================

Enter your choice (0-4): 
```

### Currency Conversion
```
💱 CURRENCY CONVERSION

Tip: Enter the 3-letter currency code (e.g., USD, EUR, JPY)
Enter source currency (default: USD): EUR
Enter amount in EUR €: 100
Enter target currency: JPY

============================================================

╔═══════════════════════════════════════════════════════╗
║                   CONVERSION RESULT                    ║
╚═══════════════════════════════════════════════════════╝

      100.00 EUR € = 15881.91 JPY ¥
      Rate: 1 EUR = 158.8191 JPY

============================================================
```

### Exchange Rate Checker
```
💱 EXCHANGE RATE CHECKER

Enter the currency codes to check the exchange rate between them.
Available currencies: AED, AUD, BGN, BRL, CAD, CHF, CNY...

Base currency (default: USD): USD
Target currency/currencies (comma separated): EUR,GBP,JPY,CAD

Exchange rates for 1 USD $:
→ 0.9340 EUR €
→ 0.8191 GBP £
→ 149.3000 JPY ¥
→ 1.3800 CAD C$
```

## 📂 Project Structure

```
Currency_Converter/
├── Currency.py       # Main application file
├── requirements.txt  # Python dependencies
├── LICENSE           # MIT License file
└── README.md         # This documentation file
```

## ⚙️ How It Works

The application connects to the VATcomply API to fetch:
1. Live exchange rates for 50+ currencies
2. User's geographic location for local currency detection

When the API cannot be reached, it falls back to stored rates to ensure the app remains functional.

## 📋 Future Improvements

- [ ] Implement historical exchange rate data
- [ ] Add graphical user interface (GUI)
- [ ] Add currency conversion history tracking
- [ ] Create charts and graphs of exchange rate trends
- [ ] Enable offline mode with cached rates
- [x] ~~Add live exchange rate updates via API~~ (Implemented!)
- [x] ~~Support for 50+ currencies~~ (Implemented!)

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Created by [@xdrew87](https://github.com/xdrew87)

## ⭐ Star This Repository

If you find this project useful, please consider giving it a star on GitHub!

---

*Note: Exchange rates are provided by the VATcomply API (https://www.vatcomply.com) and are updated daily.*



