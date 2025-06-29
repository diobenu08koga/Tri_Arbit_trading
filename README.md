# Arbitrage Opportunity Detection

A Python-based tool that detects potential arbitrage opportunities across multiple assets in cryptocurrency markets using ccxt and OctoBot libraries.

## Overview

This project identifies profitable trading cycles where you can trade through a series of assets and return to the original asset with a potential gain. It's designed for arbitrage strategies beyond just triangular cycles, supporting multi-asset arbitrage detection.

## Features

- **Multi-Asset Arbitrage**: Detect profitable cycles across multiple assets
- **Exchange Support**: Works with any exchange supported by ccxt
- **Configurable Detection**: Customizable symbol lists and filters
- **Fee Consideration**: Note: Results don't account for trading fees
- **Flexible Configuration**: Easy exchange and parameter modification

## Installation

### Prerequisites
- Python 3.10 or higher

### Setup
```bash
pip3 install -r requirements.txt
```

## Usage

Start arbitrage detection:
```bash
python3 main.py
```

## Configuration

- Edit `main.py` to change the exchange (must match ccxt exchange ID)
- Configure symbol lists for ignore/whitelist filtering
- Adjust detection parameters as needed

## How It Works

The tool analyzes price differences across multiple trading pairs to identify profitable arbitrage cycles. It calculates potential gains from trading through a series of assets and returning to the original asset.

## Important Notes

- Trading fees are not included in calculations
- Results may vary based on market conditions
- Thorough testing is recommended before live trading

## Project Structure

- `triangular_arbitrage/` - Core arbitrage logic
- `tests/` - Test files
- `main.py` - Main entry point
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container configuration

## License

MIT License
