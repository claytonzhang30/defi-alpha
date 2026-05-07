# DeFi Alpha 🏦

DeFi strategy engine for yield farming, arbitrage detection, and liquidity analysis.

## Features

- **Yield Scanner:** Discover highest APY opportunities across protocols
- **Arbitrage Detector:** Cross-DEX and cross-chain arbitrage detection
- **Liquidity Analysis:** Pool depth, impermanent loss calculator, IL hedging
- **Strategy Backtest:** Backtest yield strategies with historical data

## Quick Start

```python
from defi_alpha import YieldScanner, ArbitrageDetector

# Find best yield opportunities
scanner = YieldScanner(chain="ethereum")
opportunities = scanner.scan(min_apy=5.0, protocols=["aave", "compound", "curve"])
for opp in opportunities:
    print(f"{opp.protocol}: {opp.token_pair} @ {opp.apy:.1f}% APY")

# Detect arbitrage
detector = ArbitrageDetector()
arb = detector.find_opportunity(token="WETH", dexes=["uniswap", "sushiswap"])
if arb and arb.profit_usd > 50:
    print(f"Arb found: ${arb.profit_usd:.2f} profit")
```

## Modules

```
defi_alpha/
├── scanner/       # Yield opportunity scanner
├── arbitrage/     # Cross-DEX arbitrage engine
├── liquidity/     # Pool analysis & IL calculator
├── strategies/    # Strategy definitions
└── backtest/      # Strategy backtesting
```

## Setup

```bash
pip install web3 pandas numpy
cp .env.example .env  # Add RPC URLs and API keys
```

## License

MIT
<!-- update 1 -->
<!-- update 2 -->
<!-- update 3 -->
<!-- update 4 -->
<!-- update 5 -->
<!-- update 6 -->
<!-- update 7 -->
<!-- update 8 -->
<!-- update 9 -->
<!-- update 10 -->
<!-- update 11 -->
<!-- update 12 -->
<!-- update 13 -->
<!-- update 14 -->
<!-- update 15 -->
<!-- update 16 -->
<!-- update 17 -->
<!-- update 18 -->
<!-- update 19 -->
<!-- update 20 -->
<!-- update 21 -->
<!-- update 22 -->
<!-- update 23 -->
<!-- update 24 -->
<!-- update 25 -->
<!-- update 26 -->
<!-- update 27 -->
