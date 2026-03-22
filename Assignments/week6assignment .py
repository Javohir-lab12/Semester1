def calculate_holding_profit(stock_tuple):
    # ticker, sector, p_price, c_price, shares = stock_tuple
    # return((c_price - p_price) * shares)
    return (stock_tuple[3] - stock_tuple[2]) * stock_tuple[4]

def find_top_performer(portfolio):
    profits = []
    for i in range(len(portfolio)):
        profit = calculate_holding_profit(portfolio[i])
        profits.append(profit)
    highest_profit = max(profits)
    top_tickers = []
    for j in range(len(profits)):
        if highest_profit == profits[j]:
         top_tickers.append(portfolio[j][0])
    top_tickers.sort()
    return (top_tickers[0])

def get_tickers_in_sector(portfolio, sector_name):
    similar_tickets = []
    for i in range(len(portfolio)):
        if portfolio[i][1] == sector_name:
            similar_tickets.append(portfolio[i][0])
    similar_tickets.sort()
    return (similar_tickets)

def get_sector_value_summary(portfolio):
    sectors = []
    for i in range(len(portfolio)):
        if portfolio[i][1] not in sectors:
            sectors.append(portfolio[i][1])
    sector_summary = []
    for sector in sectors:
        total_value = 0
        tickers = get_tickers_in_sector(portfolio, sector)
        for i in range(len(portfolio)):
            if portfolio[i][0] in tickers:
                total_value += portfolio[i][3] * portfolio[i][4]
        sector_summary.append((sector, total_value))
    sector_summary.sort()
    return sector_summary
def analyze_portfolio(portfolio):
    top_performer_ticker = find_top_performer(portfolio)
    tech_tickers = get_tickers_in_sector(portfolio, "Technology")
    sector_summary = get_sector_value_summary(portfolio)
    return ((top_performer_ticker, tech_tickers, sector_summary))
        


portfolio = [
    ('AAPL', 'Technology', 150.00, 175.00, 100),  # Profit: 2500
    ('JPM', 'Finance', 160.00, 165.00, 200),     # Profit: 1000
    ('GOOG', 'Technology', 2800.00, 2750.00, 10), # Profit: -500
    ('PFE', 'Healthcare', 40.00, 55.00, 500)     # Profit: 7500
]
print(analyze_portfolio(portfolio))
