"""
SNIPPET 1 — Single Responsibility Principle (SRP)

Smell: this ONE class gathers data, formats it as HTML, AND emails it.
Three reasons to change = three responsibilities crammed together.

Your job (via the AI harness):
  Split into focused pieces so that changing the email provider does NOT
  force you to touch the formatting or the data-gathering code.
"""

# pylint: disable=too-few-public-methods

import smtplib
from typing import Protocol

FROM_ADDRESS = "reports@brunel.ac.uk"
RECIPIENT_ADDRESS = "boss@brunel.ac.uk"
SMTP_HOST = "smtp.brunel.ac.uk"
SMTP_PORT = 587


class ReportSender(Protocol):
    """Delivery interface for generated reports."""

    def send(self, content):
        """Send the report content."""


class SalesData:
    """Owns sales calculations for a report."""

    def __init__(self, sales):
        self.sales = sales

    def count(self):
        """Return the number of sales."""
        return len(self.sales)

    def total(self):
        """Return the total value of all sales."""
        return sum(self.sales)


class HtmlSalesReportFormatter:
    """Formats sales data as an HTML report."""

    def format(self, sales_data):
        """Return a sales report as HTML."""
        return (
            "<html><body>"
            "<h1>Sales Report</h1>"
            f"<p>Number of sales: {sales_data.count()}</p>"
            f"<p>Total: {sales_data.total()}</p>"
            "</body></html>"
        )


class SmtpReportSender:
    """Sends reports through SMTP."""

    def __init__(
        self,
        host=SMTP_HOST,
        port=SMTP_PORT,
        sender=FROM_ADDRESS,
        recipient=RECIPIENT_ADDRESS,
    ):
        self.host = host
        self.port = port
        self.sender = sender
        self.recipient = recipient

    def send(self, content):
        """Send report content through the configured SMTP server."""
        server = smtplib.SMTP(self.host, self.port)
        try:
            server.sendmail(self.sender, self.recipient, content)
        finally:
            server.quit()


class FakeReportSender:
    """Test sender that records reports without external delivery."""

    def __init__(self):
        self.sent_reports = []

    def send(self, content):
        """Record the report content."""
        self.sent_reports.append(content)


class SalesReport:
    """Coordinates report data, formatting, and delivery."""

    def __init__(self, sales, sender=None, formatter=None):
        self.sales_data = SalesData(sales)
        self.sender = sender or SmtpReportSender()
        self.formatter = formatter or HtmlSalesReportFormatter()

    def generate(self):
        """Generate, send, and return the report HTML."""
        html = self.formatter.format(self.sales_data)
        self.sender.send(html)
        return html


if __name__ == "__main__":
    SalesReport([120, 340, 90, 560], sender=FakeReportSender()).generate()
