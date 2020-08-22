from datetime import datetime

from kickbase_api.models.feed_item import FeedItem, FeedType

from kickbase_analysis.models.trade import Trade, TradePartner


class KickbaseAnalysis:
    
    @staticmethod
    def filter_feed_items_by_date(feed_items: [FeedItem], start_from: datetime) -> [FeedItem]:
        sorted_feed_items = sorted(feed_items, key=lambda d: d.date)
        if start_from is not None:
            sorted_feed_items = list(filter(lambda x: x.date > start_from, sorted_feed_items))
        return sorted_feed_items

    @staticmethod
    def get_trades(feed_items: [FeedItem]) -> [Trade]:
        buys = []
        sales = []
        for feed_item in feed_items:
            if feed_item.type == FeedType.BUY:
                buys.append(feed_item)
            elif feed_item.type == FeedType.SALE:
                sales.append(feed_item)
                
        trades = []
        for buy in buys:
            trades.append(Trade(feed_id=buy.id,
                                date=buy.date,
                                buyer_type=TradePartner.KICKBASE if buy.meta.buyer_id is None else TradePartner.PLAYER,
                                buyer_id=buy.meta.buyer_id, 
                                buyer_name=buy.meta.buyer_name,
                                price=buy.meta.buy_price,
                                seller_type=TradePartner.KICKBASE if buy.meta.seller_id is None else TradePartner.PLAYER,
                                seller_id=buy.meta.seller_id,
                                seller_name=buy.meta.seller_name,
                                player_id=buy.meta.player_id,
                                player_last_name=buy.meta.player_last_name))
        for sale in sales:
            trades.append(Trade(feed_id=sale.id,
                                date=sale.date,
                                buyer_type=TradePartner.KICKBASE if sale.meta.buyer_id is None else TradePartner.PLAYER,
                                buyer_id=sale.meta.buyer_id,
                                buyer_name=sale.meta.buyer_name,
                                price=sale.meta.buy_price,
                                seller_type=TradePartner.KICKBASE if sale.meta.seller_id is None else TradePartner.PLAYER,
                                seller_id=sale.meta.seller_id,
                                seller_name=sale.meta.seller_name,
                                player_id=sale.meta.player_id,
                                player_last_name=sale.meta.player_last_name))
        
        return trades
