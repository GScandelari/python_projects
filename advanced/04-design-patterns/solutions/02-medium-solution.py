# ============================================================
# advanced/04-design-patterns/solutions/02-medium-solution.py
# ============================================================

# ----------------------------------------------------------
# Exercise 1 — Observer: Stock price alerts
# ----------------------------------------------------------
class StockMarket:
    def __init__(self):
        self._subscribers = {}

    def subscribe(self, symbol, observer):
        self._subscribers.setdefault(symbol, []).append(observer)

    def unsubscribe(self, symbol, observer):
        self._subscribers.get(symbol, []).remove(observer)

    def update_price(self, symbol, price):
        for obs in self._subscribers.get(symbol, []):
            obs.notify(symbol, price)


class PriceLogger:
    def notify(self, symbol, price):
        print(f"  [LOG] {symbol}: R${price:.2f}")


class AlertSystem:
    def __init__(self, threshold):
        self.threshold = threshold

    def notify(self, symbol, price):
        if price < self.threshold:
            print(f"  [ALERT] {symbol} dropped below R${self.threshold:.2f}!")


print("--- Observer: StockMarket ---")
market = StockMarket()
market.subscribe("PETR4", PriceLogger())
market.subscribe("PETR4", AlertSystem(threshold=25.0))

market.update_price("PETR4", 28.50)   # only log
market.update_price("PETR4", 22.00)   # log + alert


# ----------------------------------------------------------
# Exercise 2 — Strategy: Discount calculator
# ----------------------------------------------------------
class NoDiscount:
    def apply(self, total):
        return total

class PercentageDiscount:
    def __init__(self, pct):
        self.pct = pct

    def apply(self, total):
        return total * (1 - self.pct / 100)

class FixedDiscount:
    def __init__(self, amount):
        self.amount = amount

    def apply(self, total):
        return max(0, total - self.amount)

class BulkDiscount:
    def __init__(self, threshold, pct):
        self.threshold = threshold
        self.pct       = pct

    def apply(self, total):
        if total >= self.threshold:
            return total * (1 - self.pct / 100)
        return total


class ShoppingCart:
    def __init__(self):
        self._items = []

    def add(self, item, price, qty=1):
        self._items.append((item, price, qty))

    def subtotal(self):
        return sum(price * qty for _, price, qty in self._items)

    def checkout(self, strategy):
        sub = self.subtotal()
        total = strategy.apply(sub)
        discount = sub - total
        return {"subtotal": round(sub, 2), "discount": round(discount, 2), "total": round(total, 2)}


print("\n--- Strategy: ShoppingCart ---")
cart = ShoppingCart()
cart.add("Notebook", 2500, 1)
cart.add("Mouse", 90, 2)

for strategy in [NoDiscount(), PercentageDiscount(10), BulkDiscount(2000, 15)]:
    result = cart.checkout(strategy)
    print(f"  {strategy.__class__.__name__:<22}: {result}")


# ----------------------------------------------------------
# Exercise 3 — Decorator (GoF): Text formatting pipeline
# ----------------------------------------------------------
class PlainText:
    def render(self, text):
        return text

class TrimDecorator:
    def __init__(self, component):
        self._component = component

    def render(self, text):
        return self._component.render(text).strip()

class UpperDecorator:
    def __init__(self, component):
        self._component = component

    def render(self, text):
        return self._component.render(text).upper()

class BoldDecorator:
    def __init__(self, component):
        self._component = component

    def render(self, text):
        return f"**{self._component.render(text)}**"

class PrefixDecorator:
    def __init__(self, prefix, component):
        self.prefix     = prefix
        self._component = component

    def render(self, text):
        return f"{self.prefix}{self._component.render(text)}"


print("\n--- GoF Decorator: Text pipeline ---")
text = "  hello world  "
renderer = BoldDecorator(UpperDecorator(TrimDecorator(PlainText())))
print(repr(renderer.render(text)))   # '**HELLO WORLD**'

renderer2 = PrefixDecorator(">>> ", UpperDecorator(PlainText()))
print(repr(renderer2.render("info message")))   # '>>> INFO MESSAGE'
