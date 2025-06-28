# Arbitrage Opportunity Detection by OctoBot

This Python-based project utilizes the ccxt and OctoBot libraries to detect potential arbitrage opportunities across multiple assets in cryptocurrency markets. It identifies profitable cycles where you can trade through a series of assets and return to the original asset with a potential gain, making it applicable for arbitrage strategies beyond just triangular cycles.

## Description

Arbitrage trading is a process where you trade from one asset or currency to another, and then continue trading through a series of assets until you eventually return to the original asset or currency. The goal is to exploit price differences between multiple assets to generate a profit. This project provides a method to identify the best arbitrage opportunities in a multi-asset cycle, given a list of last prices for different cryptocurrency pairs.

Note: The results do not account for fees during trades. This can have a significant impact on performance.

## Getting Started

### Dependencies
* Python 3.10

### Installing
```bash
pip3 install -r requirements.txt
```

### Usage
Start detection by running:
```bash
python3 main.py
```

### Configuration
To change the exchange edit `main.py` `exchange_name` value to the desired exchange. It should match the exchange ccxt id value.

You can also provide a list of symbols to ignore or whitelist when calling `run_detection`.

## Project Structure
- `triangular_arbitrage/` - Core logic
- `tests/` - Test files
- `main.py` - Entry point
- `requirements.txt` - Dependencies
- `README.md` - Documentation
