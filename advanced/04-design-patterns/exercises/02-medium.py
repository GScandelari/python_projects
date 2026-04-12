# ============================================================
# advanced/04-design-patterns/exercises/02-medium.py
# Topic: Design Patterns — Observer, Strategy, Decorator (GoF)
# Difficulty: Medium
# ============================================================

# Exercise 1 — Observer: Stock price alerts
# ------------------------------------------
# Implement the Observer pattern for a stock ticker:
#
# StockMarket (subject):
#   - subscribe(symbol, observer) → add observer for a stock symbol
#   - unsubscribe(symbol, observer) → remove observer
#   - update_price(symbol, price) → notify all observers of that symbol
#
# Observers (at least 2):
#   PriceLogger   → prints: "[LOG] {symbol}: R${price:.2f}"
#   AlertSystem   → prints a warning if price drops below a threshold
#                   "[ALERT] {symbol} below R${threshold:.2f}!"
#
# Expected:
#   market = StockMarket()
#   market.subscribe("PETR4", PriceLogger())
#   market.subscribe("PETR4", AlertSystem(threshold=25.0))
#   market.update_price("PETR4", 28.50)   → only log
#   market.update_price("PETR4", 22.00)   → log + alert

# Write your code here


# Exercise 2 — Strategy: Discount calculator
# -------------------------------------------
# Build a checkout system where the discount strategy can be
# swapped at runtime:
#
# DiscountStrategy (callable or class with apply(total) method):
#   NoDiscount         → returns total unchanged
#   PercentageDiscount(pct) → returns total * (1 - pct/100)
#   FixedDiscount(amount)   → returns max(0, total - amount)
#   BulkDiscount(threshold, pct) → applies pct% only if total >= threshold
#
# ShoppingCart:
#   - add(item, price, qty=1) → adds to cart
#   - subtotal() → sum of price*qty
#   - checkout(strategy) → returns {"subtotal": ..., "discount": ..., "total": ...}
#
# Expected:
#   cart = ShoppingCart()
#   cart.add("Notebook", 2500, 1)
#   cart.add("Mouse", 90, 2)
#   cart.checkout(NoDiscount())               → total = 2680
#   cart.checkout(PercentageDiscount(10))     → total = 2412
#   cart.checkout(BulkDiscount(2000, 15))     → total = 2278

# Write your code here


# Exercise 3 — Decorator (GoF): Text formatting pipeline
# -------------------------------------------------------
# Implement the GoF Decorator pattern (not Python @decorator syntax)
# to build a composable text formatting pipeline.
#
# TextComponent interface: render(text) → str
#
# Concrete component:
#   PlainText — render() returns text as-is
#
# Decorators (each wraps a component):
#   TrimDecorator   → strips leading/trailing whitespace
#   UpperDecorator  → converts to uppercase
#   BoldDecorator   → wraps in ** text **
#   PrefixDecorator(prefix) → prepends a prefix string
#
# Decorators can be stacked in any order.
#
# Expected:
#   text = "  hello world  "
#   renderer = BoldDecorator(UpperDecorator(TrimDecorator(PlainText())))
#   renderer.render(text)   → "**HELLO WORLD**"
#
#   renderer2 = PrefixDecorator(">>> ", UpperDecorator(PlainText()))
#   renderer2.render("info message")   → ">>> INFO MESSAGE"

# Write your code here
