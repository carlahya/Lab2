"""
SNIPPET 3 — Dependency Inversion Principle (DIP)

Smell: the high-level OrderService reaches down and builds a concrete
EmailSender itself. It is welded to one delivery mechanism, so it can't
be tested without sending real email and can't switch to SMS.

Your job (via the AI harness):
  Invert the dependency — OrderService should depend on an abstraction
  that is PASSED IN, not on a concrete class it constructs.
  Then add an SmsSender without changing OrderService.
"""

# pylint: disable=too-few-public-methods

from typing import Protocol


class Sender(Protocol):
    """Interface for sending order notifications."""

    def send(self, message):
        """Send a notification message."""


class EmailSender:
    """Sends notifications by email."""

    def send(self, message):
        """Send an email notification."""
        print("EMAIL:", message)


class SmsSender:
    """Sends notifications by SMS."""

    def send(self, message):
        """Send an SMS notification."""
        print("SMS:", message)


class FakeSender:
    """Test sender that records messages."""

    def __init__(self):
        self.messages = []

    def send(self, message):
        """Record a notification message."""
        self.messages.append(message)


class OrderService:
    """Places orders and delegates notification delivery."""

    def __init__(self, sender=None):
        self.sender = sender or EmailSender()

    def place_order(self, item):
        """Place an order and notify the customer."""
        self.sender.send(f"Your order for {item} is confirmed.")


if __name__ == "__main__":
    OrderService().place_order("keyboard")
