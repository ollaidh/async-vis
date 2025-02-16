MOCK_HISTORY_RESPONSE = {
    "symbol": "AAPL",
    "history": [
        {
            "date": "2024-02-12",
            "open": 187.50,
            "high": 190.20,
            "low": 186.80,
            "close": 189.30,
            "volume": 65234000,
        },
        {
            "date": "2024-02-13",
            "open": 189.40,
            "high": 192.00,
            "low": 188.90,
            "close": 191.50,
            "volume": 58967000,
        },
        {
            "date": "2024-02-14",
            "open": 191.60,
            "high": 193.50,
            "low": 190.50,
            "close": 192.80,
            "volume": 57312000,
        },
    ],
}


MOCK_INFO_RESPONSE = {
    "symbol": "AAPL",
    "name": "Apple Inc.",
    "sector": "Technology",
    "industry": "Consumer Electronics",
    "market_cap": 2800000000000,
    "exchange": "NASDAQ",
    "ceo": "Tim Cook",
    "headquarters": "Cupertino, CA, USA",
    "founded": 1976,
    "employees": 161000,
    "website": "https://www.apple.com",
}


MOCK_SECTORS_RESPONSE = {
    "sectors": [
        {
            "name": "Technology",
            "performance": 1.8,
            "market_cap": 15000000000000,
        },
        {
            "name": "Healthcare",
            "performance": -0.5,
            "market_cap": 8000000000000,
        },
        {"name": "Finance", "performance": 0.9, "market_cap": 7000000000000},
        {"name": "Energy", "performance": 2.3, "market_cap": 5000000000000},
        {
            "name": "Consumer Discretionary",
            "performance": -1.2,
            "market_cap": 6000000000000,
        },
    ]
}
