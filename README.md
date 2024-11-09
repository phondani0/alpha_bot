# alpha_bot - Automated Stock Trading Bot
=============================================

## Overview
------------

alpha_bot is a Python-based stock trading bot that automatically buys and sells stocks by analyzing various technical indicators. It uses the Alice Blue API for real-time trading and is highly customizable for different trading strategies.

## Features
------------

* Real-time market data via Alice Blue API
* Automated trading based on custom strategies
* Configurable indicators and trading logic
* Detailed logging for trade and market data analysis

## Getting Started
-------------------

### Prerequisites

* Python 3.7 or higher
* An Alice Blue account with API access

### Installation

1. Clone the repository: `git clone https://github.com/phondani0/alpha_bot.git`
2. Change into the project directory: `cd alpha_bot`
3. Install dependencies: `pip install -r requirements.txt`
4. Set up your Alice Blue API credentials in `config.py`

## Configuration
----------------

* Configure Alice Blue API credentials in `config.py`
* Customize your trading strategy in `strategy.py` to set indicators and parameters
* Set logging preferences for trade and market data

## Usage
---------

Run the bot with `python alpha_bot.py` to start analyzing market data and executing trades based on your strategy.

## Project Structure
---------------------

* `alpha_bot.py`: Main script to run the bot
* `config.py`: Configuration file for API credentials and bot settings
* `strategy.py`: Contains trading strategy logic

## Roadmap
------------

* Add support for additional indicators
* Implement risk management features
* Enhance logging with trade summaries and analytics

## Contributing
---------------

Contributions are welcome! Submit a pull request with any improvements or new features.

## License
------------

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
-------------------

* Alice Blue API
* TA-Lib for technical analysis indicators
