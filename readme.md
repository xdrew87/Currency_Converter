# 💱 Currency Converter

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

A feature-rich command-line currency converter application written in Python.

```
||====================================================================||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
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

This Currency Converter is a Python application that allows users to convert between different currencies using up-to-date exchange rates. The application features a user-friendly command-line interface with ASCII art for enhanced visual appeal.

## ✨ Features

- 🔄 Convert between multiple currencies
- 🌎 Support for 10 major world currencies
- 🎨 Beautiful ASCII art interface
- 💱 Display of currency symbols
- 🧮 Accurate conversion with 4 decimal precision
- ⚠️ Comprehensive error handling
- 🔢 Input validation

## 🔧 Installation

### Option 1: Clone the Repository

```bash
# Clone this repository
git clone https://github.com/suicixdalEXE/currency_converter.git

# Navigate to the project directory
cd currency_converter

# Run the application
python currency.py
```

### Option 2: Download Single File

If you only want the converter script:

1. Download the `currency.py` file from this repository
2. Run it with Python 3.6+

## 🚀 Usage

Run the program using Python:

```bash
python currency.py
```

Follow the interactive prompts:
1. Enter the source currency (or press Enter for USD)
2. Enter the amount you want to convert
3. Enter the target currency
4. View the conversion result

## 💰 Supported Currencies

| Currency Code | Currency Name        | Symbol |
|---------------|----------------------|--------|
| USD           | US Dollar            | $      |
| EUR           | Euro                 | €      |
| GBP           | British Pound        | £      |
| MYR           | Malaysian Ringgit    | RM     |
| JPY           | Japanese Yen         | ¥      |
| CAD           | Canadian Dollar      | C$     |
| AUD           | Australian Dollar    | A$     |
| CNY           | Chinese Yuan         | ¥      |
| INR           | Indian Rupee         | ₹      |
| SGD           | Singapore Dollar     | S$     |

## 📸 Screenshots

```
🌍 Available currencies 🌍
  USD: $
  EUR: €
  GBP: £
  MYR: RM
  JPY: ¥
  CAD: C$
  AUD: A$
  CNY: ¥
  INR: ₹
  SGD: S$

========================================

Enter source currency (default: USD): EUR
Enter amount in EUR €: 100
Enter target currency: JPY

========================================

╔═══════════════════════════════════════╗
║            CONVERSION RESULT          ║
╚═══════════════════════════════════════╝

    100.00 EUR € = 15881.91 JPY ¥
    Rate: 1 EUR = 158.8191 JPY

========================================
```

## 📂 Project Structure

```
currency-converter/
├── ccurrency.py              # Main application file
├── LICENSE             # MIT License file
└── README.md           # This documentation file
```

## 📋 Future Improvements

- [ ] Add live exchange rate updates via API
- [ ] Implement historical exchange rate data
- [ ] Add graphical user interface (GUI)
- [ ] Support for more currencies
- [ ] Add currency conversion history

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

*Note: Exchange rates are fixed and may not reflect current market values.*

