# model-delivery-economics

Input: offer plus currency/unit/period, capacity, revenue, relevant costs, receipt timing and obligations.

Output: delivery/capacity model, contribution and cash exposure with explicit unknowns.

Use `../scripts/economics.py` for decision-driving arithmetic. Record whether labour is included as a variable cost and keep fixed costs separate.

Forbidden: revenue=profit, cash=profit, speculative LTV presented as observed, silent unit/period mismatch.
