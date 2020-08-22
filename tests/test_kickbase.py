import os
from datetime import datetime, timezone

import pytest

from kickbase_api.kickbase import Kickbase

from kickbase_analysis.kickbase_analysis import KickbaseAnalysis


@pytest.mark.online
def test_login():
    kickbase = Kickbase()
    assert not kickbase._is_token_valid()
    user, leagues = kickbase.login(os.environ["KKBS_TEST_USERNAME"], os.environ["KKBS_TEST_PASSWORD"])
    assert kickbase._is_token_valid()
    assert user is not None
    assert leagues is not None

@pytest.mark.online
def test_trades(logged_in_kickbase):
    kickbase, user, leagues = logged_in_kickbase
    
    # Fetch all feed items
    count = 0
    feed_items = []
    while True:
        fd = kickbase.league_feed(count, leagues[0])
        feed_items = feed_items + fd
        if len(fd) == 0:
            break
        else:
            count = count + len(fd)
                                
    feed_items = KickbaseAnalysis.filter_feed_items_by_date(feed_items, start_from=datetime(year=2020, month=8, day=16,
                                                                         hour=19, minute=0, tzinfo=timezone.utc))
    trades = KickbaseAnalysis.get_trades(feed_items)
    assert(len(trades) != 0)
