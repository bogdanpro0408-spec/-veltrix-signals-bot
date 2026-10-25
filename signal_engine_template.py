"""
Template only: connect a legitimate live quote/candle provider here.
Do not emit signals without fresh, timestamped market data and tested rules.
OTC needs a source matching the platform's OTC prices.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Literal

Direction = Literal["CALL", "PUT"]


@dataclass
class Candle:
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float


@dataclass
class Signal:
    pair: str
    direction: Direction
    entry_time: datetime
    expiry: str
    source_timestamp: datetime
    strategy: str


def generate_signal(pair: str, expiry: str, candles: list[Candle]) -> Signal | None:
    """
    Implement only after connecting and validating a real data source.
    Return None when data is stale, incomplete, or the strategy has no setup.
    This function intentionally does not fabricate a CALL/PUT.
    """
    return None
