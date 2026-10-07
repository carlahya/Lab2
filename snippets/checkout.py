"""
SNIPPET 4 — Clean-code / coding practices (no SOLID needed)

Smells: cryptic names, magic numbers, duplication, deep nesting,
no guard clauses, a comment explaining what good names would say for free.

Your job (via the AI harness):
  Make it readable WITHOUT changing behaviour — meaningful names,
  named constants, guard clauses, remove duplication. Keep the output identical.
"""
MEMBERSHIP_DISCOUNTS = {
    2: 0.10,
    3: 0.20,
}
LOYALTY_POINTS_DISCOUNT_THRESHOLD = 500
LOYALTY_POINTS_DISCOUNT = 5
MINIMUM_TOTAL = 0


def calculate_total(cart_items, membership_level, loyalty_points):
    """Return the cart total after membership and loyalty discounts."""
    if not cart_items:
        return 0

    subtotal = sum(item["p"] * item["q"] for item in cart_items)
    membership_discount = MEMBERSHIP_DISCOUNTS.get(membership_level, 0)
    total = subtotal * (1 - membership_discount)

    if loyalty_points > LOYALTY_POINTS_DISCOUNT_THRESHOLD:
        total -= LOYALTY_POINTS_DISCOUNT

    return max(total, MINIMUM_TOTAL)


def calc(cart_items, membership_level, loyalty_points):
    """Compatibility wrapper for the original lab function name."""
    return calculate_total(cart_items, membership_level, loyalty_points)


if __name__ == "__main__":
    cart = [{"p": 20, "q": 2}, {"p": 15, "q": 1}]
    print("Total:", calc(cart, 3, 600))
