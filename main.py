import asyncio

import octobot_commons.symbols as symbols
import octobot_commons.os_util as os_util

import triangular_arbitrage.detector as detector

if __name__ == "__main__":
    benchmark = os_util.parse_boolean_environment_var("IS_BENCHMARKING", "False")
    if benchmark:
        import time

        s = time.perf_counter()

    # start arbitrage detection
    print("Scanning...")
    exchange_name = "binance" # allow pickable exchange_id from https://github.com/ccxt/ccxt/wiki/manual#exchanges

    best_opportunities, best_profit = asyncio.run(detector.run_detection(exchange_name))


    def opportunity_symbol(opportunity):
        return symbols.parse_symbol(str(opportunity.symbol))


    def get_order_side(opportunity: detector.ShortTicker):
        return 'buy' if opportunity.reversed else 'sell'


    if best_opportunities is not None:
        # Display arbitrage detection result
        print("-------------------------------------------")
        total_profit_percentage = round((best_profit - 1) * 100, 5)
        print(f"New {total_profit_percentage}% {exchange_name} opportunity:")
        for i, opportunity in enumerate(best_opportunities):
            # Get the base and quote currencies
            base_currency = opportunity.symbol.base
            quote_currency = opportunity.symbol.quote

            # Format the output as below (real live example):
            # -------------------------------------------
            # New 2.33873% binanceus opportunity:
            # 1. buy DOGE to BTC at 552486.18785
            # 2. sell DOGE to USDT at 0.12232
            # 3. buy ETH to USDT at 0.00038
            # 4. buy ADA to ETH at 7570.02271
            # 5. sell ADA to USDC at 0.35000
            # 6. buy SOL to USDC at 0.00662
            # 7. sell SOL to BTC at 0.00226
            # -------------------------------------------
            order_side = get_order_side(opportunity)
            print(f"{i+1}. {order_side} {base_currency} to {quote_currency} at {opportunity.last_price:.5f}")
        print("-------------------------------------------")
    else:
        print("No opportunity detected")

    if benchmark:
        elapsed = time.perf_counter() - s
        print(f"{__file__} executed in {elapsed:0.2f} seconds.")
