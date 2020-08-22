from datetime import datetime
from enum import IntEnum


class TradePartner(IntEnum):
    PLAYER = 0
    KICKBASE = 1


class Trade:
    
    feed_id: str = None
    date: datetime = None
    
    buyer_type: TradePartner = None
    buyer_id: str = None
    buyer_name: str = None
    
    price: float = None
    
    seller_type: TradePartner = None
    seller_id: str = None
    seller_name: str = None
    
    player_id: str = None
    player_last_name: str = None
    
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)