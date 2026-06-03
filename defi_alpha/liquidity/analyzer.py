"""Liquidity pool analysis."""
import numpy as np

def impermanent_loss(price_ratio: float) -> float:
    """Calculate impermanent loss given price ratio change."""
    return 2 * np.sqrt(price_ratio) / (1 + price_ratio) - 1

def optimal_range(current_price: float, volatility: float, confidence: float = 0.95):
    """Calculate optimal LP range for concentrated liquidity."""
    z_score = 1.96 if confidence == 0.95 else 2.58
    lower = current_price * (1 - z_score * volatility)
    upper = current_price * (1 + z_score * volatility)
    return lower, upper
