import csv
from time import perf_counter

def read_prices(path):
    with open(path, newline="", encoding="utf-8") as source:
        rows = csv.DictReader(source)
        if not rows.fieldnames or "price" not in rows.fieldnames:
            raise ValueError("CSV must contain a 'price' column")
        return [float(row["price"]) for row in rows]

def one_pass_profit(prices):
    if len(prices) < 2: return 0
    lowest, best = prices[0], 0
    for price in prices[1:]:
        best = max(best, price-lowest)
        lowest = min(lowest, price)
    return best

def best_subarray(values):
    # Kadane's algorithm over day-to-day price changes.
    current = best = 0
    for change in values:
        current = max(0, current+change)
        best = max(best, current)
    return best

def divide_profit(prices):
    return best_subarray([prices[i]-prices[i-1] for i in range(1,len(prices))])

if __name__ == "__main__":
    try:
        prices = read_prices("prices.csv")
    except FileNotFoundError:
        prices = [100, 95, 110, 105, 130, 120, 145]
        with open("prices.csv","w",newline="",encoding="utf-8") as target:
            writer=csv.writer(target); writer.writerow(["price"]); writer.writerows([[p] for p in prices])
    for title, function in (("Single pass",one_pass_profit),("Change-array method",divide_profit)):
        start=perf_counter(); result=function(prices)
        print(f"{title}: maximum profit = {result:.2f}, time = {perf_counter()-start:.7f}s")
