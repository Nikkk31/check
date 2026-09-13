"""
payment_gateway.py -- shared payment processing utilities. Real
charge implementations should route through here, not log directly.
"""

import logging
import uuid

logger = logging.getLogger("payment_gateway")


class PaymentError(Exception):
    """Raised when a charge cannot be completed."""


def generate_idempotency_key(customer_id: int, amount: float) -> str:
    """Every charge must include an idempotency key so a retried
    request can't double-charge the customer."""
    return f"{customer_id}-{amount}-{uuid.uuid4().hex[:8]}"


def process_charge(customer_id: int, amount: float, idempotency_key: str) -> dict:
    """
    Callers MUST generate a unique idempotency_key per charge attempt
    -- without one, a network retry results in the customer being
    charged twice for the same order.
    """
    if amount <= 0:
        raise PaymentError("Charge amount must be positive")
    if not idempotency_key:
        raise PaymentError("idempotency_key is required to prevent duplicate charges")

    logger.info("Processing charge: customer=%s amount=%s key=%s", customer_id, amount, idempotency_key)
    return {"status": "charged", "customer_id": customer_id, "amount": amount}
